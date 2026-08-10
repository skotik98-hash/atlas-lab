# AR-003 Automation Spec — T1–T5 Review-date staleness flagging

> Minimum automation specification for registry candidate AR-003, using the [Automation spec template](00_ATLAS_BRAIN.md#automation-standards). This document defines how a real staleness scan is executed and measured. It does **not** claim L1 or L2 maturity, Frequency eligibility, or Phase 1 exit criterion P1.4.

**Document ID:** `ar003_staleness_flagging_spec.md`
**Location:** `02_Brain/departments/`
**Status:** Draft
**Version:** 1.0
**Owner:** Анатолий (Knowledge hat) — per AR-003 registry Owner; Spec authored under AI-hat Spec step of the [AI adoption process](00_ATLAS_BRAIN.md#ai-adoption-process)
**Last updated:** 2026-08-10
**Review date:** 2027-02-10
**Registry candidate:** [AR-003](automation_registry.md#ar-003--t1t3-document-staleness-flagging)

---

## Automation spec fields (canonical template)

| Field | Entry |
|---|---|
| **Name** | AR-003 — T1–T5 document Review-date staleness flagging |
| **Owner** | Анатолий (Knowledge hat) |
| **SOP reference** | [`knowledge_playbook.md`](knowledge_playbook.md) § Execution guidance ("Staleness-flagging procedure") and checklist item "Flag any T1–T5 document past its `Review date`…" — provisional playbook procedure; this Spec supplies the executable mechanics |
| **Trigger** | Manual / ad hoc at a real Brain-hat or Knowledge-hat working session; or a future scheduled cadence once Frequency evidence exists. **Not** a same-session artificial re-run for Frequency credit |
| **Inputs** | (1) Reference date = calendar date of the run (YYYY-MM-DD). (2) Document headers containing a real `**Review date:**` field under in-scope paths (see Scope). (3) No secondary table (e.g. Current State document-status rows) may substitute for a missing source-header value |
| **Steps** | See [Deterministic processing steps](#deterministic-processing-steps) |
| **Outputs** | A Clear / Flagged / Invalid-or-Missing result table for human review only — see [Outputs](#outputs) |
| **Error handling** | Malformed, missing, ambiguous, or unreadable Review dates → classify **Invalid/Missing** with reason; do not guess. Tooling failures → abort run, record error, fall back to manual check |
| **Monitoring** | Per-run metrics in [Evidence / metrics](#evidence--metrics-to-collect-on-every-real-run); Evaluation updates live only in `automation_registry.md` AR-003 after human approval |
| **Maturity level** | **L0 (Manual)** — Prototype Run #1 completed 2026-08-10; not promoted |
| **Last tested** | 2026-08-10 (Prototype Run #1) |

---

## Purpose

Compare each in-scope document’s header `Review date` to the run’s reference date and produce a Clear / Flagged / Invalid-or-Missing list for the Knowledge hat. Aligns with AR-003 Purpose and Knowledge AI participation ("staleness detection"), without editing any document.

## Scope (explicit — resolves T1–T3 vs T1–T5 ambiguity)

**In scope for this Spec (matches Prototype Run #1 practice):**
- Real documents under `02_Brain/` and `03_Knowledge/` that carry a document-level metadata header with `**Review date:**`
- Includes T1–T5 artifacts that self-identify or function as governance/playbook/SOP/record documents with that header field

**Out of scope:**
- Template-placeholder Review date strings (`YYYY-MM-DD`, `[YYYY-MM-DD]`) inside example blocks
- Non-header / embedded Review dates (e.g. Decision Record body fields inside `06_DECISIONS.md`)
- Prose containing the word "review" without the exact field pattern `**Review date:**`
- `01_Projects/` working files unless/until a later Spec revision explicitly adds them
- Any write to document `Status`, archive, or content

**Note:** AR-003 registry Purpose still says "T1–T3". This Spec’s executable scope is the broader Run #1 practice (T1–T5 headers). Updating the registry Purpose line is **out of scope for this Spec create** and must be a separate, later edit if approved.

## Trigger

- **Primary (current):** Ad hoc at a real Brain/Knowledge working session
- **Future (not claimed live):** Scheduled (e.g. monthly) only after Frequency evidence exists
- **Invalid trigger for Frequency credit:** Multiple artificial executions in one session against unchanged intent solely to inflate run count

## Inputs

1. Reference date (run date)
2. In-scope file set as defined in Scope
3. For each file: first document-level `**Review date:**` value in the header block only (convention: within the opening metadata lines)

## Deterministic processing steps

1. Record run start timestamp (UTC).
2. Fix reference date `R` = today’s date for the run (YYYY-MM-DD).
3. Enumerate candidate files under Scope paths that contain `**Review date:**`.
4. For each match, apply exclusion rules in order:
   - If value is literally `YYYY-MM-DD` or `[YYYY-MM-DD]` → exclude as template placeholder (not a document row).
   - If the match is not the document-level header field (e.g. embedded DR body field) → exclude from document-staleness rows; may note in a separate "excluded matches" list for transparency.
   - If match is not the exact field pattern `**Review date:**` → ignore.
5. For each remaining document, take the header Review date value `D`:
   - If missing or unparseable as YYYY-MM-DD → **Invalid/Missing** + reason.
   - Else if `D < R` → **Flagged** + days overdue = `R - D`.
   - Else → **Clear**.
6. Never read a Review date from `05_CURRENT_STATE.md` (or any other secondary table) to fill a missing header.
7. Produce the Outputs table; record metrics; record run end timestamp.
8. Stop. Do not edit, archive, or change any `Status` field.

## Outputs

Chat-only or separately approved evidence note — **not** an automatic registry write:

| Column | Content |
|---|---|
| Document path | Relative path |
| Tier | Self-declared if present; else "not self-declared" (do not invent tier) |
| Review date | Exact header value or "(none)" |
| Result | Clear / Flagged / Invalid-or-Missing |
| Reason | Short deterministic reason |

Plus counts: total in-scope docs, Clear, Flagged, Invalid/Missing; elapsed time; errors.

## Guardrails

- May only flag / classify; must never edit, archive, rename, or change `Status`
- Must never invent a Review date
- Must never treat secondary-document claims as source-of-truth for a header field
- Must never Gate-certify, promote maturity, or update Frequency eligibility
- Must not write to `automation_registry.md` without a separate human-approved recording step

## Human-review points

1. Accept or reject the run result as valid Prototype/operational evidence
2. Decide action on each Flagged document (update, extend review date, archive — human only)
3. Decide action on each Invalid/Missing document (e.g. add missing `Review date` to `00_ATLAS_BRAIN.md`)
4. Approve any later Evaluation append to `automation_registry.md`
5. Approve any maturity/eligibility change (none implied by running this Spec)

## Owner

Анатолий (Knowledge hat) — accountable for exceptions and maintenance.  
AI hat owns registry tracking of this Spec’s existence; does not own Knowledge remediation decisions.

## Fallback procedure

If the automation/agent cannot complete a valid scan: Knowledge hat performs a manual header Review-date check using the same exclusion rules and outputs the same table format. Record that the run used Fallback.

## Evidence / metrics to collect on every real run

| Metric | Required |
|---|---|
| Run ID (Run #N) and UTC start/end / elapsed | Yes |
| Reference date | Yes |
| Documents in scope (count) | Yes |
| Clear / Flagged / Invalid-or-Missing counts | Yes |
| Guardrail violations (any edit) | Yes — target 0 |
| Unsupported / guessed dates | Yes — target 0 |
| Human sign-off that result was reviewed | Yes |
| Trigger type (ad hoc session / scheduled / fallback) | Yes |

Do not fabricate Frequency from same-session repeats.

## Mechanical vs human judgment (from Prototype Run #1)

### Made mechanical by this Spec (safe)

1. Exclude template placeholders `YYYY-MM-DD` / `[YYYY-MM-DD]`
2. Prefer first header `**Review date:**` only (exclude embedded DR-level dates)
3. Match exact field pattern `**Review date:**` (reject prose "review" false positives)
4. Read Review date only from the source document header — never from Current State claims
5. Date compare: parseable `D` vs reference `R` → Clear / Flagged

### Remain human / manual

1. What to do about Flagged or Invalid/Missing documents
2. Whether a given working session is a valid Frequency-triggering touchpoint
3. Whether tier labels should be inferred when not self-declared (Spec: report "not self-declared")
4. Whether to expand Scope beyond `02_Brain/` + `03_Knowledge/`
5. Whether to record the run into `automation_registry.md` and whether eligibility/maturity may change
6. Resolving the registry Purpose "T1–T3" vs this Spec’s T1–T5 executable scope (separate edit)

## How to record future Run #2 / Run #3

1. Execute this Spec read-only; present results in chat (or approved evidence note)
2. Human verifies metrics and guardrails
3. Only after approval: append measured results to AR-003 **Evaluation** in `automation_registry.md` (same two-line discipline as Run #1: Evaluation facts; Maturity stays L0 until promotion rules are met)
4. Do not change Frequency/Documentation/Baseline rows unless the underlying criterion is honestly newly met
5. Do not promote L0→L1/L2 in the same edit as a single run append

## Honest status toward maturity (no premature claim)

| Stage | Status under this Spec |
|---|---|
| Identify | Done (AR-003 exists) |
| Spec | This document — **proposed / to be created** |
| Prototype | Run #1 done; further runs use this Spec |
| Evaluate | **Not complete** — needs 2–4 weeks against baseline and repeated real runs |
| Deploy | **Not done** |
| Document | Playbook pointer exists; full SOP still thin |
| Maturity | **L0** until Evaluation evidence + eligibility + human approval say otherwise |
| P1.4 | **Unchanged / Not satisfied** |

## Cross references

- [`automation_registry.md`](automation_registry.md) — AR-003
- [`00_ATLAS_BRAIN.md` § Automation Standards](00_ATLAS_BRAIN.md#automation-standards) — template, eligibility, adoption process
- [`knowledge_playbook.md`](knowledge_playbook.md) — staleness procedure
- [`03_ORGANIZATION.md` § Department: Knowledge](03_ORGANIZATION.md#department-knowledge) / [§ Department: AI](03_ORGANIZATION.md#department-ai)
