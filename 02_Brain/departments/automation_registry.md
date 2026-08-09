# Automation Registry

> The AI department's populated registry of candidate internal operating automations, tracked per [Phase 1 exit criterion P1.3](04_ROADMAP.md#phase-1--operating-kernel) and the [Automation Standards](00_ATLAS_BRAIN.md#automation-standards). This is the registry itself — a tracked list of candidates against canonical fields — not a restatement of the standards that define those fields.

**Document ID:** `automation_registry.md`
**Location:** `02_Brain/departments/`
**Status:** Draft
**Version:** 1.0
**Owner:** Анатолий (AI hat) — per [`03_ORGANIZATION.md` § Department: AI § Ownership](03_ORGANIZATION.md#department-ai) ("Automation registry | AI head")
**Last updated:** 2026-08-09
**Review date:** 2027-02-09

---

## Purpose

This document satisfies [Phase 1 exit criterion P1.3](04_ROADMAP.md#phase-1--operating-kernel) ("Automation registry exists — AI owns registry; ≥5 candidates tracked") and operationalizes [`00_ATLAS_BRAIN.md` § Automation Standards § Automation portfolio review](00_ATLAS_BRAIN.md#automation-standards), which states: *"The AI department maintains an automation registry."* Registry ownership sits with the AI head per the [Department: AI ownership table](03_ORGANIZATION.md#department-ai).

This is the **populated registry**, not the intake procedure. [`ai_playbook.md`](ai_playbook.md) already defines *how* a new candidate gets logged (its Agent Design Standards intake-form template); this document is *what has actually been logged* against that procedure. The two are deliberately not merged, per [One source of truth](02_FOUNDING_PRINCIPLES.md#one-source-of-truth) — the procedure lives in one place, the instance data lives here.

## Scope boundary — Atlas-internal operations only

This registry tracks candidate automations for **Atlas's own internal holding operations only** — how the Brain, Knowledge, Finance, Operations, Assets, and Projects hats run their own recurring work.

It explicitly excludes:

- `OP-022_AI_AUTOMATION_EXPERIMENT.md` (under `01_Projects/P-001_ATLAS_OPERATING_SYSTEM/`) — this is a **portfolio/business opportunity**: a candidate AI-automation *service Atlas might sell to SMB customers*. It is not an Atlas-internal automation, has its own separate lifecycle (Research → Customer Discovery → Prototype → Paid Pilot), and is owned by the Assets/Projects hats as a venture, not by the AI hat as internal infrastructure. If that venture ever proceeds and builds its own internal tooling, that tooling would be tracked in the venture's own operating documentation — never here.
- Any other opportunity, register, brief, or retrospective under `01_Projects/` or `03_Knowledge/`. Those describe what Atlas is *evaluating as a business*; this registry describes what Atlas is *automating about itself*.

Conflating the two would misstate Atlas's actual internal AI maturity by borrowing credit from an unrelated, unproven product experiment — a violation of [Truth over comfort](02_FOUNDING_PRINCIPLES.md#truth-over-comfort).

## Relationship to canonical standards

This registry links to, and does not restate:

- [Agent Design Standards](00_ATLAS_BRAIN.md#agent-design-standards) — canonical definition of the eight fields (Purpose, Trigger, Inputs, Outputs, Guardrails, Owner, Evaluation, Fallback) populated per candidate below.
- [Automation eligibility criteria](00_ATLAS_BRAIN.md#automation-standards) — Frequency, Definition, Documentation, Measurement, Owner. Used below as an honest pass/fail check per candidate, not redefined.
- [AI maturity model (L0–L4)](00_ATLAS_BRAIN.md#ai-strategy) — canonical maturity labels used below.
- [`ai_playbook.md`](ai_playbook.md) — the AI hat's execution mechanics for intake, L2-tracking, and quarterly review. Its blank intake-form template is intentionally not duplicated here.

## How to read this registry

Every candidate below is sourced from an existing canonical reference — either the [Automation domain priority order](04_ROADMAP.md#automation-evolution) or a department playbook's own "AI participation to specify" line — not invented for this document. Per [Truth over comfort](02_FOUNDING_PRINCIPLES.md#truth-over-comfort), a candidate is labeled above **L0 (Manual)** only where repository evidence of actual repeated use exists. Today that is true for exactly one candidate, and only at an **informal, unregistered L1** — no candidate is labeled L2 or higher, because no candidate has been piloted, measured, or promoted through the [AI adoption process](00_ATLAS_BRAIN.md#ai-strategy).

## Registry summary

| ID | Candidate | Department | Maturity (honest) | Roadmap automation domain |
|---|---|---|---|---|
| AR-001 | AI-assisted governance & knowledge drafting | Brain / Knowledge | 🟡 Informal L1 (Assisted) — unregistered | #2 Knowledge capture, tagging, staleness |
| AR-002 | Decision framing & precedent packaging assist | Brain | 🔴 L0 (Manual) — proposed only | #8 Decision packaging / precedent retrieval |
| AR-003 | T1–T3 document staleness flagging | Knowledge | 🔴 L0 (Manual) — proposed only | #2 Knowledge capture, tagging, staleness |
| AR-004 | Monthly close & variance-draft assist | Finance | 🔴 L0 (Manual) — proposed only | #1 Financial reporting & reconciliation assists |
| AR-005 | KPI anomaly flagging | Operations | 🔴 L0 (Manual) — proposed only | #5 KPI anomaly detection |
| AR-006 | Project status synthesis & risk flagging | Projects | 🔴 L0 (Manual) — proposed only | #3 Project status synthesis |

**6 candidates tracked** — exceeds the ≥5 required by [P1.3](04_ROADMAP.md#phase-1--operating-kernel). Zero candidates are at L2 or above; none are in production; none have a completed evaluation cycle. This matches, and does not contradict, [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md)'s existing description of Atlas's AI usage as informal and unregistered — this registry is the first formal tracking of that reality, not a claim that the reality has changed.

---

## AR-001 — AI-assisted governance & knowledge drafting

**Source:** Roadmap [Automation domain priority order](04_ROADMAP.md#automation-evolution) #2 (Knowledge capture, tagging, staleness); [AI evolution § Department AI embedding roadmap](04_ROADMAP.md#ai-evolution), Brain P1 focus ("Draft assistance").

| Field | Entry |
|---|---|
| **Purpose** | Assist a human owner in drafting, structuring, and cross-referencing Atlas governance and knowledge documents (Brain T1 documents, department playbooks, project briefs and retrospectives) |
| **Trigger** | Manual — a human initiates each drafting session; no scheduled or event-based trigger exists |
| **Inputs** | Existing canonical Brain documents (for cross-referencing and consistency); the human owner's stated requirements for the document being drafted |
| **Outputs** | Draft Markdown document sections or files, proposed for human review before being treated as canonical or Active |
| **Guardrails** | Must never mark a document Active/canonical without human sign-off; must never assert a fact, date, or figure not present in a source document; every substantive claim is reviewed by the human owner before publication |
| **Owner** | Анатолий (currently dual-hatted across all seven departments at [Org Stage 0](03_ORGANIZATION.md#organizational-scaling)) |
| **Evaluation** | Not measured — no baseline for time saved or error rate has been recorded |
| **Fallback** | Fully manual drafting; this is the pre-existing default the pattern would revert to |

**Maturity — honest assessment:** This is the one candidate with real, if informal, usage history: all eight Brain T1 documents, all seven department playbooks, `07_GLOSSARY.md`, and the P-001 Knowledge artifacts have been drafted using this pattern under direct human review, consistent with `05_CURRENT_STATE.md`'s own description of current AI usage as informal L1 (Assisted). It is **not** labeled L2 — no automation has ever executed a step without a human directing and reviewing it, so "supervised automation" (L2) would overstate what has actually happened.

**Eligibility check** (per [Automation eligibility criteria](00_ATLAS_BRAIN.md#automation-standards)):

| Criterion | Status |
|---|---|
| Frequency ≥3×/month | ✅ Met — used dozens of times to date |
| Clear definition (inputs/steps/outputs) | 🟡 Partial — practiced consistently but never written as a formal spec |
| Documentation (SOP/playbook exists) | 🔴 Not met — no SOP exists for this pattern |
| Baseline metrics exist | 🔴 Not met — no time/error/cost measurement has ever been taken |
| Named human owner assigned | 🟡 Partial — informally named (Анатолий), not assigned via a formal Agent Design Standards record until this entry |

**Verdict:** Not yet eligible for formal promotion past its current informal state — fails on documentation and measurement, matching the self-assessment already on record in [`05_CURRENT_STATE.md` § Current Automation](05_CURRENT_STATE.md#current-automation).

---

## AR-002 — Decision framing & precedent packaging assist

**Source:** Roadmap [Automation domain priority order](04_ROADMAP.md#automation-evolution) #8 (Decision packaging / precedent retrieval); [AI evolution § Department AI embedding roadmap](04_ROADMAP.md#ai-evolution), Brain P1 focus ("decision packaging"); `brain_playbook.md` § Execution guidance ("decision-precedent retrieval").

| Field | Entry |
|---|---|
| **Purpose** | Assist the decision owner at the Frame/Evidence/Options stages of the [Decision Pipeline](06_DECISIONS.md#decision-pipeline) by drafting the framing questions, surfacing precedent from the Decision Register, and structuring evidence — never scoring or deciding |
| **Trigger** | Manual — decision owner requests drafting help at Pipeline Stage 2 (Frame) |
| **Inputs** | The decision question; the current [Decision Register](06_DECISIONS.md#decision-register); relevant Brain principles and policies |
| **Outputs** | A draft Frame section, a precedent-search summary, and a draft Options list for human review |
| **Guardrails** | Must never self-certify a Gate; must never set a DR's status to Approved or Logged; any AI-proposed risk score must be flagged for extra scrutiny per [Bias Detection](06_DECISIONS.md#bias-detection) |
| **Owner** | Анатолий (Brain hat) |
| **Evaluation** | Not measured — no baseline exists; the pattern has not been used. Would be evaluated against decision cycle time and Gate-2 pass rate if piloted |
| **Fallback** | Decision owner drafts the DR entirely manually, as was done for both `DR-2026-001` and `DR-2026-002` to date |

**Maturity — honest assessment:** **L0 (Manual).** Both decisions currently in the Register were drafted without this pattern. This is a proposal, not evidenced practice.

**Eligibility check:**

| Criterion | Status |
|---|---|
| Frequency ≥3×/month | 🔴 Not met — 2 decisions logged since inception, not a monthly-repeating volume yet |
| Clear definition | 🟡 Partial — the Decision Pipeline stages are well defined; an AI-assist role within them is not yet specified |
| Documentation | 🔴 Not met — no automation spec exists |
| Baseline metrics | 🔴 Not met |
| Named human owner | 🟡 Partial — Brain hat named; no per-agent owner record yet |

**Verdict:** Not eligible; correctly tracked as proposed-only.

---

## AR-003 — T1–T3 document staleness flagging

**Source:** Roadmap [Automation domain priority order](04_ROADMAP.md#automation-evolution) #2 (Knowledge capture, tagging, staleness); `knowledge_playbook.md` § Execution guidance ("Staleness-flagging procedure").

| Field | Entry |
|---|---|
| **Purpose** | Compare each T1–T3 document's `Review date` field against the current date and flag any document past due, per `knowledge_playbook.md`'s staleness-flagging procedure |
| **Trigger** | Proposed scheduled check (e.g., monthly), or ad hoc at each Brain-hat working session |
| **Inputs** | Metadata blocks (`Review date` field) of all active T1–T3 documents |
| **Outputs** | A list of past-due documents with named owner and days-overdue, routed to the Knowledge hat |
| **Guardrails** | May only flag; must never edit, archive, or change a document's `Status` field itself — remains a human decision |
| **Owner** | Анатолий (Knowledge hat) |
| **Evaluation** | Not measured — no staleness event has occurred yet; every governance document is within its first review window |
| **Fallback** | Knowledge hat checks review dates manually, which is current practice |

**Maturity — honest assessment:** **L0 (Manual).** No document has ever lapsed past its review date, so this pattern has never actually been exercised, even manually.

**Eligibility check:**

| Criterion | Status |
|---|---|
| Frequency ≥3×/month | 🔴 Not met — zero staleness events to date |
| Clear definition | ✅ Met — comparing a date field against today's date is fully specified |
| Documentation | 🔴 Not met — no SOP exists |
| Baseline metrics | 🔴 Not met |
| Named human owner | 🟡 Partial — Knowledge hat named; no per-agent owner record yet |

**Verdict:** Not eligible; correctly tracked as proposed-only.

---

## AR-004 — Monthly close & variance-draft assist

**Source:** Roadmap [Automation domain priority order](04_ROADMAP.md#automation-evolution) #1 (Financial reporting & reconciliation assists — top priority); [AI evolution § Department AI embedding roadmap](04_ROADMAP.md#ai-evolution), Finance P1 focus ("Close assist; variance drafts"); `finance_playbook.md` § Execution guidance.

| Field | Entry |
|---|---|
| **Purpose** | Draft the monthly close summary and variance commentary from raw financial inputs, once a chart of accounts and close cadence exist |
| **Trigger** | Proposed scheduled — monthly, on a defined close day (not yet set; no close process exists today) |
| **Inputs** | Financial transaction records, prior-period actuals, capital bucket targets |
| **Outputs** | Draft close summary and variance commentary for Finance hat review and sign-off |
| **Guardrails** | Must never post, reconcile, or file anything; every close remains human-signed-off before being treated as final |
| **Owner** | Анатолий (Finance hat) |
| **Evaluation** | Not measured — no close has ever occurred |
| **Fallback** | Fully manual close, which is the current (only) state |

**Maturity — honest assessment:** **L0 (Manual).** Per [`05_CURRENT_STATE.md` § Current Finance](05_CURRENT_STATE.md#current-finance), no chart of accounts, close process, or deployed capital currently exists — this candidate is entirely prospective and cannot be promoted until the underlying close process itself exists (a separate, not-yet-satisfied concern under [P1.5](04_ROADMAP.md#phase-1--operating-kernel)).

**Eligibility check:**

| Criterion | Status |
|---|---|
| Frequency ≥3×/month | 🔴 Not met — no close has ever run |
| Clear definition | 🔴 Not met — no chart of accounts or close SOP exists yet to automate against |
| Documentation | 🔴 Not met |
| Baseline metrics | 🔴 Not met |
| Named human owner | 🟡 Partial — Finance hat named; no per-agent owner record yet |

**Verdict:** Not eligible; blocked upstream of automation readiness, not merely unbuilt.

---

## AR-005 — KPI anomaly flagging

**Source:** Roadmap [Automation domain priority order](04_ROADMAP.md#automation-evolution) #5 (KPI anomaly detection); [AI evolution § Department AI embedding roadmap](04_ROADMAP.md#ai-evolution), Operations P1 focus ("KPI anomaly flags").

| Field | Entry |
|---|---|
| **Purpose** | Compare live KPI values against defined thresholds/targets across departments and flag outliers, once a KPI dictionary with live-value tracking exists |
| **Trigger** | Proposed scheduled — weekly, once KPI data exists |
| **Inputs** | Department KPI definitions ([`03_ORGANIZATION.md`](03_ORGANIZATION.md)); live KPI values (currently none recorded) |
| **Outputs** | An anomaly/flag list routed to the relevant department hat |
| **Guardrails** | May only flag; must never trigger an automated remediation action |
| **Owner** | Анатолий (Operations hat) |
| **Evaluation** | Not measured — not applicable; no KPI is currently instrumented |
| **Fallback** | Manual KPI review at quarterly cadence (also not yet exercised) |

**Maturity — honest assessment:** **L0 (Manual).** Per [`05_CURRENT_STATE.md` § Current KPIs](05_CURRENT_STATE.md#current-kpis), every department KPI currently reports "No data" — there is nothing yet for this candidate to monitor.

**Eligibility check:**

| Criterion | Status |
|---|---|
| Frequency ≥3×/month | 🔴 Not met — no KPI values exist to review at any frequency |
| Clear definition | 🟡 Partial — KPI definitions exist per department; live-value collection does not |
| Documentation | 🔴 Not met |
| Baseline metrics | 🔴 Not met |
| Named human owner | 🟡 Partial — Operations hat named; no per-agent owner record yet |

**Verdict:** Not eligible; blocked upstream on KPI instrumentation, not merely unbuilt.

---

## AR-006 — Project status synthesis & risk flagging

**Source:** Roadmap [Automation domain priority order](04_ROADMAP.md#automation-evolution) #3 (Project status synthesis); `projects_playbook.md` § Execution guidance ("AI participation to specify: status synthesis, risk flagging, and resource-conflict detection").

| Field | Entry |
|---|---|
| **Purpose** | Summarize project status (stage, blockers, risk) across the active project portfolio for the Projects hat |
| **Trigger** | Manual or proposed scheduled, at each project touchpoint |
| **Inputs** | Project briefs, retrospectives, and any status notes filed for active projects |
| **Outputs** | A one-page status/risk digest for human review |
| **Guardrails** | Must never change a project's lifecycle stage (e.g., Triage → Brief) on its own; that remains the DRI's call |
| **Owner** | Анатолий (Projects hat) |
| **Evaluation** | Not measured — the pattern has not been used; the existing P-001 Brief and Retrospective were produced via the general drafting-assist pattern (AR-001), not a dedicated status-synthesis agent |
| **Fallback** | DRI reviews project files manually, which is current practice |

**Maturity — honest assessment:** **L0 (Manual).** Exactly one project (P-001) has entered the Project Lifecycle to date — insufficient volume to have exercised, let alone promoted, a dedicated synthesis agent.

**Eligibility check:**

| Criterion | Status |
|---|---|
| Frequency ≥3×/month | 🔴 Not met — one active project |
| Clear definition | 🟡 Partial — inputs/outputs are describable; not yet formally specified |
| Documentation | 🔴 Not met |
| Baseline metrics | 🔴 Not met |
| Named human owner | 🟡 Partial — Projects hat named; no per-agent owner record yet |

**Verdict:** Not eligible; correctly tracked as proposed-only.

---

## Registry maintenance

Per [Automation portfolio review](00_ATLAS_BRAIN.md#automation-standards), this registry is reviewed quarterly by the AI hat, aligned to `ai_playbook.md`'s own review cadence. A review should check:

- Any candidate above that has newly cleared an eligibility criterion (update the check, not the maturity label, until the [AI adoption process](00_ATLAS_BRAIN.md#ai-strategy) — Identify → Spec → Prototype → Evaluate → Deploy → Document — has actually run).
- Any new candidate identified by a department hat, added using the same Agent Design Standards fields.
- Whether any candidate has been formally piloted; if so, its maturity label changes only with recorded evaluation evidence (time/error/cost baseline), never by assertion.

No candidate in this registry may be promoted to L1 or higher in this document without a corresponding **Evaluation** entry containing real measured evidence, per [Truth over comfort](02_FOUNDING_PRINCIPLES.md#truth-over-comfort) and the [AI adoption process](00_ATLAS_BRAIN.md#ai-strategy)'s Evaluate step.

## Status of this document

This is a **Draft T2/T3 artifact**, created to satisfy [Phase 1 exit criterion P1.3](04_ROADMAP.md#phase-1--operating-kernel) (Milestone M-A-001, "Automation registry v1"). At [Org Stage 0](03_ORGANIZATION.md#organizational-scaling), zero candidates have been built, piloted, or promoted — every entry above is a tracked proposal, not evidenced production practice, except AR-001's informal L1 usage, which is disclosed as informal rather than counted as a registered automation.

## Cross references

- [`00_ATLAS_BRAIN.md` § Automation Standards](00_ATLAS_BRAIN.md#automation-standards) — eligibility criteria, design principles, spec template, portfolio review cadence
- [`00_ATLAS_BRAIN.md` § Agent design standards](00_ATLAS_BRAIN.md#agent-design-standards) — the eight fields used per candidate above
- [`00_ATLAS_BRAIN.md` § AI Strategy](00_ATLAS_BRAIN.md#ai-strategy) — AI maturity model (L0–L4), AI adoption process
- [`03_ORGANIZATION.md` § Department: AI](03_ORGANIZATION.md#department-ai) — canonical registry ownership
- [`ai_playbook.md`](ai_playbook.md) — intake procedure this registry populates
- [`04_ROADMAP.md` § Phase 1 — Operating Kernel](04_ROADMAP.md#phase-1--operating-kernel) — P1.3 exit criterion this document evidences
- [`04_ROADMAP.md` § AI Evolution / Automation Evolution](04_ROADMAP.md#ai-evolution) — source of the domain priority order and department AI-embedding roadmap referenced per candidate
- [`06_DECISIONS.md`](06_DECISIONS.md) — Decision Register and Bias Detection referenced by AR-002
- [`07_GLOSSARY.md`](07_GLOSSARY.md) — canonical definitions (L-level, Agent, Automation, Registry)

---

*This is a Draft T2/T3 registry, not yet Active. It supplements — and does not duplicate — [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) or [`ai_playbook.md`](ai_playbook.md).*
