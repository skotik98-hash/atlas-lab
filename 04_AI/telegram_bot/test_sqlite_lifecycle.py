#!/usr/bin/env python3
"""Isolated SQLite connection-lifecycle tests. Uses temporary databases only."""

import gc
import os
import sqlite3
import sys
import tempfile
import traceback
from pathlib import Path

from sqlite_lifecycle import managed_connection
import activity_store
import approval_store
import sales_outreach_store
import task_store


ITERATIONS = 80
LIVE_DATA = Path(__file__).resolve().parent / "data"


def count_fds_for(path):
    path = Path(path).resolve()
    if not path.exists():
        return 0

    count = 0
    try:
        names = os.listdir("/dev/fd")
    except OSError:
        return -1

    for name in names:
        fd_path = Path("/dev/fd") / name
        try:
            if os.path.samefile(fd_path, path):
                count += 1
        except OSError:
            continue

    return count


def count_open_fds():
    return len(os.listdir("/dev/fd"))


def assert_not_live(path):
    resolved = Path(path).resolve()
    live = LIVE_DATA.resolve()
    if resolved == live or live in resolved.parents:
        raise AssertionError(f"Refusing to use live database path: {resolved}")


def point_store_at_temp(module, tmp_dir, filename, extra=None):
    db_path = Path(tmp_dir) / filename
    assert_not_live(db_path)

    if hasattr(module, "DB_PATH"):
        if isinstance(getattr(module, "DB_PATH"), str):
            module.DB_PATH = str(db_path)
        else:
            module.DB_PATH = db_path

    if extra:
        extra(module, tmp_dir, db_path)

    return db_path


def sales_extra(module, tmp_dir, db_path):
    module.DATA_DIR = str(tmp_dir)
    module.DB_PATH = str(db_path)


class Results:
    def __init__(self):
        self.failed = []
        self.passed = []

    def check(self, name, ok, detail=""):
        if ok:
            self.passed.append(name)
            print(f"PASS  {name}" + (f"  {detail}" if detail else ""))
        else:
            self.failed.append(name)
            print(f"FAIL  {name}" + (f"  {detail}" if detail else ""))


def test_stdlib_with_leaks(results, tmp_dir):
    path = Path(tmp_dir) / "stdlib_leak.db"
    assert_not_live(path)

    with sqlite3.connect(path) as setup:
        setup.execute("CREATE TABLE t (id INTEGER)")
        setup.commit()

    with sqlite3.connect(path) as db:
        pass
    still_open = True
    try:
        db.execute("SELECT 1")
    except sqlite3.ProgrammingError:
        still_open = False

    results.check(
        "stdlib with sqlite3.connect leaves connection open",
        still_open is True,
    )

    gc.disable()
    try:
        before = count_open_fds()
        for _ in range(ITERATIONS):
            with sqlite3.connect(path) as db:
                db.execute("SELECT 1").fetchone()
        after = count_open_fds()
    finally:
        gc.enable()
        gc.collect()

    leaked = after - before
    results.check(
        "stdlib with sqlite3.connect accumulates FDs without GC",
        leaked >= ITERATIONS - 5,
        f"process_fds {before}->{after} leaked={leaked} iterations={ITERATIONS}",
    )
    return leaked


def test_helper_does_not_leak(results, tmp_dir):
    path = Path(tmp_dir) / "helper.db"
    assert_not_live(path)

    def open_db():
        db = sqlite3.connect(path)
        db.row_factory = sqlite3.Row
        return db

    with managed_connection(open_db()) as db:
        db.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, v TEXT)")
        db.execute("INSERT INTO t(v) VALUES ('ok')")
        db.commit()

    with managed_connection(open_db()) as db:
        pass
    closed = False
    try:
        db.execute("SELECT 1")
    except sqlite3.ProgrammingError:
        closed = True
    results.check("managed_connection closes connection on exit", closed)

    gc.disable()
    try:
        process_before = count_open_fds()
        for _ in range(ITERATIONS):
            with managed_connection(open_db()) as db:
                db.execute("SELECT * FROM t").fetchall()
        process_after = count_open_fds()
    finally:
        gc.enable()
        gc.collect()

    results.check(
        "managed_connection repeated reads release FDs without GC",
        process_after <= process_before + 2,
        f"process_fds {process_before}->{process_after}",
    )


def test_helper_commit(results, tmp_dir):
    path = Path(tmp_dir) / "commit.db"
    assert_not_live(path)

    with managed_connection(sqlite3.connect(path)) as db:
        db.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, v TEXT)")
        db.execute("INSERT INTO t(v) VALUES ('kept')")
        db.commit()

    with sqlite3.connect(path) as db:
        row = db.execute("SELECT v FROM t").fetchone()
        db.commit()

    results.check("commit persists after close", row[0] == "kept")


def test_helper_rollback(results, tmp_dir):
    path = Path(tmp_dir) / "rollback.db"
    assert_not_live(path)

    with managed_connection(sqlite3.connect(path)) as db:
        db.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, v TEXT)")
        db.commit()

    try:
        with managed_connection(sqlite3.connect(path)) as db:
            db.execute("INSERT INTO t(v) VALUES ('gone')")
            raise RuntimeError("force rollback")
    except RuntimeError:
        pass

    with sqlite3.connect(path) as db:
        count = db.execute("SELECT COUNT(*) FROM t").fetchone()[0]
        db.commit()

    results.check("exception rolls back uncommitted write", count == 0)


def test_helper_exception_closes(results, tmp_dir):
    path = Path(tmp_dir) / "exc_close.db"
    assert_not_live(path)

    with sqlite3.connect(path) as db:
        db.execute("CREATE TABLE t (id INTEGER)")
        db.commit()

    before = count_fds_for(path)
    for _ in range(ITERATIONS):
        try:
            with managed_connection(sqlite3.connect(path)) as db:
                db.execute("SELECT 1")
                raise ValueError("boom")
        except ValueError:
            pass

    after = count_fds_for(path)
    results.check(
        "exceptions still release connections",
        after <= before + 1,
        f"before={before} after={after}",
    )


def test_task_store(results, tmp_dir):
    db_path = point_store_at_temp(task_store, tmp_dir, "tasks.db")
    before = count_open_fds()

    created = task_store.create_task("R1 test task", description="lifecycle")
    fetched = task_store.get_task(created["task_id"])
    listed = task_store.list_tasks(limit=10)
    updated = task_store.update_task_status(created["task_id"], "IN_PROGRESS")
    counts = task_store.count_tasks()

    for _ in range(ITERATIONS):
        task_store.get_task(created["task_id"])
        task_store.list_tasks(limit=5)
        task_store.count_tasks()

    after = count_open_fds()
    db_fds = count_fds_for(db_path)

    api_ok = (
        created["title"] == "R1 test task"
        and created["status"] == "NEW"
        and fetched["task_id"] == created["task_id"]
        and any(item["task_id"] == created["task_id"] for item in listed)
        and updated["status"] == "IN_PROGRESS"
        and counts["IN_PROGRESS"] == 1
        and counts["NEW"] == 0
    )
    results.check("task_store APIs unchanged", api_ok)
    results.check(
        "task_store repeated reads do not accumulate FDs",
        after <= before + 4 and db_fds <= 2,
        f"process_fds {before}->{after}; db_fds={db_fds}",
    )

    for _ in range(20):
        task_store.create_task("write loop")
        task_store.update_task_status(
            task_store.list_tasks(limit=1)[0]["task_id"],
            "DONE",
        )

    write_after = count_open_fds()
    write_db_fds = count_fds_for(db_path)
    results.check(
        "task_store repeated writes release connections",
        write_after <= after + 4 and write_db_fds <= 2,
        f"process_fds {after}->{write_after}; db_fds={write_db_fds}",
    )


def test_approval_store(results, tmp_dir):
    activity_path = point_store_at_temp(
        activity_store, tmp_dir, "activity.db"
    )
    db_path = point_store_at_temp(approval_store, tmp_dir, "approvals.db")
    before = count_open_fds()

    created = approval_store.create_approval(
        "APR-R1-001",
        "R1 approval",
        "TEST",
        "lifecycle check",
    )
    duplicate = approval_store.create_approval(
        "APR-R1-001",
        "R1 approval",
        "TEST",
        "duplicate",
    )
    fetched = approval_store.get_approval("APR-R1-001")
    pending = approval_store.list_pending()
    listed = approval_store.list_approvals()
    counts_before = approval_store.count_approvals()
    decided = approval_store.decide_approval(
        "APR-R1-001",
        "APPROVED",
        1,
    )
    fetched_after = approval_store.get_approval("APR-R1-001")
    already = approval_store.decide_approval(
        "APR-R1-001",
        "REJECTED",
        1,
    )
    missing = approval_store.decide_approval(
        "APR-MISSING",
        "APPROVED",
        1,
    )
    counts_after = approval_store.count_approvals()

    gc.disable()
    try:
        loop_before = count_open_fds()
        for _ in range(ITERATIONS):
            approval_store.count_approvals()
        loop_after = count_open_fds()
    finally:
        gc.enable()
        gc.collect()

    results.check(
        "approval_store count_approvals does not leak FDs without GC",
        loop_after <= loop_before + 2,
        f"process_fds {loop_before}->{loop_after} over {ITERATIONS} counts",
    )

    for _ in range(ITERATIONS):
        approval_store.count_approvals()
        approval_store.list_pending()
        approval_store.get_approval("APR-R1-001")

    after = count_open_fds()
    db_fds = count_fds_for(db_path)
    activity_fds = count_fds_for(activity_path)

    api_ok = (
        created is True
        and duplicate is False
        and fetched["status"] == "PENDING"
        and fetched_after["status"] == "APPROVED"
        and decided == "APPROVED"
        and already == "ALREADY_DECIDED"
        and missing == "NOT_FOUND"
        and counts_before["PENDING"] == 1
        and counts_after["APPROVED"] == 1
        and any(item["approval_id"] == "APR-R1-001" for item in listed)
        and isinstance(pending, list)
    )
    results.check("approval_store APIs unchanged", api_ok)
    results.check(
        "approval_store repeated reads do not accumulate FDs",
        after <= before + 4 and db_fds <= 2 and activity_fds <= 4,
        f"process_fds {before}->{after}; approvals_fds={db_fds}; activity_fds={activity_fds}",
    )


def test_sales_store(results, tmp_dir):
    db_path = point_store_at_temp(
        sales_outreach_store,
        tmp_dir,
        "sales_outreach.db",
        extra=sales_extra,
    )
    before = count_open_fds()

    created = sales_outreach_store.create_outreach(
        "OUT-R1-001",
        "TASK-0001",
        "Acme",
        "Ada",
        "CEO",
        "email",
        "READY_TO_SEND",
        "Atlas",
        "hello",
    )
    duplicate = sales_outreach_store.create_outreach(
        "OUT-R1-001",
        "TASK-0001",
        "Acme",
        "Ada",
        "CEO",
        "email",
        "READY_TO_SEND",
        "Atlas",
        "hello",
    )
    fetched = sales_outreach_store.get_outreach("OUT-R1-001")
    listed = sales_outreach_store.list_outreach()
    updated = sales_outreach_store.update_stage("OUT-R1-001", "SENT")
    replied = sales_outreach_store.record_inbound_reply(
        "OUT-R1-001",
        "Thanks, let's talk",
    )
    stages = sales_outreach_store.count_stages()

    for _ in range(ITERATIONS):
        sales_outreach_store.get_outreach("OUT-R1-001")
        sales_outreach_store.list_outreach(limit=10)
        sales_outreach_store.count_stages()

    after = count_open_fds()
    db_fds = count_fds_for(db_path)

    api_ok = (
        created is True
        and duplicate is False
        and fetched["company"] == "Acme"
        and any(item["outreach_id"] == "OUT-R1-001" for item in listed)
        and updated is True
        and replied is True
        and stages["REPLIED"] == 1
        and sales_outreach_store.get_outreach("OUT-R1-001")["stage"]
        == "REPLIED"
    )
    results.check("sales_outreach_store APIs unchanged", api_ok)
    results.check(
        "sales_outreach_store repeated reads do not accumulate FDs",
        after <= before + 4 and db_fds <= 2,
        f"process_fds {before}->{after}; db_fds={db_fds}",
    )

    for i in range(20):
        sales_outreach_store.create_outreach(
            f"OUT-R1-W{i:03d}",
            "TASK-0001",
            "Acme",
            "Ada",
            "CEO",
            "email",
            "READY_TO_SEND",
            "Atlas",
            "hello",
        )
        sales_outreach_store.update_stage(f"OUT-R1-W{i:03d}", "SENT")

    write_after = count_open_fds()
    write_db_fds = count_fds_for(db_path)
    results.check(
        "sales_outreach_store repeated writes release connections",
        write_after <= after + 4 and write_db_fds <= 2,
        f"process_fds {after}->{write_after}; db_fds={write_db_fds}",
    )


def test_activity_store(results, tmp_dir):
    db_path = point_store_at_temp(activity_store, tmp_dir, "activity.db")
    before = count_open_fds()

    event_id = activity_store.log_event(
        "R1_TEST",
        "R1",
        "lifecycle",
        "check",
        {"k": "v"},
    )
    events = activity_store.list_events(limit=5)

    for _ in range(ITERATIONS):
        activity_store.list_events(limit=5)

    after = count_open_fds()
    db_fds = count_fds_for(db_path)

    api_ok = (
        isinstance(event_id, int)
        and events[0]["event_type"] == "R1_TEST"
        and events[0]["metadata"]["k"] == "v"
    )
    results.check("activity_store APIs unchanged", api_ok)
    results.check(
        "activity_store repeated reads do not accumulate FDs",
        after <= before + 4 and db_fds <= 4,
        f"process_fds {before}->{after}; db_fds={db_fds}",
    )

    for i in range(20):
        activity_store.log_event("R1_WRITE", "R1", f"write {i}")

    write_after = count_open_fds()
    write_db_fds = count_fds_for(db_path)
    results.check(
        "activity_store repeated writes release connections",
        write_after <= after + 4 and write_db_fds <= 4,
        f"process_fds {after}->{write_after}; db_fds={write_db_fds}",
    )


def test_pragma_preserved(results, tmp_dir):
    db_path = point_store_at_temp(activity_store, tmp_dir, "activity_pragma.db")
    activity_store.initialize()

    raw = sqlite3.connect(db_path)
    try:
        mode = raw.execute("PRAGMA journal_mode").fetchone()[0]
    finally:
        raw.close()

    results.check(
        "activity_store WAL pragma preserved",
        str(mode).lower() == "wal",
        f"journal_mode={mode}",
    )


def test_pragma_setup_failure_closes(results, tmp_dir):
    db_path = point_store_at_temp(
        activity_store, tmp_dir, "activity_pragma_fail.db"
    )
    assert_not_live(db_path)

    class PragmaBoom(sqlite3.Connection):
        def execute(self, sql, parameters=(), *args, **kwargs):
            if "PRAGMA" in str(sql).upper():
                raise sqlite3.OperationalError("forced PRAGMA failure")
            return super().execute(sql, parameters, *args, **kwargs)

    real_connect = activity_store.sqlite3.connect

    def boom_connect(*args, **kwargs):
        kwargs["factory"] = PragmaBoom
        return real_connect(*args, **kwargs)

    activity_store.sqlite3.connect = boom_connect
    try:
        gc.disable()
        try:
            before = count_open_fds()
            errors = 0
            for _ in range(ITERATIONS):
                try:
                    with activity_store.connect() as db:
                        db.execute("SELECT 1")
                except sqlite3.OperationalError:
                    errors += 1
            after = count_open_fds()
        finally:
            gc.enable()
            gc.collect()
    finally:
        activity_store.sqlite3.connect = real_connect

    results.check(
        "activity_store PRAGMA setup failure closes connection",
        errors == ITERATIONS and after <= before + 2,
        f"errors={errors}; process_fds {before}->{after}",
    )


def main():
    results = Results()

    with tempfile.TemporaryDirectory(prefix="atlas-r1-") as tmp_dir:
        assert_not_live(tmp_dir)
        print(f"Using temp dir: {tmp_dir}")
        print(f"Live data dir (untouched): {LIVE_DATA}")
        print(f"Iterations: {ITERATIONS}")
        print()

        tests = [
            test_stdlib_with_leaks,
            test_helper_does_not_leak,
            test_helper_commit,
            test_helper_rollback,
            test_helper_exception_closes,
            test_task_store,
            test_approval_store,
            test_sales_store,
            test_activity_store,
            test_pragma_preserved,
            test_pragma_setup_failure_closes,
        ]

        for test in tests:
            try:
                test(results, tmp_dir)
            except Exception:
                results.failed.append(test.__name__)
                print(f"FAIL  {test.__name__}  crashed")
                traceback.print_exc()

    print()
    print(f"Passed: {len(results.passed)}")
    print(f"Failed: {len(results.failed)}")
    if results.failed:
        print("Failed tests: " + ", ".join(results.failed))
        return 1

    print("All isolated SQLite lifecycle tests passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
