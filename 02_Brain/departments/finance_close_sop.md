# Monthly Financial Close SOP

> The step-by-step procedure Finance follows to close Atlas's books each month, per [Phase 1 exit criterion P1.5](04_ROADMAP.md#phase-1--operating-kernel) and Roadmap milestone **M-F-001** ("Chart of accounts / close SOP"). This is the *procedure* — inputs, steps, outputs, ownership, cadence, evidence, and escalation — not a chart of accounts, and not a record that any close has occurred.

**Document ID:** `finance_close_sop.md`
**Location:** `02_Brain/departments/`
**Status:** Draft
**Version:** 1.0
**Owner:** Анатолий (Finance hat)
**Last updated:** 2026-08-09
**Review date:** 2027-02-09

---

## Purpose

This document satisfies the **documentary half** of [Phase 1 exit criterion P1.5](04_ROADMAP.md#phase-1--operating-kernel) ("Monthly financial close process documented — Finance SOP + actual closes"). It is a T4-tier SOP per [`00_ATLAS_BRAIN.md` § Documentation Standards](00_ATLAS_BRAIN.md#documentation-standards) (T4 example: "Monthly close SOP"), and is the deliverable `finance_playbook.md` explicitly deferred: *"The full close SOP (T4) is a distinct, not-yet-written deliverable."*

**What this document is:** the defined procedure a close will follow.
**What this document is not:** evidence that a close has happened. See [Honest current status](#honest-current-status).

## Relationship to canonical documents

This SOP does not restate, and instead links to:

- [`03_ORGANIZATION.md` § Department: Finance](03_ORGANIZATION.md#department-finance) — canonical scope, ownership table, KPIs, decision authority, escalation rules.
- [`00_ATLAS_BRAIN.md` § Capital Allocation Philosophy § Capital buckets](00_ATLAS_BRAIN.md#capital-allocation-philosophy) — bucket definitions; live percentages remain TBD in `05_CURRENT_STATE.md`.
- [`00_ATLAS_BRAIN.md` § Company Lifecycle § Integration standards](00_ATLAS_BRAIN.md#company-lifecycle) — "Financial reporting: Atlas chart of accounts mapping, monthly close, 30 days" — this SOP is the procedure that row points to once an asset is in Integrate.
- `finance_playbook.md` § Execution guidance — the T3 cadence commitment this T4 SOP supplies the mechanics for.

This document does **not** define a chart of accounts. Per [`05_CURRENT_STATE.md` § Current Finance](05_CURRENT_STATE.md#current-finance), no chart of accounts, accounting system, or bookkeeping process exists yet — building one is separate, not-yet-started work, out of scope here, and would require real entity/banking facts this SOP does not have and must not invent.

## Scope & prerequisites

This SOP defines the **procedure**, which can be written before any transaction exists — the same "ready template, unexercised" pattern already used by `automation_registry.md` and `integration_scorecard.md`. Real closes cannot run until the following prerequisites exist (none exist today):

| Prerequisite | Status |
|---|---|
| Confirmed legal entity | Unknown/TBD — see `05_CURRENT_STATE.md` § Current Infrastructure |
| Chart of accounts | Not yet built |
| Bank/financial accounts opened | Unknown/TBD |
| At least one recorded transaction | None to date |

## Monthly close procedure

A close cycle runs once a defined **period end** (last calendar day of the month) has passed. "Day" below = business days after period end.

| Step | Day | Action | Input | Output |
|---|---|---|---|---|
| 1 | Day 1 | Freeze the period — no new transactions dated inside the closing month | Transaction log (once one exists) | Frozen transaction set for the period |
| 2 | Day 1–2 | Reconcile every account (bank, capital, any ledger) against source statements | Bank/account statements; internal transaction log | Reconciliation record, one per account, with any variance noted |
| 3 | Day 2–3 | Map reconciled transactions to the chart of accounts | Reconciled transactions; chart of accounts (once it exists) | Categorized ledger for the period |
| 4 | Day 3–4 | Draft period financial statements (P&L, balance sheet, cash position) | Categorized ledger | Draft statements |
| 5 | Day 4 | Compute budget-vs-actual variance; draft commentary for any variance beyond the then-current threshold | Draft statements; prior-period actuals; budget/target (once set) | Variance commentary draft |
| 6 | Day 5 | Finance-hat review and sign-off | Draft statements + variance commentary | Signed-off close statements |
| 7 | Day 5 | File the Close Record (see [Evidence requirements](#evidence-requirements-the-close-record)) in `03_Knowledge/`; update `05_CURRENT_STATE.md` § Current Finance actual-vs-target | Signed-off close statements | Filed Close Record; updated Current State |

**Proposed cadence:** close completes by **business day 5** after period end — inside the ≤10-business-day KPI target already defined in [`03_ORGANIZATION.md` § Department: Finance § KPIs](03_ORGANIZATION.md#department-finance). This cadence is a proposed policy pending Finance-hat confirmation at the first real close; it is not yet evidenced practice.

## Roles & ownership

| Role | Owner | Note |
|---|---|---|
| Process owner (accountable for the close running and completing) | Анатолий (Finance hat) | Per [`03_ORGANIZATION.md` § Department: Finance § Ownership](03_ORGANIZATION.md#department-finance) ("Holding financial statements — Finance head") |
| AI assist (draft close summary/variance commentary only) | Candidate — see `automation_registry.md` § AR-004 | **L0 (Manual), proposed only.** This SOP's existence is a precondition AR-004 was waiting on, not evidence AR-004 has run |
| Sign-off authority | Анатолий (Finance hat) | Per [`03_ORGANIZATION.md` § Department: Finance § Decision authority](03_ORGANIZATION.md#department-finance) |

## Evidence requirements (the Close Record)

A close is only evidenced by a **Close Record** — a per-period instance (not this template) containing:

- Period covered
- Each step above, ticked with date completed
- The reconciliation record(s) from Step 2
- Signed-off statements from Step 6
- Filed location in `03_Knowledge/` (same instantiation pattern `PROJECT_BRIEF_P-001_MARKET_SCREEN_001.md` set for the Project Lifecycle template — a real, separate artifact, never edited into this template)
- The `05_CURRENT_STATE.md` § Current Finance row updated with the actual-vs-target result for that period

**No Close Record exists yet.** This template does not create one — see [Honest current status](#honest-current-status).

## Exception / escalation handling

This SOP does not define new escalation authority — it routes into the existing rules:

- Any reconciliation variance beyond the (currently TBD) threshold, or any liquidity/misstatement/compliance trigger, escalates per [`00_ATLAS_BRAIN.md` § Escalation](00_ATLAS_BRAIN.md#escalation) and [`03_ORGANIZATION.md` § Department: Finance § Escalation rules](03_ORGANIZATION.md#department-finance) — linked, not restated.
- A close that cannot complete within the proposed 5-business-day cadence is itself a **proposed** escalation trigger to Brain, pending confirmation alongside the cadence above — not yet an amendment to the canonical Escalation rules table, once the numeric variance threshold is set (see [Phase 1 exit criterion P1.7](04_ROADMAP.md#phase-1--operating-kernel), still Partially satisfied).
- Until real escalation threshold values exist, any exception during a close defaults to full escalation to Brain — the conservative default per [Truth over comfort](02_FOUNDING_PRINCIPLES.md#truth-over-comfort), not a gap in this SOP.

## Completion criteria

- **For a single close** (once real transactions exist): all 7 steps above complete, signed off, and filed as a Close Record within the KPI window.
- **For this SOP document:** it exists, is internally consistent with canonical documents, and defines every field required to run a close — this is the entirety of what the *documentary* half of P1.5 requires.
- **For P1.5 as a whole:** this SOP satisfies only the documentary half. P1.5 additionally requires "actual closes" — evidenced, plural closes — which cannot exist until Atlas has a chart of accounts and at least one real financial transaction. See below.

## Honest current status

**Procedure only — zero closes have ever occurred.** Per [`05_CURRENT_STATE.md` § Current Finance](05_CURRENT_STATE.md#current-finance) ("No chart of accounts, no accounting software, no bookkeeping process, and no monthly close cadence exists") and § Current KPIs ("Close timeline... N/A — no close process exists"), there is no live instance of this procedure anywhere in the vault, and this document does not claim otherwise. This is the same "ready template, honestly unexercised" discipline already applied in `automation_registry.md` and `integration_scorecard.md`.

## Status of this document

This is a **Draft T4 SOP**, created to advance [Phase 1 exit criterion P1.5](04_ROADMAP.md#phase-1--operating-kernel) (Milestone **M-F-001**, "Chart of accounts / close SOP" — this document satisfies the close-SOP half; the chart of accounts remains separate, unbuilt work). At [Org Stage 0](03_ORGANIZATION.md#organizational-scaling), no chart of accounts, close process, or capital deployed exists — every field above is proposed procedure, not evidenced practice, per [Truth over comfort](02_FOUNDING_PRINCIPLES.md#truth-over-comfort).

## Cross references

- [`03_ORGANIZATION.md` § Department: Finance](03_ORGANIZATION.md#department-finance) — canonical scope, ownership, KPIs, decision authority, escalation rules
- [`00_ATLAS_BRAIN.md` § Capital Allocation Philosophy](00_ATLAS_BRAIN.md#capital-allocation-philosophy) — capital buckets this close feeds actual-vs-target reporting into
- [`00_ATLAS_BRAIN.md` § Company Lifecycle § Integration standards](00_ATLAS_BRAIN.md#company-lifecycle) — "Financial reporting" row this SOP operationalizes for any future portfolio asset
- [`00_ATLAS_BRAIN.md` § Documentation Standards](00_ATLAS_BRAIN.md#documentation-standards) — T4 tier definition
- `finance_playbook.md` — the T3 stub this T4 SOP fulfills the deferred procedure for
- `automation_registry.md` § AR-004 — the close-assist automation candidate this SOP is a prerequisite for, not evidence of
- [`05_CURRENT_STATE.md` § Current Finance](05_CURRENT_STATE.md#current-finance) — live confirmation that no close has occurred (read, not modified, by this document)
- [`04_ROADMAP.md` § Phase 1 — Operating Kernel](04_ROADMAP.md#phase-1--operating-kernel) — P1.5 exit criterion this document partially evidences
- [`07_GLOSSARY.md`](07_GLOSSARY.md) — canonical definitions (SOP (Standard Operating Procedure), Financial Close, Chart of Accounts, Capital Bucket)

---

*This is a Draft T4 SOP, not yet Active. It supplements — and does not duplicate — `finance_playbook.md` or `00_ATLAS_BRAIN.md`.*
