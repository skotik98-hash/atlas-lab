#!/usr/bin/env python3
"""Isolated atomic state-transition tests. Uses temporary databases only."""

import os
import sys
import tempfile
import threading
import traceback
from pathlib import Path

import sales_outreach_store
import task_store
from task_store import apply_task_approval_decision, transition_task_status
from sales_outreach_store import transition_stage


LIVE_DATA = Path(__file__).resolve().parent / "data"


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


def make_outreach(outreach_id, stage="READY_TO_SEND"):
    return sales_outreach_store.create_outreach(
        outreach_id,
        "TASK-0001",
        "Acme",
        "Ada",
        "CEO",
        "email",
        stage,
        "Atlas",
        "hello",
    )


def test_task_happy_path(results, tmp_dir):
    point_store_at_temp(task_store, tmp_dir, "tasks.db")
    created = task_store.create_task("R2 start")
    task_id = created["task_id"]

    first = transition_task_status(task_id, "IN_PROGRESS")
    results.check(
        "NEW -> IN_PROGRESS succeeds",
        first["ok"] is True
        and first["task"]["status"] == "IN_PROGRESS"
        and first["task"]["completed_at"] is None,
    )

    second = transition_task_status(task_id, "IN_PROGRESS")
    results.check(
        "second NEW -> IN_PROGRESS attempt fails",
        second["ok"] is False
        and second["reason"] == "INVALID_TRANSITION"
        and task_store.get_task(task_id)["status"] == "IN_PROGRESS",
    )

    done = transition_task_status(task_id, "DONE")
    results.check(
        "IN_PROGRESS -> DONE succeeds",
        done["ok"] is True
        and done["task"]["status"] == "DONE"
        and bool(done["task"]["completed_at"]),
    )
    completed_at = done["task"]["completed_at"]

    dup = transition_task_status(task_id, "DONE")
    after = task_store.get_task(task_id)
    results.check(
        "duplicate DONE completion fails safely",
        dup["ok"] is False
        and after["status"] == "DONE"
        and after["completed_at"] == completed_at,
    )


def test_task_unsupported(results, tmp_dir):
    point_store_at_temp(task_store, tmp_dir, "tasks.db")
    new_task = task_store.create_task("cannot skip")
    skip = transition_task_status(new_task["task_id"], "DONE")
    still_new = task_store.get_task(new_task["task_id"])
    results.check(
        "NEW -> DONE fails",
        skip["ok"] is False
        and still_new["status"] == "NEW"
        and still_new["completed_at"] is None,
    )

    started = task_store.create_task("to complete")
    task_store.update_task_status(started["task_id"], "IN_PROGRESS")
    task_store.update_task_status(started["task_id"], "DONE")
    resurrect = transition_task_status(started["task_id"], "IN_PROGRESS")
    blocked = transition_task_status(started["task_id"], "BLOCKED")
    after = task_store.get_task(started["task_id"])
    results.check(
        "DONE -> IN_PROGRESS fails",
        resurrect["ok"] is False and after["status"] == "DONE",
    )
    results.check(
        "DONE -> BLOCKED resurrection fails",
        blocked["ok"] is False
        and after["status"] == "DONE"
        and bool(after["completed_at"]),
    )
    results.check(
        "completed_at remains set after rejected resurrection",
        after["completed_at"] is not None,
    )


def test_stale_expected_status(results, tmp_dir):
    point_store_at_temp(task_store, tmp_dir, "tasks.db")
    created = task_store.create_task("stale expected")
    task_store.update_task_status(created["task_id"], "IN_PROGRESS")
    stale = transition_task_status(
        created["task_id"],
        "IN_PROGRESS",
        expected_status="NEW",
    )
    after = task_store.get_task(created["task_id"])
    results.check(
        "stale expected-state update changes zero rows",
        stale["ok"] is False
        and stale["reason"] == "INVALID_TRANSITION"
        and after["status"] == "IN_PROGRESS",
    )


def test_task_concurrency(results, tmp_dir):
    point_store_at_temp(task_store, tmp_dir, "tasks.db")
    created = task_store.create_task("concurrent start")
    task_id = created["task_id"]
    outcomes = []
    barrier = threading.Barrier(2)

    def attempt():
        barrier.wait()
        outcomes.append(
            transition_task_status(task_id, "IN_PROGRESS")
        )

    threads = [
        threading.Thread(target=attempt),
        threading.Thread(target=attempt),
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    wins = sum(1 for item in outcomes if item["ok"])
    after = task_store.get_task(task_id)
    results.check(
        "concurrent NEW -> IN_PROGRESS has exactly one winner",
        wins == 1
        and after["status"] == "IN_PROGRESS"
        and len(outcomes) == 2,
        f"wins={wins} status={after['status']}",
    )


def test_approval_propagation(results, tmp_dir):
    point_store_at_temp(task_store, tmp_dir, "tasks.db")

    fresh = task_store.create_task("approval new")
    approved = apply_task_approval_decision(
        fresh["task_id"],
        "APPROVED",
        approval_id="TASK-0001-20260813-000000",
    )
    results.check(
        "approval APPROVED on NEW -> IN_PROGRESS",
        approved["ok"] is True
        and approved["task"]["status"] == "IN_PROGRESS",
    )

    rejected_src = task_store.create_task("approval reject")
    rejected = apply_task_approval_decision(
        rejected_src["task_id"],
        "REJECTED",
    )
    results.check(
        "approval REJECTED on NEW -> BLOCKED",
        rejected["ok"] is True
        and rejected["task"]["status"] == "BLOCKED",
    )

    done = task_store.create_task("terminal")
    task_store.update_task_status(done["task_id"], "IN_PROGRESS")
    task_store.update_task_status(done["task_id"], "DONE")
    completed_at = task_store.get_task(done["task_id"])["completed_at"]

    stale_approve = apply_task_approval_decision(
        done["task_id"],
        "APPROVED",
    )
    stale_reject = apply_task_approval_decision(
        done["task_id"],
        "REJECTED",
    )
    after = task_store.get_task(done["task_id"])
    results.check(
        "stale approval cannot resurrect terminal task",
        stale_approve["ok"] is False
        and stale_reject["ok"] is False
        and after["status"] == "DONE"
        and after["completed_at"] == completed_at,
    )
    results.check(
        "propagated state update result is checked",
        stale_approve["reason"] == "INVALID_TRANSITION"
        and "ok" in stale_approve,
    )


def test_pipeline_supported(results, tmp_dir):
    point_store_at_temp(
        sales_outreach_store,
        tmp_dir,
        "sales.db",
        extra=sales_extra,
    )

    make_outreach("OUT-R2-001")
    path = [
        ("SENT", "READY_TO_SEND"),
        ("WAITING_REPLY", "SENT"),
        ("REPLIED", "WAITING_REPLY"),
        ("MEETING", "REPLIED"),
        ("PROPOSAL", "MEETING"),
        ("WON", "PROPOSAL"),
    ]
    for dest, src in path:
        outcome = transition_stage(
            "OUT-R2-001",
            dest,
            expected_stage=src,
        )
        item = sales_outreach_store.get_outreach("OUT-R2-001")
        results.check(
            f"pipeline {src} -> {dest} succeeds",
            outcome["ok"] is True and item["stage"] == dest,
        )

    make_outreach("OUT-R2-LOST-M")
    sales_outreach_store.update_stage("OUT-R2-LOST-M", "SENT")
    sales_outreach_store.update_stage("OUT-R2-LOST-M", "WAITING_REPLY")
    sales_outreach_store.update_stage("OUT-R2-LOST-M", "REPLIED")
    sales_outreach_store.update_stage("OUT-R2-LOST-M", "MEETING")
    lost_m = transition_stage("OUT-R2-LOST-M", "LOST")
    results.check(
        "pipeline MEETING -> LOST succeeds",
        lost_m["ok"] is True
        and sales_outreach_store.get_outreach("OUT-R2-LOST-M")["stage"]
        == "LOST",
    )

    make_outreach("OUT-R2-LOST-P")
    for dest in ("SENT", "WAITING_REPLY", "REPLIED", "MEETING", "PROPOSAL"):
        sales_outreach_store.update_stage("OUT-R2-LOST-P", dest)
    lost_p = transition_stage("OUT-R2-LOST-P", "LOST")
    results.check(
        "pipeline PROPOSAL -> LOST succeeds",
        lost_p["ok"] is True
        and sales_outreach_store.get_outreach("OUT-R2-LOST-P")["stage"]
        == "LOST",
    )

    make_outreach("OUT-R2-REPLY")
    sales_outreach_store.update_stage("OUT-R2-REPLY", "SENT")
    replied = sales_outreach_store.record_inbound_reply(
        "OUT-R2-REPLY",
        "Thanks",
    )
    results.check(
        "pipeline SENT -> REPLIED via inbound reply succeeds",
        replied is True
        and sales_outreach_store.get_outreach("OUT-R2-REPLY")["stage"]
        == "REPLIED",
    )


def test_pipeline_invalid_and_stale(results, tmp_dir):
    point_store_at_temp(
        sales_outreach_store,
        tmp_dir,
        "sales.db",
        extra=sales_extra,
    )

    make_outreach("OUT-R2-BAD")
    skip = transition_stage("OUT-R2-BAD", "WAITING_REPLY")
    skip_won = transition_stage("OUT-R2-BAD", "WON")
    after = sales_outreach_store.get_outreach("OUT-R2-BAD")
    results.check(
        "invalid source -> destination transition fails",
        skip["ok"] is False
        and skip_won["ok"] is False
        and after["stage"] == "READY_TO_SEND",
    )

    sales_outreach_store.update_stage("OUT-R2-BAD", "SENT")
    dup = transition_stage("OUT-R2-BAD", "SENT")
    results.check(
        "duplicate/stale pipeline transition fails",
        dup["ok"] is False
        and sales_outreach_store.get_outreach("OUT-R2-BAD")["stage"]
        == "SENT",
    )

    sales_outreach_store.record_inbound_reply("OUT-R2-BAD", "first")
    dup_reply = sales_outreach_store.record_inbound_reply(
        "OUT-R2-BAD",
        "second",
    )
    results.check(
        "duplicate inbound reply does not re-advance",
        dup_reply is False
        and sales_outreach_store.get_outreach("OUT-R2-BAD")["stage"]
        == "REPLIED",
    )


def test_pipeline_concurrency(results, tmp_dir):
    point_store_at_temp(
        sales_outreach_store,
        tmp_dir,
        "sales.db",
        extra=sales_extra,
    )
    make_outreach("OUT-R2-CC")
    outcomes = []
    barrier = threading.Barrier(2)

    def attempt():
        barrier.wait()
        outcomes.append(
            transition_stage("OUT-R2-CC", "SENT")
        )

    threads = [
        threading.Thread(target=attempt),
        threading.Thread(target=attempt),
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    wins = sum(1 for item in outcomes if item["ok"])
    after = sales_outreach_store.get_outreach("OUT-R2-CC")
    results.check(
        "concurrent duplicate advancement allows exactly one winner",
        wins == 1 and after["stage"] == "SENT" and len(outcomes) == 2,
        f"wins={wins} stage={after['stage']}",
    )


def test_no_fd_leak(results, tmp_dir):
    point_store_at_temp(task_store, tmp_dir, "tasks.db")
    created = task_store.create_task("fd")
    before = count_open_fds()
    for _ in range(40):
        task_store.get_task(created["task_id"])
        transition_task_status(created["task_id"], "IN_PROGRESS")
        transition_task_status(created["task_id"], "DONE")
    after = count_open_fds()
    results.check(
        "R2 transitions do not accumulate FDs",
        after <= before + 2,
        f"process_fds {before}->{after}",
    )


def main():
    results = Results()

    with tempfile.TemporaryDirectory(prefix="atlas-r2-") as tmp_dir:
        assert_not_live(tmp_dir)
        print(f"Using temp dir: {tmp_dir}")
        print(f"Live data dir (untouched): {LIVE_DATA}")
        print()

        tests = [
            test_task_happy_path,
            test_task_unsupported,
            test_stale_expected_status,
            test_task_concurrency,
            test_approval_propagation,
            test_pipeline_supported,
            test_pipeline_invalid_and_stale,
            test_pipeline_concurrency,
            test_no_fd_leak,
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

    print("All isolated R2 state-transition tests passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
