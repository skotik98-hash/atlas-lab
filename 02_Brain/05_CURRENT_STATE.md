# Atlas Current State

> The canonical present-tense snapshot of Atlas — what exists, what works, what is missing, and what is true right now. This document reports reality. It does not set strategy, define principles, or describe structure — it measures them against the world as it stands today.

**Document ID:** `05_CURRENT_STATE.md`
**Location:** `02_Brain/`
**Status:** Active
**Version:** 1.3.1
**Owner:** Brain (Brain lead; instance values contributed by all departments — currently all held by the same individual, see [Current Organization](#current-organization))
**Classification:** Governance — current state snapshot
**Last updated:** 2026-08-10
**Review date:** 2026-11-08
**Update trigger:** Quarterly on calendar, **or immediately** on any material change — phase transition, first portfolio asset, first hire, first logged decision, first production automation
**Supersedes:** — (first populated version; document previously existed as an empty placeholder)
**Authority:** This document is the authoritative source for *instance values* — the actual, current, dated facts of Atlas today. It holds numbers, names, statuses, and gaps. It does not hold philosophy ([`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md)), principles ([`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md)), structure ([`03_ORGANIZATION.md`](03_ORGANIZATION.md)), or sequencing ([`04_ROADMAP.md`](04_ROADMAP.md)). Where this document and a sibling document appear to disagree, the sibling wins on *type* and this document wins on *instance* — see [Document Authority](#document-authority).

---

## Table of Contents

1. [Purpose](#purpose)
2. [Document Authority](#document-authority)
3. [How to Read Current State](#how-to-read-current-state)
4. [Current Executive Summary](#current-executive-summary)
5. [Snapshot Dashboard](#snapshot-dashboard)
6. [Current Mission Status](#current-mission-status)
7. [Current Strategic Position](#current-strategic-position)
8. [Current Organizational Maturity](#current-organizational-maturity)
9. [Current Capability Maturity](#current-capability-maturity)
10. [Current AI Maturity](#current-ai-maturity)
11. [Current AI Capabilities](#current-ai-capabilities)
12. [Current Brain Status](#current-brain-status)
13. [Current Knowledge System](#current-knowledge-system)
14. [Current Organization](#current-organization)
15. [Current Departments](#current-departments)
16. [Current Ownership](#current-ownership)
17. [Current Roles](#current-roles)
18. [Current Decision System](#current-decision-system)
19. [Current Governance](#current-governance)
20. [Current Assets](#current-assets)
21. [Current Projects](#current-projects)
22. [Current Automation](#current-automation)
23. [Current Infrastructure](#current-infrastructure)
24. [Current Technical Stack](#current-technical-stack)
25. [Current Security](#current-security)
26. [Current Finance](#current-finance)
27. [Current Operations](#current-operations)
28. [Current Workflows](#current-workflows)
29. [Current Interfaces](#current-interfaces)
30. [Current Communication](#current-communication)
31. [Current Planning Process](#current-planning-process)
32. [Current Review Process](#current-review-process)
33. [Current Metrics](#current-metrics)
34. [Current KPIs](#current-kpis)
35. [Current Scorecards](#current-scorecards)
36. [Current Risks](#current-risks)
37. [Current Constraints](#current-constraints)
38. [Current Bottlenecks](#current-bottlenecks)
39. [Current Technical Debt](#current-technical-debt)
40. [Current Organizational Debt](#current-organizational-debt)
41. [Current Documentation Coverage](#current-documentation-coverage)
42. [Current Documentation Gaps](#current-documentation-gaps)
43. [Current Quality Assessment](#current-quality-assessment)
44. [Current Scaling Readiness](#current-scaling-readiness)
45. [Current Hiring Readiness](#current-hiring-readiness)
46. [Current Expansion Readiness](#current-expansion-readiness)
47. [Current Operational Health](#current-operational-health)
48. [Appendix A — Current State Field Reference](#appendix-a--current-state-field-reference)
49. [Appendix B — Next 90 Days Watch List](#appendix-b--next-90-days-watch-list)
50. [Appendix C — Full Milestone Register Status](#appendix-c--full-milestone-register-status)
51. [Appendix D — Candidate Glossary Terms](#appendix-d--candidate-glossary-terms)
52. [Appendix E — Decision Record Backlog](#appendix-e--decision-record-backlog)
53. [Appendix F — Vendor and Tooling Registry](#appendix-f--vendor-and-tooling-registry)
54. [Appendix G — Principle Adherence Self-Audit](#appendix-g--principle-adherence-self-audit)
55. [Appendix H — Roadmap Success Criteria (H0) Cross-Check](#appendix-h--roadmap-success-criteria-h0-cross-check)
56. [Appendix I — Onboarding Path Dry-Run](#appendix-i--onboarding-path-dry-run)
57. [Appendix J — First Quarterly Brain Review — Draft Agenda](#appendix-j--first-quarterly-brain-review--draft-agenda)
58. [Cross References](#cross-references)
59. [Document Maintenance](#document-maintenance)

**Related documents:** [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) · [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) · [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) · [`03_ORGANIZATION.md`](03_ORGANIZATION.md) · [`04_ROADMAP.md`](04_ROADMAP.md) · [`06_DECISIONS.md`](06_DECISIONS.md) · [`07_GLOSSARY.md`](07_GLOSSARY.md)

---

## Purpose

### What this document is

This document answers one question, asked continuously: **what is true about Atlas right now?**

It is the instance layer beneath five type-defining documents:

- [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) defines what Atlas optimizes for and how it decides.
- [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) defines why Atlas exists at all.
- [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) defines the immutable judgment infrastructure.
- [`03_ORGANIZATION.md`](03_ORGANIZATION.md) defines who owns what and how authority flows.
- [`04_ROADMAP.md`](04_ROADMAP.md) defines where Atlas is going and in what order.

None of those documents change often, and none of them tell you what is true **today**. This document does. It is deliberately unglamorous: a ledger of facts, statuses, gaps, and dated commitments — not a pitch, not a plan, not a manifesto.

### What this document is not

| This document is not | It lives instead in |
|---|---|
| Vision, mission, or operating philosophy | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) |
| Founding narrative or philosophical conviction | [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) |
| Immutable principles or their extended rationale | [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) |
| Department charters, authority boundaries, escalation rules | [`03_ORGANIZATION.md`](03_ORGANIZATION.md) |
| Strategic sequencing, phases, horizons, milestone definitions | [`04_ROADMAP.md`](04_ROADMAP.md) |
| Decision records and precedents | [`06_DECISIONS.md`](06_DECISIONS.md) |
| Canonical term definitions | [`07_GLOSSARY.md`](07_GLOSSARY.md) |

This document never originates a principle, a department, a phase definition, or a milestone taxonomy. It only reports **where Atlas stands** against frameworks defined elsewhere. When this document needs to describe a concept not yet defined canonically, it flags the gap rather than inventing the definition here.

### Why this document exists

Per [Knowledge Management](00_ATLAS_BRAIN.md#knowledge-management) and [Onboarding knowledge path](00_ATLAS_BRAIN.md#onboarding-knowledge-path), every new operator, agent, or reviewer reads Brain → Why → Glossary → playbooks → **Current State + Roadmap**. Without a maintained Current State, that final step collapses into guesswork or Slack archaeology — exactly the failure mode [Why Atlas Exists](01_WHY_ATLAS_EXISTS.md#why-traditional-companies-fail) was written to prevent.

Per [Truth over comfort](02_FOUNDING_PRINCIPLES.md#truth-over-comfort) and [Evidence over opinion](02_FOUNDING_PRINCIPLES.md#evidence-over-opinion), Atlas does not narrate progress it has not made. This document exists to make that discipline structural rather than aspirational: every claim below is either evidenced, explicitly marked as a target defined elsewhere, or explicitly marked **TBD**, **Unknown**, **Not Yet Implemented**, or **Planned (see Roadmap)**.

### Non-goals of this document

- It does not forecast. Forecasts belong in the [Roadmap](04_ROADMAP.md) and in Finance planning artifacts once they exist.
- It does not motivate. No narrative framing, no marketing language, no aspirational tone dressed as fact.
- It does not duplicate. Every recurring framework (AI maturity levels, CM dimensions, org stages, phases, decision framework) is referenced, never restated in full.
- It does not fabricate. Where Atlas has not yet produced a fact, the field says so plainly.

---

## Document Authority

### Authority scope

This document has authority over **instance values only** — the specific, dated, current answer to questions the sibling documents leave as templates. Where the Brain, Organization, or Roadmap documents explicitly defer a live number or name to this document, this is the file where that number or name must live.

| Sibling document says | This document holds |
|---|---|
| "Exact percentages are set in `05_CURRENT_STATE.md`" ([Capital buckets](00_ATLAS_BRAIN.md#capital-buckets)) | Actual capital bucket allocation — see [Current Finance](#current-finance) |
| "Current headcount, active roles, staffing gaps" ([Organization § Purpose](03_ORGANIZATION.md#purpose)) | Actual headcount and named roles — see [Current Organization](#current-organization), [Current Roles](#current-roles) |
| "Escalation threshold categories… Actual % thresholds this quarter" ([Organization § Relationship to Current State](03_ORGANIZATION.md#relationship-to-current-state)) | Live escalation thresholds — see [Current Governance](#current-governance) |
| "Current headcount band, named department heads, active threshold values" ([Organization § Cross References](03_ORGANIZATION.md#cross-references)) | Same, cross-referenced across sections below |
| "What phase we are in and what is true today" ([Roadmap § How Current State interacts](04_ROADMAP.md#how-to-read-this-roadmap)) | Current phase, horizon, era, and CM scores — see [Current Strategic Position](#current-strategic-position), [Current Capability Maturity](#current-capability-maturity) |
| "Live numeric thresholds" ([Roadmap § Non-goals](04_ROADMAP.md#purpose)) | Same |
| "Live states belong in Current State" ([Roadmap § Milestone health states](04_ROADMAP.md#strategic-milestones)) | Milestone status — see [Current Strategic Position](#current-strategic-position) |

### What this document does not have authority over

- **Definitions.** If a term, level, phase, or dimension is not yet defined canonically, this document cannot define it on the fly. It flags the gap and routes to the owning document.
- **Structure.** This document cannot create a department, an org stage, or a decision type. Those changes require a Decision Record and Brain approval per [Governance Boundaries](03_ORGANIZATION.md#governance-boundaries).
- **Strategy.** This document cannot set a new priority. Priorities are set in the [Roadmap](04_ROADMAP.md) and quarterly priority memos.
- **Precedent.** This document does not adjudicate past decisions. That is [`06_DECISIONS.md`](06_DECISIONS.md).

### Conflict resolution

If this document and a sibling document disagree:

1. If the disagreement is about **what is true today** (a number, a name, a status) — this document wins; fix the discrepancy here immediately.
2. If the disagreement is about **what should be true, or how something is structured or defined** — the sibling document wins; this document is out of date and must be corrected at the next review, or immediately if the error is material.
3. Any correction that reveals a **structural** gap (e.g., an org stage rule that does not fit reality) is escalated to Brain per [Organization Executes the Brain](03_ORGANIZATION.md#organization-executes-the-brain) rather than silently patched here.

### Chain of custody for facts in this document

| Fact category | Source of truth | How it enters this document |
|---|---|---|
| Phase, horizon, era, CM scores | Brain lead assessment against [Roadmap](04_ROADMAP.md) rubrics | Quarterly Brain review (not yet run — see [Current Review Process](#current-review-process)) |
| Headcount, roles, ownership | Direct observation | Updated on any hiring/offboarding event |
| Decision log statistics | [`06_DECISIONS.md`](06_DECISIONS.md) | Counted at each update |
| Financial figures | Finance systems (Not Yet Implemented) | TBD once Finance department is active |
| Automation registry statistics | [`automation_registry.md`](departments/automation_registry.md) (exists; 6 candidates) | Live candidate/maturity counts from registry; production L2 remains 0 |
| Portfolio statistics | Assets department tracker (Not Yet Implemented) | TBD once first asset exists |

---

## How to Read Current State

### Reading rules

1. **Read this document only after the five type documents.** Facts without frameworks are noise. If you have not read [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md), [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md), [`03_ORGANIZATION.md`](03_ORGANIZATION.md), and [`04_ROADMAP.md`](04_ROADMAP.md), the labels below (CM-1, L0, P0, Stage 0) will not mean anything.
2. **Treat every unfilled field as information, not embarrassment.** A field marked **Not Yet Implemented** is more valuable than a field silently omitted or optimistically guessed. See [Truth over comfort](02_FOUNDING_PRINCIPLES.md#truth-over-comfort).
3. **Dates matter.** Every section implicitly carries the "Last updated" date at the top of this document. If you are reading this more than one quarter after that date, treat every field as potentially stale and check for a newer version before acting on it.
4. **This document is short-lived by design.** Unlike the Brain, Principles, Organization, and Roadmap — which change rarely — this document is *expected* to be materially rewritten every quarter. Do not build long-lived automation logic against specific field values here without a review-date check.

### Legend used throughout this document

| Marker | Meaning |
|---|---|
| **Active** | Exists, is in use, and is current |
| **Not Yet Implemented** | Defined or expected in the framework, but no work has started |
| **Planned (see Roadmap)** | Scheduled for a specific future phase or milestone; not due yet |
| **TBD** | To be decided; owner and/or target date not yet assigned |
| **Unknown** | Not yet investigated or recorded; distinct from TBD because no decision is pending — only information-gathering |
| **In progress** | Work has started; not complete |
| 🟢 / 🟡 / 🔴 / 🔵 | Status colors matching [Project health signals](00_ATLAS_BRAIN.md#project-health-signals): Green = on track, Yellow = minor delay, Red = material miss, Blue = deprioritized |

### Reading paths by audience

| If you are… | Read these sections first |
|---|---|
| A new operator joining Atlas | [Current Executive Summary](#current-executive-summary), [Snapshot Dashboard](#snapshot-dashboard), [Current Organization](#current-organization), [Current Roles](#current-roles) |
| Anton (Brain lead), doing a weekly self-check | [Snapshot Dashboard](#snapshot-dashboard), [Current Risks](#current-risks), [Appendix B — Next 90 Days Watch List](#appendix-b--next-90-days-watch-list) |
| An AI agent retrieving context for a task | [Current Ownership](#current-ownership), [Current Governance](#current-governance), [Current Documentation Coverage](#current-documentation-coverage) |
| A future hire evaluating whether to join | [Current Mission Status](#current-mission-status), [Current Strategic Position](#current-strategic-position), [Current Scaling Readiness](#current-scaling-readiness) |
| A future investor or advisor | [Current Executive Summary](#current-executive-summary), [Current Finance](#current-finance), [Current Assets](#current-assets), [Current Risks](#current-risks) |
| Brain, preparing the next quarterly review | Every section — this document is the input to that review, see [Current Review Process](#current-review-process) |

---

## Current Executive Summary

Atlas is, as of 2026-08-10, a **single-operator holding-company-in-formation** with a complete first-generation governance substrate, Draft department playbooks, an automation registry, and early project/automation evidence — still without revenue, portfolio assets, or production L2 automations.

In concrete terms:

- **What exists:** All eight Brain governance documents ([`00`](00_ATLAS_BRAIN.md)–[`07`](07_GLOSSARY.md)) Active — a complete mission, principle set, organizational model, multi-decade roadmap, decision framework ([`06_DECISIONS.md`](06_DECISIONS.md) v1.0), and shared vocabulary ([`07_GLOSSARY.md`](07_GLOSSARY.md) v1.0, ~150 terms). **4 Decision Records logged** (DR-2026-001 through DR-2026-004). This document ([`05`](05_CURRENT_STATE.md)) is Active v1.3.1. The knowledge base exists as a version-controlled local vault.
- **What does not yet exist:** Portfolio assets, production L2 automations, hired employees/contractors, a live financial system with chart of accounts and actual closes, legal-entity confirmation, customers, revenue, and external stakeholder relationships of record. (Draft playbooks, one close SOP, the automation registry, and P-001/Market Screen artifacts **do** exist — see below.)
- **Who runs it:** One person — **Антон (Anton)**, acting as Brain Lead / Holding Lead and, per [Org Stage 0 rules](03_ORGANIZATION.md#stage-0-one-operator), simultaneously wearing all seven department hats.
- **What phase this is:** [Roadmap Phase P1 — Operating Kernel](04_ROADMAP.md#phase-1--operating-kernel), entered 2026-08-08 via DR-2026-002, inside [Horizon H0 — Foundation](04_ROADMAP.md#vision-horizon) and [Era E0 — Substrate](04_ROADMAP.md#multi-year-evolution). **Phase P0 exited** 2026-08-08 — all exit criteria met or acceptably partial (P0.9).
- **What the near-term priority is:** P1 exit criteria that remain open — especially **P1.2** (strict project-lifecycle evidence across ≥3 initiatives), **P1.4** (≥3 processes at L2), and **P1.5** (actual financial closes). **P1.1** and **P1.3** are Met. Milestone **M-A-001** remains only **Partial** (detailed Done-means not fully satisfied — see milestone rows).
- **What the Holding Capability Maturity score is:** CM-0 (weakest-link) overall; CM-1 for governance documentation per narrow interpretation adopted in DR-2026-002. Seven dimensions remain at CM-0 — expected at Stage 0 entering P1.

**The honest one-line summary:** Atlas has exited Phase P0 and entered P1 — constitution, 7 Draft department playbooks, automation registry (6 candidates), and 4 logged decisions exist; **P1.1 / P1.3 / P1.6 / P1.7 / P1.8 are Met**. **P1.2 / P1.4 / P1.5 remain Not Met**; Phase 1 exit = **No**. Portfolio revenue, production L2 automations, and actual financial closes still do not exist.

---

## Snapshot Dashboard

A single-glance reference. Every value below is expanded with evidence in its own section further down this document.

| Field | Current value |
|---|---|
| **Document set status** | 8 of 8 Brain documents Active (`00`–`07`) |
| **Vision horizon** | H0 — Foundation (Years 0–2) |
| **Evolution era** | E0 — Substrate (Years 0–2) |
| **Roadmap phase** | P1 — Operating Kernel (**entered 2026-08-08** via DR-2026-002) |
| **Holding Capability Maturity (weakest-link)** | CM-0 — Implicit (CM-1 governance docs per DR-2026-002 narrow reading) |
| **Holding Capability Maturity (average across 10 dimensions)** | ~0.6 / 5 |
| **Org scale stage** | Stage 0 — One operator |
| **Named headcount** | 1 (Антон — Brain Lead / Holding Lead, all seven hats) |
| **Contractors / vendors** | 0 documented; Unknown whether any exist informally |
| **Portfolio assets (any lifecycle stage)** | 0 |
| **Decision records logged** | 4 (DR-2026-001 through DR-2026-004) |
| **Glossary terms published** | ~150 (Active v1.0 in [`07_GLOSSARY.md`](07_GLOSSARY.md)) |
| **Department playbooks (T3) published** | 7 of 7 (Draft stubs in `02_Brain/departments/`) |
| **SOPs (T4) published** | 1 (`finance_close_sop.md`); chart of accounts still absent |
| **Production automations / agents** | 6 candidates in [`automation_registry.md`](departments/automation_registry.md); formal L2 = 0; AR-003 Spec committed; AR-002/003/006 each have Prototype Run #1 only (still L0) |
| **AI maturity of any process** | L0 (Manual) formally; informal AI drafting assistance in practice, unregistered |
| **Capital bucket allocation** | TBD — not yet set by Finance + Brain |
| **Legal entity status** | Unknown / TBD |
| **Financial close process** | SOP documented (`finance_close_sop.md`); **0 actual closes**; P1.5 Not Met |
| **Projects run through full lifecycle** | 0 full closes; P-001 active with partial Market Screen lifecycle evidence — **P1.2 Not Met** (strict) |
| **Escalation events logged** | 0 |
| **Quarterly Brain reviews held** | 0 |
| **Next scheduled review** | 2026-11-08 |
| **Overall operational health** | 🟢 Green for stage — appropriate progress for Phase P1, Stage 0; primary watch item is key-person concentration (see [Current Risks](#current-risks)) |

---

## Current Mission Status

The Brain defines the mission as three activities — **Build, Acquire, Operate** — evaluated against [three mission questions](00_ATLAS_BRAIN.md#mission-in-practice). This section reports status against that mission, not the mission itself.

### Mission activity status

| Activity | Definition (see Brain) | Current status | Evidence |
|---|---|---|---|
| **Build** | Launch new ventures from first principles | **Not started** | No venture brief, no build project, no build-vs-acquire analysis on file |
| **Acquire** | Purchase businesses with clear operational leverage | **Not started** | No pipeline, no target list, no due diligence artifact on file |
| **Operate** | Run portfolio companies through the shared operating layer | **Not applicable — no portfolio exists yet** | Zero assets in [Company Lifecycle](00_ATLAS_BRAIN.md#company-lifecycle) |

### Mission question self-check

Applying the [three mission questions](00_ATLAS_BRAIN.md#mission-in-practice) to the work actually completed to date (writing the Brain document set):

| Mission question | Self-assessment | Rationale |
|---|---|---|
| Does this make the holding OS stronger? | Yes | The governance substrate is the holding OS's first layer by design — see [The holding as product](00_ATLAS_BRAIN.md#the-holding-as-product) |
| Does this create durable value? | Yes, contingent | Durable only if the documents are used, reviewed, and kept current — see [Current Documentation Gaps](#current-documentation-gaps) for what would undermine this |
| Does this align with AI-native operations? | Partially | Documents were drafted with AI assistance under human review (an informal L1 pattern); no AI-native *operational* workflow exists yet because there is no operation to embed AI into |

### What "mission in practice" looks like today

There is no operating business to evaluate. The mission is currently being executed **entirely at the meta-level** — building the infrastructure that will later evaluate and run Build/Acquire/Operate decisions. This is consistent with [Long-term Purpose § Years 1–3](00_ATLAS_BRAIN.md#long-term-purpose): "Establish the holding OS — Brain, Knowledge, AI, and core operating standards" precedes "Build or acquire initial portfolio assets."

### Mission status risk

The single largest risk to mission status is **documentation without subsequent action** — the "docs as theater" failure mode explicitly named in [Phase 0 risks](04_ROADMAP.md#phase-0--brain-substrate). This document's own existence is a partial mitigation (it forces an honest look at what has *not* happened), but mitigation is only real if the [Appendix B watch list](#appendix-b--next-90-days-watch-list) is actually acted on.

---

## Current Strategic Position

### Position on the horizon/era/phase stack

| Layer | Current value | Defined in |
|---|---|---|
| Horizon | **H0 — Foundation** (Years 0–2) | [Vision Horizon](04_ROADMAP.md#vision-horizon) |
| Era | **E0 — Substrate** (Years 0–2) | [Multi-Year Evolution](04_ROADMAP.md#multi-year-evolution) |
| Phase | **P1 — Operating Kernel** (entered 2026-08-08) | [Major Phases](04_ROADMAP.md#major-phases) |
| Org stage | **Stage 0 — One operator** | [Organizational Scaling](03_ORGANIZATION.md#organizational-scaling) |
| AI evolution arc (Arc C) | **Pre-C1** — informal use only; C1 (L1 assisted, formally registered) not yet reached | [Arc C](04_ROADMAP.md#multi-year-evolution) |
| Knowledge evolution arc (Arc D) | **D1 in progress** — Glossary v1 published; 4 Register entries; onboarding path executable end-to-end (P1.8 Met) | [Arc D](04_ROADMAP.md#multi-year-evolution) |
| Portfolio evolution arc (Arc B) | **Pre-B1** — no first asset closed | [Arc B](04_ROADMAP.md#multi-year-evolution) |
| OS evolution arc (Arc A) | **A1** — Brain documents and org model exist | [Arc A](04_ROADMAP.md#multi-year-evolution) |
| Org evolution arc (Arc E) | **E1 in progress** — Stage 0, 1 person | [Arc E](04_ROADMAP.md#multi-year-evolution) |

### Phase P0 exit criteria — final status (exited 2026-08-08)

Per [Phase 0 — Brain Substrate exit criteria](04_ROADMAP.md#phase-0--brain-substrate). **P0 exited via DR-2026-002.**

| # | Criterion | Status | Evidence |
|---|---|---|---|
| P0.1 | Brain root document active | ✅ Met | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) Status: Active, v1.1 |
| P0.2 | Why document active | ✅ Met | [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) Status: Active, v1.0 |
| P0.3 | Principles active | ✅ Met | [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) Status: Active, v1.0 |
| P0.4 | Organization active | ✅ Met | [`03_ORGANIZATION.md`](03_ORGANIZATION.md) Status: Active, v1.0 |
| P0.5 | Roadmap active | ✅ Met | [`04_ROADMAP.md`](04_ROADMAP.md) Status: Active, v1.0 |
| P0.6 | Current State initialized | ✅ Met | This document, v1.2 |
| P0.7 | Decision log initialized | ✅ Met | DR-2026-001 logged |
| P0.8 | Glossary initialized | ✅ Met | v1.0, ~150 terms |
| P0.9 | Seven departments labeled in practice | 🟡 **Accepted partial** at Stage 0 — dual-hat labeling in this document; dept tracker deferred to P1 |

**Phase gate status: P0 exited 2026-08-08.** M-G-007 met via DR-2026-002. Atlas is now in **Phase P1 — Operating Kernel**.

### Strategic position narrative

Atlas has no market position, no competitive position, and no customer position, because Atlas has not yet built or acquired anything a market, competitor, or customer could observe. The only strategic position that exists today is **internal**: a complete, coherent, version-controlled governance substrate, produced faster than the typical Phase P0 timeline implies, with zero operational debt because zero operations have run.

### What is deliberately not being pursued right now

Per [Phase 0 explicit non-goals](04_ROADMAP.md#phase-0--brain-substrate), the following are correctly **absent** and should not be read as failures:

| Explicitly out of scope for P0 | Status |
|---|---|
| Large acquisition volume | Correctly absent |
| Building the Atlas OS software platform | Correctly absent (that is Phase P4) |
| Hiring to Org Stage 2+ | Correctly absent |
| External brand campaigns | Correctly absent |

---

## Current Organizational Maturity

"Organizational maturity" here means **Org Stage** per [Organizational Scaling](03_ORGANIZATION.md#organizational-scaling), distinct from Holding Capability Maturity (CM, see next section) and AI maturity (L-levels, see below).

### Current stage

**Stage 0 — One operator.** Per the [Stage 0 profile](03_ORGANIZATION.md#stage-0-one-operator): "Founder / holding lead; possibly zero employees." Atlas currently has exactly this profile.

### Stage 0 structural rules — compliance check

| Rule (from Organization doc) | Compliance | Evidence |
|---|---|---|
| Still assign single owner on every outcome, even if the owner is the same human | 🟡 Partial | Ownership is assigned by department hat in [Current Ownership](#current-ownership), but no formal role-charter documents (T3) exist yet to make this machine-legible |
| Still write Decision Records for material calls | 🔴 Not yet | Zero decisions logged to date, including the material call to activate this document |
| Still separate project work from BAU in briefs | 🟡 Partial | P-001 / Market Screen briefs exist; Brain drafting still largely outside formal briefs; **P1.2 Not Met** |
| Do not skip metadata blocks | ✅ Met | All eight active Brain documents carry full T1 metadata blocks |

### Distance to Stage 1

[Stage 1 (~10 people)](03_ORGANIZATION.md#stage-1-10-people) requires, among other things: department heads named (even if dual-hatted with distinct people), role charters published, interface SLAs activated, first dedicated Project DRI, and first production agents with named owners. Atlas currently satisfies **none** of these because there is only one person and zero production agents. Stage transition is **not a goal in itself** — per [Scaling Without Changing Principles](03_ORGANIZATION.md#scaling-without-changing-principles), staffing should follow demonstrated need, not calendar pressure. There is no current plan or date to move to Stage 1 — see [Current Hiring Readiness](#current-hiring-readiness).

### Coordination tax

At Stage 0 with one operator, coordination tax as defined in [Why Traditional Companies Fail § The coordination tax](01_WHY_ATLAS_EXISTS.md#why-traditional-companies-fail) is **effectively zero** — there is no one to coordinate with. This is the one dimension of organizational health that cannot regress further; watch for it to emerge the moment a second person joins.

---

## Current Capability Maturity

Holding Capability Maturity (CM) is defined in [Capability Maturity Model](04_ROADMAP.md#capability-maturity-model) as ten dimensions scored 0–5, with the holding-level score taken as the **minimum** across dimensions (weakest link) for gating purposes, and the **average** used for diagnostics.

### Inaugural CM scorecard (first-ever scoring, 2026-08-08)

| ID | Dimension | Score | Rubric match | Rationale |
|---|---|---|---|---|
| CM-D1 | Governance & judgment | **1** | "Docs exist; rarely used in live decisions" | Framework exists; 4 DRs logged, but operating volume still very low |
| CM-D2 | Knowledge compounding | **1** | "Docs exist; hard to find" *(partially inaccurate — docs are findable; retrieval tooling still thin)* | Onboarding dry-run complete (P1.8); AR-003 Prototype Run #1 only — no recurring staleness process yet |
| CM-D3 | AI & automation | **1** | "Ad-hoc assistant usage unmanaged" | Registry + AR-003 Spec now exist; usage still largely unmanaged relative to L2; production L2 = 0; AR-001 informal L1 only |
| CM-D4 | Financial truth | **0** | "Unreliable numbers" *(more precisely: no numbers exist)* | Close SOP exists; no chart of accounts, **0 actual closes**, no capital deployed; **P1.5 Not Met** |
| CM-D5 | Operational integration | **0** | "Each asset invents ops" *(not applicable — no assets)* | No portfolio to integrate |
| CM-D6 | Portfolio stewardship | **0** | "No lifecycle" | No assets in any [Company Lifecycle](00_ATLAS_BRAIN.md#company-lifecycle) stage |
| CM-D7 | Delivery system | **0** | "Ad-hoc initiatives" | P-001/Market Screen has partial lifecycle evidence; no initiative has completed full lifecycle; **P1.2 Not Met** |
| CM-D8 | Organizational clarity | **2** | "Owners named; dual-hats labeled" | Ownership is named per department hat (see [Current Ownership](#current-ownership)); no interface SLA activity yet because there is no second party |
| CM-D9 | Platform / infrastructure | **1** | "Inventory" | A minimal tooling inventory exists implicitly (see [Current Technical Stack](#current-technical-stack)); no preferred-stack policy or access baseline documented |
| CM-D10 | Learning loop | **0** | "No retros" | One Market Screen stage retrospective exists; no project-close or quarterly decision-review cycle completed |

### Aggregate scores

| Method | Score | Interpretation |
|---|---|---|
| Weakest link (gating) | **CM-0 — Implicit** | Still expected early in Phase P1 at Stage 0; seven of ten dimensions remain at CM-0 |
| Average (diagnostic) | **0.6 / 5** | Reflects genuine progress on governance/knowledge/org clarity even though the floor is 0 |

### CM-to-phase gate check

Per [CM to phase mapping](04_ROADMAP.md#capability-maturity-model), the P0 → P1 transition required **CM-1** ("Docs real"). **Resolved via DR-2026-002:** narrow reading adopted — aggregate governance documentation is real (CM-1 for gate purposes). Strict per-dimension CM-1 deferred; seven dimensions remain at CM-0, which is expected at Stage 0 entering P1.

### What would move each dimension from 0/1 to 2

| Dimension | Minimum next action |
|---|---|
| CM-D1 | Log the first real Decision Record in [`06_DECISIONS.md`](06_DECISIONS.md) |
| CM-D2 | Publish [`07_GLOSSARY.md`](07_GLOSSARY.md) v1 and execute the onboarding reading path once, even solo |
| CM-D3 | Write a spec for the documentation-drafting AI-assistance pattern and register it, even informally, with a named owner |
| CM-D4 | Confirm legal entity status and open a basic accounting record, even a spreadsheet, per [Simple before complex](02_FOUNDING_PRINCIPLES.md#simple-before-complex) |
| CM-D5 | N/A until first asset — no action possible yet |
| CM-D6 | N/A until first asset — no action possible yet |
| CM-D7 | Run one real initiative through the full [Project Lifecycle](00_ATLAS_BRAIN.md#project-lifecycle), including a brief and a retrospective |
| CM-D8 | Publish role-charter language for the Brain-lead-as-all-departments arrangement |
| CM-D9 | Publish a minimal tooling inventory and an access/identity baseline note |
| CM-D10 | Close the loop on this document's own first review — the retrospective on "did the P0 exit gaps get closed" is CM-D10's first data point |

---

## Current AI Maturity

AI maturity here refers to the **process-level L0–L4 model** in [AI Strategy § AI maturity model](00_ATLAS_BRAIN.md#ai-maturity-model), distinct from Holding CM above.

### Process inventory and maturity

| Process | Current L-level | Notes |
|---|---|---|
| Brain document drafting / editing | **Informal L1** (Assisted) | AI assistance used to draft and structure Brain documents; human (Антон) directs, reviews, and approves every substantive claim. Not yet formally spec'd, registered, or owned per [Agent design standards](00_ATLAS_BRAIN.md#agent-design-standards) — this is a gap, not a maturity claim |
| Financial close | **N/A** | No financial process exists yet |
| Customer support | **N/A** | No customers exist yet |
| Due diligence | **N/A** | No deal pipeline exists yet |
| Reporting / dashboards | **N/A** | No data exists yet to report on |
| Every other repeated Atlas process | **L0 (Manual)**, by default, because no repeated process has been identified yet | Per [AI maturity model](00_ATLAS_BRAIN.md#ai-maturity-model), L0 is "acceptable only for novel or high-stakes work" — everything today is novel, first-time work, so L0 is the correct and expected default |

### Distance to default target

The Brain's default target is **L2 or higher within 90 days of process stabilization** ([AI Strategy](00_ATLAS_BRAIN.md#ai-strategy)). No process has stabilized yet (nothing has been repeated three times), so the 90-day clock has not started for any workflow. This remains expected early in Phase P1.

### AI adoption process status

Per the [AI adoption process](00_ATLAS_BRAIN.md#ai-adoption-process) (Identify → Spec → Prototype → Evaluate → Deploy → Document):

| Stage | Status |
|---|---|
| Identify | Informally identified: documentation drafting is repetitive enough to be a candidate |
| Spec | 🟡 Partial — AR-003 Spec committed (`ar003_staleness_flagging_spec.md`); other candidates lack Specs |
| Prototype | 🟡 Partial — AR-002, AR-003, AR-006 each have Prototype Run #1 recorded; not promoted |
| Evaluate | **Not Yet Implemented** — no 2–4 week Evaluate against baseline |
| Deploy | **Not Yet Implemented** |
| Document | 🟡 Partial — registry Evaluation lines + AR-003 Spec only |

### Data and security posture for AI

Per [Data and security principles](00_ATLAS_BRAIN.md#data-and-security-principles): portfolio company data segmentation is **not applicable** (no portfolio exists), and AI output traceability is currently informal (a human directly supervises every AI-assisted document). No sensitive data categories (financial, personal, legal) are in scope yet.

---

## Current AI Capabilities

This section describes **what AI can actually do inside Atlas today**, as distinct from the maturity-level assessment above.

### What exists

| Capability | Status | Description |
|---|---|---|
| AI-assisted document drafting | **Active, informal** | Used to produce the Brain document set, including this document, under direct human direction and review |
| AI-assisted research or analysis | **Not Yet Implemented** | No due diligence, market research, or financial analysis has been performed |
| AI-assisted operational execution | **Not Yet Implemented** | No operations exist to execute |
| AI agents with defined guardrails/owners | 🟡 Partial | Registry exists with 6 candidates; none promoted to production L2; guardrails recorded as proposed fields |
| AI-assisted decision scoring | **Not Yet Implemented** | No decision has been scored against the [Decision Framework](00_ATLAS_BRAIN.md#decision-framework) criteria table yet |
| AI-assisted retrieval over the knowledge base | **Not Yet Implemented** | The knowledge base is small enough today to read directly; retrieval tooling has not been built |

### Model and vendor posture

Atlas's stated principle is to [stay model-agnostic](00_ATLAS_BRAIN.md#ai-strategy) and evaluate continuously. In practice today: **Unknown / TBD** — no formal model evaluation, vendor comparison, or model selection policy has been documented. The AI assistance used to date has been ad hoc, through whatever tooling the operator had on hand (an AI coding/writing assistant embedded in the operator's editor), not the product of a deliberate model-selection process.

### Gap between capability and standard

The single largest gap: Atlas has *used* AI before it has *governed* its use of AI per its own [Automation Standards](00_ATLAS_BRAIN.md#automation-standards). This is a normal and low-risk gap at Stage 0 with no sensitive data and no external stakeholders, but it should not persist once a second workflow or a second person is introduced. See [Current Automation](#current-automation) for the registry gap specifically.

---

## Current Brain Status

### Document-by-document status

| Document | Status | Version | Last updated | Review date |
|---|---|---|---|---|
| [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) | Active | 1.1 | 2026-08-08 | 2026-11-08 |
| [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) | Active | 1.0 | 2026-08-08 | 2026-11-08 |
| [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) | Active | 1.0 | 2026-08-08 | 2026-11-08 |
| [`03_ORGANIZATION.md`](03_ORGANIZATION.md) | Active | 1.0 | 2026-08-08 | 2026-11-08 |
| [`04_ROADMAP.md`](04_ROADMAP.md) | Active | 1.0 | 2026-08-08 | 2026-11-08 |
| [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) | Active (this document) | 1.3.1 | 2026-08-10 | 2026-11-08 |
| [`06_DECISIONS.md`](06_DECISIONS.md) | Active | 1.0 | 2026-08-08 | 2026-11-08 |
| [`07_GLOSSARY.md`](07_GLOSSARY.md) | Active | 1.0 | 2026-08-08 | 2026-11-08 |

### Brain document freshness

Brain document freshness is a Brain-level KPI ([Brain § KPIs](03_ORGANIZATION.md#department-brain)): "% on review schedule." Today, 8 of 8 documents (100%) are on schedule by virtue of having just been created; the review-schedule discipline has not yet been tested by the passage of time. The first real test of this KPI is 2026-11-08.

### Brain-level decisions pending

| Pending Brain-level question | Status | Notes |
|---|---|---|
| Interpretation of the CM-1 phase gate (narrow vs strict reading) | **Closed** — narrow reading adopted in DR-2026-002 | Resolved at P0→P1 gate |
| Whether/when to declare P0 exited | **Closed** — P0 exited 2026-08-08 via DR-2026-002 | Phase P1 active |
| Formal registration of the AI-assisted-drafting pattern | **Open** | Candidate **DR-2026-008** (unused ID; live DR-2026-003 is irreversible-commitment threshold); flagged in [Current AI Maturity](#current-ai-maturity) |

**Unknown / TBD.** No board, advisor, or investor relationship is documented anywhere in the current vault. If any exists informally, it is not yet reflected in governance and should be, per [Transparency](02_FOUNDING_PRINCIPLES.md#transparency) and [Integrity](02_FOUNDING_PRINCIPLES.md#integrity).

---

## Current Knowledge System

### Knowledge architecture — actual vs designed

[Knowledge architecture](00_ATLAS_BRAIN.md#knowledge-management) specifies: `02_Brain/` for strategy, department playbooks for execution knowledge, a decision log, a glossary, project archives, and research. Actual state:

| Designed layer | Actual state |
|---|---|
| `02_Brain/` strategy and principles | ✅ Present — 8 active documents (`00`–`07`) |
| Department playbooks/SOPs | 🟡 **Partial** — 7 of 7 Draft T3 playbooks exist; T4 sparse (`finance_close_sop.md` only) |
| `06_DECISIONS.md` decision log | ✅ **Operational** — Active v1.0; **4 Register entries** (DR-2026-001 through DR-2026-004) |
| `07_GLOSSARY.md` shared vocabulary | ✅ **Active** — v1.0, ~150 terms |
| Project archives | 🟡 **Partial** — P-001 active; Market Screen brief + stage retrospective in `03_Knowledge/`; **P1.2 Not Met** under strict criterion |
| Research folder | 🔴 **Not Yet Implemented** — no separate research commission beyond P-001 screening artifacts |

### Knowledge lifecycle status

Against the five-stage [Knowledge lifecycle](00_ATLAS_BRAIN.md#knowledge-management) (Capture → Organize → Surface → Validate → Apply):

| Stage | Status |
|---|---|
| Capture | 🟡 Partial — Brain docs + 4 Decision Records captured; P-001/Market Screen brief + stage retrospective exist in Knowledge; capture is incomplete, not zero |
| Organize | 🟡 Partial — numbered filenames and cross-references exist; no tagging system beyond the file naming convention |
| Surface | 🔴 Not started — no search or retrieval tooling; findability today depends on direct file reading |
| Validate | 🔴 Not started — no document has yet reached its first review date |
| Apply | 🟡 Early — live DRs and the P0→P1 gate used governance docs as evidence; repeated day-to-day evidence-based decision practice is still limited/immature |

### Onboarding knowledge path — execution status

The [onboarding reading path](00_ATLAS_BRAIN.md#onboarding-knowledge-path) (Brain → Why → Glossary → playbooks → Current State/Roadmap) has been executed as a dry-run and **all five steps succeed** — see [Appendix I](#appendix-i--onboarding-path-dry-run). Step 4 (department playbooks), previously blocked, now succeeds because all 7 department playbooks exist. This is milestone **M-K-002** ([Knowledge cluster](04_ROADMAP.md#strategic-milestones)) — status **Met**, and is the evidence for [Phase 1 exit criterion P1.8](04_ROADMAP.md#phase-1--operating-kernel) ("Onboarding path executed once").

### Single source of truth audit

A spot-check against [One source of truth](02_FOUNDING_PRINCIPLES.md#one-source-of-truth): no duplication has been detected across the eight active Brain documents. Each of the seven department definitions, the AI maturity model, and the decision framework are defined exactly once in their canonical homes and referenced, not restated, elsewhere. This document has been written under the same discipline — see the extensive cross-references throughout.

---

## Current Organization

### Headcount

| Metric | Value |
|---|---|
| Named individuals | 1 |
| Full-time equivalents | 1 |
| Contractors on record | 0 |
| Advisors on record | 0 |
| Board members on record | 0 |
| Total departments with a named head | 7 of 7 (same individual for all seven) |

### The one operator

**Антон (Anton)** — Brain Lead / Holding Lead. Per [Stage 0](03_ORGANIZATION.md#stage-0-one-operator), this individual currently holds every department head role concurrently. Role, self, something else — role classification beyond "Brain Lead / Holding Lead" is not further specified in any document to date.

### Department staffing table

| Department | Head (current) | Additional staff | Staffing gap vs Stage 1 target |
|---|---|---|---|
| Brain | Антон | None | Stage 1 expects a named Brain lead distinct in function, if not headcount, from other heads — met by role clarity, not by headcount |
| Knowledge | Антон (dual-hat) | None | No dedicated Knowledge function yet |
| AI | Антон (dual-hat) | None | No dedicated AI function yet |
| Finance | Антон (dual-hat) | None | No dedicated Finance function yet |
| Operations | Антон (dual-hat) | None | No dedicated Operations function yet |
| Assets | Антон (dual-hat) | None | No dedicated Assets function yet |
| Projects | Антон (dual-hat) | None | No dedicated Projects function yet |

### Reporting lines

There are no reporting lines to report — a single individual has no peer, superior, or subordinate inside Atlas today. The [Reporting Relationships](03_ORGANIZATION.md#reporting-relationships) framework becomes active at Stage 1.

### Dual-hat labeling discipline

Per [Stage 0 primary risk mitigation](03_ORGANIZATION.md#stage-0-one-operator), dual-hatting must be labeled in writing when acting across departments. This document is itself an example: it is being produced under the **Brain hat**, with inputs that would, at scale, come from Knowledge, AI, Finance, Operations, Assets, and Projects heads — all currently the same person, contributing no separately labeled input because no separate function exists yet to label. This is flagged here explicitly rather than silently assumed.

---

## Current Departments

Department **definitions, scope, responsibilities, and interfaces** are canonical in [Organization § Department: Brain](03_ORGANIZATION.md#department-brain) through [Department: Projects](03_ORGANIZATION.md#department-projects) — not restated here. This section reports **current activity level** only.

| Department | Mission (link) | Current activity level | Current output |
|---|---|---|---|
| [Brain](03_ORGANIZATION.md#department-brain) | Define direction, maintain governance | **Active — primary activity to date** | 5 active T1 documents; this document |
| [Knowledge](03_ORGANIZATION.md#department-knowledge) | Institutional memory | 🟡 **Early** | Glossary + 4 DRs + Draft playbooks exist; depth still early |
| [AI](03_ORGANIZATION.md#department-ai) | Intelligent infrastructure | 🟡 **Early** | Registry (6 candidates) + AR-003 Spec; Prototype Runs on AR-002/003/006; production L2 = 0 |
| [Finance](03_ORGANIZATION.md#department-finance) | Capital and economic truth | 🟡 **Early** | Close SOP exists; no CoA, **0 closes**, capital buckets TBD; **P1.5 Not Met** |
| [Operations](03_ORGANIZATION.md#department-operations) | Execution discipline | 🟡 **Early** | Integration scorecard template exists (P1.6); KPI dictionary / broad SOP library still missing |
| [Assets](03_ORGANIZATION.md#department-assets) | Portfolio ownership | **Dormant** | No pipeline, no portfolio company, no due diligence artifact |
| [Projects](03_ORGANIZATION.md#department-projects) | Initiative delivery | 🟡 **Early** | P-001 active with Market Screen intake/triage/brief evidence; **P1.2 Not Met** (strict) |

### Department KPI status

Every department KPI defined in the Brain and Organization documents (e.g., "Brain document freshness," "Escalation resolution time," "Integration scorecard completeness") is currently **unmeasured** because no measurement system exists. See [Current KPIs](#current-kpis) for the full inventory of defined-but-unmeasured KPIs.

### Cross-department interaction matrix — current reality

The [Cross-department interaction matrix](00_ATLAS_BRAIN.md#cross-department-interaction-matrix) describes seven departments exchanging information. Today, every cell in that matrix collapses to "the same person talking to themselves in writing." This is not a defect — writing to oneself under department labels is exactly the Stage 0 discipline the Organization document prescribes — but it means the matrix has not yet been *tested* by an actual cross-party interaction.

### Department deep dives

Each subsection below walks the department's canonical responsibility, ownership, KPI, and decision-authority tables from [`03_ORGANIZATION.md`](03_ORGANIZATION.md) and reports the current status of every line item. Designed content (responsibility names, KPI targets, decision types) is quoted, not redefined, from the Organization document; only the "Current status" and "Live value" columns originate here.

#### Brain — deep dive

Canonical section: [Department: Brain](03_ORGANIZATION.md#department-brain).

| Responsibility (designed) | Designed output | Current status |
|---|---|---|
| Maintain Brain documents (00–07) | Updated governance docs | 🟢 8 of 8 documents Active; 4 Register entries |
| Set holding priorities | Quarterly priority memo | 🔴 No priority memo has been produced |
| Resolve cross-department ownership disputes | Decision Record | 🔴 No dispute has occurred (impossible with one person) |
| Approve principle exceptions | DR + Principles log | 🔴 Zero exceptions requested |
| Review escalation above department thresholds | Escalation resolution | 🔴 Zero escalations received |
| Coordinate board / investor communication | Board materials | 🔴 No board/investor relationship documented |

**KPI live values:**

| KPI (target) | Live value |
|---|---|
| Brain document freshness ≥ on-schedule (Quarterly) | 100% (8/8 docs exist and are dated) |
| Decision Record completeness (Per decision) | 100% for 4 logged decisions (DR-2026-001 through DR-2026-004) |
| Decision log search success rate (> 95%) | N/A — 4 entries; formal search not yet tested |
| Escalation resolution time (median < 5 business days) | N/A — 0 escalations |
| Cross-department dispute count (trending down) | 0 (floor value — cannot go lower) |
| Strategic priority clarity score (quarterly survey) | Not surveyed — no survey instrument exists |

**Decision authority exercised:** 2 Strategic DL-4 (DR-2026-001, DR-2026-002) and 2 Operational (DR-2026-003 DL-1, DR-2026-004 DL-2) logged. Other authority types remain at 0.

#### Knowledge — deep dive

Canonical section: [Department: Knowledge](03_ORGANIZATION.md#department-knowledge).

| Responsibility (designed) | Designed output | Current status |
|---|---|---|
| Maintain documentation standards | T2 standards docs | 🟡 Standards exist embedded inside T1 documents; no standalone T2 artifact |
| Operate knowledge base architecture | Index, taxonomy, search | 🔴 No index, taxonomy, or search tooling — direct file reading only |
| Curate onboarding reading paths | Onboarding guides | ✅ All 5 steps pass; P1.8 Met — see [Appendix I](#appendix-i--onboarding-path-dry-run) |
| Flag stale / orphaned documents | Staleness reports to owners | 🟡 No recurring production automation; AR-003 Spec + Prototype Run #1 exist (still L0); production L2 = 0; AR-002/006 also have Prototype Run #1 only |
| Support due diligence research | Research briefs (with Assets) | 🔴 No DD request has occurred |
| Maintain decision log structure | Searchable `06_DECISIONS.md` | ✅ **4 entries** (DR-2026-001 through DR-2026-004) |
| Coordinate glossary updates | Proposals to Brain for `07_GLOSSARY.md` | ✅ Glossary v1.0 published; maintenance process defined in [`07_GLOSSARY.md`](07_GLOSSARY.md) |

**KPI live values:**

| KPI (target) | Live value |
|---|---|
| Document staleness rate (< 10%) | 0% measured — not a real 0%, simply unmeasured; no document has passed its review date |
| Onboarding path completion time (< 5 business days) | ✅ Dry-run complete within hours — P1.8 Met; see [Appendix I](#appendix-i--onboarding-path-dry-run) |
| Decision log search success rate (> 95%) | N/A — 4 entries; formal search not yet tested |
| Playbook compliance (% processes with SOP) | Sparse — 1 T4 SOP (`finance_close_sop.md`) against Draft playbooks; most processes still lack SOPs |
| Knowledge reuse rate (trending up) | N/A — no reuse events possible with one reader |

**Decision authority exercised:** 0 of any type (T2 standard changes, taxonomy changes, archive decisions, research prioritization, tool selection).

#### AI — deep dive

Canonical section: [Department: AI](03_ORGANIZATION.md#department-ai).

| Responsibility (designed) | Designed output | Current status |
|---|---|---|
| Build and maintain agents | Production agents in registry | 🔴 Registry exists with 6 candidates; **0 production agents**; L2 = 0 |
| Enforce agent design standards | Specs with owner, guardrails, fallback | 🟡 1 Spec written (AR-003); other candidates lack Specs |
| Operate automation registry | Quarterly portfolio review | 🟡 Registry exists (6 candidates); quarterly portfolio review not yet run |
| Evaluate and adopt models | Model evaluation reports | 🔴 No formal evaluation has been run; model choice is informal/ad hoc |
| Embed AI in Operations workflows | L2+ automations for repeated processes | 🔴 No Operations workflows exist yet to embed AI into |
| Support Finance reporting automation | Automated pipelines | 🔴 Not applicable — no Finance reporting exists |
| Support Assets analysis | DD automation tooling | 🔴 Not applicable — no deal pipeline exists |

**KPI live values:**

| KPI (target) | Live value |
|---|---|
| Repeated processes at L2+ (90% within 90 days of stabilization) | 0% — no process has stabilized (none has repeated ≥3×) |
| Automation ROI (positive for all production automations) | N/A — 0 production automations |
| Agent failure rate (below threshold per agent) | N/A — 0 agents |
| Mean time to deploy new automation (trending down) | N/A — no baseline exists yet |
| Cross-portfolio agent reuse rate (trending up) | N/A — no portfolio, no agents |

**Decision authority exercised:** 0 — no agent deployment, model vendor selection, holding-wide AI standard change, cross-portfolio data access grant, or autonomy promotion has occurred.

#### Finance — deep dive

Canonical section: [Department: Finance](03_ORGANIZATION.md#department-finance).

| Responsibility (designed) | Designed output | Current status |
|---|---|---|
| Monthly / quarterly financial close | Financial statements | 🟡 Close SOP exists; **0 actual closes**/statements; **P1.5 Not Met** |
| Portfolio KPI dashboards | Unit economics reports | 🔴 Not applicable — no portfolio |
| Investment memos (financial section) | Models and scenarios | 🔴 No memo has been drafted |
| Capital bucket management | Allocation reports | 🔴 Buckets are structurally defined in the Brain; live percentages are **TBD** (see [Current Finance](#current-finance)) |
| Threshold definition for escalations | Updated threshold tables | ✅ Threshold table populated (P1.7 Met) via live values + [DR-2026-003](06_DECISIONS.md#dr-2026-003-adopt-brain-default-irreversible-commitment-escalation-threshold-for-finance) / [DR-2026-004](06_DECISIONS.md#dr-2026-004-set-temporary-phase-1-capital-commitment-escalation-threshold-at-10-of-deployable-capital); first quarterly refresh not yet due (next review 2026-11-08); thresholds have not been exercised against a real production commitment |
| Compliance and tax filing | Filed returns, audit readiness | 🔴 **Unknown/TBD** whether any filing obligation currently exists |

**KPI live values:**

| KPI (target) | Live value |
|---|---|
| Close timeline (≤ 10 business days) | N/A — SOP exists but **0 actual closes** have run |
| Forecast accuracy, rolling 90-day (within band) | N/A — no forecast exists |
| Portfolio reporting compliance (100% on-time) | N/A — no portfolio |
| Unit economics coverage (100% of operating assets) | N/A — 0 operating assets |
| Escalation threshold freshness (updated quarterly) | ✅ Values published (P1.7 Met via live thresholds + DR-2026-003/004); first quarterly refresh not yet due |

**Decision authority exercised:** 0 — no expense approval, budget reallocation, capital deployment, hurdle rate change, or financial vendor decision has occurred.

#### Operations — deep dive

Canonical section: [Department: Operations](03_ORGANIZATION.md#department-operations).

| Responsibility (designed) | Designed output | Current status |
|---|---|---|
| Define and maintain core SOPs | T4 SOP library | 🟡 1 SOP published (`finance_close_sop.md`); library otherwise empty |
| Operate shared services | Service catalog | 🔴 Not applicable — no shared services exist |
| Monitor operational KPIs | Dashboards | 🔴 No dashboard exists |
| Run integration playbooks | Integration scorecards | 🔴 Not applicable — no asset to integrate |
| Incident response (ops) | Incident reports | 🔴 0 incidents; runbook never exercised |
| Identify automation candidates | Automation intake queue | ✅ Formal queue exists — [`automation_registry.md`](departments/automation_registry.md) with 6 candidates; AR-001 remains informal/unregistered L1; AR-002/003/006 remain L0 with Prototype Run #1 only |

**KPI live values:**

| KPI (target) | Live value |
|---|---|
| SOP coverage for repeated processes (> 95%) | Near-zero — 1 SOP exists; repeated-process volume still low |
| Integration scorecard completion (100%, on timeline) | N/A — no integration underway |
| Operational incident MTTR (per severity SLA) | N/A — 0 incidents |
| KPI dashboard freshness (daily for critical metrics) | N/A — no dashboard |
| Automation candidate conversion rate (trending up) | N/A — 0 candidates converted to production; 6 registered; Prototype Runs only |

**Decision authority exercised:** 0 — no process change, vendor selection, or incident-containment action has occurred.

#### Assets — deep dive

Canonical section: [Department: Assets](03_ORGANIZATION.md#department-assets).

| Responsibility (designed) | Designed output | Current status |
|---|---|---|
| Pipeline management | Opportunity briefs | 🔴 0 opportunity briefs; pipeline existence itself is **Unknown** (see [Current Assets](#current-assets)) |
| Due diligence | DD reports | 🔴 0 DD reports |
| Deal closing / venture launch | Close checklists | 🔴 0 deals closed, 0 ventures launched |
| Board materials and governance | Board packs | 🔴 Not applicable — no portfolio company boards |
| Exit analysis | Exit memos | 🔴 Not applicable — nothing to exit |
| Portfolio operator performance management | Performance reviews | 🔴 Not applicable — no portfolio operators |

**KPI live values:**

| KPI (target) | Live value |
|---|---|
| Pipeline quality — conversion to close (per strategy) | N/A — no pipeline on record |
| Integration initiation within SLA (100%) | N/A — no integration |
| Portfolio company KPI vs plan (monitored monthly) | N/A — 0 portfolio companies |
| MOIC / IRR by asset (vs hurdle rate) | N/A — 0 invested capital |
| Exit discipline (per capital policy) | N/A — no exits possible |

**Decision authority exercised:** 0 — no pass/proceed-to-DD/LOI/close/exit decision has occurred.

#### Projects — deep dive

Canonical section: [Department: Projects](03_ORGANIZATION.md#department-projects).

| Responsibility (designed) | Designed output | Current status |
|---|---|---|
| Operate intake and triage | Approved / deferred / rejected log | 🟡 Used on P-001/Market Screen (A–E triage); no standing intake tracker yet; **P1.2 Not Met** |
| Maintain project portfolio view | Status dashboard | 🔴 No dashboard exists |
| Assign DRIs and contributors | Project briefs | 🟡 P-001 / Market Screen briefs exist; not a standing multi-brief cadence; **P1.2 Not Met** |
| Run milestone reviews | Gate decisions | 🔴 0 gate reviews held |
| Conduct retrospectives | Retro docs → Knowledge | 🟡 1 Market Screen stage retrospective in Knowledge; no project-close retros; **P1.2 Not Met** |
| Confirm handoffs | Handoff checklists | 🔴 0 handoffs — nothing has been produced by a tracked project to hand off |

**KPI live values:**

| KPI (target) | Live value |
|---|---|
| On-time milestone delivery (> 80%) | Partial tracking — Phase 1 / P-001 / Market Screen milestones and evidence exist; not all complete; on-time % not yet a meaningful rate |
| Projects with approved brief before execution (100%) | Partial — P-001/Market Screen briefs exist; Brain drafting largely preceded formal briefs; **P1.2 Not Met** |
| Handoff completion before project close (100%) | N/A — 0 projects closed under the lifecycle |
| Retrospective within 5 days of close (100%) | N/A — 0 closes |
| Red project escalation to Brain within 48 hours | N/A — P-001 is tracked/active; 0 red escalations recorded |

**Decision authority exercised:** 0 — no intake/triage/scope-change/handoff decision has been formally made through the Projects process, though informal equivalents of these decisions were made without the tracking apparatus.

---

## Current Ownership

Per [Single Owner Principle](03_ORGANIZATION.md#single-owner-principle) and [Ownership](02_FOUNDING_PRINCIPLES.md#ownership), every artifact must have exactly one named human owner.

### Document ownership

| Artifact | Owner | Hat worn |
|---|---|---|
| `00_ATLAS_BRAIN.md` | Антон | Brain |
| `01_WHY_ATLAS_EXISTS.md` | Антон | Brain |
| `02_FOUNDING_PRINCIPLES.md` | Антон | Brain |
| `03_ORGANIZATION.md` | Антон | Brain |
| `04_ROADMAP.md` | Антон | Brain |
| `05_CURRENT_STATE.md` | Антон | Brain (with input intended from all departments, currently self-supplied) |
| `06_DECISIONS.md` (once initialized) | Антон | Brain (curation); decision owners submit records |
| `07_GLOSSARY.md` (once initialized) | Антон | Brain (curation); all departments propose terms |
| The Atlas vault / knowledge base itself | Антон | Knowledge |
| AI-assisted drafting workflow | Антон | AI |
| (No financial ledger exists yet) | — | Finance — unowned pending existence |
| `finance_close_sop.md` | Антон (Finance hat) | Finance — close SOP; other SOPs still absent |
| (No portfolio asset exists yet) | — | Assets — unowned pending existence |
| P-001 / Market Screen briefs | Антон (Projects hat) | Projects — see `01_Projects/…` and `03_Knowledge/`; **P1.2 Not Met** |

### Ownership audit

Per the [Ownership counter-examples](02_FOUNDING_PRINCIPLES.md#ownership), ownership without authority is performative. At Stage 0, the sole operator holds full authority over every artifact listed above by default — there is no authority gap to audit yet. This will need explicit re-verification the moment a second person is granted any ownership.

### Unowned gaps

The following still have **no artifact yet to attach ownership to**: financial ledger, first portfolio asset. **Now exist and are owned:** `finance_close_sop.md`, P-001/Market Screen project briefs, automation registry candidates / AR-003 Spec (Антон). Existence here does **not** imply operational completion (e.g. **0 closes**, **P1.2 Not Met**, production L2 = 0).

---

## Current Roles

### Named roles

| Role | Individual | Status |
|---|---|---|
| Brain Lead / Holding Lead | Антон | Active |
| Head of Knowledge | Антон (dual-hat) | Active, informal |
| Head of AI | Антон (dual-hat) | Active, informal |
| Head of Finance / CFO | Антон (dual-hat) | Active, informal |
| Head of Operations / COO | Антон (dual-hat) | Active, informal |
| Head of Assets | Антон (dual-hat) | Active, informal |
| Head of Projects | Антон (dual-hat) | Active, informal |

### Role charters

Per [Stage 1 requirement](03_ORGANIZATION.md#stage-1-10-people), "Role charters published" as T3 documents is a Stage 1 marker, not a Stage 0 requirement — but per [Stage 0 structural rules](03_ORGANIZATION.md#stage-0-one-operator), owners must still be assigned even without full charters. **No role charter document exists yet for any of the seven hats.** This is an acceptable gap at Stage 0 and a recommended early action regardless (see [Appendix B](#appendix-b--next-90-days-watch-list)).

### Open roles

**None formally open.** No requisition, job description, or hiring intent has been documented for any role. See [Current Hiring Readiness](#current-hiring-readiness) for why this is currently correct.

### Role, self, something else

Per user-level context available to this document, the operator's role is recorded elsewhere as "Something else" rather than a fixed corporate title — consistent with the fluid, all-hats nature of Stage 0 and not treated here as a gap.

---

## Current Decision System

### Decision Framework activation status

The [Decision Framework](00_ATLAS_BRAIN.md#decision-framework) has been run end-to-end once — **DR-2026-001** (Build full Brain governance set before operating activity), logged retroactively in [`06_DECISIONS.md`](06_DECISIONS.md).

### Decision log

| Metric | Value |
|---|---|
| Total Decision Records logged | **2** |
| `06_DECISIONS.md` status | Active v1.0 — **4 entries** (DR-2026-001 through DR-2026-004) |
| Oldest open decision | N/A |
| Decisions overdue for review | N/A |
| Decisions by type (Investment / Operational / Strategic / Personnel / Technical) | Strategic: 2; all others: 0 |

### The nearest thing to a decision made so far

**DR-2026-001 through DR-2026-004 logged.** See [`06_DECISIONS.md` § Decision Register](06_DECISIONS.md#decision-register).

### Escalation activity

| Metric | Value |
|---|---|
| Escalations raised | 0 |
| Escalations resolved | 0 |
| Median escalation resolution time | N/A — no data |
| Escalation thresholds currently in force | See [Current Governance](#current-governance) |

### One-way vs two-way door classification practice

No decision has yet been explicitly classified as a [one-way or two-way door](00_ATLAS_BRAIN.md#one-way-vs-two-way-doors). The practice is defined but unexercised.

---

## Current Governance

### Governance boundary status

[Governance Boundaries](03_ORGANIZATION.md#governance-boundaries) and the [Decision Framework escalation table](00_ATLAS_BRAIN.md#escalation) define triggers and thresholds. Live numeric values for those thresholds are supposed to live in this document. **All five now carry live values — three by explicit N/A/count, two by formal decision (Irreversible commitment, Capital commitment) — see the table below.**

### Escalation thresholds — live values

| Trigger category | Defined threshold type | Current numeric value |
|---|---|---|
| Capital commitment | % of deployable capital | **10%** (temporary Phase 1 default) — see [DR-2026-004](06_DECISIONS.md#dr-2026-004-set-temporary-phase-1-capital-commitment-escalation-threshold-at-10-of-deployable-capital). No real deployable-capital figure exists yet, so this threshold has not been exercised against a real commitment. |
| New portfolio asset | Any acquisition or venture launch | N/A — escalates to self at Stage 0; will require real process at Stage 1 |
| Holding-wide standard change | Affects 2+ departments | N/A — all departments are the same person today |
| Irreversible commitment | Contract > 12 months, exclusivity, IP transfer | **Adopted as-is** (Brain default, unmodified) — see [DR-2026-003](06_DECISIONS.md#dr-2026-003-adopt-brain-default-irreversible-commitment-escalation-threshold-for-finance). No contract has triggered it to date. |
| Principle exception | Any deviation from Core Principles | 0 exceptions granted to date |

### Governance council / advisory bodies

Per [Stage 3 profile](03_ORGANIZATION.md#stage-3-200-people), a governance council becomes relevant much later, as advisory-only. **Not applicable at Stage 0.** No advisory body of any kind currently exists — see [Current Brain Status § Board/investor relationship](#current-brain-status).

### Principle exceptions on record

**Zero.** No exception to any [Founding Principle](02_FOUNDING_PRINCIPLES.md) has been requested or granted.

### Governance review cadence — actual vs designed

| Review | Designed cadence | Times actually held |
|---|---|---|
| Quarterly Brain review | Quarterly | 0 |
| Quarterly org review checklist | Quarterly | 0 |
| Quarterly risk review | Quarterly | 0 |
| Annual comprehensive risk audit | Annual | 0 |
| Annual portfolio-level assessment | Annual | 0 (no portfolio) |

---

## Current Assets

### Portfolio inventory

**Zero portfolio assets exist at any [Company Lifecycle](00_ATLAS_BRAIN.md#company-lifecycle) stage** — Prospect, Evaluate, Acquire/Build, Integrate, Operate, Optimize, or Exit/Hold.

| Lifecycle stage | Count | Names |
|---|---|---|
| Prospect | 0 | — |
| Evaluate | 0 | — |
| Acquire / Build | 0 | — |
| Integrate | 0 | — |
| Operate | 0 | — |
| Optimize | 0 | — |
| Exit / Hold | 0 | — |

### Pipeline

**Unknown / TBD.** No opportunity brief, target list, or informal pipeline tracker exists in the vault. If any informal pipeline exists in the operator's head, it is — per [Extreme documentation](02_FOUNDING_PRINCIPLES.md#extreme-documentation) — not yet real for organizational purposes.

### Build-vs-acquire posture

The [Build vs. acquire framework](00_ATLAS_BRAIN.md#build-vs-acquire-framework) exists as a decision tool but has not been applied to any real opportunity. No sector, geography, or thesis preference has been documented.

### Integration capability

The [Integration standards](00_ATLAS_BRAIN.md#company-lifecycle) (30/45/60/14/45-day thresholds) are canonical in Brain. Milestone **M-O-002 / P1.6**: Draft template [`integration_scorecard.md`](departments/integration_scorecard.md) exists and is **Met** as scorecard v1; **zero assets** have triggered a live scored instance.

### Exit posture

**Not applicable.** [Exit criteria](00_ATLAS_BRAIN.md#exit-criteria) cannot be evaluated against a portfolio that does not exist.

---

## Current Projects

### Project portfolio

**P-001 — Atlas Operating System** is **Active** under `01_Projects/P-001_ATLAS_OPERATING_SYSTEM/`, with Market Screen artifacts and a Knowledge-layer brief + stage retrospective.

**Phase 1 exit criterion P1.2 remains Not Met** under the strict reading: lifecycle use on ≥3 initiatives with the required Briefs + retrospectives in Knowledge. Current evidence is partial (one Knowledge brief + one stage retrospective covering Market Screen triage of initiatives A–E; only Initiative A reached a fuller project brief in the Projects folder). This is **not** self-certified as P1.2 complete.

| Lifecycle stage | Count (honest) |
|---|---|
| Intake | ≥1 (P-001 / Market Screen) |
| Triage | 5 initiatives (A–E) recorded in Market Screen materials |
| Brief | 1 Knowledge brief (Market Screen) + OP-022 brief in Projects for Initiative A |
| Plan | 0 |
| Execute | 0 |
| Review | 0 project-close reviews; 1 stage retrospective in Knowledge (Intake→Triage→Brief only) |
| Handoff | 0 |

### Informal work vs formal projects

The eight active Brain documents were substantial work largely outside formal project briefs. P-001 now supplies the first formal project container. Brain drafting still lacks a dedicated retroactive Infrastructure brief — a known gap, not hidden.

### Project health signals

P-001 / Market Screen, if scored informally at current stage, reads 🟡 Yellow — real triage and documentation exist, but no initiative has reached Plan/Execute, and **P1.2 is not satisfied**.

### Milestone register progress (canonical IDs)

Cross-referencing the [Milestone register](04_ROADMAP.md#strategic-milestones):

| Milestone ID | Milestone | Status |
|---|---|---|
| M-G-001 | Brain OS document set Active | 🟡 8 of 8 Active; 4 Register entries |
| M-G-007 | Phase gate P0→P1 passed | ✅ Met — DR-2026-002 |
| M-G-002 | Current State v1 published | ✅ Met |
| M-G-003 | Decision log operational | ✅ Met — DR-2026-001 logged |
| M-K-001 | Glossary v1 | ✅ Met |
| M-K-002 | Onboarding path executed | ✅ Met — all 5 steps pass; see [Appendix I](#appendix-i--onboarding-path-dry-run) |
| M-K-003 | Playbook skeleton ×7 | ✅ Met — 7 Draft playbooks (P1.1 Met) |
| M-A-001 | Automation registry v1 | 🟡 Partial — registry + 6 candidates + owners/maturity exist (**P1.3 Met**); detailed Done-means incomplete (no production entries; most candidates lack SOP links) |
| M-A-002 | First 3 agents in production | 🔴 Not met |
| M-F-001 | Chart of accounts / close SOP | 🟡 Partial — close SOP exists; chart of accounts absent; **P1.5 Not Met** |
| M-O-001 | KPI dictionary v1 | 🔴 Not met |
| M-O-002 | Integration scorecard v1 | ✅ Met — Draft unscored template (P1.6 Met); zero live integrations |
| M-S-001 | Build-vs-acquire checklist in use | 🔴 Not met |
| M-P-001 | Intake/triage process live | 🟡 Partial — P-001/Market Screen used intake/triage; not yet a standing process; **P1.2 Not Met** |
| M-I-001 | Tooling inventory + preferred stack | 🟡 Informal inventory only (see [Current Technical Stack](#current-technical-stack)) |
| M-I-002 | Identity/access baseline | 🔴 Not met |
| All P1 milestones | 🟡 **Active** — P1 entered; P1.1/P1.3/P1.6/P1.7/P1.8 Met; P1.2/P1.4/P1.5 Not Met; Phase 1 exit = No |

---

## Current Automation

### Automation registry

**Exists.** [`automation_registry.md`](departments/automation_registry.md) tracks **six** candidates (AR-001 through AR-006). This satisfies **P1.3**. Ownership: AI hat.

Honest maturity note: **AR-001** remains informal L1 (unregistered). **AR-002, AR-003, and AR-006** each have **Prototype Run #1** evidence recorded; **none** of those three has been promoted beyond **L0**. **AR-003** has a committed Automation Spec (`ar003_staleness_flagging_spec.md`). **P1.4 remains Not Met** (production L2 count = 0).

### Production automations

| Metric | Value |
|---|---|
| Automations registered (candidates tracked) | 6 |
| Automations at formal L1 | 0 (AR-001 is informal L1 only) |
| Automations at L2+ | **0** |
| Automations retired | 0 |
| Prototype Run #1 recorded | AR-002, AR-003, AR-006 (still L0) |
| Committed automation Specs | 1 (AR-003) |

### Automation eligibility review

Per [Automation eligibility criteria](00_ATLAS_BRAIN.md#automation-standards), no candidate has cleared Frequency + Baseline + Evaluate requirements for promotion. AR-003 is furthest along (Spec + Clear definition + Named owner; Documentation Partial) but remains **L0**. **No L1/L2 promotion is claimed.**

### Automation spec inventory

**One** automation Spec exists using the [Automation spec template](00_ATLAS_BRAIN.md#automation-standards): [`ar003_staleness_flagging_spec.md`](departments/ar003_staleness_flagging_spec.md). Other candidates do not yet have Specs.

---

## Current Infrastructure

Distinct from [Current Technical Stack](#current-technical-stack) below: this section covers organizational/operational infrastructure (legal, access, identity), not specific software tools.

| Infrastructure item | Status |
|---|---|
| Legal entity formation | **Unknown / TBD** |
| Jurisdiction | **Unknown / TBD** |
| Banking relationship | **Unknown / TBD** |
| Business insurance | **Unknown / TBD** |
| Identity and access management baseline (milestone M-I-002) | **Not Yet Implemented** |
| Data segmentation policy (milestone M-I-003) | **Not Yet Implemented** — not applicable without a portfolio |
| Backup and disaster recovery policy for the knowledge base | **Not Yet Implemented** — vault is git-versioned locally; no documented offsite backup policy |
| Vendor contracts on record | 0 |
| Physical or cloud infrastructure (servers, hosting) | **Unknown / TBD** — none referenced in any document |

### Infrastructure risk note

The single knowledge base — the entire operating memory of Atlas today — exists as a local, git-versioned folder with **no documented backup or redundancy policy**. This is disproportionately risky relative to how little else exists to lose, and disproportionately cheap to fix. See [Current Risks](#current-risks) and [Appendix B](#appendix-b--next-90-days-watch-list).

---

## Current Technical Stack

### Tooling in active use

| Layer | Tool | Notes |
|---|---|---|
| Knowledge base / documentation | Local Markdown files in an Obsidian vault ("Atlas Lab") | Primary and only knowledge system today |
| Version control | Git (local repository) | 2 commits on `main` as of this writing: initial Brain structure, and the Roadmap addition |
| AI assistance | AI coding/writing assistant (Cursor) | Used to draft and structure governance documents under human direction |
| Project management / tracking | **None** | No tool in use |
| Financial system | **None** | No tool in use |
| CRM / deal pipeline | **None** | No tool in use |
| Communication / collaboration | **Unknown / TBD** | Not referenced in any document |
| Automation / workflow platform | **None** | No tool in use |

### Preferred stack policy

Per [Company Lifecycle § Tooling autonomy](00_ATLAS_BRAIN.md#portfolio-company-autonomy-spectrum), Atlas intends a "preferred stack recommended" posture for portfolio companies. **No preferred stack has been documented for the holding itself yet** — milestone M-I-001 (tooling inventory + preferred stack) is only partially met, informally, by the fact that a stack is *in use*, without having been through a deliberate selection or documentation process.

### Build vs buy status

No build-vs-buy analysis has been performed for any internal tool, because no internal tool has been built. All current tooling is off-the-shelf (git, Obsidian, an AI assistant) — fully consistent with [Simple before complex](02_FOUNDING_PRINCIPLES.md#simple-before-complex) at this scale.

---

## Current Security

### Security posture summary

Atlas today has **minimal attack surface and minimal formal security posture**, roughly proportionate to each other. There is one operator, one local knowledge base, no customer data, no employee data beyond the operator, and no financial systems.

| Security domain | Status |
|---|---|
| Data classification policy | **Not Yet Implemented** |
| Access control policy | **Not Yet Implemented** — implicitly single-user |
| Least-privilege enforcement (humans/agents) | **Not Yet Implemented** — not yet applicable with one user and no agents holding credentials |
| Portfolio data segmentation | **Not applicable** — no portfolio |
| AI output traceability | Informal only — human reviews all AI-assisted output directly |
| Vendor/model security evaluation | **Not Yet Implemented** |
| Incident response plan | **Not Yet Implemented** — the general [Incident response](00_ATLAS_BRAIN.md#risk-management) process is defined at the Brain level but has never been exercised |
| Backup / recovery for knowledge base | **Not Yet Implemented** (see [Current Infrastructure](#current-infrastructure)) |
| Compliance / regulatory registration | **Unknown / TBD** |

### Security incidents

**Zero** recorded to date.

### Security risk framing

Per the [Risk assessment matrix](00_ATLAS_BRAIN.md#risk-management), the likelihood and impact of a security incident today are both low (small, self-contained system with no external data), placing current security risk in the **Accept** cell of the matrix. This will change materially the moment a second person, a financial system, or a portfolio company with customer data is introduced — flagged proactively here so the transition is not missed.

---

## Current Finance

### Financial systems

**Partial.** Monthly Financial Close SOP exists: [`finance_close_sop.md`](departments/finance_close_sop.md). **No chart of accounts**, no accounting software, and **zero actual closes** have occurred. **P1.5 remains Not Met** (requires Finance SOP + actual closes; chart/operating prerequisites still absent).

### Capital

| Field | Value |
|---|---|
| Deployable capital | **Unknown / TBD** |
| Capital committed to portfolio | $0 (no portfolio) |
| Capital committed to infrastructure | **Unknown / TBD** |
| Reserve | **Unknown / TBD** |

### Capital bucket allocation — live values

Per [Capital buckets](00_ATLAS_BRAIN.md#capital-buckets), the Brain explicitly defers exact percentages to this document, reviewed quarterly by Finance + Brain. **No allocation has been set.**

| Bucket | Purpose | Current allocation |
|---|---|---|
| Operating | Day-to-day holding expenses | **TBD** |
| Growth | Build, acquire, expand | **TBD** |
| Infrastructure | Holding OS — AI, systems, knowledge, automation | **TBD** |
| Reserve | Opportunistic / defensive capital | **TBD** |
| Experimental | Small bets, capped % of Growth | **TBD** |

**Action required:** Finance + Brain (currently the same person) must set an initial allocation, even a provisional one, at the next review — an unset table is worse than a provisional one per [Action over perfection](02_FOUNDING_PRINCIPLES.md#action-over-perfection).

### Hurdle rates

**Not Yet Implemented.** No hurdle rate policy (milestone M-F-003) has been published.

### Return measurement

None of the return metrics in [Return measurement](00_ATLAS_BRAIN.md#return-measurement) (ROI, IRR, MOIC, unit economics, Holding ROIC) can be calculated — there is no invested capital and no operating business to measure.

### Financial reporting cadence

**Not Yet Implemented.** No monthly, quarterly, or annual financial report has been produced.

---

## Current Operations

### Operational systems

**Partial.** Integration scorecard template exists (P1.6). Close SOP lives under Finance. Operations still lacks a KPI dictionary (M-O-001), a broad T4 SOP library, vendor management, and any incident-response drill.

### Vendor relationships

**Zero** vendor contracts on record. The AI assistant tool in use (see [Current Technical Stack](#current-technical-stack)) is used under its standard terms; no formal vendor evaluation or contract review has been documented.

### Operational KPI tracking

No operational KPI is currently instrumented. See [Current KPIs](#current-kpis) for the full list of KPIs that are *defined* but *not measured*.

### Incident history

**Zero** operational incidents recorded.

### Continuous improvement cadence — actual vs designed

Per [Continuous improvement as a system](00_ATLAS_BRAIN.md#continuous-improvement-as-a-system), Atlas designs for weekly metric reviews, monthly retrospectives, quarterly strategic reviews, and annual portfolio assessments. **None of these cadences have run a single cycle yet.** The activation of this document is, itself, the first artifact that could anchor a review cadence going forward.

---

## Current Workflows

### Workflow inventory

| Workflow | Status | Notes |
|---|---|---|
| Governance document drafting and versioning | **Active** | The only workflow currently exercised; git commit history and version metadata blocks serve as the audit trail |
| Decision framing and logging | 🟡 Partial | Framework + 4 logged DRs; AR-002 Prototype Run #1 only |
| Project intake and triage | 🟡 Partial | Used on P-001/Market Screen; not a standing multi-initiative cadence; **P1.2 Not Met** |
| Financial close | 🟡 Partial | SOP exists; **0 actual closes**; **P1.5 Not Met** |
| Due diligence | **Not Yet Implemented** | — |
| Integration | 🟡 Partial | Scorecard template exists (P1.6 Met); zero live integrations |
| Onboarding (new operator) | ✅ Dry-run complete | P1.8 Met — see [Appendix I](#appendix-i--onboarding-path-dry-run) |
| Offboarding | **Not Yet Implemented** | Not applicable — no one has ever left |
| Incident response | **Not Yet Implemented** | Framework exists; unused |
| Automation eligibility review | **Not Yet Implemented** | Framework exists; unused |

### Workflow documentation quality

The one active workflow (governance drafting) is **not itself formally documented as an SOP** — it exists only as demonstrated practice (five documents produced with consistent metadata, structure, and cross-referencing). Per [Systems over heroes](02_FOUNDING_PRINCIPLES.md#systems-over-heroes), the fact that this practice currently depends on one person's undocumented habits is itself a flagged gap — see [Current Documentation Gaps](#current-documentation-gaps).

---

## Current Interfaces

Department interface **definitions and SLAs** are canonical in [Department Interfaces](03_ORGANIZATION.md#department-interfaces) and the [Cross-department interaction matrix](00_ATLAS_BRAIN.md#cross-department-interaction-matrix). This section reports current activation status only.

### Interface activation status

| Interface | Designed SLA | Current status |
|---|---|---|
| Brain ↔ Knowledge (doc standards) | Standards updated within 5 days of Brain approval | **Not activated** — one person; no formal hand-off exists |
| Brain ↔ AI (AI strategy) | Strategy doc reviewed quarterly | **Not activated** |
| Brain ↔ Finance (capital policy) | Policy reviewed quarterly | **Not activated** |
| Brain ↔ Operations (ops standards) | Standard changes communicated within 48 hours | **Not activated** |
| Brain ↔ Assets (portfolio direction) | Priority stack updated quarterly | **Not activated** |
| Brain ↔ Projects (priorities) | Priority changes reflected within 1 week | **Not activated** |
| All other department-to-department interfaces | Various | **Not activated** — all collapse to self-interaction at Stage 0 |

### Why interfaces are not yet meaningful

Interface SLAs measure the latency and quality of *hand-offs between distinct accountable parties*. With one party, there is no hand-off to measure. Per [Stage 1 marker](03_ORGANIZATION.md#stage-1-10-people) ("Interface SLAs activate; peer dept heads acknowledge"), this becomes a real, testable system only once a second head is named. Flagged here so the first real interface test is recognized as a milestone when it happens, not treated as routine.

---

## Current Communication

### Internal communication

With one operator, none of the [internal communication principles](00_ATLAS_BRAIN.md#internal-communication) (write it down, default to transparent, bad news fast, one voice, context not just conclusions, async first) have been tested against a second party. They have been partially exercised in the *writing it down* sense — this entire document is an exercise in writing down uncomfortable truths (empty Register, no portfolio) rather than hiding them.

### External communication

| Channel | Status |
|---|---|
| Investor relations | **Unknown / TBD** — no investor relationship documented |
| Press / public communication | **None** |
| Partner communication | **None** |
| Customer communication | **Not applicable** — no customers |

### Communication channels by purpose — activation status

| Purpose (per Brain) | Designed channel | Current status |
|---|---|---|
| Strategic direction | Brain documents, quarterly reviews | 🟡 Documents exist; no quarterly review cycle has run yet |
| Project status | Written status reports | 🟡 P-001/Market Screen artifacts exist; no standing status-report cadence |
| Operational issues | Direct escalation + incident reports | 🔴 No operations to escalate from |
| Decision records | `06_DECISIONS.md` | ✅ Operational — 4 live Register entries |
| Portfolio performance | Finance dashboards + board materials | 🔴 Not applicable |
| Knowledge sharing | Knowledge base, playbooks | 🟡 Base + 7 Draft playbooks exist; depth/usage still early |

---

## Current Planning Process

### Planning artifacts — actual vs designed

Per [Planning artifacts](04_ROADMAP.md#roadmap-architecture):

| Artifact | Designed cadence | Instances produced to date |
|---|---|---|
| Roadmap (T1) | Semi-annual review | 1 (this initial version, v1.0) |
| Annual plan memo | Annual | 0 |
| Quarterly priorities | Quarterly | 0 |
| Department roadmap appendix | Quarterly | 0 |
| Project portfolio | Weekly/monthly | 1 active container (P-001); no weekly/monthly portfolio pack yet |
| Current State | Quarterly | 1 (this document, first activation) |
| Decision Records | On decision | 4 (DR-2026-001 through DR-2026-004) |

### Quarterly Planning Model — status

The [Quarterly Planning Model](04_ROADMAP.md#quarterly-planning-model) exists as a defined process but **has never been run.** The first quarterly planning cycle should be anchored to this document's review date, 2026-11-08.

### Annual Planning Model — status

The [Annual Planning Model](04_ROADMAP.md#annual-planning-model) has never been run formally. Informal P1 theme: **"Make Atlas executable"** — department playbooks, automation registry, project lifecycle (per Roadmap P0–P1 foundation quarter).

---

## Current Review Process

### Review cadences — actual vs designed

| Review | Designed cadence | Held to date | Next due |
|---|---|---|---|
| T1 governance document review | Quarterly | 0 | 2026-11-08 |
| Quarterly Brain review | Quarterly | 0 | 2026-11-08 |
| Quarterly org review checklist | Quarterly | 0 | 2026-11-08 |
| Quarterly risk review | Quarterly | 0 | 2026-11-08 |
| Monthly department retrospective | Monthly | 0 | 2026-09-08 (indicative) |
| Weekly operational metrics review | Weekly | 0 | Not applicable — no operational metrics exist |
| Annual comprehensive risk audit | Annual | 0 | 2027-08 (indicative) |
| Annual portfolio-level assessment | Annual | 0 | Not applicable — no portfolio |

### What the first real review should evaluate

1. P0 exit remains closed; verify **P1.1** remains valid; focus open exit criteria **P1.2 / P1.4 / P1.5**.
2. Decision log health — four live DRs exist; are open Appendix E proposals advancing without ID collisions?
3. Whether the informal AI-assistance pattern has been formally Spec'd/owned (candidate DR-2026-008).
4. Whether the capital bucket table has moved from **TBD** to real, even provisional, values (candidate DR-2026-009).
5. Whether legal entity and infrastructure **Unknown/TBD** items have been resolved to at least a documented decision to investigate.

---

## Current Metrics

Atlas has defined many metrics across its Brain and Roadmap documents. **None are currently instrumented or measured.** This section is an honest inventory of the gap between "metric defined" and "metric measured," not a dashboard of live numbers.

| Metric category | Defined in | Currently measured? |
|---|---|---|
| Brain document freshness (% on schedule) | [Brain KPIs](03_ORGANIZATION.md#department-brain) | No — assessable only qualitatively today (see [Current Brain Status](#current-brain-status)) |
| Decision Record completeness | [Brain KPIs](03_ORGANIZATION.md#department-brain) | No — 0 records to assess |
| Escalation resolution time | [Brain KPIs](03_ORGANIZATION.md#department-brain) | No — 0 escalations |
| Cross-department dispute count | [Brain KPIs](03_ORGANIZATION.md#department-brain) | No — 0 possible with 1 person |
| Time saved / error reduction from AI | [AI Strategy](00_ATLAS_BRAIN.md#ai-strategy) | No — no automation deployed |
| Portfolio ROIC | [Return measurement](00_ATLAS_BRAIN.md#return-measurement) | No — no portfolio |
| Integration time vs baseline | [Roadmap SC-H1-01](04_ROADMAP.md#success-criteria) | No — no integration |
| Knowledge findability | [Roadmap SC-H1-04](04_ROADMAP.md#success-criteria) | No — no findability study run |

---

## Current KPIs

Department-level KPI **definitions** live in each department's section of [Organization](03_ORGANIZATION.md) and the [Brain](00_ATLAS_BRAIN.md). This section reports **live values**, which are uniformly absent.

| Department | KPI (defined) | Live value |
|---|---|---|
| Brain | Decision Record completeness | 0 (no decisions to be complete or incomplete) |
| Brain | Escalation resolution time (median) | No data |
| Knowledge | % docs with owner/review date | 100% of active Brain docs; Draft playbooks carry owner/review metadata |
| Knowledge | Staleness rate | No data — no document has reached a review date yet |
| AI | Automation ROI | No data — no automation |
| AI | L2+ coverage % of eligible processes | 0% |
| Finance | Close timeliness | No data — SOP exists; **0 actual closes** |
| Finance | Reserve intact (Y/N) | No data — no reserve defined |
| Operations | KPI dictionary completeness | 0% (dictionary does not exist) |
| Assets | Pipeline hygiene | No data — no pipeline |
| Projects | Retrospective compliance % | Partial — 1 stage retrospective for Market Screen; no project-close retros |

**Interpretation:** a KPI table that is still mostly "no data" is itself a meaningful and honest signal early in Phase P1 — it confirms that Atlas has not begun claiming operating progress it cannot evidence.

---

## Current Scorecards

### Evolution track scorecards — inaugural light score

Using the [Evolution Track Scorecard questions](04_ROADMAP.md#appendix-b--evolution-track-scorecards) as a self-assessment guide (full question sets are canonical in the Roadmap; only scores and short evidence notes are recorded here):

| Track | Self-score (qualitative) | Evidence |
|---|---|---|
| AI track | Weak–improving | Registry exists (6 candidates) + AR-003 Spec; Prototype Runs recorded; still no L2, no ROI reporting, limited guardrail testing |
| Knowledge track | Weak-to-moderate | Docs have owners and review dates; findability and staleness tooling absent; onboarding path unexecuted |
| Infrastructure track | Weak | No access review, no restore test, no tooling inventory beyond informal use |
| Organization track | Moderate | Single owners present by construction (only one person); dual-hats are implicitly labeled but not charter-documented; no shadow structures possible yet |
| Product (HOS) track | Not applicable | No HOS increments have shipped to any user other than the operator |
| Automation track | Weak–improving | Six candidates queued in registry; Prototype Runs on AR-002/003/006; production L2 = 0 |
| Finance track | Weak | No close, no buckets set, no hurdles, no reporting |
| Assets track | Not applicable | No pipeline, no memos, no integrations |

### Company lifecycle scorecard

**Not applicable.** No asset exists to score against the [Integration standards](00_ATLAS_BRAIN.md#company-lifecycle) timelines (30/45/60/14/45 days).

---

## Current Risks

Applying the [Risk categories](00_ATLAS_BRAIN.md#risk-management) and [Risk assessment matrix](00_ATLAS_BRAIN.md#risk-management) to Atlas as it exists today, organized by the six canonical categories so no category is silently skipped.

### Strategic risks

| Risk | Likelihood | Impact | Matrix cell | Mitigation status |
|---|---|---|---|---|
| Documentation without subsequent action ("docs as theater") | Medium | Medium | Monitor | Partially mitigated by this document's honest gap-reporting; requires follow-through to remain mitigated |
| Premature portfolio scale before P0/P1 gates clear | Low (no pipeline exists to act on prematurely) | High if it occurred | Monitor | Mitigated by explicit P0 non-goals; risk is currently low because there is nothing to act on prematurely |
| Mission drift — meta-work (governance) substituting indefinitely for real work (Build/Acquire/Operate) | Low today | High if sustained for years | Monitor | Mitigated only by the [Appendix B watch list](#appendix-b--next-90-days-watch-list) forcing near-term action items |
| No competitive or market thesis yet validated | Not applicable | Not applicable | Accept | Still acceptable early in Phase P1; becomes material once a build or acquire thesis is drafted and tested |

### Financial risks

| Risk | Likelihood | Impact | Matrix cell | Mitigation status |
|---|---|---|---|---|
| Financial capital status unknown/undocumented | Unknown likelihood | Potentially high | **Escalate to Brain** | Not yet mitigated |
| Capital bucket allocation unset (all buckets TBD) | Certain (already true) | Medium — no capital is at risk of misallocation because none is allocated | Monitor | Flagged in [Current Finance](#current-finance); low urgency until real capital exists |
| No reserve policy to protect against shocks | Unknown — depends on whether capital exists at all | Potentially high once capital exists | **Escalate to Brain** once capital is confirmed | Not yet mitigated; not yet urgent |

### Operational risks

| Risk | Likelihood | Impact | Matrix cell | Mitigation status |
|---|---|---|---|---|
| Key person dependency — 100% of institutional knowledge in one person | High | High | **Escalate to Brain** (per matrix, though Brain is the same person) | Partially mitigated by [Extreme documentation](02_FOUNDING_PRINCIPLES.md#extreme-documentation) discipline; not mitigated by cross-training (impossible with one person) or succession planning (not yet started) |
| Most repeated tasks still lack SOPs | High (certain — only 1 T4 SOP today) | Low today, rising with any repetition | Monitor | Close SOP exists; other SOPs still absent; urgency low while repetition volume remains low |
| Vendor dependency on a single AI assistance tool with no documented evaluation | Medium | Low today | Accept | Will require a multi-vendor evaluation before material reliance grows |

### Technical risks

| Risk | Likelihood | Impact | Matrix cell | Mitigation status |
|---|---|---|---|---|
| Knowledge base has no backup/redundancy policy | Medium | High | Mitigate | **Not yet mitigated** — top action item |
| AI usage without governance (unregistered informal pattern) | Low today (no sensitive data) | Low today, rising with scale | Accept (today) | Will require mitigation before any sensitive data is introduced |
| No access/identity baseline (milestone M-I-002) | Medium | Low today (single user) | Accept | Becomes urgent the moment a second credentialed user or agent is introduced |

### Compliance / legal risks

| Risk | Likelihood | Impact | Matrix cell | Mitigation status |
|---|---|---|---|---|
| Legal entity / compliance status unknown | Unknown likelihood | Potentially high | **Escalate to Brain** | Not yet mitigated — status itself is unresolved |
| Tax / regulatory filing obligations unknown | Unknown likelihood | Potentially high | **Escalate to Brain** | Not yet investigated |
| No contracts reviewed for irreversibility triggers | Not applicable | Not applicable | Accept | 0 contracts exist |

### Reputational risks

| Risk | Likelihood | Impact | Matrix cell | Mitigation status |
|---|---|---|---|---|
| No external stakeholder relationship exists to damage | Not applicable | Not applicable | Accept | Still expected early in Phase P1 — reputational risk remains effectively zero while there is no external audience |
| Future risk: publishing an incomplete or inaccurate Current State would itself be a small integrity/reputational risk once external readers exist | Low today | Low today, rising once shared externally | Monitor | Mitigated by this document's TBD/Unknown discipline rather than optimistic guessing |

### Risk register summary

| Category | # risks tracked | # actively mitigated | # accepted at current scale | # escalated / open |
|---|---|---|---|---|
| Strategic | 4 | 1 | 2 | 1 |
| Financial | 3 | 0 | 0 | 3 |
| Operational | 3 | 1 | 1 | 1 |
| Technical | 3 | 0 | 2 | 1 |
| Compliance / legal | 3 | 0 | 1 | 2 |
| Reputational | 2 | 1 | 1 | 0 |
| **Total** | **18** | **3** | **7** | **8** |

### Standard mitigations not yet applied

Per [Standard mitigations](00_ATLAS_BRAIN.md#risk-management), the following defined mitigations remain unapplied: cross-training (impossible at Stage 0 by definition), diversification targets (not applicable, no portfolio), multi-vendor evaluation (no vendors), and AI evaluation metrics (no automation deployed).

### Incident response readiness

Zero incidents have occurred, and the [Incident response](00_ATLAS_BRAIN.md#risk-management) process (Contain → Communicate → Resolve → Analyze → Prevent → Record) has never been exercised, even in a drill. This is a readiness gap worth closing before the first real incident, per milestone M-O-004 (Incident response drills).

---

## Current Constraints

| Constraint | Description | Source |
|---|---|---|
| Single-operator capacity | All work is bounded by one person's available hours; no parallelization possible without hiring | Structural, per Stage 0 |
| Undefined capital | Cannot commit to any acquisition, build, or hire until capital status is resolved (see [Current Finance](#current-finance)) | Financial |
| Undefined legal entity | Cannot sign contracts, open accounts, or formally hire until entity status is resolved | Legal |
| No decision precedent corpus | Every decision currently must be made without the benefit of prior logged Atlas-specific precedent | Knowledge |
| No automation | Every task is currently manual by default, per [Current AI Maturity](#current-ai-maturity) | Technical |
| Phase gate discipline | Per [Phase vs calendar discipline](04_ROADMAP.md#major-phases), Atlas should not advance to P1 activities (multi-asset expansion, Stage 2+ hiring) merely because time has passed — exit criteria must be met first | Strategic, self-imposed by design |

---

## Current Bottlenecks

| Bottleneck | Where it bites | Fix effort |
|---|---|---|
| Empty Decision Register | ~~Blocks P0.7~~ | ✅ **Closed** — DR-2026-001 through DR-2026-004 logged |
| ~~Empty glossary~~ | ~~Blocks M-K-001, CM-D2, P0.8~~ | ✅ **Closed** — Glossary v1.0 published |
| No financial visibility | Blocks any real capital allocation decision, blocks CM-D4 | Medium — depends on resolving legal entity/banking Unknowns first |
| No backup policy for the knowledge base | Single point of failure for the entire institutional memory of Atlas | Low — establish an offsite/cloud backup or mirror |
| No role charters | Blocks clean Stage 0→1 transition when a second person eventually joins | Low-medium — draft charter language per hat |

---

## Current Technical Debt

**Minimal to none**, because minimal software has been built. The only candidate items:

| Item | Debt type | Severity |
|---|---|---|
| Informal AI-assistance pattern used without a spec | Process debt (not code debt) | Low today; rising if reused without formalization |
| No automated backup for the vault | Infrastructure debt | Medium — cheap to fix, meaningfully risky to leave |
| No tooling inventory document despite tools being in active use | Documentation debt | Low |

There is, notably, **no accumulated code debt, integration debt, or automation debt**, because Atlas has not yet written software, integrated a portfolio company, or deployed an automation. This is worth stating explicitly: Atlas is in the rare position of having essentially zero technical debt because it has not yet built anything to accrue debt against.

---

## Current Organizational Debt

Per the [Organizational Anti-Patterns](03_ORGANIZATION.md#organizational-anti-patterns) table, checked against current reality:

| Anti-pattern | Present today? | Notes |
|---|---|---|
| Management middleware | No | Impossible with one person |
| Committee ownership | No | Impossible with one person |
| Hero culture | **Latent risk** | Every deliverable to date has been produced by one person; not yet a "culture" because there is no alternative to compare against, but the pattern to watch is real |
| Meeting as workflow | No | No meetings occur |
| Shadow governance | No | All governance is written in the eight active Brain documents |
| Org chart in stealth | No | This document and the Organization document make the (trivial, one-person) org chart explicit |
| Project permanence | Watch | P-001 exists; risk is treating it as permanent without kill/continue criteria discipline |
| Knowledge in Slack / informal channels | **Unknown** | No communication tooling is documented; if informal notes exist outside the vault, they represent undocumented knowledge in violation of [Extreme documentation](02_FOUNDING_PRINCIPLES.md#extreme-documentation) |
| AI without owner | 🟡 Watch (AR-001) | Registered candidates/Spec list Антон as owner; residual debt is **informal AR-001** drafting not yet formally Spec'd/registered (candidate DR-2026-008), plus any future AI artifact created without an owner |
| Portfolio silo | Not applicable | No portfolio |
| Title as authority | No | No titles have been asserted beyond role description |
| Escalation punishment | No | No escalation has occurred to punish or reward |
| Duplicate Brain | No | Single source of truth audit passed, see [Current Knowledge System](#current-knowledge-system) |
| Hiring ahead of workflow | No | No hiring has occurred |
| Reorg as performance fix | Not applicable | No org exists to reorganize |

**Net organizational debt: very low**, with residual informal-AR-001 / future-unowned-AI watch item and one latent risk (hero culture) to watch as headcount grows.

---

## Current Documentation Coverage

| Document tier (per [Documentation Standards](00_ATLAS_BRAIN.md#documentation-standards)) | Expected examples | Current coverage |
|---|---|---|
| T1 — Governance | Brain, principles, frameworks | 8 of 8 core Brain files Active (`00`–`07`) |
| T2 — Standards | Doc standards, automation specs, templates | Defined *inside* T1 documents (e.g., [Documentation Standards](00_ATLAS_BRAIN.md#documentation-standards), [Automation spec template](00_ATLAS_BRAIN.md#automation-standards)); no standalone T2 artifact yet, which is acceptable at this scale |
| T3 — Playbooks | Integration playbook, hiring playbook | **7 of 7** Draft department playbooks exist (P1.1 Met) |
| T4 — SOPs | Monthly close SOP, onboarding checklist | **1** SOP (`finance_close_sop.md`); others absent |
| T5 — Records | Decision records, meeting notes, reports | **4** Decision Records (DR-2026-001 through DR-2026-004) |

### Coverage by department

| Department | T3 playbook | T4 SOPs |
|---|---|---|
| Brain | Draft (`brain_playbook.md`) | 0 |
| Knowledge | Draft (`knowledge_playbook.md`) | 0 |
| AI | Draft (`ai_playbook.md`) | 0 |
| Finance | Draft (`finance_playbook.md`) | 1 (`finance_close_sop.md`) |
| Operations | Draft (`operations_playbook.md`) | 0 (integration scorecard is a template, not an SOP) |
| Assets | Draft (`assets_playbook.md`) | 0 |
| Projects | Draft (`projects_playbook.md`) | 0 |

---

## Current Documentation Gaps

Ranked by how much they block other progress:

| Gap | Blocks | Priority |
|---|---|---|
| ~~No department playbooks (T3)~~ | ~~P1.1~~ | ✅ **Closed** — 7 Draft playbooks; P1.1 / M-K-003 Met |
| ~~No automation registry~~ | ~~P1.3~~ | ✅ **Closed** — registry + 6 candidates; **P1.3 Met**; **M-A-001 Partial** (no production entries / sparse SOP links) |
| P1.2 strict lifecycle evidence incomplete | Phase 1 exit | **Highest** — need ≥3 initiatives with required Knowledge briefs + retrospectives |
| P1.4 — zero processes at L2 | Phase 1 exit | **Highest** — Frequency / Evaluate / Deploy still open |
| P1.5 — no actual financial closes; no chart of accounts | Phase 1 exit; live Finance | **High** — SOP exists; closes and CoA absent |
| Sparse T4 SOPs beyond close SOP | Automation eligibility for other processes | High |
| No role charters | Clean Stage 0→1 transition | Medium |
| No automation Spec for AR-001 / AR-002 / AR-006 (AR-003 Spec exists) | Adoption process completeness | Medium |
| No tooling inventory document | M-I-001; general findability for future operators | Low |
| No informal-pipeline documentation (if any pipeline exists in the operator's head) | Assets department credibility; mission "Acquire" activity readiness | Medium, contingent on whether informal pipeline exists (Unknown) |

---

## Current Quality Assessment

### Quality of what exists

The eight active Brain documents (`00`–`07`) exhibit:

- **Structural consistency** — consistent metadata blocks, TOCs, cross-references, and writing style across all documents.
- **Low duplication** — spot-checked against [One source of truth](02_FOUNDING_PRINCIPLES.md#one-source-of-truth); no material restatement of principles, department definitions, or frameworks found between documents.
- **High internal cross-referencing** — every document links extensively to siblings rather than restating their content, matching the design intent of [Documentation Standards](00_ATLAS_BRAIN.md#documentation-standards).
- **Unverified external quality** — no third party (advisor, hire, investor) has yet read or stress-tested these documents. Quality has been assessed only by the author. This is a real limitation: per [Evidence over opinion](02_FOUNDING_PRINCIPLES.md#evidence-over-opinion), self-assessed quality is a hypothesis, not a validated conclusion.

### Quality of what does not exist

Decision Records, Glossary, and at least the Finance Close SOP **have been written**. Quality of those early artifacts is only lightly self-assessed; broad operational SOP/playbook *depth* and outside validation remain incomplete. Prefer coverage + honesty over claiming finished quality (see [Current Documentation Coverage](#current-documentation-coverage)).

### Overall quality verdict

**Governance layer: high quality, unvalidated by outside use.** Early execution-layer artifacts now also exist (7 Draft playbooks, finance close SOP, automation registry, AR-003 Spec, integration scorecard template, P-001 + Knowledge Market Screen artifacts) — mostly draft/prototype/unexercised. Atlas still lacks mature repeatable operations, production automation, customers, revenue, and a completed operating cycle.

---

## Current Scaling Readiness

### Readiness against Stage 1 requirements

| Stage 1 requirement | Ready? |
|---|---|
| Department heads named (distinct people or clearly dual-hatted) | 🟡 Named but not distinct — all dual-hatted to one person |
| Role charters published | 🔴 Not ready |
| Interface SLAs activated | 🔴 Not ready — requires a second party |
| First dedicated Project DRI | 🔴 Not ready |
| First production agents with named owners | 🔴 Not ready |

### Readiness against P1 (Operating Kernel) entry

Per [Phase 1 entry criteria](04_ROADMAP.md#phase-1--operating-kernel): **Met** — P0 exited 2026-08-08; Brain approved P1 entry via DR-2026-002.

### Phase 1 exit criteria — honest status

| # | Criterion | Status |
|---|---|---|
| P1.1 | Department playbook skeleton ×7 | ✅ **Met** |
| P1.2 | Project lifecycle used on ≥3 initiatives (Briefs + retrospectives in Knowledge) | 🔴 **Not Met** (strict) |
| P1.3 | Automation registry exists (≥5 candidates) | ✅ **Met** |
| P1.4 | ≥3 processes at L2 | 🔴 **Not Met** (L2 count = 0) |
| P1.5 | Monthly financial close process documented (SOP + actual closes) | 🔴 **Not Met** (SOP exists; 0 closes) |
| P1.6 | Integration scorecard v1 | ✅ **Met** (Draft unscored template; no live integrations) |
| P1.7 | Escalation thresholds published | ✅ **Met** |
| P1.8 | Onboarding path executed once | ✅ **Met** |
| **Phase 1 exit** | All exit criteria | 🔴 **No** |

### Overall scaling verdict

Atlas has **exited P0 and entered P1**. Several P1 exit criteria are now Met (P1.1, P1.3, P1.6, P1.7, P1.8); **P1.2, P1.4, and P1.5 remain Not Met**, so Phase 1 exit = **No**.

---

## Current Hiring Readiness

### Hiring status

**No hiring is in progress and none is recommended yet.** Per [Organizational Anti-Patterns § Hiring ahead of workflow](03_ORGANIZATION.md#organizational-anti-patterns) ("Three people, no SOP" → fix: "Document; automate; then hire"), hiring before the relevant workflows are understood and usable SOP coverage exists would itself be an anti-pattern. (One Finance close SOP exists; broad role-ready SOP coverage does not.)

### Readiness checklist

| Prerequisite for first hire | Status |
|---|---|
| Outcome needed is defined (not just headcount) | 🔴 Not defined for any role |
| Single owner for the role's outcomes defined | 🔴 Not applicable — no role opened |
| Success metrics at 30/90/180 days | 🔴 Not defined |
| At least one SOP or playbook the new hire would use | 🟡 7 Draft playbooks + 1 close SOP exist; depth still early |
| Legal entity able to employ or contract | 🔴 Unknown/TBD |

### Recommendation

Per [Leverage over headcount](03_ORGANIZATION.md#organizational-design-principles), the correct next moves are automation and documentation, not headcount, until a specific, evidenced need appears (e.g., a real acquisition target requiring diligence capacity beyond one person's bandwidth). No such need is currently documented.

---

## Current Expansion Readiness

### Readiness against expansion modes

Per [Expansion modes](04_ROADMAP.md#expansion-strategy):

| Mode | Earliest phase | Atlas ready? |
|---|---|---|
| E-Build | P1 | 🟡 **P1 active** — build path open per Roadmap caution; no opportunity documented yet |
| E-Acquire | P2 (P1 with caution) | 🔴 Not ready |
| E-Integrate-deep | P2+ | 🔴 Not applicable — nothing to integrate |
| E-Shared-services | P3 | 🔴 Not ready |
| E-Platform | P4 | 🔴 Not ready |
| E-Sector / E-Geo | P3+ | 🔴 Not ready |
| E-External-knowledge | P5+ | 🔴 Not ready |
| E-Operator-network | P4+ | 🔴 Not ready |

### Expansion sequencing rule check

Per [Expansion sequencing rules](04_ROADMAP.md#expansion-strategy) ("OS before logos — no multi-asset expansion while P0 incomplete"), Atlas **exited P0 on 2026-08-08** and is now in P1. Multi-asset expansion remains correctly deferred until P1/P2 gates; E-Build path is cautiously open per Roadmap.

### First-mover readiness for E-Build or E-Acquire

The [Build vs. acquire framework](00_ATLAS_BRAIN.md#build-vs-acquire-framework) is ready to apply — P0 has exited; a real opportunity can be evaluated when one exists.

---

## Current Operational Health

### Health verdict by area

| Area | Health | Rationale |
|---|---|---|
| Governance | 🟢 Green | Complete, consistent, in active use for self-assessment |
| Knowledge | 🟡 Yellow | Glossary live; 4 Register entries; 7 Draft playbooks; P1.2 still open |
| Organization | 🟢 Green for stage | Stage 0 rules are being followed; gaps are known and listed, not hidden |
| AI | 🟡 Yellow | Usage exists ahead of governance; low risk today, needs closure before scale |
| Finance | 🔴 Red-if-judged-as-a-company / 🟢 Green-if-judged-as-Phase-P1-early | Genuinely nonexistent; correct for early P1, would be alarming if unchanged at P1 exit |
| Operations | 🟢 Green for stage | Nothing to operate yet; no defect |
| Assets | 🟢 Green for stage | Nothing to own yet; no defect |
| Projects | 🟡 Yellow | P-001 active with partial lifecycle evidence; **P1.2 Not Met** |
| Security | 🟢 Green for stage, with one flagged gap | Backup policy for the knowledge base should not wait |
| Overall | 🟢 **Green for Phase P1, Stage 0** | P0 exited; P1 entered; execution layer work ahead |

### The single most important health signal

**Atlas has told the truth about itself in its first Current State document.** Per [Truth over comfort](02_FOUNDING_PRINCIPLES.md#truth-over-comfort), this is the leading indicator that matters most at this stage — more than any single metric above.

---

## Appendix A — Current State Field Reference

Quick-lookup table for values that other documents explicitly defer to this one. Update this table first when any of these values change; then reflect the change into the relevant section body above.

| Field | Current value | Section |
|---|---|---|
| Current phase | P1 — Operating Kernel (entered 2026-08-08) | [Current Strategic Position](#current-strategic-position) |
| Current horizon | H0 — Foundation | [Current Strategic Position](#current-strategic-position) |
| Current era | E0 — Substrate | [Current Strategic Position](#current-strategic-position) |
| Current org stage | Stage 0 — One operator | [Current Organizational Maturity](#current-organizational-maturity) |
| Holding CM (weakest link) | CM-0 | [Current Capability Maturity](#current-capability-maturity) |
| Holding CM (average) | ~0.6 / 5 | [Current Capability Maturity](#current-capability-maturity) |
| Headcount | 1 | [Current Organization](#current-organization) |
| Portfolio assets | 0 | [Current Assets](#current-assets) |
| Decision records | 4 | [Current Decision System](#current-decision-system) |
| Glossary terms | ~150 | [Current Knowledge System](#current-knowledge-system) |
| Capital bucket allocation | TBD (all buckets) | [Current Finance](#current-finance) |
| Legal entity status | Unknown / TBD | [Current Infrastructure](#current-infrastructure) |
| Production automations | 0 at L2+; 6 candidates tracked | [Current Automation](#current-automation) |
| Escalation thresholds | Live (P1.7 Met); capital/irreversible defaults temporary | [Current Governance](#current-governance) |

---

## Appendix B — Next 90 Days Watch List

Ordered by leverage (impact ÷ effort), not by department:

1. ~~**Conduct P0→P1 gate review**~~ — ✅ **Done** (DR-2026-002; P1 entered 2026-08-08).
2. ~~**Department playbook skeleton ×7**~~ — ✅ **Done** (P1.1 / M-K-003 Met).
3. **Establish a backup/redundancy policy for the knowledge base** — single point of failure ([Current Risks](#current-risks)); candidate DR-2026-006.
4. **Resolve legal entity and banking status** — move from Unknown/TBD to a documented answer; candidate DR-2026-005.
5. **Spec and name an owner for the AI-assistance pattern** — candidate **DR-2026-008** (do not reuse live DR-2026-003).
6. **Set a provisional capital bucket allocation** — candidate **DR-2026-009** (do not reuse live DR-2026-004).
7. **Run the first Quarterly Brain review** — 2026-11-08.
8. ~~**Automation registry (P1.3)**~~ — ✅ **Done** (registry + ≥5 candidates). **M-A-001** remains 🟡 Partial (detailed Done-means not fully satisfied).
9. **Advance P1.2 / P1.4 / P1.5 honestly** — strict lifecycle evidence; L2 maturity; actual closes — without fabricating Frequency or closes.

---

## Appendix C — Full Milestone Register Status

Full status against every milestone ID defined in the [Roadmap's Milestone register](04_ROADMAP.md#strategic-milestones). Milestone names and IDs are canonical there; only the status column originates here. This is the complete register — [Current Projects](#current-projects) shows only the subset most relevant to near-term work.

### Governance cluster (M-G)

| ID | Milestone | Phase | Status |
|---|---|---|---|
| M-G-001 | Brain OS document set Active | P0 | 🟡 8 of 8 Active; 4 Register entries |
| M-G-002 | Current State v1 published | P0 | ✅ Met |
| M-G-003 | Decision log operational | P0 | ✅ Met — DR-2026-001 logged |
| M-G-004 | Escalation thresholds live | P1 | ✅ Met — all 5 of 5 rows carry live values; Capital commitment and Irreversible commitment are explicitly temporary/unexercised defaults (DR-2026-004, DR-2026-003) |
| M-G-005 | Quarterly Brain review running | P1 | 🔴 Not met — 0 reviews held |
| M-G-006 | Annual planning model executed once | P1 | 🔴 Not met |
| M-G-007 | Phase gate P0→P1 passed | P0/P1 | ✅ Met — DR-2026-002, 2026-08-08 |
| M-G-008 | Phase gate P1→P2 passed | P1/P2 | 🔵 Not applicable yet |
| M-G-009 | Phase gate P2→P3 passed | P2/P3 | 🔵 Not applicable yet |
| M-G-010 | Phase gate P3→P4 passed | P3/P4 | 🔵 Not applicable yet |
| M-G-011 | Succession exercise designed | P4 | 🔵 Not applicable yet |
| M-G-012 | Succession exercise passed | P5 | 🔵 Not applicable yet |

### Knowledge cluster (M-K)

| ID | Milestone | Phase | Status |
|---|---|---|---|
| M-K-001 | Glossary v1 | P0–P1 | ✅ Met |
| M-K-002 | Onboarding path executed | P1 | ✅ Met — all 5 steps pass; see [Appendix I](#appendix-i--onboarding-path-dry-run) |
| M-K-003 | Playbook skeleton ×7 | P1 | ✅ Met — 7 Draft playbooks (P1.1 Met) |
| M-K-004 | SOP quality bar defined | P1 | 🔴 Not met |
| M-K-005 | Staleness flags live | P2–P3 | 🔵 Not applicable yet |
| M-K-006 | Retrieval for operators | P2 | 🔵 Not applicable yet |
| M-K-007 | Precedent search for decisions | P3 | 🔵 Not applicable yet |
| M-K-008 | Cross-portfolio research briefs cadence | P3 | 🔵 Not applicable yet |
| M-K-009 | Knowledge-as-product UX | P4 | 🔵 Not applicable yet |
| M-K-010 | Selective external knowledge products | P5+ | 🔵 Not applicable yet |

### AI / Automation cluster (M-A)

| ID | Milestone | Phase | Status |
|---|---|---|---|
| M-A-001 | Automation registry v1 | P1 | 🟡 Partial — 6 candidates + owners/maturity (**P1.3 Met**); no production entries; most candidates lack SOP links |
| M-A-002 | First 3 agents in production | P1 | 🔴 Not met |
| M-A-003 | L2 default on repeated holding processes | P2 | 🔵 Not applicable yet |
| M-A-004 | Agent template library | P3 | 🔵 Not applicable yet |
| M-A-005 | AI ROI dashboard | P2 | 🔵 Not applicable yet |
| M-A-006 | Model-agnostic eval harness | P2–P3 | 🔵 Not applicable yet |
| M-A-007 | L3 on majority eligible BAU | P4 | 🔵 Not applicable yet |
| M-A-008 | L4 pilot domain | P4–P5 | 🔵 Not applicable yet |
| M-A-009 | Automated decision support | P4 | 🔵 Not applicable yet |
| M-A-010 | Cross-portfolio intelligence | P5 | 🔵 Not applicable yet |

### Finance cluster (M-F)

| ID | Milestone | Phase | Status |
|---|---|---|---|
| M-F-001 | Chart of accounts / close SOP | P1 | 🟡 Partial — close SOP exists; chart of accounts absent; P1.5 Not Met |
| M-F-002 | Capital bucket policy published | P1 | 🔴 Not met — see [Current Finance](#current-finance) |
| M-F-003 | Hurdle rate policy published | P1 | 🔴 Not met |
| M-F-004 | Portfolio reporting package | P2 | 🔵 Not applicable yet |
| M-F-005 | Unit economics standard | P2 | 🔵 Not applicable yet |
| M-F-006 | Investment memo standard | P1–P2 | 🔴 Not met |
| M-F-007 | Automated reporting L2+ | P3 | 🔵 Not applicable yet |
| M-F-008 | Holding ROIC published quarterly | P2+ | 🔵 Not applicable yet |

### Operations cluster (M-O)

| ID | Milestone | Phase | Status |
|---|---|---|---|
| M-O-001 | KPI dictionary v1 | P1 | 🔴 Not met |
| M-O-002 | Integration scorecard v1 | P1 | ✅ Met — Draft unscored template (P1.6 Met) |
| M-O-003 | Vendor management framework | P2 | 🔵 Not applicable yet |
| M-O-004 | Incident response drills | P2 | 🔵 Not applicable yet |
| M-O-005 | Integration playbook v2 | P3 | 🔵 Not applicable yet |
| M-O-006 | Shared services catalog | P3 | 🔵 Not applicable yet |
| M-O-007 | Portfolio dashboard spec live | P2–P3 | 🔵 Not applicable yet |
| M-O-008 | Coordination tax audit v1 | P4 | 🔵 Not applicable yet |

### Assets / Portfolio cluster (M-S)

| ID | Milestone | Phase | Status |
|---|---|---|---|
| M-S-001 | Build-vs-acquire checklist in use | P1 | 🔴 Not met |
| M-S-002 | First asset Acquire or Build complete | P1–P2 | 🔴 Not met |
| M-S-003 | First Integrate complete | P2 | 🔵 Not applicable yet |
| M-S-004 | Second asset integrated | P2–P3 | 🔵 Not applicable yet |
| M-S-005 | Third asset integrated | P3 | 🔵 Not applicable yet |
| M-S-006 | Exit/hold rationale standard | P2 | 🔵 Not applicable yet |
| M-S-007 | Portfolio operator model live | P3 | 🔵 Not applicable yet |
| M-S-008 | Sector or geo cluster model | P4 | 🔵 Not applicable yet |

### Projects cluster (M-P)

| ID | Milestone | Phase | Status |
|---|---|---|---|
| M-P-001 | Intake/triage process live | P1 | 🟡 Partial — used on P-001/Market Screen; P1.2 Not Met |
| M-P-002 | 100% approved projects have briefs | P1 | 🔴 Not met |
| M-P-003 | Retrospective compliance ≥90% | P2 | 🔵 Not applicable yet |
| M-P-004 | Handoff confirmation gate | P2 | 🔵 Not applicable yet |
| M-P-005 | Infrastructure project portfolio visible | P3 | 🔵 Not applicable yet |

### Infrastructure / Platform cluster (M-I)

| ID | Milestone | Phase | Status |
|---|---|---|---|
| M-I-001 | Tooling inventory + preferred stack | P1 | 🟡 Informal inventory only (see [Current Technical Stack](#current-technical-stack)) |
| M-I-002 | Identity/access baseline | P1 | 🔴 Not met |
| M-I-003 | Data segmentation policy | P2 | 🔵 Not applicable yet |
| M-I-004 | Atlas OS platform MVP | P4 | 🔵 Not applicable yet |
| M-I-005 | Self-serve portal | P4 | 🔵 Not applicable yet |
| M-I-006 | Operator network (internal) | P4–P5 | 🔵 Not applicable yet |

### Register summary

| Status | Count |
|---|---|
| ✅ Met | 2 |
| 🟡 Partially met | 2 |
| 🔴 Not met (in-phase, actionable now) | 20 |
| 🔵 Not applicable yet (future phase) | 43 |
| **Total milestones tracked** | **67** |

---

## Appendix D — Candidate Glossary Terms

[`07_GLOSSARY.md`](07_GLOSSARY.md) is now Active v1.0 (~150 terms). This appendix is **retained for historical reference only** — it listed candidate terms before M-K-001 closed. It is **not** a substitute glossary; no document should cite this appendix as a definition source.

| Candidate term | Appears in | Why it needs a canonical definition |
|---|---|---|
| DRI (Directly Responsible Individual) | Organization, Principles | Used dozens of times without an on-page definition |
| Holding OS / HOS | Brain, Why, Organization, Roadmap | Central concept, never formally defined in one place |
| One-way door / two-way door | Brain, Principles | Defined descriptively in Brain but not glossary-formalized |
| Believability(-weighted) | Organization | Introduced via the "Ray Dalio principle" reference; no formal definition |
| Org stage (0–4) | Organization, Roadmap | Numeric levels referenced across documents |
| CM level (0–5) / CM dimension | Roadmap | Ten dimensions and six levels, referenced heavily in this document |
| L-level (L0–L4) | Brain, Principles, Roadmap | AI process maturity levels |
| Horizon (H0–H4) | Roadmap | Time bands |
| Era (E0–E4) | Roadmap | Evolution eras |
| Phase (P0–P6) | Roadmap | Gated stages |
| Gate | Roadmap | Go/no-go review before phase transition |
| Track | Roadmap | Parallel evolution stream |
| Decision Record (DR) | Brain, Principles | Template exists; term itself not glossary-defined |
| Integration scorecard | Brain, Organization, Roadmap | Referenced as an artifact type without a canonical definition |
| Single Owner Principle | Organization, Principles | Named principle without a glossary cross-reference |
| Dual-hat / dual-hatted | Organization | Informal term used to describe Stage 0/1 role-sharing |
| Automation maturity / registry | Brain, Organization, Roadmap | Referenced but not defined as a standalone term |
| Weakest-link scoring | Roadmap | Methodology term used for CM aggregation |
| Holding ROIC | Brain, Organization | Financial term specific to Atlas's model |
| Portfolio autonomy spectrum | Brain | Named concept without a glossary entry |
| Coordination tax | Why, Organization | Central diagnostic term for organizational health |

**Recommended next step:** promote this table into `07_GLOSSARY.md` with full canonical definitions, one term at a time, starting with the terms this very document leans on most heavily (Org stage, CM level, L-level, Phase, DRI).

---

## Appendix E — Decision Record Backlog

Live Register entries are authoritative in [`06_DECISIONS.md`](06_DECISIONS.md). This appendix separates **logged** decisions from **open proposals**. Open proposals must **not** reuse IDs already assigned in the live Register.

### Logged (live Register)

| ID | Decision | Type | Status | Notes |
|---|---|---|---|---|
| DR-2026-001 | Build the full Brain governance document set before any operating activity | Strategic | **Logged / Approved** | Live |
| DR-2026-002 | Approve Phase P0→P1 transition (includes CM-1 narrow reading) | Strategic | **Logged / Approved** | Live — CM-1 interpretation is closed here, not a separate open ID |
| DR-2026-003 | Adopt Brain-default "Irreversible commitment" escalation threshold for Finance | Operational | **Logged / Approved** | Live |
| DR-2026-004 | Set temporary Phase 1 "Capital commitment" escalation threshold at 10% of deployable capital | Operational | **Logged / Approved** | Live |

### Open proposals (unused future IDs only)

| Proposed ID | Decision | Type | Status | Notes |
|---|---|---|---|---|
| DR-2026-005 (proposed) | Legal entity formation path and jurisdiction | Strategic / Compliance | Open, undecided | [Current Infrastructure](#current-infrastructure) |
| DR-2026-006 (proposed) | Knowledge base backup/redundancy approach | Technical | Open, undecided | [Current Risks](#current-risks) |
| DR-2026-007 (proposed) | Whether an informal deal pipeline exists and should be documented | Investment | Open, undecided (Unknown fact) | [Current Assets](#current-assets) |
| DR-2026-008 (proposed) | Whether to formally register the AI-assisted-drafting pattern as an automation | Technical | Open, undecided | Was incorrectly labeled DR-2026-003 in older drafts — that ID is live for irreversible commitment |
| DR-2026-009 (proposed) | Initial (even provisional) capital bucket allocation | Investment / Operational | Open, undecided | Was incorrectly labeled DR-2026-004 in older drafts — that ID is live for capital-commitment threshold |

**Process note:** open proposals still require full Decision Record fields before becoming live Register entries.

---

## Appendix F — Vendor and Tooling Registry

Per milestone M-I-001 (tooling inventory), a first-pass inventory of everything currently in use, to seed a future formal registry.

| Category | Item | Vendor relationship documented? | Contract on file? |
|---|---|---|---|
| Knowledge base | Obsidian (local vault) | No | No |
| Version control | Git (local repository) | Not applicable — no vendor, local tool | No |
| AI assistance | AI coding/writing assistant (Cursor) | No | No |
| Financial system | None in use | — | — |
| Project management | None in use | — | — |
| CRM / deal pipeline | None in use | — | — |
| Communication / email | Unknown / TBD | Unknown | Unknown |
| Cloud hosting / backup | None documented | — | — |
| Banking | Unknown / TBD | Unknown | Unknown |
| Legal / compliance services | Unknown / TBD | Unknown | Unknown |

**Vendor risk note:** zero of the tools above have been through a [multi-vendor evaluation](00_ATLAS_BRAIN.md#risk-management) or an exit-plan review. This is acceptable at Stage 0 with no sensitive data and no spend of consequence, and should be revisited the moment any paid, data-bearing, or contractual vendor relationship begins.

---

## Appendix G — Principle Adherence Self-Audit

A one-time, honest self-check of current practice against every immutable principle in [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md). This audit does not modify or reinterpret any principle — it only asks "is Atlas, in its first days, actually living this?"

| Principle | Current adherence | Evidence |
|---|---|---|
| [Long-term thinking](02_FOUNDING_PRINCIPLES.md#long-term-thinking) | 🟢 Strong | Governance built before any operating pressure existed; no shortcuts taken to simulate progress |
| [Truth over comfort](02_FOUNDING_PRINCIPLES.md#truth-over-comfort) | 🟢 Strong | This entire document is the test case — every gap stated plainly |
| [Evidence over opinion](02_FOUNDING_PRINCIPLES.md#evidence-over-opinion) | 🟡 Partial | Documents are evidence-structured, but zero real decisions have been evidence-tested yet |
| [Systems over heroes](02_FOUNDING_PRINCIPLES.md#systems-over-heroes) | 🟡 Partial | Systems are designed; execution to date has depended entirely on one person's undocumented working habits (see [Current Organizational Debt](#current-organizational-debt)) |
| [Compounding over optimization](02_FOUNDING_PRINCIPLES.md#compounding-over-optimization) | 🟢 Strong for governance | The document set is explicitly built for reuse and cross-reference, not one-off convenience |
| [Ownership](02_FOUNDING_PRINCIPLES.md#ownership) | 🟢 Strong | Every artifact has exactly one named owner, per [Current Ownership](#current-ownership) |
| [Transparency](02_FOUNDING_PRINCIPLES.md#transparency) | 🟡 Partial | Fully transparent internally; no external audience yet exists to test transparency against |
| [Extreme documentation](02_FOUNDING_PRINCIPLES.md#extreme-documentation) | 🟡 Partial | Strong for governance; playbooks + close SOP + 4 DRs now exist; depth and operating exercise still early — see [Current Documentation Gaps](#current-documentation-gaps) |
| [AI-first thinking](02_FOUNDING_PRINCIPLES.md#ai-first-thinking) | 🟡 Partial | AI was used to help build the governance layer; no operational workflow yet exists to test AI-first design against |
| [Automation by default](02_FOUNDING_PRINCIPLES.md#automation-by-default) | 🔴 Weak | Registry exists but production L2 = 0; Prototype Runs only; Frequency/Evaluate not met |
| [Simple before complex](02_FOUNDING_PRINCIPLES.md#simple-before-complex) | 🟢 Strong | Tooling choices (markdown, git, no custom platform) are the simplest adequate solution at this scale |
| [Reversible decisions](02_FOUNDING_PRINCIPLES.md#reversible-decisions) | 🟡 Not yet tested | No decision has been explicitly classified as one-way or two-way |
| [Human accountability](02_FOUNDING_PRINCIPLES.md#human-accountability) | 🟢 Strong | Every AI-assisted output has a named human reviewer (the sole operator) |
| [Capital efficiency](02_FOUNDING_PRINCIPLES.md#capital-efficiency) | 🔵 Not yet testable | No capital has been deployed |
| [Integrity](02_FOUNDING_PRINCIPLES.md#integrity) | 🟢 Strong | No misrepresentation found in this document's self-review; every claim is either evidenced or flagged as unknown |
| [Optionality](02_FOUNDING_PRINCIPLES.md#optionality) | 🟢 Strong | No irreversible commitments have been made; all tooling and structural choices remain easily reversible |
| [Continuous improvement](02_FOUNDING_PRINCIPLES.md#continuous-improvement) | 🟡 Not yet tested | No review cycle has completed to demonstrate the loop closing |
| [Knowledge compounds](02_FOUNDING_PRINCIPLES.md#knowledge-compounds) | 🟡 Partial | Compounding infrastructure exists; the corpus is too young to show compounding in practice |
| [Build before buy](02_FOUNDING_PRINCIPLES.md#build-before-buy) | 🟢 Consistent | No premature internal build has occurred; all current tooling is bought/adopted off-the-shelf, correctly, at this scale |
| [Acquire when leverage exists](02_FOUNDING_PRINCIPLES.md#acquire-when-leverage-exists) | 🔵 Not yet testable | No acquisition has been evaluated |
| [Data before intuition](02_FOUNDING_PRINCIPLES.md#data-before-intuition) | 🔵 Not yet testable | No decision requiring this trade-off has occurred |
| [Action over perfection](02_FOUNDING_PRINCIPLES.md#action-over-perfection) | 🟢 Strong | This document itself was published at v1.0 with many open TBDs rather than delayed for completeness |
| [One source of truth](02_FOUNDING_PRINCIPLES.md#one-source-of-truth) | 🟢 Strong | Verified — see [Current Knowledge System § Single source of truth audit](#current-knowledge-system) |

### Adherence summary

| Rating | Count |
|---|---|
| 🟢 Strong | 10 |
| 🟡 Partial / not yet tested | 9 |
| 🔴 Weak | 1 |
| 🔵 Not yet testable (no relevant activity exists) | 3 |

**Interpretation:** the one 🔴 (Automation by default) and the cluster of 🟡 ratings concentrated in documentation completeness, decision practice, and automation governance point to the same root cause already identified throughout this document — Atlas has built the constitution but has not yet exercised it. No 🟢 rating here should be read as "done forever"; all are subject to re-audit at the next quarterly review.

---

## Appendix H — Roadmap Success Criteria (H0) Cross-Check

Cross-checking current reality against the [H0 success criteria](04_ROADMAP.md#success-criteria) defined in the Roadmap — the most immediate horizon-level bar Atlas is being measured against.

| ID | Criterion | Metric / evidence required | Current status |
|---|---|---|---|
| SC-H0-01 | Brain is operable | T1 set Active; used in decisions | 🟡 T1 set is 6/8 Active; not yet used in any *logged* decision |
| SC-H0-02 | Ownership exists | Single owners on material outcomes | ✅ Met — see [Current Ownership](#current-ownership) |
| SC-H0-03 | Truth channel open | Current State + bad news examples | 🟡 Current State now exists (this document); no "bad news" example yet exists because no operating activity has produced any bad news to report — the closest analogue is this document's own gap disclosures |
| SC-H0-04 | First execution loop | ≥1 project full lifecycle | 🔴 Not met — 0 projects through the full [Project Lifecycle](00_ATLAS_BRAIN.md#project-lifecycle) |
| SC-H0-05 | First capital discipline | Buckets + hurdles written | 🔴 Not met — buckets and hurdles remain TBD |

**H0 verdict:** 1 of 5 criteria fully met, 2 partially met, 2 not met. This is consistent with the P0 exit-criteria status reported in [Current Strategic Position](#current-strategic-position) — the two frameworks corroborate each other, which is itself a small positive signal that this document's assessment is internally consistent.

---

## Appendix I — Onboarding Path Dry-Run

A literal attempt to execute the [onboarding knowledge path](00_ATLAS_BRAIN.md#onboarding-knowledge-path) today, step by step, recording exactly where it succeeds and where it blocks. This satisfies milestone M-K-002 and is the evidence for [Phase 1 exit criterion P1.8](04_ROADMAP.md#phase-1--operating-kernel) ("Onboarding path executed once — New operator or simulated dry-run").

| Step | Designed instruction | Dry-run result |
|---|---|---|
| 1 | Read `00_ATLAS_BRAIN.md` | ✅ Succeeds — document is Active and complete |
| 2 | Read `01_WHY_ATLAS_EXISTS.md` | ✅ Succeeds — document is Active and complete |
| 3 | Read `07_GLOSSARY.md` | ✅ Succeeds — Active v1.0, ~150 terms |
| 4 | Read relevant department playbooks | ✅ Succeeds — 7 of 7 department playbooks exist (`brain_playbook.md`, `knowledge_playbook.md`, `ai_playbook.md`, `finance_playbook.md`, `operations_playbook.md`, `assets_playbook.md`, `projects_playbook.md`) |
| 5 | Read `05_CURRENT_STATE.md` and `04_ROADMAP.md` | ✅ Succeeds — both documents Active |

### Dry-run verdict

**The onboarding path now completes end to end.** A new operator, advisor, or AI agent following the designed path exactly succeeds at all five steps, including step 4, which previously blocked on missing department playbooks. This dry-run itself is the "simulated dry-run" evidence required by P1.8; no separate execution artifact was needed once the step-4 blocker cleared.

### Time-to-complete

Per [Knowledge § KPIs](03_ORGANIZATION.md#department-knowledge) ("Onboarding path completion time < 5 business days for core path"), all five steps — including step 4, now that 7 playbook stubs exist — complete within under an hour of reading time. The KPI is now measurable for the full path, and passes.

---

## Appendix J — First Quarterly Brain Review — Draft Agenda

No quarterly Brain review has ever been held (see [Current Review Process](#current-review-process)). This appendix drafts the agenda for the first one, due 2026-11-08, built entirely from gaps and action items already surfaced elsewhere in this document — so that the first review has a concrete starting point rather than a blank page.

1. **Phase gate check** — ✅ **Completed 2026-08-08.** P0 exited; P1 entered via DR-2026-002. Verify **P1.1** remains valid; prioritize open criteria **P1.2 / P1.4 / P1.5**.
2. **CM re-score** — Re-run the [Current Capability Maturity](#current-capability-maturity) scorecard. Did any dimension move from 0/1 to 2? Which is now the weakest link?
3. **Decision log health** — How many Decision Records exist? Does the count match the [Decision Record Backlog](#appendix-e--decision-record-backlog) items that were supposed to be logged?
4. **Risk review** — Walk the [Current Risks](#current-risks) register category by category. Has the knowledge-base backup risk been closed? Has legal entity status moved from Unknown to Known?
5. **Capital bucket check** — Has [Current Finance](#current-finance)'s all-TBD bucket table received even a provisional allocation?
6. **Headcount and role check** — Still Stage 0? If not, has [Current Scaling Readiness](#current-scaling-readiness) been re-run against Stage 1 criteria before any hire was made?
7. **Principle adherence spot-check** — Re-score 2–3 of the weakest items from [Appendix G](#appendix-g--principle-adherence-self-audit) (Automation by default; Extreme documentation).
8. **Set next quarter's watch list** — Replace [Appendix B](#appendix-b--next-90-days-watch-list) with a new ranked list reflecting whatever remains open.
9. **Version this document** — Bump to v1.1 or higher per [Versioning Policy](00_ATLAS_BRAIN.md#versioning-policy), log the changelog entry, and update the review date.

---

## Cross References

This document is the **instance layer** of Atlas. Every sibling document supplies the type this document reports against — **link, never duplicate**.

| Document | Relationship to Current State |
|---|---|
| [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) | Source of the AI maturity model (L0–L4), decision framework, department definitions, and capital bucket structure this document reports live values against. |
| [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) | Source of the philosophical conviction this document's honesty discipline is grounded in — see especially [Why Every Decision Must Become Knowledge](01_WHY_ATLAS_EXISTS.md#why-every-decision-must-become-knowledge) and [What Success Looks Like](01_WHY_ATLAS_EXISTS.md#what-success-looks-like). |
| [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) | Source of [Truth over comfort](02_FOUNDING_PRINCIPLES.md#truth-over-comfort) and [Evidence over opinion](02_FOUNDING_PRINCIPLES.md#evidence-over-opinion), the two principles this document exists to operationalize most directly. |
| [`03_ORGANIZATION.md`](03_ORGANIZATION.md) | Source of Org Stage definitions, department scope, ownership rules, and the explicit instruction that headcount, roles, and threshold instance values live here. |
| [`04_ROADMAP.md`](04_ROADMAP.md) | Source of horizons, eras, phases, milestone IDs, and the CM dimension rubrics this document scores against. Roadmap sets *what phase we are building toward*; this document reports *what phase we are actually in*. |
| [`06_DECISIONS.md`](06_DECISIONS.md) | Active v1.0 — **4 Register entries** (DR-2026-001 through DR-2026-004); decision-count statistics sourced from that file. |
| [`07_GLOSSARY.md`](07_GLOSSARY.md) | Active v1.0 — terms used in this document (DRI, believability, one-way door, CM, L-level) resolve to that canonical source. |

### Relationship to Principles

| Principle | How this document expresses it |
|---|---|
| Truth over comfort | Entire document — every gap stated plainly |
| Evidence over opinion | Every claim marked Active is evidenced by a file, date, or count; every unevidenced claim is marked TBD/Unknown |
| Extreme documentation | This document is itself an act of documenting the absence of documentation elsewhere |
| Ownership | [Current Ownership](#current-ownership) names a single owner for every existing artifact |
| One source of truth | No framework is redefined here; every framework is linked to its canonical home |
| Action over perfection | Published now, at Stage 0, with many TBDs, rather than delayed until a "complete" picture exists |

---

## Document Maintenance

| Field | Value |
|---|---|
| **Canonical owner** | Brain department (Brain lead) |
| **Suggested readers** | All operators (currently one); future hires during onboarding; AI agents retrieving live instance values; any future advisor or investor |
| **Change process** | Update directly on any material change (new hire, first decision, first asset, phase transition); otherwise reviewed and rewritten at each quarterly cadence per [Versioning Policy](00_ATLAS_BRAIN.md#versioning-policy) |
| **Review cadence** | Quarterly, or immediately on material change |
| **AI retrieval note** | Agents should treat this document as authoritative for **live instance values only** — headcount, ownership, phase, CM score, financial figures, decision/glossary counts. Agents must defer to [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md), [`03_ORGANIZATION.md`](03_ORGANIZATION.md), and [`04_ROADMAP.md`](04_ROADMAP.md) for definitions, structure, and sequencing — never infer type-level rules from this document. |

### Changelog

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-08-08 | Initial population. First honest snapshot of Atlas at Phase P0 / Org Stage 0: 5 active Brain documents, 1 operator, 0 portfolio assets, 0 decisions logged, 0 glossary terms, 0 automations, full gap inventory across all 47 requested current-state dimensions. |
| 1.1 | 2026-08-08 | Synced instance layer to reflect populated [`06_DECISIONS.md`](06_DECISIONS.md) (framework v1.0) and [`07_GLOSSARY.md`](07_GLOSSARY.md) (v1.0, ~150 terms). P0.8 met; P0.7 partially met (Register empty); onboarding dry-run updated (blocked at step 4, not step 3). |
| 1.2 | 2026-08-08 | Logged DR-2026-001 and DR-2026-002; P0 exited and P1 entered; M-G-003 and M-G-007 met; CM-1 narrow interpretation resolved; near-term priority shifted to P1 playbook work. |
| 1.3 | 2026-08-10 | Truth-layer sync: 7 Draft playbooks (P1.1 Met); registry + 6 candidates (P1.3 Met); integration scorecard template (P1.6 Met); 4 live DRs; AR-002/003/006 Prototype Run #1 + AR-003 Spec noted without maturity promotion; P-001/Market Screen project evidence without marking P1.2 Met; finance close SOP noted with P1.5 still Not Met; Appendix E ID collisions removed; Founder name normalized to Антон / Anton. Phase 1 exit remains No. |
| 1.3.1 | 2026-08-10 | Second truth-sync pass + final micro-fixes: remaining contradictory stale claims; **M-A-001** Partial (P1.3 remains Met); Last updated → 2026-08-10; threshold-table wording aligned to P1.7; present-tense P0 framing corrected to early P1 where current; P1.1 review wording updated (Met); hiring/SOP absolute wording made precise. |

---

*This document reports what is true. For what Atlas optimizes for, see [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md). For why Atlas exists, see [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md). For who owns what, see [`03_ORGANIZATION.md`](03_ORGANIZATION.md). For where Atlas is going, see [`04_ROADMAP.md`](04_ROADMAP.md).*
