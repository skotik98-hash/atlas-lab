# Atlas Technical Handoff

> Checkpoint for a **fresh agent** continuing Atlas Lab technical remediation.
> This file is state-transfer only. It does not start R3, change runtime code, or amend Decision Records.

**Document ID:** `TECHNICAL_HANDOFF.md`  
**Location:** `02_Brain/`  
**Status:** Active checkpoint — awaiting Founder review / next-agent bootstrap  
**Date:** 2026-08-13  
**Owner:** Founder (Анатолий) / next technical agent  
**Authority:** Runtime and git facts below were verified at write time. Canonical governance remains `05_CURRENT_STATE.md`, `06_DECISIONS.md`, and project briefs. This file does **not** replace those documents.

---

## A. Current baseline

Verified 2026-08-13 (local machine, after R2 push):

| Fact | Value |
|---|---|
| HEAD | `0f2451bdc6c6f4ee302d76396dfe01bab1872cfe` |
| Subject | Enforce atomic state transitions |
| `origin/main...main` | `0 0` (synchronized) |
| Working tree | clean (before this uncommitted handoff file) |
| Parent | `5fa281bea7a0bd8e45e9df785730b928a627028f` (R1) |

**Runtime (launchd, same PIDs as R2 live smoke; not restarted for this checkpoint):**

| Service | Label | PID | state | runs | last exit |
|---|---|---|---|---|---|
| Control Bot | `com.atlaslab.controlbot` | 5569 | running | 38 | 0 |
| Watcher | `com.atlaslab.watcher` | 5571 | running | 6 | — |

Working directory: `04_AI/telegram_bot`. Python: repo `.venv`. Watcher interval: 15s.

**Roles:**

- **Telegram Control Bot** — owner-supervised operator UI: tasks, Sales Pipeline (manual confirmations; Atlas does not send company messages), approvals inbox, status/activity. Not an autonomous builder.
- **Watcher** — polls local git/working-tree/approval counts; logs activity; may notify via Telegram. Not Night Build. Not a job runner with leases.

**Atlas is still a supervised system.** It is **not** autonomous Night Build infrastructure. Night Build is a **target** (DR-2026-012), not live.

Runtime code lives under `04_AI/telegram_bot/`. Live SQLite files are under `04_AI/telegram_bot/data/` (gitignored). Isolated tests must use temporary databases only.

---

## B. Completed remediation

Only **R1** and **R2** have been formally assigned, accepted, and pushed. Do not invent additional R-numbers as completed.

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
- Approval **propagation** into tasks uses `apply_task_approval_decision` and checks the result. `decide_approval` itself was **not** redesigned.
- Independent Claude review: **PASS**. Live runtime smoke under R2 code: **PASS**.
- Tests: `04_AI/telegram_bot/test_state_transitions.py` — **28 passed / 0 failed**.
- Combined R1+R2: **49 passed / 0 failed**.

**Authoritative graphs after R2 (do not expand without Founder instruction):**

Tasks: `NEW|WAITING_APPROVAL → IN_PROGRESS`; `IN_PROGRESS → DONE`; `NEW|IN_PROGRESS|WAITING_APPROVAL → BLOCKED`.  
`WAITING_APPROVAL` has **no current writer**; those sources are dormant. Telegram start remains `NEW → IN_PROGRESS` only.

Pipeline: `READY_TO_SEND → SENT → WAITING_REPLY → REPLIED → MEETING → PROPOSAL → WON`; `MEETING|PROPOSAL → LOST`; inbound reply `SENT|WAITING_REPLY → REPLIED`.

---

## C. Remaining technical remediation

**R-numbers beyond R2 are not assigned.** The next approved block is named R3 in process only. Scope of R3 is **not** defined here.

Classifications use current repo/runtime evidence only.

| Area | Status | Evidence |
|---|---|---|
| SQLite connection close (R1) | **CLOSED** | `managed_connection`; live FD smoke |
| Task/pipeline expected-source transitions (R2) | **CLOSED** | store `WHERE` + tests |
| Approval-to-execution durability / transactional coupling | **OPEN** | Approval row commit, then separate task update, then **no** automatic external execution (`bot.py` still says action is not executed) |
| Approval decision concurrency / authoritative linkage | **PARTIALLY ADDRESSED** | `decide_approval` uses `UPDATE ... AND status = 'PENDING'`. Task link is **parsed** from `approval_id` (`TASK-NNNN-...`), not a foreign key. R2 only made the **task write** CAS-safe |
| Durable run / attempt / lease / heartbeat for autonomous work | **OPEN** | No run/attempt/lease tables or workers |
| Idempotency / duplicate-effect prevention | **PARTIALLY ADDRESSED** | R2 prevents duplicate **state** advances. No idempotency keys for notifications or other effects |
| Checkpoint / crash recovery / reconciliation | **OPEN** | No checkpoint or reconciler |
| Transactional outbox (multi-step effects) | **OPEN** | No outbox. Owner “I sent” is still two updates: `SENT` then `WAITING_REPLY` |
| Watcher notification delivery durability | **OPEN** | `notifier.py` sends Telegram; no durable delivery/retry store |
| Two-step Sales Pipeline send atomicity | **OPEN** | Intentionally out of R2; crash between steps can leave `SENT` |
| Inbound-reply metadata concurrency | **OPEN** | Stage advance is atomic; `metadata_json` is still read-modify-write |
| Truthful runtime health / heartbeat / last-success | **OPEN** | `atlas_status.py` is local git + approval counts; no process heartbeat / last-success field |
| Git synchronization truth and fetch policy | **OPEN** | `atlas_status.git()` does **not** `fetch`; ahead/behind is local-only |
| Centralized error handling / durable operational failure reporting | **OPEN** | Watcher prints exception type; no durable failure ledger |
| SQLite schema constraints / migrations / foreign keys | **OPEN** | `CREATE TABLE IF NOT EXISTS`; no migration runner; no FKs |
| Backup / restore / migration procedures | **OPEN** | Live DBs gitignored; no documented restore path |
| launchd singleton / crash-loop / log rotation | **PARTIALLY ADDRESSED** | `KeepAlive` in LaunchAgents; no `ThrottleInterval` / log rotation in install script |
| Runtime / client-data permissions | **OPEN** | `data/` local files; no extra OS permission model beyond gitignore |
| Repository-wide secret / runtime-data safeguards | **PARTIALLY ADDRESSED** | `04_AI/telegram_bot/.gitignore` ignores `.env` and `data/`; not a full repo secret scan/policy |
| Automated concurrency / restart / recovery tests | **PARTIALLY ADDRESSED** | R1 FD tests + R2 two-thread CAS tests exist. No crash-restart/recovery suite |

Do not mark any **OPEN** or **PARTIALLY ADDRESSED** row as done without a Founder-accepted commit.

---

## D. Next step

**NEXT EXECUTION PHASE:** Technical Remediation **R3**

**R3 HAS NOT STARTED.**

The fresh agent must:

1. Re-read this handoff.
2. Inspect the repository.
3. Verify HEAD / sync / runtime.
4. Wait for a **separate Founder-approved R3 instruction**.

Do not choose R3 scope from this list without that instruction.

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
9. Isolated tests only on temporary databases. Do not write live Atlas DBs for tests.
10. Do not contact companies. Do not start Night Build. Do not treat factories as shipped.

**Note:** Some sentences in `05_CURRENT_STATE.md` still describe an earlier “no software yet” posture. That document remains canonical for **governance instance values**. For **runtime remediation status**, this handoff and `git log` on `04_AI/telegram_bot/` win until Current State is explicitly updated by Founder instruction.

---

## Key paths

| Path | Role |
|---|---|
| `04_AI/telegram_bot/sqlite_lifecycle.py` | R1 connection helper |
| `04_AI/telegram_bot/task_store.py` | Tasks + R2 transitions |
| `04_AI/telegram_bot/sales_outreach_store.py` | Pipeline + R2 transitions |
| `04_AI/telegram_bot/approval_store.py` | Approvals (R1 close; decision engine not R2) |
| `04_AI/telegram_bot/activity_store.py` | Activity log (R1) |
| `04_AI/telegram_bot/bot.py` | Telegram Control Bot |
| `04_AI/telegram_bot/watcher.py` | Watcher |
| `04_AI/telegram_bot/test_sqlite_lifecycle.py` | R1 tests |
| `04_AI/telegram_bot/test_state_transitions.py` | R2 tests |
| `04_AI/telegram_bot/scripts/install_services.sh` | launchd install (do not reinstall unless asked) |
