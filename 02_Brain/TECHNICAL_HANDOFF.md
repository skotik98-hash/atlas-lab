# Atlas Technical Handoff

> Checkpoint for a **fresh agent** continuing Atlas Lab technical remediation.
> This file is state-transfer only. It does not start R5, change runtime code, or amend Decision Records.

**Document ID:** `TECHNICAL_HANDOFF.md`  
**Location:** `02_Brain/`  
**Status:** Active checkpoint — awaiting Founder review / next-agent bootstrap  
**Date:** 2026-08-15  
**Owner:** Founder (Анатолий) / next technical agent  
**Authority:** Runtime and git facts below were verified at write time. Canonical governance remains `05_CURRENT_STATE.md`, `06_DECISIONS.md`, and project briefs. This file does **not** replace those documents.

---

## A. Current baseline

Verified 2026-08-15 (local machine, immediately after R4 push; this handoff file is the only intended uncommitted change):

| Fact | Value |
|---|---|
| HEAD | `afe1c36e812ac01f6359f2cdeab143e4d1dc1101` |
| Subject | Add durable work ownership kernel |
| `origin/main` | `afe1c36e812ac01f6359f2cdeab143e4d1dc1101` (HEAD == origin/main) |
| `origin/main...main` | `0 0` (synchronized) |
| Working tree immediately after R4 push | clean (`git status --short` empty) |
| Parent of R4 | `71f00edc2dc22b46846cb90fd9d53a6130e9edaa` (post-R3 handoff commit) |

**Runtime (launchd; last verified at R4 push, 2026-08-15 ~16:56 +0300, and re-checked at this handoff write ~17:19 +0300):**

| Service | Label | PID | state | runs | last exit |
|---|---|---|---|---|---|
| Control Bot | `com.atlaslab.controlbot` | 22966 | running | 39 | 0 |
| Watcher | `com.atlaslab.watcher` | 22965 | running | 7 | Terminated: 15 (from controlled R3 migration `kickstart -k`; unchanged since) |

These PIDs are from the **controlled R3 live-migration restart** (2026-08-13 19:15:44 / 19:15:45). They were **not** restarted for the R3 push, the R3 handoff, R4 implementation, R4 blocker remediation, the R4 amend, the R4 push, or this handoff. No restart loop observed (`runs` stayed at 39 / 7).

Working directory: `04_AI/telegram_bot`. Python: repo `.venv`. Watcher interval: 15s.

**Roles:**

- **Telegram Control Bot** — owner-supervised operator UI: tasks, Sales Pipeline (manual confirmations; Atlas does not send company messages), approvals inbox, status/activity. Not an autonomous builder. Does **not** import `run_store`.
- **Watcher** — polls local git/working-tree/approval counts; logs activity; may notify via Telegram. Not Night Build. Not a job runner with leases. Does **not** import `run_store`.

**Atlas is still a supervised system.** It is **not** autonomous Night Build infrastructure. Night Build is a **target** (DR-2026-012), not live.

**R4 closure does NOT authorize autonomous worker execution.** The ownership kernel exists in code and isolated tests only. Live `04_AI/telegram_bot/data/runs.db` was **never created**. External execution remains disabled. Pre-FOP external-commercial-contact freeze remains in force (DR-2026-011).

Runtime code lives under `04_AI/telegram_bot/`. Live SQLite files are under `04_AI/telegram_bot/data/` (gitignored). Isolated tests must use temporary databases only.

---

## B. Completed remediation

Only **R1**, **R2**, **R3**, and **R4** have been formally assigned, accepted, and pushed. Do not invent additional R-numbers as completed. **R5 HAS NOT STARTED.**

### R1 — SQLite connection lifecycle

| | |
|---|---|
| Status | **CLOSED** and **pushed** |
| Commit | `5fa281bea7a0bd8e45e9df785730b928a627028f` |
| Message | Fix SQLite connection lifecycle leaks |

- Deterministic close via `sqlite_lifecycle.managed_connection` (`commit`/`rollback` + `finally: close()`).
- Stores: `task_store`, `approval_store`, `sales_outreach_store`, `activity_store`.
- `activity_store` PRAGMA setup failure also closes the raw connection.
- Live FD leak (watcher `approvals.db` accumulation) verified gone after restart.
- Independent Claude review: **PASS**.
- Tests: `04_AI/telegram_bot/test_sqlite_lifecycle.py` — **21 passed / 0 failed**.

### R2 — Atomic state transitions

| | |
|---|---|
| Status | **CLOSED** and **pushed** |
| Commit | `0f2451bdc6c6f4ee302d76396dfe01bab1872cfe` |
| Message | Enforce atomic state transitions |

- Task and Sales Pipeline transition authority is in the **store** layer, not UI guards.
- Compare-and-set: `UPDATE ... WHERE id = ? AND status/stage IN (allowed sources)`; success iff `rowcount == 1`.
- Terminal task resurrection blocked (`DONE` / `CANCELLED` cannot be moved to `IN_PROGRESS` or `BLOCKED`).
- `completed_at` set on terminal entry; non-terminal updates do not clear it.
- Stale/concurrent task and pipeline mutations rejected (exactly one winner).
- Approval **propagation** into tasks uses `apply_task_approval_decision` and checks the result. Decision durability itself was completed in **R3**.
- Independent Claude review: **PASS**. Live runtime smoke under R2 code: **PASS**.
- Tests: `04_AI/telegram_bot/test_state_transitions.py` — **28 passed / 0 failed**.

**Authoritative graphs after R2 (do not expand without Founder instruction):**

Tasks: `NEW|WAITING_APPROVAL → IN_PROGRESS`; `IN_PROGRESS → DONE`; `NEW|IN_PROGRESS|WAITING_APPROVAL → BLOCKED`.  
`WAITING_APPROVAL` has **no current writer**; those sources are dormant. Telegram start remains `NEW → IN_PROGRESS` only.

Pipeline: `READY_TO_SEND → SENT → WAITING_REPLY → REPLIED → MEETING → PROPOSAL → WON`; `MEETING|PROPOSAL → LOST`; inbound reply `SENT|WAITING_REPLY → REPLIED`.

### R3 — Durable approval-to-task propagation

| | |
|---|---|
| Status | **CLOSED** and **pushed** |
| Commit | `3d063764886fabacc99967dfcd82eb9fec86fed5` |
| Message | Make approval-to-task propagation durable |
| Files | `approval_store.py`, `bot.py`, `test_approval_durability.py` |

- Explicit `approvals.task_id` is the authoritative approval→task link. Production bot no longer parses `TASK-*` from `approval_id`.
- Decision CAS checks `rowcount == 1`. Linked rows mark `propagation_status=PENDING` until `APPLIED` or `INCOMPATIBLE`.
- Crash between approval commit and task write remains `PENDING` and is retried by a duplicate callback or `recover_pending_propagations()` (Control Bot `post_init`).
- Duplicate callbacks after `APPLIED` / `INCOMPATIBLE` do not re-run task writes.
- Concurrent schema init (B-1): `initialize()` uses a dedicated connection (`timeout=30`, `PRAGMA busy_timeout=30000`) and `BEGIN IMMEDIATE`; `_add_column_if_missing()` re-reads columns immediately before each `ALTER`.
- External commercial/action execution is **still not performed**. R3 durable-couples approval **decision → task write** only.

**R3 verification history (all PASS; blocking findings at final acceptance: NONE; rollback required: NO):**

- Cursor implementation review
- Targeted read-only review
- Integration reachability review
- Independent Claude review
- B-1 blocking migration-race finding (`duplicate column name: task_id` under concurrent `initialize()`)
- B-1 remediation
- Independent Claude B-1 re-review: **PASS**
- Controlled live migration verification: **PASS**
- Final independent Claude live acceptance review: **PASS**

**Regression at R3 close:**

| Suite | Result |
|---|---|
| R1 `test_sqlite_lifecycle.py` | **21 passed / 0 failed** |
| R2 `test_state_transitions.py` | **28 passed / 0 failed** |
| R3 `test_approval_durability.py` | **36 passed / 0 failed** |

**Live `approvals.db` migration (controlled verification, 2026-08-13 ~19:15 +0300):**

- Byte-for-byte backup **before** restart: `04_AI/telegram_bot/data/backups/approvals.db.pre-r3-20260813-191527` (gitignored `data/`)
- Source and backup size: **12288** bytes
- SHA-256 (matched before restart): `bc6435d01cb38150a31c7b7aba300a2653438835333a259cfa1f3115685269e9`
- After migration: `task_id`, `propagation_status`, `propagation_error` present; indexes `idx_approvals_task_id` and `idx_approvals_propagation` present
- Historical rows preserved; row count **5 / 5**; historical `task_id=NULL`, `propagation_status=NONE`, `propagation_error=NULL`
- No partial migration; no duplicate columns; no `OperationalError` / database locked / duplicate-column error in logs
- Control Bot and Watcher restarted **only** for this controlled migration (`launchctl kickstart -k`; plists not reinstalled). They remained stable afterward (PIDs 22966 / 22965; no restart loop)
- `tasks.db` and `sales_outreach.db` SHA-256 unchanged; no task / pipeline / outreach / approval-decision mutation

### R4 — Durable work ownership kernel

| | |
|---|---|
| Status | **CLOSED** and **pushed** |
| Commit | `afe1c36e812ac01f6359f2cdeab143e4d1dc1101` |
| Message | Add durable work ownership kernel |
| Files | `04_AI/telegram_bot/run_store.py`, `04_AI/telegram_bot/test_run_durability.py` |
| Parent | `71f00edc2dc22b46846cb90fd9d53a6130e9edaa` |

R4 is a **durable runs / attempts ownership kernel** only. It is **not** a live worker, not Night Build, and not production-wired. `bot.py` and `watcher.py` do **not** import `run_store`. Live `data/runs.db` does **not** exist.

**Functionality (isolated kernel; no autonomous execution):**

- Durable `runs` / `attempts` ownership state in SQLite
- Atomic lease acquisition (`BEGIN IMMEDIATE` + CAS)
- Stale / wrong-worker rejection
- Lease heartbeats (extend only; cannot shorten)
- Completion / failure ownership validation
- Expired lease reclamation
- `MAX_ATTEMPTS = 5` retry cap (no sixth attempt; exhausted run becomes `FAILED`)
- Rollback-safe attempt creation (`fail_after_attempt_insert` test hook)
- Canonical UTC timestamp handling for all public `now=` APIs

**Independently discovered R4 blockers and resolution:**

| ID | Finding | Resolution |
|---|---|---|
| B-1 | Concurrent first-touch `initialize()` of a fresh runs DB failed with `sqlite3.OperationalError: database is locked` at `PRAGMA journal_mode=WAL` | **FIXED** by removing the journal-mode conversion. R4 init matches the proven R3 pattern: `timeout=30`, `PRAGMA busy_timeout=30000`, `isolation_level=None`, `BEGIN IMMEDIATE`, `CREATE TABLE` / `CREATE INDEX IF NOT EXISTS`, `COMMIT`, rollback on exception, deterministic close. Correctness relies on transactional serialization, not WAL. |
| B-2 | Non-canonical timezone offsets preserved in stored ISO strings; SQLite lexical `lease_until <= now` could disagree with Python chronological comparison (premature reclaim / late reclaim; double-execution window) | **FIXED** by canonicalizing every accepted aware timestamp to `timezone.utc` before serialization and comparison. Stored form is UTC ISO with `+00:00`. Equivalent instants (`+02:00` / `-05:00` / `+00:00`) serialize identically. |
| B-3 | Naive / offset-less timestamps could be stored, then compared against aware UTC datetimes (`TypeError: can't compare offset-naive and offset-aware datetimes`) | **FIXED** by rejecting naive `datetime` objects, offset-less ISO strings, and malformed timestamps with `ValueError` **before** any DB mutation. Naive input is not guessed to be UTC. |

**Final independent acceptance:** **PASS — R4 READY TO PUSH**. Blocking findings: **NONE**. Push of `afe1c36e812ac01f6359f2cdeab143e4d1dc1101` to `origin/main` completed successfully (`71f00ed..afe1c36`).

**Verification evidence:**

| Check | Result |
|---|---|
| Final R4 suite `test_run_durability.py` | **84 passed / 0 failed** |
| Consecutive complete R4 runs during blocker re-review | **12 / 12** passed at 84/84 each |
| Final post-amend independent verification | **84 / 0** repeatedly; verdict **PASS — R4 READY TO PUSH** |
| R1 regression | **21 passed / 0 failed** |
| R2 regression | **28 passed / 0 failed** |
| R3 regression | **36 passed / 0 failed** |
| Cold-start concurrency after B-1 fix | **zero** lock failures (2 / 8 / 16 processes, multiple rounds, brand-new temp DB each round; independent re-review: 0 failures across 1,820 cold-start processes) |
| Ownership / concurrency regressions | **none** (acquire one-winner, reclaim one-winner, stale-worker rejection, retry cap, rollback) |
| FD lifecycle | **intact** (R4 suite FD check stable; R1 21/0) |
| Live `data/runs.db` | **never created** |
| Live `tasks.db` / `approvals.db` / `sales_outreach.db` | **not modified** by R4 verification or push |
| Telegram / external actions | **none** |
| Control Bot / Watcher | **not restarted** for R4 (PIDs 22966 / 22965; `runs` 39 / 7 at R4 push verification) |

**R4 non-blocking observations (carry-forward only; do not fix without Founder instruction):**

1. **NB-1:** Falsy `now` values currently fall back to wall-clock time instead of raising because of the existing `now or utc_now()` idiom. Explicitly non-blocking.
2. Latent `rowcount != 1` early-return paths in `heartbeat` / `complete_attempt` / `fail_attempt` are safe today because `BEGIN IMMEDIATE` makes the split-state path unreachable, but should be hardened before locking assumptions are relaxed.
3. SQLite uses **delete** journal mode for `runs.db` rather than WAL. This is correct at current R4 scale (serialized `BEGIN IMMEDIATE`) but should be reconsidered if R5 or later introduces a larger concurrent worker fleet.
4. Test-only failure hook `fail_after_attempt_insert` remains production-importable (default `False`); accepted as non-blocking for R4, same class as R3 test hooks.

Other previously noted non-blocking items (`run_id NOT NULL`, status CHECK constraints, redundant `idx_attempts_run_id`, unused `CANCELLED`, no FK, redundant `initialize()` calls, compileall `__pycache__`, inconsistent heartbeat rejection shape) remain carry-forward observations. They did **not** block R4 close.

---

## C. Remaining technical remediation

**R-numbers beyond R4 are not assigned.** The next approved block would be named R5 in process only. Scope of R5 is **not** defined here. **R5 HAS NOT STARTED.**

Classifications use current repo/runtime evidence only. Do **not** mark **OPEN** or **PARTIALLY ADDRESSED** rows as done without a Founder-accepted commit.

| Area | Status | Evidence |
|---|---|---|
| SQLite connection close (R1) | **CLOSED** | `managed_connection`; live FD smoke |
| Task/pipeline expected-source transitions (R2) | **CLOSED** | store `WHERE` + tests |
| Approval-to-task propagation durability (R3) | **CLOSED** | `task_id` + `propagation_status` + CAS `rowcount` + `recover_pending_propagations`; live migration PASS |
| Durable run / attempt / lease / heartbeat kernel (R4) | **CLOSED** | `run_store.py` ownership kernel pushed (`afe1c36`); isolated tests 84/0. **Not** production-wired. No live `runs.db`. R4 does **not** authorize autonomous workers |
| Autonomous worker execution / Night Build runner | **OPEN** | Kernel exists; Control Bot and Watcher do not import `run_store`; no live worker process |
| Automatic external execution after approval | **OPEN** | `bot.py` still does not execute the approved external action; R3 stops at the task write |
| Production wiring of `create_approval(task_id=...)` | **OPEN** | Only production caller is `send_approval.py`, which does **not** pass `task_id`. No current reachable production path creates a linked approval. Linked durability is live only when a caller sets `task_id` |
| Cross-DB atomic commit (approvals + tasks) | **OPEN** | Two SQLite files. R3 is detectable + recoverable two-phase, not one transaction |
| Checkpoint / crash recovery / reconciliation (beyond approval PENDING retry and R4 reclaim API) | **OPEN** | `recover_pending_propagations()` runs on Control Bot `post_init` only. `reclaim_expired_leases()` exists in `run_store` but is not scheduled. Watcher does not recover pending propagations or expired leases |
| Transactional outbox (multi-step effects) | **OPEN** | No outbox. Owner “I sent” is still two updates: `SENT` then `WAITING_REPLY` |
| Watcher notification delivery durability | **OPEN** | `notifier.py` sends Telegram; no durable delivery/retry store. Watcher stdout to file is block-buffered (log flush lags; process health is not log-mtime) |
| Two-step Sales Pipeline send atomicity | **OPEN** | Intentionally out of R2/R3/R4; crash between steps can leave `SENT` |
| Inbound-reply metadata concurrency | **OPEN** | Stage advance is atomic; `metadata_json` is still read-modify-write |
| Truthful runtime health / heartbeat / last-success | **OPEN** | `atlas_status.py` is local git + approval counts; no process heartbeat / last-success field |
| Git synchronization truth and fetch policy | **OPEN** | `atlas_status.git()` does **not** `fetch`; ahead/behind is local-only |
| Centralized error handling / durable operational failure reporting | **OPEN** | Watcher prints exception type; no durable failure ledger |
| SQLite schema constraints / migrations / foreign keys **beyond R3/R4** | **PARTIALLY ADDRESSED** | Approvals: additive `ALTER` under `BEGIN IMMEDIATE`. R4 runs/attempts: `CREATE TABLE IF NOT EXISTS` under `BEGIN IMMEDIATE`. No migration runner. No FKs |
| Backup / restore / migration procedures | **PARTIALLY ADDRESSED** | One-off pre-R3 `approvals.db` backup exists under `data/backups/` (hash-verified). No documented general backup/restore SOP for other DBs. No live `runs.db` yet |
| launchd singleton / crash-loop / log rotation | **PARTIALLY ADDRESSED** | `KeepAlive` in LaunchAgents; no `ThrottleInterval` / log rotation in install script |
| Runtime / client-data permissions | **OPEN** | `data/` local files; no extra OS permission model beyond gitignore |
| Repository-wide secret / runtime-data safeguards | **PARTIALLY ADDRESSED** | `04_AI/telegram_bot/.gitignore` ignores `.env` and `data/`; not a full repo secret scan/policy |
| Automated concurrency / restart / recovery tests | **PARTIALLY ADDRESSED** | R1 FD tests, R2 two-thread CAS tests, R3 concurrent schema-init + pending-recovery tests, R4 multiprocess acquire / reclaim / cold-init tests exist. No automated launchd crash-restart/recovery suite |
| Idempotency / duplicate-effect prevention | **PARTIALLY ADDRESSED** | R2 prevents duplicate **state** advances. R3 retries pending task propagation idempotently. R4 `complete_attempt` is idempotent for the current owner (`ALREADY_SUCCEEDED`). No idempotency keys for notifications or other effects |

**R3 non-blocking observations that remain applicable:**

1. Dest-match is **status-only**: if the task is already at the destination (`IN_PROGRESS` / `BLOCKED`), propagation is marked `APPLIED` even if this approval did not cause the move.
2. Historical live `TASK-*` approval rows were **not** backfilled (`task_id` remains `NULL`; recovery skips them). Already-decided historical duplicates stay decided.
3. `decide_approval` string wrapper still returns `"APPROVED"`/`"REJECTED"` and hides `INCOMPATIBLE`. Bot uses the dict API (`apply_approval_decision`).
4. Recovered duplicate callback UI shows “already decided” and does not mention that task sync just completed.
5. Test-only hooks `fail_after_decision` / `fail_after_task_before_mark` exist in production `approval_store.py` (default `False`).
6. `WAITING_APPROVAL` remains a dormant task source (no current writer).

**R4 non-blocking observations:** listed under R4 above (NB-1 and related carry-forwards). Do not treat them as R5 scope unless a separate Founder instruction says so.

---

## D. Next step

**NEXT EXECUTION PHASE:** Technical Remediation **R5** (name only; not scoped)

**R5 HAS NOT STARTED.**

**Night Build is still NOT live.** External execution remains disabled. Pre-FOP freeze remains in force. R4 closure does **not** authorize autonomous worker execution.

The fresh agent must:

1. Re-read this handoff.
2. Inspect the repository.
3. Verify HEAD / sync / runtime.
4. Wait for a **separate Founder-approved R5 instruction**.

Do not choose R5 scope from this list without that instruction. Do not implement R5 in the same step as reading this file. Do not wire `run_store` into Control Bot, Watcher, or launchd without that instruction.

---

## E. Safety / governance boundaries

Canonical: [DR-2026-011](06_DECISIONS.md#dr-2026-011-pre-fop-period-no-external-commercial-contact) (Pre-FOP freeze). Do not rewrite that DR.

**Until FOP registration:**

- no external commercial outreach
- no contacting real companies (including Daniel Cobb / Gosselin)
- no real sales messages
- no OUT records intended for sending
- no payment collection
- no external commercial execution

**Allowed:**

- internal research
- real-company research as **internal benchmark only**
- synthetic orders
- internal simulations
- factory development (internal)
- isolated testing
- technical remediation

External execution, production deploy, spending, and credentials remain **Founder-gated** (DR-2026-012).

---

## F. Product / factory direction (reference only)

Canonical: [DR-2026-012](06_DECISIONS.md) and `01_Projects/P-002_ATLAS_BUILD_FACTORY/PROJECT_BRIEF.md`. Do not redesign here.

Five factories:

1. Atlas Bot Factory  
2. Atlas Web Factory  
3. Atlas Business App / Mini-CRM Factory  
4. Atlas AI Office Factory  
5. Atlas Document & Workflow Factory  

Sales / Recruiting / Support / Operations / Marketing are **packages of AI Office Factory**, not separate product codebases.

**Night Build is a target, not a current live capability.**

This handoff is not a product roadmap.

---

## G. Fresh-agent boot procedure

1. Read this file.
2. Read `02_Brain/05_CURRENT_STATE.md`, `02_Brain/06_DECISIONS.md` (especially DR-2026-011, DR-2026-012), and the relevant project brief (`P-001` / `P-002` as applicable).
3. Inspect actual `git rev-parse HEAD`, `git status --short`, `git rev-list --left-right --count origin/main...main`.
4. Inspect the **code** for the remediation being requested — do not trust chat summaries.
5. If runtime-relevant, inspect launchd PIDs/state and logs under `04_AI/telegram_bot/data/` **read-only** unless instructed otherwise.
6. Never assume a previous chat’s claim is true if repo/runtime evidence can verify it.
7. Work on **one** Founder-approved remediation block at a time.
8. Stop for Founder review before commit/push unless explicitly authorized.
9. Isolated tests only on temporary databases. Do not write live Atlas DBs for tests. Do not create live `data/runs.db` unless a Founder instruction explicitly requires it.
10. Do not contact companies. Do not start Night Build. Do not treat factories as shipped.
11. Do not start R5 unless a separate Founder instruction names its scope.
12. Do not treat R4 as authorization to run autonomous workers.

**Note:** Some sentences in `05_CURRENT_STATE.md` still describe an earlier “no software yet” / pre-runtime posture and do not yet record R1–R4. That document remains canonical for **governance instance values**. For **runtime remediation status**, this handoff and `git log` on `04_AI/telegram_bot/` win until Current State is explicitly updated by Founder instruction.

---

## Key paths

| Path | Role |
|---|---|
| `04_AI/telegram_bot/sqlite_lifecycle.py` | R1 connection helper |
| `04_AI/telegram_bot/task_store.py` | Tasks + R2 transitions |
| `04_AI/telegram_bot/sales_outreach_store.py` | Pipeline + R2 transitions |
| `04_AI/telegram_bot/approval_store.py` | Approvals (R1 close + R3 durable propagation / schema init) |
| `04_AI/telegram_bot/activity_store.py` | Activity log (R1) |
| `04_AI/telegram_bot/run_store.py` | R4 durable run / attempt / lease kernel (**not** production-wired) |
| `04_AI/telegram_bot/bot.py` | Telegram Control Bot (`apply_approval_decision`, `recover_pending_propagations`; does **not** import `run_store`) |
| `04_AI/telegram_bot/watcher.py` | Watcher (does **not** import `run_store`) |
| `04_AI/telegram_bot/send_approval.py` | Only production `create_approval()` caller (does not pass `task_id`) |
| `04_AI/telegram_bot/test_sqlite_lifecycle.py` | R1 tests (21) |
| `04_AI/telegram_bot/test_state_transitions.py` | R2 tests (28) |
| `04_AI/telegram_bot/test_approval_durability.py` | R3 tests (36) |
| `04_AI/telegram_bot/test_run_durability.py` | R4 tests (84) |
| `04_AI/telegram_bot/scripts/install_services.sh` | launchd install (do not reinstall unless asked) |
| `04_AI/telegram_bot/data/backups/approvals.db.pre-r3-20260813-191527` | Pre-R3 live DB backup (gitignored) |
