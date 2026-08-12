# Atlas Decisions

> The canonical decision framework for Atlas — how decisions get made, by whom, under what authority, with what evidence, at what level of rigor, and how they become institutional knowledge. This document defines the *machinery* of judgment. It does not restate *why* Atlas holds the values it holds, *who* sits in which role today, or *what* has actually been decided so far — it points to the sibling documents that own those facts.

**Document ID:** `06_DECISIONS.md`
**Location:** `02_Brain/`
**Status:** Active
**Version:** 1.1
**Owner:** Brain
**Classification:** Governance — decision framework
**Last updated:** 2026-08-12
**Review date:** 2026-11-08
**Supersedes:** — (first populated version; document previously existed as an empty placeholder)
**Authority:** This document is the authoritative source for *how Atlas makes decisions* — authority bands applied to decisions, decision classes, the decision pipeline, gates, evidence requirements, risk and opportunity scoring, AI participation rules, escalation mechanics, reversibility doctrine, delegation and ownership rules, logging mechanics, the live Decision Register, quality metrics, bias controls, postmortem and audit cadences, and anti-patterns. It does not hold philosophy ([`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md)), principles rationale ([`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md)), organizational structure ([`03_ORGANIZATION.md`](03_ORGANIZATION.md)), strategic sequencing ([`04_ROADMAP.md`](04_ROADMAP.md)), or instance facts about what has actually happened ([`05_CURRENT_STATE.md`](05_CURRENT_STATE.md)). Where this document and a sibling appear to disagree, the sibling wins on *type* (mission, principles, structure, roadmap) and this document wins on *decision mechanics* — see [Relationship to Other Brain Documents](#relationship-to-other-brain-documents).

---

## Table of Contents

1. [Purpose](#purpose)
2. [Relationship to Other Brain Documents](#relationship-to-other-brain-documents)
3. [Decision Philosophy](#decision-philosophy)
4. [Decision Authority](#decision-authority)
5. [Decision Levels](#decision-levels)
6. [Decision Classes](#decision-classes)
7. [Decision Lifecycle](#decision-lifecycle)
8. [Decision Pipeline](#decision-pipeline)
9. [Decision Templates](#decision-templates)
10. [Decision Gates](#decision-gates)
11. [Required Evidence](#required-evidence)
12. [Risk Assessment](#risk-assessment)
13. [Opportunity Assessment](#opportunity-assessment)
14. [Capital Allocation](#capital-allocation)
15. [AI-Assisted Decisions](#ai-assisted-decisions)
16. [Human Override Rules](#human-override-rules)
17. [Escalation Rules](#escalation-rules)
18. [One-Way vs Two-Way Decisions](#one-way-vs-two-way-decisions)
19. [Reversible Decisions](#reversible-decisions)
20. [Irreversible Decisions](#irreversible-decisions)
21. [Delegation Rules](#delegation-rules)
22. [Ownership Rules](#ownership-rules)
23. [Decision Logging](#decision-logging)
24. [Decision Register](#decision-register)
25. [Decision Quality Metrics](#decision-quality-metrics)
26. [Bias Detection](#bias-detection)
27. [Failure Analysis](#failure-analysis)
28. [Postmortem Process](#postmortem-process)
29. [Quarterly Decision Review](#quarterly-decision-review)
30. [Annual Decision Audit](#annual-decision-audit)
31. [Decision Anti-patterns](#decision-anti-patterns)
32. [Worked Examples](#worked-examples)
33. [Appendices](#appendices)
    - [Appendix A — Decision Record Template (Canonical)](#appendix-a--decision-record-template-canonical)
    - [Appendix B — Decision Classification Flowchart](#appendix-b--decision-classification-flowchart)
    - [Appendix C — Evidence Checklists by Class](#appendix-c--evidence-checklists-by-class)
    - [Appendix D — Bias Self-Audit Checklist](#appendix-d--bias-self-audit-checklist)
    - [Appendix E — Postmortem Template](#appendix-e--postmortem-template)
    - [Appendix F — Escalation Packet Template](#appendix-f--escalation-packet-template)
    - [Appendix G — First-Time Decision Owner Quick-Start](#appendix-g--first-time-decision-owner-quick-start)
    - [Appendix H — Candidate Glossary Terms](#appendix-h--candidate-glossary-terms)
    - [Appendix I — One-Page Quick Reference Card](#appendix-i--one-page-quick-reference-card)
    - [Appendix J — Frequently Asked Questions](#appendix-j--frequently-asked-questions)
    - [Appendix K — Master Checklist Index](#appendix-k--master-checklist-index)
    - [Appendix L — Delegation Record Template](#appendix-l--delegation-record-template)
    - [Appendix M — Full Worked Evidence Packet (Illustrative DL-4 Capital Decision)](#appendix-m--full-worked-evidence-packet-illustrative-dl-4-capital-decision)
    - [Appendix N — Decision Level and Class Quick Matrix](#appendix-n--decision-level-and-class-quick-matrix)
34. [Cross References](#cross-references)
35. [Document Maintenance](#document-maintenance)

**Related documents:** [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) · [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) · [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) · [`03_ORGANIZATION.md`](03_ORGANIZATION.md) · [`04_ROADMAP.md`](04_ROADMAP.md) · [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) · [`07_GLOSSARY.md`](07_GLOSSARY.md)

---

## Purpose

### What this document is

This document defines **how Atlas makes decisions** — the complete operating mechanism that converts a question ("should we do X?") into a logged, owned, evidence-backed, reviewable commitment.

It answers:

- **Who has the authority to decide** — mapped onto the [Decision Authority](03_ORGANIZATION.md#decision-authority) bands already defined in Organization, with decision-specific mechanics layered on top
- **What kind of decision this is** — the taxonomy that determines which gates, evidence, and rigor apply
- **What sequence a decision moves through** — from framing to logging to review, with defined gates between stages
- **What evidence is mandatory** — by decision level, class, and reversibility
- **How risk and opportunity get scored** — quantified, not vibes
- **How AI participates** — where it helps, where it is capped, and where a human must sign
- **When to escalate, delegate, or override** — and what happens when someone does none of those and should have
- **How a decision becomes knowledge** — logging mechanics and the live Decision Register
- **How Atlas gets better at deciding** — quality metrics, bias controls, postmortems, quarterly review, annual audit

### What this document is not

| This document | Lives elsewhere |
|---|---|
| Mission, vision, high-level Decision Framework summary | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md#decision-framework) |
| Why traditional organizations decide badly; why AI-native decisioning wins | [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) |
| Why principles exist; principle-level conflict resolution and the Decision Checklist | [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md#decision-checklist) |
| Who holds which authority band today; department ownership of decision types | [`03_ORGANIZATION.md`](03_ORGANIZATION.md#decision-authority) |
| Strategic sequencing, phase gates, milestone dependencies | [`04_ROADMAP.md`](04_ROADMAP.md) |
| Actual decisions logged to date; live escalation thresholds; current decision-system maturity | [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md#current-decision-system) |
| Canonical term definitions (DRI, believability, one-way door, etc.) | [`07_GLOSSARY.md`](07_GLOSSARY.md) |

This document defines the **type** — the reusable machine. [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) holds the **instance** — how many decisions have run through the machine, and what it found. Confusing the two is the single most common failure mode of governance documentation, and this document actively guards against it throughout.

### Primary audience

| Audience | How to use this document |
|---|---|
| **Decision owners** (any DRI facing a non-trivial choice) | Section 5 (levels) to size the decision, Section 8 (pipeline) to run it, Section 9 (templates) to document it |
| **Brain** | Sections 4, 10, 17, 21, 29, 30 — authority, gates, escalation, delegation, and the review/audit cadence Brain runs |
| **Department heads** | Sections 5–6 to classify decisions inside their domain; Section 21 to delegate downward correctly |
| **AI agents** | Section 15 for participation rules and caps; Sections 9, 23, 24 as the literal schema for drafting and logging decisions |
| **New operators** | Read after Brain, Principles, and Organization; this is where judgment becomes procedure |
| **Future auditors / annual review** | Sections 25–30 define what "good decisioning" looks like and how it is measured over time |

### Design intent

A decision framework that exists only as prose is advice. A decision framework with levels, gates, mandatory fields, a register, and an audit cadence is **infrastructure** — the same standard Atlas applies to documentation, automation, and organizational design. See [Documentation Is Infrastructure](00_ATLAS_BRAIN.md#documentation-standards) and [Why Every Decision Must Become Knowledge](01_WHY_ATLAS_EXISTS.md#why-every-decision-must-become-knowledge).

### What "good" looks like when this document is actually working

A concrete picture of success, beyond the metrics in Section 25: a new operator can read [Appendix G](#appendix-g--first-time-decision-owner-quick-start), make a defensible first decision within an hour, and log it correctly without needing to ask anyone a clarifying question. A department head facing a genuinely hard, irreversible call reaches for the full pipeline instinctively, not because a rule forced them to, but because the scoring and evidence structure visibly makes their case stronger. Brain's Quarterly Review takes thirty minutes because the Register already answers most of the standing agenda's questions on its own. And a year from now, a new hire reading the Register's precedent for a decision they're about to make finds a well-evidenced, honestly-scored prior attempt — successful or not — that makes their own decision measurably easier than it would have been with no institutional memory at all. That compounding effect, more than any single gate or metric, is what this document is actually for.

### Non-goals of this document

Stated explicitly, to prevent scope creep in future amendments:

- This document does not set financial thresholds, hurdle rates, or bucket percentages — those are instance values ([Current Finance](05_CURRENT_STATE.md#current-finance)).
- This document does not name who currently holds any authority band, department head role, or escalation target — those are instance values ([Current Organization](05_CURRENT_STATE.md#current-organization)).
- This document does not replace judgment with a formula. Scoring rubrics (Sections 12–13) structure judgment; they do not automate it away.
- This document does not create a second, competing authority hierarchy alongside [Organization's](03_ORGANIZATION.md) — it applies the existing one.
- This document does not mandate specific software tooling for the Register, gates, or metrics — see [Known limitations](#document-maintenance) for the current, deliberately tooling-free state.
- This document does not retroactively re-litigate decisions made before it existed — see [Decision Logging § Retroactive logging](#decision-logging).

This document is written to be **usable at Stage 0** (a single operator, zero portfolio companies, zero logged decisions — see [Current Organizational Maturity](05_CURRENT_STATE.md#current-organizational-maturity)) and to **scale without a rewrite** as Atlas adds departments, capital, headcount, and portfolio companies. Every mechanism below specifies what changes as Atlas scales and what does not.

### Who wrote this document, and why that matters

This document was drafted at Brain's direction as the canonical decision framework, synthesizing and operationalizing decision-related content already scattered across [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md), [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md), and [`03_ORGANIZATION.md`](03_ORGANIZATION.md) into a single, self-contained mechanism. Nothing in this document introduces a new principle or a new authority holder — every rule here is traceable to a sibling document's existing statement, made specific enough to gate, template, and measure. Where this document appears to say something new, it is elaboration of an existing rule's mechanics, not a new policy — and if that distinction ever seems to fail in a specific section, that is a defect worth raising via the amendment process in [Document Maintenance](#document-maintenance), not a precedent to build on.

### Scope test — does a question belong in this document?

Before adding anything new here, apply this test:

| Question | If "yes," it belongs... |
|---|---|
| Does it change *why* Atlas values something? | [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) |
| Does it change *who* holds an authority band or *how departments interface*? | [`03_ORGANIZATION.md`](03_ORGANIZATION.md) |
| Does it change *when* Atlas plans to reach a capability or milestone? | [`04_ROADMAP.md`](04_ROADMAP.md) |
| Does it report a *fact about today* — a count, a name, a live threshold? | [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) |
| Does it define a *term* used across documents? | [`07_GLOSSARY.md`](07_GLOSSARY.md) |
| Does it define *how a decision moves from question to logged knowledge*? | **This document** |

A proposed addition that fails this test is redirected to the correct sibling document rather than absorbed here, even if the proposer's instinct was to put it in "the decisions doc." Guarding this boundary is itself a Knowledge-department responsibility, exercised on Brain's behalf per [Knowledge Management](00_ATLAS_BRAIN.md#knowledge-management).

### How to use this document under time pressure

Not every reader has time to read all thirty-five sections before a decision is due. The fast path:

1. If the decision feels urgent and small, jump straight to [Decision Levels](#decision-levels)'s sizing test — most decisions resolve to DL-0/DL-1 in under a minute and the rest of the document does not apply yet.
2. If it feels urgent and large, jump to [Appendix G — First-Time Decision Owner Quick-Start](#appendix-g--first-time-decision-owner-quick-start) and follow the eleven steps in order.
3. Only return to the full section text when a specific step in the quick-start raises a question the eleven steps don't answer — e.g., "how exactly do I score risk" sends you to [Risk Assessment](#risk-assessment).

This document is structured so that **depth is optional and procedure is not** — a reader who never opens Sections 4–31 in full can still make a well-governed decision by following Appendix G alone, provided they actually do each step rather than skip to a conclusion.

### Document map

The thirty-five sections group into six functional clusters. Understanding the clusters makes it easier to find the right section without re-reading the full Table of Contents each time:

| Cluster | Sections | What it answers |
|---|---|---|
| **Foundations** | 1–3 (Purpose, Relationship to Other Brain Documents, Decision Philosophy) | Why this document exists and how it fits with its siblings |
| **Classification** | 4–7 (Authority, Levels, Classes, Lifecycle) | What kind of decision this is and who decides it |
| **Mechanics** | 8–11 (Pipeline, Templates, Gates, Required Evidence) | How a decision actually moves from question to documented answer |
| **Judgment tools** | 12–16 (Risk, Opportunity, Capital Allocation, AI-Assisted Decisions, Human Override) | How to score, fund, and appropriately automate a decision |
| **Governance mechanics** | 17–22 (Escalation, One-way/Two-way, Reversible, Irreversible, Delegation, Ownership) | Who gets involved, when, and how authority moves |
| **Learning loop** | 23–31 (Logging, Register, Quality Metrics, Bias, Failure Analysis, Postmortem, Quarterly Review, Annual Audit, Anti-patterns) | How Atlas gets better at deciding over time |
| **Grounding** | 32–35 (Worked Examples, Appendices, Cross References, Document Maintenance) | Concrete illustration, fillable tools, and document governance |

A reader troubleshooting a specific problem ("my decision is stuck," "I don't know how much evidence I need," "we keep missing our own success metrics") can usually identify which cluster it falls into and jump directly there rather than reading linearly.

### How long this document takes to read

At normal reading speed, the full document (including appendices) takes roughly ninety minutes to two hours end to end — comparable to [`03_ORGANIZATION.md`](03_ORGANIZATION.md) and [`04_ROADMAP.md`](04_ROADMAP.md) in the same document set. Most readers will never need the full read-through; [Appendix G](#appendix-g--first-time-decision-owner-quick-start) and [Appendix I](#appendix-i--one-page-quick-reference-card) are each under five minutes and cover the majority of day-to-day use.

---

## Relationship to Other Brain Documents

Atlas maintains **one source of truth per concept**. This document does not repeat philosophy, principles, structure, roadmap, or instance state — it links to them and adds only what is unique to decision mechanics.

### How this document composes with its siblings

| Document | What it contributes to decision-making | What this document adds on top |
|---|---|---|
| [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) | The five-step [Decision Framework](00_ATLAS_BRAIN.md#decision-framework) (frame → evidence → options → decide → execute), the [Decision Record minimum fields](00_ATLAS_BRAIN.md#documentation-standards), default owners by decision type, review cadences by size, [one-way vs two-way doors](00_ATLAS_BRAIN.md#one-way-vs-two-way-doors) | Turns the five steps into an eleven-stage pipeline with named gates; extends the minimum-fields template into the full canonical template; adds scoring math, evidence checklists, AI participation rules, bias controls, and the audit cadence |
| [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) | The philosophical case for [why every decision must become knowledge](01_WHY_ATLAS_EXISTS.md#why-every-decision-must-become-knowledge) and why AI-native verification beats bureaucratic committee review | Nothing philosophical — this document is pure mechanism. Read the philosophy doc for conviction, this doc for procedure. |
| [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) | The [Principle Hierarchy](02_FOUNDING_PRINCIPLES.md#principle-hierarchy) used to break ties, the [Decision Checklist](02_FOUNDING_PRINCIPLES.md#decision-checklist) (Frame/Evidence/Options/Alignment/Execute/Learn), the definition of [Reversible decisions](02_FOUNDING_PRINCIPLES.md#reversible-decisions) as a principle | This document operationalizes the checklist into gates with owners, timeboxes, and mandatory artifacts; operationalizes reversibility into a formal door-type classification test |
| [`03_ORGANIZATION.md`](03_ORGANIZATION.md) | The [Decision Authority](03_ORGANIZATION.md#decision-authority) bands (L0–L4), [Escalation Authority](03_ORGANIZATION.md#escalation-authority) paths, [Single Owner Principle](03_ORGANIZATION.md#single-owner-principle), believability-weighted input | This document is the authority bands **applied specifically to decisions** — which band a decision needs is a function of decision level, class, and door type defined here |
| [`04_ROADMAP.md`](04_ROADMAP.md) | Phase gates, milestone dependencies, the [Capability Maturity Model](04_ROADMAP.md#capability-maturity-model) that scores the decision system itself (CM dimension "D" tracks decision-system maturity) | This document is what CM dimension D is scoring **against** — the decision system Roadmap expects to mature |
| [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) | Live escalation threshold values, current Decision Register population count, current CM score for the decision dimension, [Appendix E — Decision Record Backlog](05_CURRENT_STATE.md#appendix-e--decision-record-backlog) | Nothing — this is the sibling that reports facts *about* this document's usage. This document never states current counts, current named owners, or current threshold percentages as fact; it says "see Current State." |
| [`07_GLOSSARY.md`](07_GLOSSARY.md) | Canonical definitions of DRI, believability, holding OS, one-way door, CM, L-level | This document is a major *source* of new candidate terms (see [Appendix H](#appendix-h--candidate-glossary-terms)) pending Glossary formalization |

### The non-duplication rule, applied here

If a sentence in this document could be copy-pasted into `00_ATLAS_BRAIN.md`, `02_FOUNDING_PRINCIPLES.md`, `03_ORGANIZATION.md`, `04_ROADMAP.md`, or `05_CURRENT_STATE.md` without modification and still be true there, it does not belong in this document — it belongs in a cross-reference. This document exists **only** for content that is uniquely about the mechanics of deciding: pipeline stages, gates, templates, scoring rubrics, register schema, quality metrics, bias controls, and the review/audit cadence specific to decisions.

### What happens when documents conflict

Per [Single source of truth](00_ATLAS_BRAIN.md#single-source-of-truth): conflicts are resolved by Brain, and the resolution is logged — in this Register, using the standard template, classified as a **Governance** decision (see [Decision Classes](#decision-classes)).

### Worked conflict-resolution example

Suppose [Current State](05_CURRENT_STATE.md) reports an escalation threshold value that appears to contradict a trigger category defined in [Organization](03_ORGANIZATION.md#default-brain-escalation-thresholds). Resolution sequence:

1. Confirm which document is reporting **type** (Organization: "capital commitment above a % threshold escalates") versus **instance** (Current State: "that % is currently TBD" or a specific number).
2. If the type definition itself seems wrong — e.g., the trigger category no longer makes sense at Atlas's current scale — this is a Governance-class, DL-4 decision to amend Organization, run through this document's pipeline.
3. If only the instance value is stale or missing, this is an Operational-class, DL-1 decision to update Current State — no framework change required.
4. Log whichever of the two actually occurred, so future readers can see the conflict was noticed and deliberately resolved rather than silently patched.

### Reading order for a new operator

Consistent with [Knowledge Management's onboarding path](00_ATLAS_BRAIN.md#onboarding-knowledge-path), this document is read **after** Brain, Why Atlas Exists, Founding Principles, and Organization — never before them. A reader who opens this document first will see authority bands, decision types, and terminology (DRI, believability, one-way door) asserted without derivation. That is intentional: derivation lives upstream, and re-deriving it here would violate the non-duplication rule this section exists to protect.

---

## Decision Philosophy

This section is intentionally short. Depth belongs in [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md); this is the minimum orientation needed before reading the mechanics below.

### Decisions are hypotheses, not verdicts

Every decision in this framework is treated as a testable hypothesis with a stated success metric and a review date — never a final verdict to be defended. See [Data-driven decisions](00_ATLAS_BRAIN.md#data-driven-decisions) and [Execute, measure, and iterate](00_ATLAS_BRAIN.md#5-execute-measure-and-iterate). This reframing is what makes postmortems blameless (Section 28) and failed hypotheses celebrated rather than punished.

### Speed and rigor are not opposites

Atlas does not trade speed for rigor or rigor for speed — it buys both simultaneously with pre-built templates, defined authority, and AI-assisted evidence gathering. See [Speed with rigor](00_ATLAS_BRAIN.md#speed-with-rigor). The pipeline in Section 8 is designed so that a fully reversible, low-stakes decision can clear every gate in minutes, while an irreversible, high-stakes decision is forced through every gate at full depth — the machinery is the same; the depth is not.

### The default is document, not remember

A decision that exists only in someone's memory does not exist for the purposes of scaling, delegation, or AI retrieval. See [Documentation before execution](00_ATLAS_BRAIN.md#documentation-before-execution). This document treats **unlogged decisions as provisional** regardless of how confidently they were made — see [Decision Logging](#decision-logging).

### Evidence outranks conviction; conviction does not outrank evidence-free silence

Believability-weighted input (see [Organization](03_ORGANIZATION.md#believability-weighted-input)) means track record and evidence quality earn more weight than title — but a strong opinion with no evidence is still weaker than a modest opinion with data. This document's evidence and scoring rubrics (Sections 11–13) exist to make that comparison explicit rather than social.

### When principles conflict, use the hierarchy — do not litigate it here

This document assumes the [Principle Hierarchy](02_FOUNDING_PRINCIPLES.md#principle-hierarchy) and Brain's [Core Principle order](00_ATLAS_BRAIN.md#principle-hierarchy) as inputs. It does not re-derive them. When a decision genuinely pits two high-order principles against each other, that tension is itself evidence to log (see [Required Evidence](#required-evidence) and [Decision Anti-patterns](#decision-anti-patterns) on "unexamined trade-offs").

### Rigor scales with reversibility and stakes, not with seniority

A DL-4 decision made by the most junior operator in the organization requires exactly the same evidence, scoring, and gates as one made by Brain itself — the pipeline does not get lighter because someone senior is confident. Conversely, a DL-0 decision made by Brain does not need to justify itself with a scoring table just because Brain made it. This is the decision-specific expression of [Believability-weighted input](03_ORGANIZATION.md#believability-weighted-input): weight attaches to evidence quality, and rigor attaches to stakes and reversibility — neither attaches to title.

### The framework must work identically for one person and for a thousand

Atlas is built to scale without rewriting its own operating system (see [Scaling Without Changing Principles](03_ORGANIZATION.md#scaling-without-changing-principles)). This document is written the same way: every mechanism — levels, classes, pipeline, gates, register — is designed to be exercised meaningfully by a single founder holding every authority band simultaneously, and to keep working, unmodified, once Atlas has seven staffed departments and a multi-company portfolio making dozens of decisions a week. What changes with scale is *volume and named ownership*, never the *mechanism*.

### A decision framework's job is to make the org right more often, not to make every individual decision right

No process guarantees a correct outcome for any single decision — see [Decisions are hypotheses, not verdicts](#decision-philosophy) above. What a good framework guarantees is a **higher long-run hit rate** and **faster learning from misses**, because every decision leaves a comparable, evidenced trace. Judge this document's success by trends across many logged decisions (Section 25), never by whether any one decision "worked out."

---

## Decision Authority

Atlas does not create a second authority system for decisions. It **applies** the authority bands already defined in [Organization § Decision Authority](03_ORGANIZATION.md#decision-authority) and adds the decision-specific rigor that rides on top of each band.

### The authority chain, restated for decisions

```
Principles → Decision Rules (this document) → Process Owners → Executors
```

[Organization](03_ORGANIZATION.md#decision-authority) defines who decides. This document defines **what that person must do** to decide well, at each band.

### Authority bands applied to decisions

| Band | Scope (from Organization) | What this document requires beyond authority |
|---|---|---|
| **L0 — Operational** | Reversible, within SOP, below spend threshold | Pipeline may compress to a single sentence in a status update; no DR required unless it sets a precedent |
| **L1 — Departmental** | Affects one department, reversible | Lightweight DR (Section 9, short form) if any capital, headcount, or external commitment is involved |
| **L2 — Cross-department** | Affects 2+ departments or portfolio | Full DR mandatory; Required Evidence (Section 11) mandatory; Risk + Opportunity scoring (Sections 12–13) mandatory |
| **L3 — Holding** | Strategic, capital, irreversible | Full DR + Brain sign-off + door-type classification (Section 18) mandatory; scoring mandatory; postmortem scheduled at logging time |
| **L4 — Governance** | Principles, structure, T1 docs | Full DR + Brain approval + version bump on the affected document + entry in that document's changelog |

### Who this document assumes decides what

This document assumes — and does not restate — [Organization's default owners by decision type](03_ORGANIZATION.md#default-owners-by-decision-type) and Brain's [decision types and default owners](00_ATLAS_BRAIN.md#1-frame-the-decision) table. Current named individuals holding each role are **instance data** — see [Current Organization](05_CURRENT_STATE.md#current-organization) and [Current Departments](05_CURRENT_STATE.md#current-departments). At Stage 0, one operator holds every band simultaneously; the bands still apply because they determine **rigor**, not just **who**.

### Authority is not seniority

Per [Believability-weighted input](03_ORGANIZATION.md#believability-weighted-input), authority to decide is assigned by role and ownership, not rank. A department head deciding inside their L1 domain outranks Brain's *opinion* on that decision, even though Brain sits above them in escalation — Brain can only override by invoking [Escalation Rules](#escalation-rules) or [Human Override Rules](#human-override-rules), not by seniority alone.

### Authority cannot be assumed by inaction

If no one explicitly owns a decision, the decision defaults to the nearest department head in the domain, per [Ownership Rules](#ownership-rules). Silence is never a valid authority claim — see [Decision Anti-patterns](#decision-anti-patterns), "decision by silence."

### Multi-owner decisions are not permitted

Every decision has exactly one **decision owner** (DRI) even when multiple co-owners contribute input. See [Single Owner Principle](03_ORGANIZATION.md#single-owner-principle) and [Ownership Rules](#ownership-rules) below. Committees recommend; they do not decide.

### Authority under time-critical conditions

Speed pressure does not create new authority. When a decision must be made faster than the normal escalation path allows (e.g., an operational incident requiring an immediate response), the person on the scene acts using the **incident commander** model from [Risk Management's incident response](00_ATLAS_BRAIN.md#incident-response) — contain first, formally decide and log within the normal framework afterward. This is not a bypass of authority bands; it is the band structure's own emergency provision: [Organization's escalation paths](03_ORGANIZATION.md#escalation-paths-by-trigger) already routes "Operational incident (severity 1)" to immediate escalation with same-day resolution expected, and the DR documenting the response is logged retroactively per [Decision Logging](#decision-logging), exactly like any other retroactive entry.

What time pressure never justifies: skipping Gate 4 (Approve) permanently, or treating an emergency response as precedent for future non-emergency decisions of the same type without running them through the full pipeline.

### Authority audit trail

Every DR at DL-2+ records not just *what* was decided but *who was authorized to decide it and how that was confirmed*. This produces an audit trail answering three questions on demand, without needing to reconstruct context after the fact:

| Question | Where the answer lives |
|---|---|
| Who decided this? | DR `Owner` field |
| Were they authorized at this level? | DR `Escalation approval` field — populated if above the owner's own band, explicitly "N/A — within owner's own band" if not |
| What evidence did the authorizer see? | DR `Evidence` section, unchanged from what the owner submitted, unless the authorizer requested revisions (logged as a Gate 2/3 return) |

This audit trail is what makes the [Annual Decision Audit](#annual-decision-audit)'s compliance sampling (Section 30) possible without reinterviewing anyone — the DR alone should be sufficient evidence of whether the correct authority band was used.

### Frequently asked authority questions

| Question | Answer |
|---|---|
| Can a department head decide something above their band if they're confident? | No. Confidence is not evidence of authority. Escalate per Section 17. |
| Can Brain decide something below Brain's own band, bypassing the department head? | Brain can, but doing so routinely undermines the department head's ownership and is flagged as an anti-pattern (Section 31, "Brain bypass," borrowed from [Organization's failure mode FM-02](03_ORGANIZATION.md#organizational-anti-patterns)) unless there is a specific, stated reason (e.g., the department head is unavailable). |
| What if the "right" authority holder disagrees with the evidence? | They can request more evidence (return to Gate 2) or override with a logged rationale (Section 16) — they cannot simply refuse to engage. |
| Does authority transfer automatically when someone changes roles? | No — see [Ownership Rules § Ownership transfer](#ownership-rules) for the explicit transfer mechanism. |
| Who has authority when two department heads disagree and neither is Brain? | Escalates to Brain per [Organization's escalation paths by trigger](03_ORGANIZATION.md#escalation-paths-by-trigger), "Ownership dispute." |

---

## Decision Levels

Decision Levels answer the question every decision owner asks first: **"How much process does this actually need?"** They map directly onto the L0–L4 authority bands (Section 4) but add the specific pipeline depth, evidence load, and review cadence that a decision at that level requires.

### The five decision levels

| Level | Maps to authority band | Typical trigger | Pipeline depth | Template | Review cadence |
|---|---|---|---|---|---|
| **DL-0 — Trivial** | L0 | Fully reversible, no capital, no external party, no precedent | Frame + Decide (2 stages) | None, or one-line log entry | None required |
| **DL-1 — Routine** | L0–L1 | Reversible, within a documented SOP or department budget | Frame → Evidence (light) → Decide → Log | Short-form DR (Appendix A, short variant) | 30 days if any spend/commitment involved |
| **DL-2 — Significant** | L1–L2 | Affects 2+ departments, meaningful resource commitment, or sets a reusable precedent | Full pipeline (Section 8), all gates | Full DR | 30 / 90 days |
| **DL-3 — Major** | L2–L3 | Portfolio-level impact, real capital at risk, hard or costly to reverse | Full pipeline + Risk/Opportunity scoring + Brain sign-off | Full DR + scoring appendix | 30 / 90 / 180 days |
| **DL-4 — Strategic** | L3–L4 | Direction-changing, principle-level, or structurally irreversible (see [Irreversible Decisions](#irreversible-decisions)) | Full pipeline + scoring + Brain approval + version bump if a governance doc is affected | Full DR + scoring appendix + changelog entry on affected document | Quarterly until stable, per [Brain's review cadence table](00_ATLAS_BRAIN.md#5-execute-measure-and-iterate) |

This mirrors — and is deliberately parallel in shape to — the [AI maturity model](00_ATLAS_BRAIN.md#ai-maturity-model) (L0–L4) and the org [Authority bands](03_ORGANIZATION.md#authority-bands) (L0–L4). Atlas uses consistent five-tier scales across authority, AI maturity, and decision weight so that operators and agents learn one mental model and reuse it everywhere. The letters differ (**DL** for Decision Level) specifically so a reader is never unsure whether "L2" refers to an AI maturity level, an authority band, or a decision level — always read the prefix.

### Sizing test — how to pick a level in under a minute

Answer in order; stop at the first "yes":

1. **Is this irreversible, or capital/precedent-setting at the holding level?** → DL-4
2. **Does real capital move, or is this hard to reverse within 90 days?** → DL-3
3. **Does this affect more than one department, or create a reusable pattern?** → DL-2
4. **Is this inside one department's documented budget/SOP and reversible?** → DL-1
5. **None of the above** → DL-0

If two answers could both apply, **take the higher level**. Under-classifying a decision is a named anti-pattern (Section 31); over-classifying merely costs some time.

### Level determines evidence and scoring load, not urgency

A DL-4 decision under time pressure still requires full evidence and scoring — it does not get to skip gates because the deadline is close. If genuinely no time exists to run the pipeline at the required depth, that is itself an escalation trigger (Section 17), not a license to downgrade the level.

### Level can be revised mid-pipeline

New evidence can raise or lower a decision's level between Frame and Decide (see [Decision Pipeline](#decision-pipeline), Gate 2). A decision that looked like DL-1 at framing but reveals cross-department impact during evidence-gathering is re-classified DL-2 before proceeding — never forced through the lighter pipeline it started in.

### Worked level examples across departments

To make the abstract sizing test concrete, here is how the same trigger type resolves to different levels depending on facts, across several departments:

| Department | Trigger | Facts that make it DL-1 | Facts that make it DL-3 |
|---|---|---|---|
| Operations | Switch a vendor | Month-to-month contract, < department threshold, easy migration | Multi-year contract, data migration risk, customer-facing impact |
| AI | Deploy a new agent | Internal tool, L1 supervised, single department | Customer-facing automation, L3 autonomous target, holding-wide rollout |
| Finance | Reforecast a budget line | Within-quarter adjustment, no bucket reallocation | Reallocates between capital buckets, changes Reserve adequacy |
| Assets | Engage with a prospect | Informal exploratory call, no commitment | Signing a letter of intent or exclusivity period |
| Projects | Reprioritize a sprint | Single team, no external commitment changed | Reprioritization delays a commitment made to a portfolio company or partner |
| Knowledge | Update a playbook | Clarifying existing guidance, no policy change | Playbook update that materially changes how a T1/T2 document is applied |

### Level inflation and level deflation

Two symmetric failure tendencies exist and are both worth naming even though only one appears in the anti-patterns table (Section 31, "over-classification drag" and "authority mismatch" respectively cover the two directions):

- **Level inflation** — routinely classifying decisions one notch higher than the sizing test supports, usually to avoid the discomfort of being wrong about classification, or to borrow the escalation target's authority as social cover. Costs organizational speed for no rigor benefit.
- **Level deflation** — routinely classifying decisions one notch lower than the sizing test supports, usually to avoid the evidence and scoring burden of the higher level. Costs rigor and is the more dangerous of the two, because it is invisible until a postmortem (Section 28) traces a bad outcome back to insufficient evidence that a correctly-assigned level would have required.

Both are visible in aggregate at the [Quarterly Decision Review](#quarterly-decision-review) by comparing self-assigned levels against the sizing test criteria for a sample of logged decisions.

### Level and the AI-assistance cap interact

Recall from [AI-Assisted Decisions](#ai-assisted-decisions) that AI decision-support is capped at L2 (supervised) maturity for DL-2+ decisions. This means the Decision Level an owner assigns has a direct, mechanical effect on how much autonomy AI is permitted in drafting that specific decision — under-classifying a decision does not just skip evidence gates, it also (incorrectly) grants AI more latitude than the framework intends.

---

## Decision Classes

Decision Classes are **what kind** of decision this is. Atlas uses exactly the five types already fixed in Brain's [Decision Record template](00_ATLAS_BRAIN.md#decision-record-template) — this document does not add a sixth type, it adds sub-classes, typical evidence, and typical gates underneath each of the five, so the taxonomy stays stable while guidance underneath it deepens.

### The five canonical types

| Type | Definition | Typical DL range | Default owner (per Organization) |
|---|---|---|---|
| **Investment** | Capital deployed into an asset, venture, or instrument expected to return value | DL-2 to DL-4 | Assets deal owner (+ Finance, + Brain per Organization's [default owners table](03_ORGANIZATION.md#default-owners-by-decision-type)) |
| **Operational** | Process, tooling, vendor, or workflow change inside existing operations | DL-0 to DL-2 | Operations process owner |
| **Strategic** | Direction, priority, positioning, or structural change to the holding itself | DL-3 to DL-4 | Brain |
| **Personnel** | Hiring, role change, compensation, separation, or delegation of authority to a person | DL-1 to DL-3 | Relevant department head (Brain if precedent-setting, per Organization) |
| **Technical** | System, architecture, AI/automation, or data decision | DL-0 to DL-3 | Agent owner + AI head, or domain owner |

### Sub-classes

Sub-classes exist to route evidence checklists (Section 11, [Appendix C](#appendix-c--evidence-checklists-by-class)) and typical scoring emphasis (Sections 12–13) without expanding the top-level taxonomy Brain already fixed.

| Type | Sub-class | Example trigger | Evidence emphasis |
|---|---|---|---|
| Investment | M&A / acquisition | Acquiring a portfolio company | Due diligence packet, valuation model, integration scorecard forecast |
| Investment | New venture / build | Launching a venture from scratch | Market sizing, MVP plan, build-vs-acquire comparison |
| Investment | Follow-on / reinvestment | Additional capital into an existing asset | Unit economics trend, prior decision outcomes (precedent) |
| Investment | Exit / divestiture | Selling or winding down an asset | Exit criteria check ([Company Lifecycle](00_ATLAS_BRAIN.md#company-lifecycle)), alternative-use-of-capital comparison |
| Operational | Process change | New SOP, workflow redesign | Baseline metrics, affected-party sign-off |
| Operational | Vendor / tooling | New vendor, tool switch, contract renewal | Cost comparison, switching cost, contract term length (door-type relevant) |
| Operational | Incident response | Reactive fix to an operational failure | Root cause analysis, blast radius |
| Strategic | Priority / roadmap change | Reprioritizing phases or milestones | Roadmap impact assessment, dependency check |
| Strategic | Capital bucket policy | Changing bucket allocation percentages | Portfolio-level return data, reserve adequacy check |
| Strategic | Principle exception | Deviating from a Core or Founding Principle | Written rationale, sunset date, Brain approval |
| Strategic | Governance / document change | Amending a T1/T2 document | Version bump plan, affected-document impact list |
| Personnel | Hire / role creation | New role or headcount | Role charter, budget source, hiring philosophy fit |
| Personnel | Separation | Ending a role or engagement | Knowledge-transfer plan, offboarding checklist |
| Personnel | Authority delegation | Temporarily or permanently delegating a decision band | Scope, duration, revocation trigger (see [Delegation Rules](#delegation-rules)) |
| Technical | AI / automation deployment | New agent or automation going live | Agent design standard fields, maturity level target, fallback plan |
| Technical | Architecture / infrastructure | System or data architecture change | Migration plan, rollback plan, security review |
| Technical | Model / vendor evaluation | Changing AI model or technical vendor | Evaluation criteria, cost/latency/accuracy comparison |

### Type definitions, restated with boundary cases

To sharpen the boundary between adjacent types beyond the one-line definitions in the table above:

- **Investment vs. Operational** — if capital is deployed expecting a return on that capital specifically, it's Investment; if capital is spent as a cost of running existing operations (even a large one-time cost), it's Operational. Buying equity in a company is Investment; buying a year of a SaaS subscription is Operational, even though both involve writing a check.
- **Strategic vs. Operational** — if the decision changes *what* Atlas does or *how* Atlas is structured/governed, it's Strategic; if it changes *how well* an existing, unchanged activity is carried out, it's Operational. Deciding to enter a new sector is Strategic; deciding how to run the existing sales process better is Operational.
- **Personnel vs. Operational** — if the decision is fundamentally about a person's role, compensation, or continued engagement, it's Personnel, even if it happens to also change a process; if the decision is about the process and a person merely executes the outcome, it's Operational.
- **Technical vs. Operational** — if the hard part of the decision is architecture, data, or automation design, it's Technical; if the hard part is workflow, sequencing, or human coordination and the technology is incidental, it's Operational.

These boundary cases are guidance, not a formula — see [Class selection FAQ](#decision-classes) below for the cases that come up most often in practice, and default to whichever type determines the *harder* trade-off when a decision genuinely straddles two.

### Multi-class decisions

Some decisions are genuinely more than one type — an acquisition (Investment) that also creates new roles (Personnel) and deploys new automation (Technical). Log the **primary** type in the DR's `Type` field per Brain's template, and list secondary classes in the DR's context section. Evidence and gates apply from **every** class touched, at the highest applicable Decision Level.

### Classes not covered here

A decision that fits none of the five types is a signal, not an exception — either the taxonomy needs a documented extension (Governance / L4 change to this document) or the decision has not been framed correctly yet. Do not invent an ad-hoc sixth type per decision.

### Why exactly five types, and why not more

Brain fixed five types deliberately narrow rather than exhaustive, because a taxonomy with too many top-level categories stops being useful for routing (Section 4's authority mapping, Section 11's evidence checklists) and starts requiring its own judgment call just to classify. Five types map cleanly onto Atlas's seven departments without a one-to-one mismatch, cover every decision category observed in the sibling documents' own examples (capital, process, direction, people, systems), and leave room for depth via sub-classes rather than proliferation via new top-level types. If a future era of Atlas (see [Roadmap's Phases of evolution](01_WHY_ATLAS_EXISTS.md#the-long-term-vision-50-years)) reveals a genuinely new category of decision that doesn't fit any of the five even at the sub-class level, that is itself significant enough to warrant a full Governance-class review of this section, not a quiet workaround.

### Class selection FAQ

| Question | Guidance |
|---|---|
| A decision is both Operational and Technical — which do I pick? | Pick whichever type the *primary* trade-off sits in. A process change implemented via a new automation is Operational if the process design is the hard part; Technical if the automation architecture is the hard part. |
| Is deciding to hire an AI agent's human owner Personnel or Technical? | Personnel — the decision is about a person's role and accountability, not the system itself. The system's deployment is a separate, linked Technical decision. |
| Is a decision to change how capital buckets are split Strategic or Investment? | Strategic — per [Capital Allocation](#capital-allocation), changing the *policy* is Strategic-class; deploying capital *within* the existing policy is Investment-class. |
| What about a decision that is purely about documentation itself, like amending this document? | Strategic-class, Governance/document-change sub-class, always DL-4. |
| Is choosing between two candidates for the same role a single decision or two? | One decision — "who to hire for role X" — with the candidates as the options in stage 5, not two independent Personnel decisions. |

### Class-to-department cross-check

Because Organization already assigns default owners per type (Section 4), the Class a decision receives should never surprise the department that ends up owning it. If classifying a decision as, say, Technical would hand ownership to a department that has no context on it, that is a signal the classification itself is wrong — revisit Section 6's sub-class table before overriding the default-owner mapping.

### Classes and the Register's long-run value

The reason this taxonomy matters more than it might first appear: every metric in [Decision Quality Metrics](#decision-quality-metrics) that is sliced "by Class" — hit rate, reversal rate, precedent reuse — is only meaningful if the same decision would have been classified the same way by two different owners. A taxonomy that drifts in practice (one owner calls a vendor switch Operational, another calls an identical situation Technical) quietly corrupts every one of those comparisons. This is why Section 6 spends this much space on boundary cases and an FAQ rather than leaving classification to instinct — the taxonomy's value compounds only if it is applied consistently across the whole Register, not just within any single decision.

### Class stability over time

The five canonical types are fixed by Brain and are treated as **immutable** in the same sense as [Founding Principles' immutable tier](02_FOUNDING_PRINCIPLES.md#principle-evolution) — changing them would invalidate historical Register entries' comparability. Sub-classes (the second table in this section) are **slow-changing**: new sub-classes may be added via a Governance-class DR as Atlas's activities diversify (e.g., a "Divestiture" sub-class already exists under Investment; a future "Joint venture" sub-class might be added once that activity type actually occurs), but the five top-level types do not expand.

### Class-to-department ownership matrix

Cross-referencing [Decision Classes](#decision-classes) against Atlas's seven departments, showing typical involvement (Owner / Contributor / Rarely involved) per [Organization's default owners table](03_ORGANIZATION.md#default-owners-by-decision-type):

| Department | Investment | Operational | Strategic | Personnel | Technical |
|---|---|---|---|---|---|
| Brain | Approver (DL-3+) | Rarely | Owner | Approver (precedent-setting) | Approver (holding-wide) |
| Knowledge | Contributor (precedent, docs) | Owner (doc standards) | Contributor | Rarely | Contributor (retrieval, docs) |
| AI | Contributor (leverage scoring) | Contributor (automation) | Rarely | Rarely | Owner |
| Finance | Owner (capital) | Contributor (cost) | Contributor (capital policy) | Contributor (budget) | Rarely |
| Operations | Contributor (integration) | Owner | Rarely | Contributor | Contributor (deployment) |
| Assets | Owner (deals) | Rarely | Contributor | Rarely | Rarely |
| Projects | Contributor (delivery) | Contributor | Rarely | Rarely | Contributor (delivery) |

This matrix is a **decision-routing aid**, not a new authority source — when it appears to conflict with [Organization's default owners table](03_ORGANIZATION.md#default-owners-by-decision-type), Organization wins, per this document's own non-duplication rule (Section 2).

---

## Decision Lifecycle

The Decision Lifecycle is the **state machine** every decision moves through, independent of level or class. It is the vocabulary used in the [Decision Record template](#appendix-a--decision-record-template-canonical)'s `Status` field and in the [Decision Register](#decision-register)'s `Status` column.

### States

```
Proposed → Approved → Implemented → Reviewed → Superseded
                 ↘ Rejected            ↘ Reopened
```

| State | Meaning | Who sets it | Can a decision skip it? |
|---|---|---|---|
| **Proposed** | Framed, evidence gathered, options scored — awaiting a decision from the owner or escalation target | Decision owner drafts; state is default on DR creation | No — every decision starts here, even DL-0 (implicitly, in the instant before the decision is made) |
| **Rejected** | The proposal was declined — no option was chosen, or the status quo was explicitly reaffirmed | Decision owner or escalation target | N/A — terminal state; still logged (see [Decision Logging](#decision-logging), "no-decision is a decision") |
| **Approved** | An option was chosen; execution has not yet started or is in progress | Decision owner (or Brain, if escalated) | Yes, for DL-0/DL-1 this can be near-instantaneous with Proposed |
| **Implemented** | The chosen option is live / in effect | Decision owner or delegated executor | No |
| **Reviewed** | The decision has reached its scheduled review date and outcome has been assessed against its success metrics | Decision owner, or Brain for DL-3/DL-4 | No — every Approved decision must eventually reach Reviewed or Superseded |
| **Superseded** | A later decision replaced this one before or after review | The later decision's owner, with a link back | N/A — terminal state |
| **Reopened** | A Reviewed decision's outcome diverged enough from its success metric to warrant re-deciding | Decision owner or Brain | Returns the decision to **Proposed** with a link to the prior record |

### Lifecycle rules

1. **No state may be skipped**, though DL-0/DL-1 decisions may pass through Proposed → Approved → Implemented in the time it takes to write one sentence.
2. **Rejected is not a lesser outcome than Approved.** A well-evidenced "no" is exactly as valuable a logged decision as a well-evidenced "yes" — see [Decision Quality Metrics](#decision-quality-metrics).
3. **A decision without a Reviewed or Superseded end-state after its review date is overdue** and appears on the Quarterly Decision Review agenda (Section 29) as an open item.
4. **Superseding requires a link both ways** — the new DR references the old one, and the old DR is updated to point forward. This preserves the precedent chain that makes the Register useful for pattern-matching (see [Why Every Decision Must Become Knowledge](01_WHY_ATLAS_EXISTS.md#why-every-decision-must-become-knowledge)).

### Lifecycle vs pipeline — the distinction

The **Lifecycle** (this section) is the small number of states a decision's record can be in. The **Pipeline** (Section 8) is the detailed sequence of *work* the owner does to get the record from one state to the next. Lifecycle is the state diagram; Pipeline is the flowchart inside the "Proposed" state.

### Allowed and forbidden transitions

| From | To | Allowed? | Notes |
|---|---|---|---|
| Proposed | Approved | Yes | Standard path |
| Proposed | Rejected | Yes | Standard path — a first-class outcome |
| Approved | Implemented | Yes | Standard path |
| Approved | Rejected | Yes, rarely | New evidence before execution starts reverses an approval; logged as an update to the same DR, not a new one |
| Implemented | Reviewed | Yes | Standard path |
| Implemented | Rejected | **No** | Once implemented, the correct next state after evaluation is Reviewed (even if the outcome was bad) or, if reversed, Superseded by a new DR that undoes it |
| Reviewed | Superseded | Yes | A later decision replaces this one |
| Reviewed | Reopened | Yes | Outcome diverged enough from the success metric to warrant re-deciding |
| Reopened | Proposed | Yes | Automatic — Reopened always routes back through the pipeline |
| Rejected | Proposed | Yes | A rejected proposal can be reframed and resubmitted as a new attempt, but gets a **new** DR ID, linked to the rejected one as precedent |
| Superseded | (any) | **No** | Terminal — a superseded decision is never reactivated; a new decision is made instead, referencing it |

### Timing constraints on transitions

| Transition | Maximum time allowed before it is "overdue" |
|---|---|
| Proposed → Approved/Rejected | Per Decision Level's pipeline depth (Section 8) — no hard ceiling, but a decision stuck here past its stated deadline (Frame stage) triggers the 48-hour blocked-decision escalation trigger ([Organization](03_ORGANIZATION.md#escalation-paths-by-trigger)) |
| Approved → Logged | Per the logging SLA (Section 23) — 24 hours for DL-2+ |
| Implemented → Reviewed | Per the decision's stated review date (Section 5's cadence table) |
| Reviewed/Rejected → (terminal, no further transition expected) | N/A |

### Why Rejected and Superseded are both terminal, and why that's different

A **Rejected** decision never happened — no option was chosen, the status quo continues. A **Superseded** decision *did* happen and was later replaced by a *different, later* decision. Conflating the two loses information a future reader needs: "we considered this and said no" (Rejected) is a different, equally valuable precedent from "we did this, and later did something else instead" (Superseded).

---

## Decision Pipeline

The Decision Pipeline expands Brain's five-step [Decision Framework](00_ATLAS_BRAIN.md#decision-framework) (Frame → Evidence → Options → Decide → Execute) into eleven concrete stages with named gates between them. Every decision moves through every stage; the *depth* of work at each stage scales with [Decision Level](#decision-levels).

### The eleven stages

```
1. Intake      →  2. Frame     →  3. Classify   →  4. Evidence
→  5. Options  →  6. Score     →  7. Decide     →  8. Approve
→  9. Log      →  10. Execute  →  11. Review
```

| # | Stage | Owner | Output | Gate to pass |
|---|---|---|---|---|
| 1 | **Intake** | Anyone who spots the decision point | A one-sentence problem statement and a proposed owner | Gate 0 |
| 2 | **Frame** | Decision owner | Brain's five framing questions answered (decision, deadline, owner, do-nothing cost, type) | Gate 1 |
| 3 | **Classify** | Decision owner | Decision Level (Section 5) + Class/sub-class (Section 6) + preliminary door-type guess (Section 18) | Gate 1 |
| 4 | **Evidence** | Decision owner (+ AI assist, Section 15) | Evidence checklist for the class satisfied (Section 11, [Appendix C](#appendix-c--evidence-checklists-by-class)) | Gate 2 |
| 5 | **Options** | Decision owner | At least two viable options with trade-offs stated (Brain requires this for any significant decision) | Gate 2 |
| 6 | **Score** | Decision owner (+ contributors via believability-weighted input) | Risk score + Opportunity score + criteria scoring per [Brain's scoring table](00_ATLAS_BRAIN.md#3-generate-and-evaluate-options) | Gate 3 |
| 7 | **Decide** | Decision owner | Chosen option, rejected-alternatives rationale | Gate 3 |
| 8 | **Approve** | Escalation target if above owner's authority band; otherwise owner self-approves | Signed-off DR at the correct authority level | Gate 4 |
| 9 | **Log** | Decision owner | Entry added to the [Decision Register](#decision-register) within the logging SLA | Gate 5 |
| 10 | **Execute** | Decision owner or delegated executor | Chosen option is implemented; status set to Implemented | Gate 5 |
| 11 | **Review** | Decision owner (Brain for DL-3/DL-4) | Outcome vs. success metric assessed; status set to Reviewed, Superseded, or Reopened | Gate 6 |

### Stage depth by level

| Stage | DL-0 | DL-1 | DL-2 | DL-3 | DL-4 |
|---|---|---|---|---|---|
| Intake–Frame | Implicit, seconds | One sentence | Written framing | Written framing + deadline stated | Written framing + Brain notified at intake |
| Classify | Skip (assumed DL-0) | Self-classified | Self-classified, spot-checked at review | Confirmed by escalation target | Confirmed by Brain |
| Evidence | None | Light — cite the SOP | Full checklist for class | Full checklist + precedent search in Register | Full checklist + precedent search + external validation if available |
| Options | Skip | One alternative named | ≥2 options with trade-offs | ≥2 options scored | ≥2 options scored + sensitivity check on top risk |
| Score | Skip | Skip | Full criteria table | Full criteria table + Risk/Opportunity scoring (Sections 12–13) | Full criteria table + Risk/Opportunity scoring + capital-at-risk stated |
| Decide/Approve | Owner decides silently | Owner decides, notes in status update | Owner decides, DR drafted | Escalation target approves | Brain approves; version bump if governance doc affected |
| Log | Optional one-liner | Short-form DR within 30 days if any commitment | Full DR within 24 hours of Approve | Full DR within 24 hours + Brain copy | Full DR within 24 hours + changelog entry on affected document |
| Review | None | If committed capital/spend, at 30 days | 30/90 days | 30/90/180 days | Quarterly until stable |

### Where AI participates in the pipeline

See [AI-Assisted Decisions](#ai-assisted-decisions) for full rules. In summary: AI may draft stages 2–6 (frame, classify, evidence-gather, options, score) as a **proposal** for the human owner to accept, edit, or reject. AI never executes stage 7 (Decide) or stage 8 (Approve) — those require a human owner or escalation target, always, regardless of AI maturity level elsewhere in the organization.

### Pipeline exits

A decision can exit the pipeline early at three points, and each exit is still a logged outcome:

| Exit point | Meaning | Resulting status |
|---|---|---|
| **Killed at Frame** | The problem dissolves, becomes moot, or is reassigned to a different owner/decision entirely | Not logged as a DR unless it was already at DL-2+ classification, in which case log as **Rejected** with reason "superseded by reframing" |
| **Killed at Evidence** | Evidence reveals the decision is premature (missing prerequisite) | Log as **Rejected** with reason "insufficient evidence — revisit by [date]" if DL-1+ |
| **Rejected at Decide/Approve** | The owner or escalation target explicitly declines every option, including the status quo option | Log as **Rejected** with full rationale — this is a first-class outcome, not a non-event |

### Pipeline compression for DL-0/DL-1

Nothing in this section requires a DL-0 decision to be written down stage by stage. The eleven stages describe the *thinking* that must happen, not eleven separate documents. For trivial and routine decisions, stages 1–8 can happen in a single sentence of internal reasoning; only stages 9 (log, if applicable) and 11 (review, if applicable) leave any artifact at all.

### Common failure at each stage

Naming the typical way a stage breaks down helps an owner recognize it in the moment rather than discover it only at postmortem.

| Stage | Common failure | Symptom |
|---|---|---|
| Intake | The decision point is never named at all | Something was clearly decided in retrospect, but no one can say when |
| Frame | The deadline or "do nothing" cost is left vague | "We should probably figure this out at some point" energy, no forcing function |
| Classify | Owner picks the level that matches the evidence they already have, rather than the level the decision actually warrants | Level matches convenience, not stakes |
| Evidence | Stopping as soon as evidence supports the preferred option | See [Bias Detection](#bias-detection), "evidence shopping" |
| Options | Only one real option plus a strawman | Gate 2 should catch this, but self-certification at DL-1/DL-2 can miss it without a second reviewer |
| Score | Scoring performed after the decision is already emotionally made, to justify it | Scores cluster suspiciously close to whatever supports the preferred option |
| Decide | Deciding without stating why the alternatives were rejected | Future reader cannot learn anything from the "why not" |
| Approve | Skipping escalation because the deadline is close | Directly the anti-pattern "escalation avoidance" (Section 31) |
| Log | Logging happens, but weeks late, after memory of the reasoning has faded | DR reads as reconstructed rationale, not contemporaneous reasoning |
| Execute | What gets executed quietly diverges from what was decided | No one updates the DR to reflect the divergence — the record becomes wrong |
| Review | Review date passes silently | Directly the anti-pattern "zombie decision" (Section 31) |

### Parallel vs sequential stages

Stages 4 (Evidence) and 5 (Options) are typically worked in parallel, not strictly sequentially — gathering evidence often generates new options, and generating options reveals what evidence is missing. The pipeline diagram presents them in sequence for clarity of gating, not to mandate a strict waterfall. What must be sequential is only the **gate order**: Gate 2 cannot pass without both Evidence and Options being satisfied together, regardless of which was finished first.

### Pipeline instrumentation

For DL-2+ decisions, the DR itself is the instrumentation — timestamps on Frame, Decide, Approve, and Log are recoverable from the Register's `Date` field plus the DR's own dated sections, which is what makes [Decision Quality Metrics](#decision-quality-metrics) like time-to-decision and time-to-log computable without a separate tracking system.

### Stage inputs and outputs

For clarity on exactly what feeds each stage and what it produces:

| Stage | Inputs | Outputs |
|---|---|---|
| 1. Intake | An observed problem, opportunity, or recurring pattern | Problem statement + proposed owner |
| 2. Frame | Problem statement | Deadline, owner, do-nothing cost, decision type — Brain's five framing questions answered |
| 3. Classify | Framing output | Decision Level, Class/sub-class, preliminary door-type guess |
| 4. Evidence | Classification + evidence checklist for the class | Populated Evidence section, precedent search results |
| 5. Options | Evidence + creative option generation | ≥2 options with stated trade-offs |
| 6. Score | Options + Risk/Opportunity rubrics | Populated scoring tables, headline risk rating, opportunity cost named |
| 7. Decide | Scored options | Chosen option + rejected-alternatives rationale |
| 8. Approve | Decision + authority-band check | Signed-off DR at the correct level, or an escalation packet if above the owner's band |
| 9. Log | Approved DR | New Register row + attached full DR content |
| 10. Execute | Logged, approved decision | Implemented change; `Status` updated |
| 11. Review | Implemented decision + elapsed time to review date | Outcome-vs-metric comparison; `Status` resolved to Reviewed/Superseded/Reopened; postmortem if required |

A stage that cannot produce its stated output has not actually completed — e.g., "Options" with only one entry has not produced a valid output for any DL-2+ decision, regardless of how much time was spent on it.

### The pipeline as a checklist, not a bureaucracy

It is worth restating plainly, because eleven named stages can *sound* heavier than they are in practice: for the overwhelming majority of Atlas's day-to-day decisions (DL-0 and DL-1, per [Decision Levels](#decision-levels)), running this pipeline takes less time than it took to read this section. The eleven stages exist to give the *rare*, *high-stakes* decision a complete, checkable structure — and the price of that structure is that trivial decisions get named stages that pass instantly, not that trivial decisions become slow. A useful mental model: the pipeline is a **staircase with a handrail on every step**, not a **maze**. Someone in a hurry can take the stairs two at a time; the handrail is there for the person carrying something heavy.

---

## Decision Templates

Every decision above DL-0 produces a written artifact. This section defines which template applies at which level; the templates themselves are reproduced in full in [Appendix A](#appendix-a--decision-record-template-canonical).

### Template tiers

| Tier | Applies to | Base | What it adds beyond Brain's minimum fields |
|---|---|---|---|
| **Micro-log** | DL-0 with any downstream effect worth a trace | A single line: date, one-sentence decision, owner | Nothing — this is the floor, not a template |
| **Short-form DR** | DL-1 | Brain's [minimum fields](00_ATLAS_BRAIN.md#documentation-standards): ID, date, owner, summary, options, chosen option + rationale, success metric, review date | Nothing structurally; may omit the scoring appendix |
| **Full DR** | DL-2, DL-3 | Short-form DR | Decision Level, Class/sub-class, Door type (Section 18), Evidence checklist reference, Risk score, Opportunity score, Escalation approval field, AI-assistance flag (Section 15) |
| **Full DR + Governance annex** | DL-4 | Full DR | Affected document(s), version bump plan, changelog entry draft, sunset/re-review date if a principle exception |

### Mandatory fields, all tiers above micro-log

These are Brain's [Decision Record minimum fields](00_ATLAS_BRAIN.md#documentation-standards), restated as the floor every tier must satisfy:

| Field | Required |
|---|---|
| Decision ID (`DR-YYYY-NNN`) | Yes |
| Date | Yes |
| Owner | Yes |
| Summary | Yes |
| Options considered | Yes |
| Chosen option + rationale | Yes |
| Success metrics | Yes |
| Review date | Yes |
| Escalation approval | Conditional — required whenever the decision exceeds the owner's own authority band |

### Fields this document adds for Full DR and above

| Field | Required from | Purpose |
|---|---|---|
| **Level** (DL-0…DL-4) | DL-2+ | Routes gate depth (Section 10) and review cadence (Section 5) |
| **Class / sub-class** | DL-2+ | Routes evidence checklist ([Appendix C](#appendix-c--evidence-checklists-by-class)) |
| **Door type** (one-way / two-way) | DL-2+ | Sets default rigor per [One-Way vs Two-Way Decisions](#one-way-vs-two-way-decisions) |
| **Risk score** | DL-3+ (optional at DL-2) | See [Risk Assessment](#risk-assessment) |
| **Opportunity score** | DL-3+ (optional at DL-2) | See [Opportunity Assessment](#opportunity-assessment) |
| **AI-assistance flag** | DL-1+ whenever AI materially contributed | See [AI-Assisted Decisions](#ai-assisted-decisions) |
| **Precedent check** | DL-2+ | Confirms the Register was searched for similar prior decisions before deciding |

### Where the canonical template lives

The full, fillable template — with every field, in order, ready to copy — is [Appendix A](#appendix-a--decision-record-template-canonical). Do not maintain a second copy of the template anywhere else; if a department needs a specialized variant (e.g., an M&A-specific due-diligence annex), it extends Appendix A via a documented addendum, it does not fork it.

### Template versioning

The template is itself governed by this document's [Versioning Policy](00_ATLAS_BRAIN.md#versioning-policy) inheritance — a change to the mandatory fields is a MAJOR change to this document (Section 35). Existing logged decisions are never retroactively reformatted; only new entries use the updated template.

### Field-by-field guidance

Guidance for the fields owners most often struggle to fill in well:

| Field | Weak version | Strong version |
|---|---|---|
| Summary | "Decide on the vendor situation" | "Choose between renewing Vendor X at increased price vs. switching to Vendor Y, given Vendor X's 40% price increase at renewal" |
| Options considered | "Option A: do it. Option B: don't." | Two or more options that a reasonable person could actually choose, each with a real trade-off, not a strawman built to lose |
| Chosen option + rationale | "Option A seemed better" | "Option A, because [specific evidence point] outweighs [specific risk], and Option B's [specific weakness] made it non-viable despite [its genuine strength]" |
| Success metrics | "It should go well" | "Support ticket volume for this workflow drops below 5/week within 30 days" — measurable, dated, falsifiable |
| Review date | Left blank, "later" | An actual calendar date, set at logging time, not deferred |
| Escalation approval | Left blank when escalation was actually required | Explicitly names the approver and date of approval, or explicitly states "N/A — within owner's own band" so the absence is a deliberate statement, not an oversight |

### Short-form DR — full example

For DL-1 decisions, here is a complete, filled short-form example (illustrative, tag `EX`, not a Register entry):

```markdown
## EX — Adopt weekly async status format for Projects updates

**Date:** 2026-08-08
**Owner:** Projects lead
**Status:** Approved
**Type:** Operational

### Summary
Switch weekly Projects status updates from a live meeting to a written async post, per Communication Principles' async-first default.

### Options considered
1. Keep the weekly live meeting.
2. Written async post, with an optional 15-minute call only if a blocker is flagged.

### Decision
Option 2 — the meeting has consistently been used for status reporting rather than discussion, which Communication Principles reserves meetings for.

### Success metrics
Meeting time spent on Projects status drops to zero within 2 weeks; blockers still get surfaced within 24 hours via the async post.

### Review date
2026-09-08
```

### When a template field genuinely does not apply

Every field in [Appendix A](#appendix-a--decision-record-template-canonical) should be addressed, but "addressed" can mean explicitly marking it not applicable with a one-clause reason (e.g., "Precedent: none found — first decision of this sub-class") rather than silently omitting it. A silently blank field is indistinguishable from a forgotten field; an explicitly marked "N/A, because..." is not.

### Template fields mapped to pipeline stages

For an owner assembling a DR incrementally as they move through the [Decision Pipeline](#decision-pipeline) rather than filling out the template in one sitting at the end, this shows which template section corresponds to which pipeline stage — so partial drafts are always coherent, not just complete-or-nothing:

| Template section | Populated during pipeline stage |
|---|---|
| Header fields (ID, Date, Owner, Status, Type) | Frame / Classify (stages 2–3) |
| Context | Frame (stage 2) |
| Evidence | Evidence (stage 4) |
| Options considered | Options (stage 5) |
| Risk score / Opportunity score | Score (stage 6) |
| Decision | Decide (stage 7) |
| Success metrics / Review date | Decide (stage 7), confirmed at Approve (stage 8) |
| Postmortem | Review (stage 11) — left blank until then, never pre-filled |
| Related documents / precedent | Evidence (stage 4), updated at Log (stage 9) if new links surface |

A DR that has its Postmortem section filled in before Review has happened is a sign the review process itself has been shortcut — see [Decision Anti-patterns](#decision-anti-patterns), "postmortem theater."

---

## Decision Gates

Gates are the checkpoints between pipeline stages (Section 8) that must be satisfied before work proceeds. A gate is not a meeting — it is a checklist. Most gates are self-certified by the owner at DL-0–DL-2; escalation targets and Brain certify gates at DL-3–DL-4.

### The seven gates

| Gate | Sits between stages | Pass criteria | Fails if |
|---|---|---|---|
| **Gate 0 — Worth deciding** | Intake → Frame | A real decision point exists with a clear "do nothing" alternative already identifiable | The problem is actually already decided, or is not yet actionable |
| **Gate 1 — Framed** | Frame/Classify → Evidence | Brain's five framing questions answered; Level and Class assigned | Any framing question is unanswerable — the decision is "not ready for evaluation" per [Brain](00_ATLAS_BRAIN.md#1-frame-the-decision) |
| **Gate 2 — Evidenced** | Evidence/Options → Score | Evidence checklist for the class satisfied; ≥2 options stated with trade-offs | Evidence is one-sided (see [Bias Detection](#bias-detection)) or fewer than 2 options exist for a DL-2+ decision |
| **Gate 3 — Scored & Decided** | Score/Decide → Approve | Criteria table complete; high-weight criteria (strategic fit, risk) are not scored 1 without an explicit override rationale (per [Brain](00_ATLAS_BRAIN.md#3-generate-and-evaluate-options)) | A veto-triggering score of 1 exists with no override rationale |
| **Gate 4 — Approved** | Approve → Log | Decision is within the deciding party's authority band, or has been escalated and approved at the correct band | A DL-2+ decision is approved by someone below the required authority band |
| **Gate 5 — Logged & Executing** | Log/Execute → Review | DR entered in the Register within the logging SLA (Section 23); execution has started | The decision sits "Approved" but unlogged past the SLA — this is itself an anti-pattern (Section 31) |
| **Gate 6 — Reviewed** | Review → close | Outcome compared to the stated success metric; status resolved to Reviewed, Superseded, or Reopened | The review date passes with no review performed — flagged automatically on the Quarterly Decision Review (Section 29) |

### Gate ownership by level

| Level | Who certifies Gates 0–3 | Who certifies Gate 4 (Approve) | Who certifies Gates 5–6 |
|---|---|---|---|
| DL-0 | Owner, implicitly | Owner, implicitly | N/A |
| DL-1 | Owner | Owner | Owner |
| DL-2 | Owner | Owner, or department head if cross-department | Owner |
| DL-3 | Owner | Escalation target (Brain + relevant department per [Organization](03_ORGANIZATION.md#default-owners-by-decision-type)) | Owner logs; Brain spot-checks at Quarterly Review |
| DL-4 | Owner | Brain | Owner logs; Brain certifies Gate 6 directly |

### Gates are sequential but not always slow

A gate can be passed in the same conversation it is opened — gates are about **completeness**, not elapsed time. A DL-2 decision with clean evidence already in hand can clear Gates 1–4 in under an hour. The gates exist to make sure nothing is skipped, not to impose a minimum duration.

### Gate failure is not punished — it is routed

Failing a gate returns the decision to the prior stage with the specific deficiency named (e.g., "Gate 2 failed: only one option considered — return to Options"). This is normal pipeline behavior, not an escalation-worthy event, unless the same gate fails repeatedly (see [Decision Anti-patterns](#decision-anti-patterns), "gate laundering").

### Gate failure examples

| Gate | Example failure | What "return to prior stage" looks like in practice |
|---|---|---|
| Gate 0 | Proposed decision is actually already settled by an existing SOP | Redirect to the SOP; no DR needed |
| Gate 1 | Deadline is "eventually," owner is "the team" | Owner names an actual date and an actual single name before proceeding |
| Gate 2 | Evidence section cites only sources favorable to the preferred option | Owner (or AI, prompted) adds at least one source or consideration against the leading option |
| Gate 3 | Strategic fit scored 1 with no override rationale | Owner writes the override rationale, or the option is dropped from consideration |
| Gate 4 | DL-3 decision approved by the owner alone, no escalation target signature | Route to the correct escalation target before Log |
| Gate 5 | Decision sits Approved for 5 days with no Register entry | Owner logs immediately; if the delay reveals a forgotten decision, mark it "logged retroactively" per [Decision Logging](#decision-logging) |
| Gate 6 | Review date passed two weeks ago, no postmortem started | Escalates automatically to the next [Quarterly Decision Review](#quarterly-decision-review) agenda |

### Who can waive a gate

No one. Gates are not waivable — they can only be passed, or the decision can be re-routed to a lower Decision Level if reclassification (Section 5) genuinely changes what's required. This is a deliberate design choice: a waivable gate is not a gate, it is a suggestion, and Atlas already tried the "suggestion" model before writing this document — see [Current Decision System](05_CURRENT_STATE.md#current-decision-system) on decisions made in substance without ever running the framework.

### Gates as a checklist, not a meeting

At Stage 0 and through early scale, gates are self-certified checklists the owner runs against their own DR, not synchronous review meetings. Meetings are reserved, per [Meeting standards](00_ATLAS_BRAIN.md#meeting-standards), for genuine discussion and decision — a gate check that always passes without discussion does not need a meeting; a gate check that reveals a real disagreement is exactly the kind of thing a meeting should be for.

---

## Required Evidence

Brain requires that "before options are evaluated, relevant data is collected" and that "decisions made without written support are provisional." This section makes that requirement checkable.

### Evidence categories

| Category | What it covers | Typical source |
|---|---|---|
| **Financial** | Projections, historical performance, unit economics, cash impact | Finance models, [Current Finance](05_CURRENT_STATE.md#current-finance) |
| **Market / competitive** | Market sizing, competitive positioning, timing | Knowledge research briefs, external data |
| **Operational feasibility** | Resourcing, capacity, dependencies, timeline realism | Operations, Projects intake criteria |
| **Principle alignment** | Fit against [Core Principles](00_ATLAS_BRAIN.md#core-principles) and [Founding Principles](02_FOUNDING_PRINCIPLES.md#atlas-core-principles) | Decision owner's own analysis, checked against [Decision Checklist](02_FOUNDING_PRINCIPLES.md#decision-checklist) |
| **Precedent** | Similar past decisions in the [Decision Register](#decision-register) and their outcomes | Register search (mandatory at DL-2+) |
| **Risk / downside** | Named failure scenarios, reversibility, capital at risk | [Risk Assessment](#risk-assessment) |
| **Opportunity / upside** | Expected value, leverage, optionality created | [Opportunity Assessment](#opportunity-assessment) |
| **Stakeholder input** | Believability-weighted contributor input, dissent captured | Written input per [believability-weighted input](03_ORGANIZATION.md#believability-weighted-input) |

### Evidence requirement matrix by level

| Level | Financial | Market | Operational | Principle | Precedent | Risk/Opportunity | Stakeholder |
|---|---|---|---|---|---|---|---|
| DL-0 | — | — | — | — | — | — | — |
| DL-1 | If spend involved | — | If capacity-constrained | Spot-check | Optional | Optional | — |
| DL-2 | Required if capital involved | Required if market-facing | Required | Required | Required | Required | Required from affected departments |
| DL-3 | Required | Required | Required | Required | Required, cited | Required, scored | Required, dissent logged if any |
| DL-4 | Required | Required | Required | Required, explicit | Required, cited | Required, scored | Required, Brain review |

Class-specific checklists that instantiate this matrix in detail are in [Appendix C](#appendix-c--evidence-checklists-by-class).

### The "no written support" default

Per [Brain](00_ATLAS_BRAIN.md#2-gather-evidence): decisions made without written evidence are **provisional** — they may be acted on under time pressure but must be backed with evidence within the logging SLA (Section 23) or explicitly reopened as under-evidenced. A provisional decision is flagged in the Register with `Status: Approved (provisional)` until evidence is attached.

### Evidence sufficiency, not evidence volume

More documents are not automatically better evidence. Evidence is sufficient when it would change the decision if it turned out to be wrong — i.e., it addresses the specific uncertainty the decision hinges on, not every conceivable fact about the topic. Gate 2 (Section 10) fails on **thinness or one-sidedness**, not on page count.

### Evidence and AI

AI agents may gather, summarize, and cite evidence (see [AI-Assisted Decisions](#ai-assisted-decisions)), but the decision owner is accountable for verifying that AI-sourced evidence is traceable to a real source, per [Data and security principles](00_ATLAS_BRAIN.md#data-and-security-principles): "AI outputs that inform decisions must be traceable to sources where feasible."

### Evidence quality bar — weak, medium, strong

Not all evidence that technically satisfies a checklist item is equally useful. A rough quality bar, by example, for the same evidence category:

| Category | Weak | Medium | Strong |
|---|---|---|---|
| Financial | "This should be profitable" | A rough back-of-envelope model with named assumptions | A sensitivity-tested model with a base/bear/bull case and named data sources |
| Market | "Competitors are also doing this" | A named list of 2–3 comparable companies and their approach | Named comparables plus a specific data point on market size or growth rate with a source |
| Precedent | "I don't remember us deciding anything like this before" | A quick Register keyword search, no hits found, noted as such | A full Register search with specific prior DR IDs cited, including any Rejected/Reopened ones that are relevant |
| Stakeholder input | Verbal "sounds good" from a colleague | A written Slack/doc comment from an affected department | Written input specifically addressing the decision's stated risk or trade-off, from someone with relevant believability |

Gate 2 does not require "Strong" evidence in every category for every decision — DL-2 can pass on solid Medium evidence throughout. DL-4 decisions should not pass Gate 2 with more than one category still at "Weak."

### Evidence decay

Evidence gathered long before Decide (stage 7) can go stale, especially market and financial evidence. For any decision where more than 60 days elapse between Evidence (stage 4) and Decide (stage 7), the owner briefly re-confirms the evidence is still current before proceeding — a one-line "re-confirmed as of [date]" note is sufficient if nothing material changed; a full re-gather is required if it did.

### What "traceable to sources where feasible" means in practice

For a DR's evidence citations, "traceable" means a future reader (human or AI) could locate the original source from the citation alone — a named document, URL, dataset, or person, not "general knowledge" or an unlinked paraphrase. Where a source genuinely cannot be produced (e.g., informal market color from a conversation), the DR states that explicitly rather than dressing up an unsourced claim as if it were documented.

### Evidence gathering responsibilities by department

Reflecting [Organization's department architecture](03_ORGANIZATION.md#department-architecture-overview), the typical source of each evidence category:

| Evidence category | Typical department source |
|---|---|
| Financial | Finance |
| Market / competitive | Knowledge (research briefs) |
| Operational feasibility | Operations |
| Principle alignment | Decision owner directly, checked against Brain/Founding Principles |
| Precedent | Knowledge (Register maintenance), searched directly by the owner |
| Risk / downside | Owner + relevant domain department (Finance for financial risk, AI for technical risk, etc.) |
| Opportunity / upside | Owner + Assets (for leverage assessment) |
| Stakeholder input | Whichever departments are affected, per [Organization's cross-department interaction matrix](03_ORGANIZATION.md#cross-department-interaction-matrix) |

An owner who cannot get timely input from the typical source department for a required evidence category treats that as a blocker subject to the standard 48-hour escalation trigger (Section 17) — evidence-gathering delays are a legitimate, common escalation reason, not something to route around by proceeding without the evidence.

---

## Risk Assessment

Brain's [Risk Assessment Matrix](00_ATLAS_BRAIN.md#risk-assessment-matrix) (Likelihood × Impact) is the holding-wide risk tool. This section is how that matrix is **applied inside a specific decision's scoring**, at the granularity a Full DR requires.

### Risk scoring inputs

Every DL-3+ decision (optional at DL-2) scores risk across the categories already defined in [Risk Management](00_ATLAS_BRAIN.md#risk-management):

| Category | Question for this decision | Score 1 (low) | Score 5 (high) |
|---|---|---|---|
| **Strategic** | Does this expose the portfolio direction to a competitive or market shift risk? | No exposure change | Materially increases exposure to a single thesis |
| **Financial** | What is the capital at risk relative to the relevant [capital bucket](00_ATLAS_BRAIN.md#capital-buckets)? | Trivial vs. bucket size | A material fraction of the bucket |
| **Operational** | Does this create a new single point of failure or key-person dependency? | None created | New critical dependency with no documented backup |
| **Technical** | Could this cause data loss, outage, or an AI error with downstream consequence? | Sandboxed / reversible | Production-critical, hard to roll back |
| **Compliance / legal** | Does this create regulatory, contractual, IP, or tax exposure? | None | New binding exposure |
| **Reputational** | Could this damage trust with partners, customers, or the public if it goes wrong? | Contained / internal | Public-facing, hard to walk back |

### Composite risk score

For each category, score **Likelihood** (1–5) and **Impact** (1–5) using [Brain's matrix](00_ATLAS_BRAIN.md#risk-assessment-matrix) bands (High/Medium/Low), take the highest-severity category as the decision's **headline risk rating**, and record all six category scores in the DR's scoring appendix (see [Appendix A](#appendix-a--decision-record-template-canonical)).

| Likelihood \ Impact | Low | Medium | High |
|---|---|---|---|
| **High** | Monitor | Mitigate | **Escalate to Brain** |
| **Medium** | Accept | Monitor | Mitigate |
| **Low** | Accept | Accept | Monitor |

Any category landing in "Escalate to Brain" or "Mitigate" **requires a written mitigation plan** in the DR before Gate 3 (Section 10) can pass — this is the decision-level enforcement of Brain's rule that "all Medium-Impact+ and High-Likelihood+ risks require documented mitigation plans."

### Capital-at-risk framing

For Investment-class and Capital Allocation decisions specifically (Section 14), the Financial risk category is expressed in three concrete terms in the DR:

1. **Absolute capital at risk** — the dollar amount that could be lost in the worst realistic scenario
2. **Relative capital at risk** — that amount as a percentage of the relevant [capital bucket](00_ATLAS_BRAIN.md#capital-buckets) (values for current bucket sizes live in [Current Finance](05_CURRENT_STATE.md#current-finance), not here)
3. **Recovery path** — what happens to the reserve/growth bucket allocation if the downside materializes

### Downside scenario requirement

Every DL-3+ decision states an explicit **worst-realistic-case** scenario in prose — not just a score. "What does failure look like, concretely, in 90 days?" is a mandatory prompt in the Full DR template. A risk score with no worst-case narrative fails Gate 2.

### Risk scoring and AI

AI may propose an initial risk score from precedent and stated facts (see [AI-Assisted Decisions](#ai-assisted-decisions)); the human owner must confirm or adjust every category score before Gate 3, and any AI-proposed score the human accepts unchanged is flagged for extra scrutiny at the Quarterly Decision Review (Section 29) as a bias-detection measure (see [Bias Detection](#bias-detection), "automation bias").

### Worked numeric example

To make the scoring mechanism concrete, consider a hypothetical DL-3 decision to adopt a new core financial system:

| Category | Likelihood (1–5) | Impact (1–5) | Cell | Action required |
|---|---|---|---|---|
| Strategic | 1 | 2 | Accept | None |
| Financial | 2 | 3 | Monitor | None beyond standard tracking |
| Operational | 4 | 3 | Mitigate | Written mitigation plan: parallel-run old and new system for 60 days before cutover |
| Technical | 3 | 4 | Mitigate | Written mitigation plan: full data-export test before migration; documented rollback procedure |
| Compliance/legal | 1 | 2 | Accept | None |
| Reputational | 2 | 2 | Accept | None |

**Headline risk rating:** Mitigate (from Operational and Technical, the two highest-severity categories). **Worst-realistic-case narrative:** "Migration data-integrity issue discovered after cutover, requiring a 1-week rollback to the old system and a manual reconciliation of the intervening period's transactions — costly in operator time, not existential, given the rollback procedure is pre-tested."

This decision passes Gate 2/3 because both Mitigate-cell categories carry a written mitigation plan; it would fail if either mitigation plan were missing.

### Risk score aggregation rule

The **headline risk rating** is always the single highest-severity cell across all six categories — never an average. A decision with five "Accept" categories and one "Escalate to Brain" category is an Escalate-to-Brain decision, full stop; averaging would hide the one category that actually matters. This mirrors how [Brain's own scoring guidance](00_ATLAS_BRAIN.md#3-generate-and-evaluate-options) treats high-weight criteria as veto filters rather than averaged inputs.

### Re-scoring after new evidence

If evidence gathered after an initial risk score changes a category's likelihood or impact by more than one point on either axis, the score is redone before Gate 3, not patched with a footnote. A category moving from Accept to Mitigate mid-pipeline is exactly the kind of change that should visibly re-open Gate 2/3, not be quietly absorbed.

---

## Opportunity Assessment

Risk without a matching upside framework produces an organization that only says no. Opportunity Assessment is the deliberate counterpart to [Risk Assessment](#risk-assessment) — it forces the same rigor onto the upside case that Atlas already demands of the downside case.

### Opportunity scoring inputs

Drawn from Brain's [option-scoring criteria](00_ATLAS_BRAIN.md#3-generate-and-evaluate-options):

| Criterion | Question for this decision | Score 1 (low) | Score 5 (high) |
|---|---|---|---|
| **Return potential** | What is the expected financial/non-financial upside over the stated horizon? | Marginal or unclear | Large, well-evidenced upside |
| **Operational leverage** | How much does Atlas's existing infrastructure (AI, systems, knowledge) amplify this outcome versus a standalone effort? | None — this is a one-off | High — existing systems make this disproportionately cheap or fast |
| **Time to impact** | How quickly does value show up? | Multi-year before any signal | Fast, visible signal |
| **Knowledge contribution** | Does this generate a reusable system, playbook, or precedent? | None | Directly extends the holding OS |
| **Optionality created** | Does choosing this option preserve or expand future choices? | Forecloses alternatives | Expands future paths |

### Composite opportunity score

Score each criterion 1–5 with brief justification, exactly as Brain's [scoring guidance](00_ATLAS_BRAIN.md#3-generate-and-evaluate-options) prescribes for the existing criteria table — Opportunity Assessment is not a separate process, it is the explicit expansion of the "Return potential," "Operational leverage," "Time to impact," and "Knowledge contribution" rows that table already contains, plus "Optionality created" as this document's addition.

### Expected value framing

For Investment-class decisions, state (even roughly):

```
Expected Value ≈ (P success × Upside) − (P failure × Downside) − Opportunity cost of capital/time
```

This is a **framing discipline**, not a demand for false precision — a rough order-of-magnitude estimate with stated assumptions is more useful than no estimate, and far more useful than an unstated one. The assumptions themselves are evidence and belong in the DR.

### Opportunity cost is mandatory, not optional

Per [Brain](00_ATLAS_BRAIN.md#3-generate-and-evaluate-options), Opportunity cost — "what else could this capital, time, or attention achieve?" — is a Medium-weight scoring criterion. This document elevates it to **mandatory** (not just scored) for every DL-2+ decision: the DR must name at least one concrete alternative use of the same capital/time, even if that alternative is "do nothing and preserve dry powder."

### Asymmetric bets

Atlas explicitly favors options with **capped downside and uncapped or large upside** — this is the natural intersection of [Risk Assessment](#risk-assessment) and this section. When an option shows this asymmetry, name it explicitly in the DR; it is a strong positive signal that should be visible to a future reader of the Register, not buried inside two separate numeric scores.

### Worked numeric example

Continuing the financial-system example from [Risk Assessment](#risk-assessment):

| Criterion | Score (1–5) | Justification |
|---|---|---|
| Return potential | 4 | Eliminates ~10 hours/month of manual reconciliation once live |
| Operational leverage | 5 | Directly reusable across every future portfolio company's onboarding — this is holding-OS infrastructure, not a one-off tool |
| Time to impact | 2 | Full benefit only realized after the 60-day parallel-run period and team ramp-up |
| Knowledge contribution | 4 | Produces a documented migration playbook reusable for future system changes |
| Optionality created | 3 | Modern system makes future integrations (AI-assisted reconciliation, real-time dashboards) easier; some vendor lock-in risk offsets this |

**Opportunity cost named:** "The same implementation time could instead go toward closing the AI/automation audit gap flagged in Current State — this decision is prioritized over that one because the financial system is a dependency for accurate reporting the automation audit would itself rely on."

**Asymmetry check:** Downside is capped (worst case: a costly but recoverable 1-week rollback, per the Risk Assessment worked example); upside compounds across every future portfolio company. This is flagged explicitly in the DR as a favorable asymmetric bet.

### Distinguishing genuine leverage from wishful leverage

"Operational leverage" (score of 4–5) is only justified when a *specific, named* future reuse is identified — not a generic claim that "this will help scale." The DR should name at least one concrete future use case (as the example above names "every future portfolio company's onboarding"). A leverage score with no named future use case fails Gate 2 for insufficient evidence.

### Opportunity scoring and AI

As with Risk scoring, AI may propose an initial Opportunity score from stated facts and precedent; the same override and flagging rules from [AI-Assisted Decisions](#ai-assisted-decisions) and [Risk Assessment](#risk-assessment)'s AI subsection apply symmetrically here.

---

## Capital Allocation

This section defines the **decision process** for capital-allocation decisions. It does not restate [Capital Allocation Philosophy](00_ATLAS_BRAIN.md#capital-allocation-philosophy) (the principles), [capital bucket](00_ATLAS_BRAIN.md#capital-buckets) definitions, or live bucket percentages and hurdle rates (which are instance data in [Current Finance](05_CURRENT_STATE.md#current-finance)).

### Capital decisions are Investment-class or Strategic-class

Per [Decision Classes](#decision-classes): deploying capital into an asset is Investment-class; changing *how* capital is allocated (bucket policy, hurdle rate changes) is Strategic-class. Both follow the full pipeline (Section 8) at DL-3 or DL-4.

### The capital decision sequence

1. **Frame against the bucket, not just the deal.** Every capital DR states which [capital bucket](00_ATLAS_BRAIN.md#capital-buckets) (Operating / Growth / Infrastructure / Reserve / Experimental) the capital draws from, before evaluating the opportunity itself.
2. **Test against the hurdle rate first.** An opportunity that does not clear the applicable hurdle rate (value from [Current Finance](05_CURRENT_STATE.md#current-finance)) does not proceed to full scoring — it is Rejected at Gate 2 unless a documented strategic override is logged (see below).
3. **Score Risk and Opportunity in full** (Sections 12–13), with capital-at-risk expressed in absolute and relative terms against the specific bucket.
4. **Check reserve adequacy.** Per [Preserve dry powder](00_ATLAS_BRAIN.md#capital-allocation-philosophy), confirm the Reserve bucket remains above its policy minimum after this deployment — if not, this becomes a DL-4 decision requiring Brain approval regardless of deal size.
5. **Compare against the build-vs-acquire framework** ([Brain](00_ATLAS_BRAIN.md#build-vs-acquire-framework)) when the capital decision is a new venture or acquisition.
6. **Approve at the correct band.** Per [Organization](03_ORGANIZATION.md#default-owners-by-decision-type): Finance head owns policy; Assets deal owner + Finance own individual deployments; Brain approves anything crossing the escalation thresholds in [Escalation Rules](#escalation-rules).
7. **Log with return-measurement metrics attached.** The DR's success metrics must use one of [Brain's return measurement](00_ATLAS_BRAIN.md#return-measurement) metrics (ROI, IRR, MOIC, unit economics, or holding ROIC) appropriate to the capital type — not a vague "it should go well."

### Hurdle rate override

A capital decision that fails the hurdle rate test may still proceed only if:

- The DR explicitly names the strategic (non-financial) rationale — e.g., knowledge gain, defensive positioning, optionality
- The rationale is scored honestly in [Opportunity Assessment](#opportunity-assessment) rather than used to bypass scoring entirely
- Brain approves the override regardless of the deploying department's authority band (this is always at least DL-3)
- The override is tagged in the Register so pattern-analysis (Section 26, Section 30) can track how often hurdle-rate overrides occur and whether they are earning their keep

### Cutting losers

Per [Cut losers honestly](00_ATLAS_BRAIN.md#capital-allocation-philosophy), a decision to exit or stop funding an asset uses the **same pipeline** as a new investment — it is not exempt from evidence or scoring merely because it "feels" like an easy call. Sunk cost is explicitly excluded as a valid entry in the Opportunity Assessment; if sunk cost appears in a DR's rationale, Gate 3 fails (see [Decision Anti-patterns](#decision-anti-patterns), "sunk-cost persistence").

### Reinvestment priority

Per [Reinvest compounding winners](00_ATLAS_BRAIN.md#capital-allocation-philosophy), when two capital decisions compete for the same limited bucket, the comparison itself is logged as a single DR naming both options — never two independent DRs that each unilaterally assume the capital is available.

### Worked capital decision walk-through

Illustrative, not a Register entry. Suppose Atlas has two live opportunities both drawing on the Growth bucket in the same quarter: a follow-on investment into an existing, performing portfolio company, and a new acquisition target.

1. **Frame against the bucket** — both explicitly state "draws from Growth bucket"; the DR notes the bucket cannot fund both in full this quarter.
2. **Hurdle rate test** — both are tested against the current hurdle rate (value from [Current Finance](05_CURRENT_STATE.md#current-finance)); suppose both clear it.
3. **Risk/Opportunity scoring** — the follow-on scores lower Risk (established track record, known team) and moderate Opportunity (steady, proven unit economics); the acquisition scores higher Risk (integration unknowns) and higher Opportunity (larger absolute return potential, new-sector optionality).
4. **Reserve adequacy check** — funding both in full would breach the Reserve bucket's policy minimum; funding either alone would not.
5. **Comparison, not two independent DRs** — a single DR frames this explicitly as "Growth bucket allocation: Follow-on vs. Acquisition vs. Split vs. Defer both," scores all four options, and picks one, with the rejected options' rationale stated (e.g., "full funding of both breaches Reserve policy; a 50/50 split undersizes both bets below their effective minimum viable check size").
6. **Approve at the correct band** — Brain approves given the Reserve-adequacy trigger makes this at least DL-4 regardless of either individual deal's size.
7. **Log with return metrics** — the DR states which [return measurement](00_ATLAS_BRAIN.md#return-measurement) metric applies to each funded option and the review cadence for each.

### Capital decisions and the milestone register

Capital decisions that fund a specific Roadmap milestone (see [Milestone Dependencies](04_ROADMAP.md#milestone-dependencies)) should cite the milestone ID in the DR's context section — this lets a future reader connect "why we spent this money" directly to "what strategic outcome it was funding," without needing to cross-reference two documents from memory.

### What this section does not decide

This section defines *process*. It does not set the hurdle rate, the bucket percentages, or the Reserve minimum — those are [Current Finance](05_CURRENT_STATE.md#current-finance) instance values, reviewed quarterly by Finance and Brain per [Brain's capital allocation philosophy](00_ATLAS_BRAIN.md#capital-buckets). A capital DR always cites the *current* values rather than restating them from memory, since they change on a cadence this document does not track.

---

## AI-Assisted Decisions

AI is core infrastructure at Atlas (see [AI Strategy](00_ATLAS_BRAIN.md#ai-strategy)), and the decision pipeline is one of the highest-leverage places for it to operate. This section defines exactly where AI helps, where it is capped, and what must always remain human.

### The governing rule

**AI may recommend at any stage. AI may decide at none.** This is the decision-specific instantiation of [Maintain human accountability](00_ATLAS_BRAIN.md#ai-strategy) and [Human accountability](02_FOUNDING_PRINCIPLES.md#human-accountability) as a principle: "AI recommends and executes within defined boundaries. Humans own outcomes, approve high-stakes actions, and handle exceptions."

### AI participation by pipeline stage

| Stage | AI may do | AI may never do |
|---|---|---|
| Intake | Flag a recurring pattern that looks like an undecided decision point | Decide the problem doesn't need a decision |
| Frame | Draft the five framing questions from context | Set the deadline unilaterally if it affects external parties |
| Classify | Propose a Decision Level and Class | Finalize the classification without human confirmation at DL-2+ |
| Evidence | Gather, summarize, and cite financial/market/operational/precedent evidence; search the Register for precedent | Fabricate or extrapolate evidence beyond traceable sources (see [Data and security principles](00_ATLAS_BRAIN.md#data-and-security-principles)) |
| Options | Draft candidate options, including ones a human may not have considered | Eliminate an option from consideration without flagging it as eliminated, with reasoning, for human review |
| Score | Propose Risk and Opportunity scores with justification | Finalize a score the human has not reviewed |
| Decide | Present a recommended option with rationale | Select the option |
| Approve | Draft the escalation packet ([Appendix F](#appendix-f--escalation-packet-template)) | Grant approval, at any authority band |
| Log | Draft the full DR in the canonical template format | Mark a decision Logged without human sign-off that the content is accurate |
| Execute | Carry out execution steps that are themselves already-approved automations (per [Automation Standards](00_ATLAS_BRAIN.md#automation-standards)) | Take an action that itself crosses an escalation threshold |
| Review | Draft the outcome-vs-metric comparison from available data | Decide whether to Reopen |

### AI decision-support maturity cap

Per [AI maturity model](00_ATLAS_BRAIN.md#ai-maturity-model), decision *support* is explicitly capped at **L2 — Supervised automation** for DL-2+ decisions, regardless of how mature AI tooling becomes elsewhere in the holding: AI may execute the routine steps of drafting, gathering, and scoring, but a human reviews every exception and every output before it moves to Approve. DL-0/DL-1 decisions may run at L3 (autonomous within guardrails) once a specific decision pattern has been proven stable, per the standard [AI adoption process](00_ATLAS_BRAIN.md#ai-adoption-process).

### The AI-assistance flag

Every DR (Full DR tier and above) carries an **AI-assistance flag** stating which stages AI materially contributed to. This is not a compliance formality — it is the input to the bias check on "automation bias" (Section 26) and lets the Quarterly Decision Review (Section 29) track AI's real contribution to decision quality over time, per [Measure AI ROI explicitly](00_ATLAS_BRAIN.md#ai-strategy).

### Guardrails specific to decision-support agents

Per [Agent design standards](00_ATLAS_BRAIN.md#agent-design-standards), any agent used in the decision pipeline must define its **Guardrails** field to explicitly exclude: approving decisions, closing escalations, or marking a DR as Logged without a named human sign-off. Its **Fallback** field must specify what happens when the agent is uncertain — the answer is always "surface to the human owner," never "proceed with best guess" for anything DL-2+.

### AI failure modes specific to decisions

| Failure mode | What it looks like | Mitigation |
|---|---|---|
| **Confident fabrication** | AI cites a source or precedent that does not actually exist or does not say what is claimed | Owner independently verifies any AI-cited source before Gate 2; per [Data and security principles](00_ATLAS_BRAIN.md#data-and-security-principles) |
| **Silent scope creep** | AI-drafted options quietly expand beyond what was actually framed at stage 2 | Owner re-reads the Frame stage output before accepting AI-drafted options |
| **Flattery drift** | AI's recommended option converges toward whatever the owner seemed to prefer in the framing conversation, rather than the strongest case | Occasionally prompt AI to argue explicitly for the option it did *not* recommend, as a check |
| **Precedent over-matching** | AI cites a Register precedent that is superficially similar but materially different in a way that matters | Owner confirms the precedent's actual facts match the current decision's material facts, not just its category label |
| **Score anchoring** | AI proposes a score first, and the human's "independent" review unconsciously anchors to it | For DL-4 decisions, consider having the human draft an initial score *before* seeing the AI's proposal, then compare |

### Suggested prompt pattern for decision-support agents

To operationalize Section 15's stage-by-stage participation table, a decision-support agent's system prompt should explicitly state: its current Decision Level cap (L2 for DL-2+), that it must present at least one option it does not itself recommend, that every evidence citation must be traceable, and that it must never write "Approved," "Logged," or set a `Status` field — only a human owner does that. This is guidance for building the agent, not a mandate that one currently exists; see [Current AI Capabilities](05_CURRENT_STATE.md#current-ai-capabilities) for what is actually deployed today.

### Illustrative AI-assisted drafting exchange

To make Section 15's abstract participation table concrete, here is what AI participation looks like in practice for a DL-2 Operational decision (illustrative, not a real transcript):

> **Owner:** "We need to decide whether to keep our current knowledge-base search tool or switch to a new one — draft the Frame and Evidence sections."
>
> **AI (drafts Frame):** States the decision, a 2-week deadline tied to the current tool's contract renewal, and the do-nothing cost (renewing at a 30% price increase).
>
> **AI (drafts Evidence):** Gathers the current tool's usage stats, the new tool's pricing and feature comparison, and searches the Register — finds no prior precedent, notes this explicitly rather than fabricating one.
>
> **AI (drafts Options):** Proposes three options: renew as-is, switch to the new tool, or negotiate the renewal price — and flags that it has not verified whether negotiation is realistic, recommending the owner confirm this with the vendor directly rather than treating it as settled.
>
> **Owner reviews:** Confirms the usage stats are accurate, adds one piece of context AI didn't have (a planned headcount increase that changes the cost comparison), and asks AI to re-score Opportunity with that update.
>
> **AI re-scores, owner decides:** The owner selects "negotiate the renewal price" after independently calling the vendor — a step AI could not take on its own — and writes the final rationale themselves, explicitly citing the negotiated outcome as the deciding evidence.
>
> **Owner approves and logs**, with the AI-assistance flag set to "Drafting, Evidence-gathering, Scoring" — accurately reflecting that AI touched three of the eleven pipeline stages, and that Decide, Approve, and Log were entirely human.

This example demonstrates the governing rule from Section 15 concretely: AI did real, load-bearing work at four stages, and the decision itself — the actual judgment call and the vendor negotiation that produced the winning evidence — remained entirely human.

### Measuring whether AI assistance is actually helping

Per [Measure AI ROI explicitly](00_ATLAS_BRAIN.md#ai-strategy), the AI-assistance flag (Section 9) exists specifically so [Decision Quality Metrics](#decision-quality-metrics) can compare hit rate, time-to-decision, and evidence completeness for AI-assisted versus non-AI-assisted decisions of comparable Level and Class. If AI-assisted decisions show a materially *lower* hit rate at comparable stakes, that is a trigger for a Failure Analysis (Section 27) on the AI participation pattern itself, not just on individual decisions.

---

## Human Override Rules

Every AI recommendation, score, or draft in the decision pipeline can be overridden by the accountable human owner. This section defines when override is silent, when it must be justified, and when it must be logged.

### The override hierarchy

| Situation | Override requires justification? | Override requires logging? |
|---|---|---|
| Human edits an AI-drafted frame, evidence summary, or option list before Gate 1/2 | No — this is normal collaborative drafting | No |
| Human rejects an AI-proposed Risk or Opportunity score | Yes — one sentence minimum | Yes, in the DR's scoring appendix, for DL-2+ |
| Human decides against an AI's recommended option | Yes | Yes — the rationale becomes part of "chosen option + rationale" |
| Human overrides an escalation-target's decision | Only Brain may do this, and only via a new DR that explicitly supersedes | Yes — full DR, classified Governance |
| Escalation target overrides the owner's recommended option | Yes | Yes — logged in the same DR, noting divergence from owner's recommendation |

### Why override is always available, never silent for AI

Per [Automation Standards](00_ATLAS_BRAIN.md#automation-design-principles): "Human override always available — any automation can be paused, bypassed, or corrected by its owner." Applied to decisions: a human can always override AI. The asymmetry is deliberate — AI overriding a human is never permitted at any stage, at any level, under any AI maturity setting.

### Overriding data-backed recommendations

When a human overrides a recommendation that was well-evidenced and well-scored (not just an AI draft, but a genuinely strong case), Gate 3 requires the override rationale to address the evidence directly — "I disagree" is insufficient; "the evidence didn't account for X, which changes the risk profile" is sufficient. This protects against **authority bias** (Section 26) quietly discarding good analysis.

### Overriding one's own past decision

Reopening a Reviewed decision (Section 7) is a form of self-override and follows the same rule: the new DR must state what changed (new evidence, changed circumstances, or a recognized error in the original scoring) — it cannot simply assert a different preference with no new information, or it fails Gate 2 for insufficient evidence.

### No override without accountability transfer

Overriding a decision does not remove the original owner's accountability for having framed and evidenced it; it adds the overriding party's accountability for the override itself. Both are visible in the Register (see [Decision Register](#decision-register) schema).

### Override frequency as a signal

A single override is normal — it is the framework working as intended. A *pattern* of the same escalation target overriding the same owner's recommendations repeatedly is a signal worth naming explicitly at the [Quarterly Decision Review](#quarterly-decision-review): it may indicate a miscalibrated authority band (the owner's decisions should be escalating earlier, or should not need to escalate at all), a systematic evidence gap in that owner's DRs, or a genuine, healthy difference in risk appetite that should be discussed directly rather than replayed decision-by-decision.

### Override and believability

An override does not by itself change anyone's believability (see [Organization](03_ORGANIZATION.md#believability-weighted-input)) — believability is earned by track record across many decisions, not assigned by a single override event. A postmortem (Section 28) that later shows the overridden recommendation would have performed better is the kind of evidence that should influence believability over time; the override itself is not.

### Overriding an AI recommendation never requires escalation

Because AI never holds decision authority (Section 15's governing rule), a human overriding an AI recommendation is always within the human's own existing authority band — it is not itself an escalation-triggering event, regardless of Decision Level. Contrast this with overriding another *human's* decision above the overrider's own band, which does require the authority (Brain, or the correct escalation target) to do so.

### Illustrative override, logged correctly

An AI decision-support agent, gathering evidence for a DL-2 vendor decision, scores Opportunity's "operational leverage" criterion at 4/5, citing the vendor's stated integration with Atlas's existing tools. The human owner, who has direct experience with a similar integration failing at a prior employer, overrides the score to 2/5.

**Logged override rationale (excerpt from the DR's scoring appendix):** "AI-proposed score of 4 assumed the vendor's stated integration works as documented; overriding to 2 based on first-hand experience that this specific integration pattern has a history of silent data-sync failures not visible in vendor documentation — recommend a technical spike to verify before fully committing, rather than trusting the vendor's claim at face value."

This is a correctly-logged override: it addresses the evidence directly (the vendor's documentation claim), states a concrete reason grounded in experience rather than a bare preference, and produces an actionable follow-up (the technical spike) rather than simply asserting a different number.

---

## Escalation Rules

Escalation moves a decision to the lowest authority level capable of resolving it. [Organization § Escalation Authority](03_ORGANIZATION.md#escalation-authority) defines organizational mechanics; this section defines when a **decision**, specifically, must escalate as it moves through the pipeline.

### Escalation triggers specific to decisions

| Trigger | Detected at pipeline stage | Escalates to |
|---|---|---|
| Decision Level reclassified upward mid-pipeline (Section 5) | Classify, or re-classify at Evidence | The authority band matching the new level |
| A high-weight scoring criterion (strategic fit, risk) scores 1 with no override rationale | Score (Gate 3) | Brain |
| Hurdle rate not cleared, no override logged | Score, for Capital Allocation decisions | Finance head → Brain if override requested |
| Risk category lands in "Escalate to Brain" cell of the [risk matrix](#risk-assessment) | Score | Brain |
| Decision would create or deepen a Reserve-bucket shortfall | Score, for Capital decisions | Brain (always DL-4, per [Capital Allocation](#capital-allocation)) |
| Decision requires a Founding or Core Principle exception | Frame or Score | Brain, per [Principle exception](00_ATLAS_BRAIN.md#escalation) |
| Decision affects 2+ departments and owners disagree on the chosen option | Decide | Brain arbitrates, per [Organization](03_ORGANIZATION.md#escalation-paths-by-trigger) |
| Owner is blocked past 48 hours on a decision they own | Any stage | Department head, then Brain if cross-department, per [Organization](03_ORGANIZATION.md#escalation-paths-by-trigger) |
| A decision is discovered to have been made and acted on without being logged | Log (post-hoc) | Brain — this is a process failure, handled per [Decision Anti-patterns](#decision-anti-patterns), not hidden |

### Escalation does not restart the pipeline

Escalating a decision transfers **Approve** authority (Gate 4) to the escalation target; it does not require the escalation target to redo Frame, Evidence, Options, or Score from scratch. The escalation target reviews the existing work product and either approves, sends it back for more evidence (Gate 2/3 failure), or overrides (Section 16).

### The escalation packet

Every escalation — decision-related or otherwise — uses [Organization's escalation packet requirements](03_ORGANIZATION.md#escalation-packet-requirements): problem statement, owner, options, recommendation, evidence, decision-needed-by date, and specific authority requested. For decisions, this packet **is** the DR at whatever stage it has reached; no separate escalation document is drafted. See [Appendix F](#appendix-f--escalation-packet-template).

### Escalation thresholds are instance data

The specific percentage/dollar/duration thresholds that trigger mandatory escalation (e.g., "> X% of deployable capital") are defined in type by [Brain](00_ATLAS_BRAIN.md#escalation) and [Organization](03_ORGANIZATION.md#default-brain-escalation-thresholds), and their **current numeric values** live in [Current Governance § Escalation thresholds — live values](05_CURRENT_STATE.md#current-governance). This document never states a specific number, because that number changes quarterly and this document does not.

### Escalating is correct behavior

Per [Organization](03_ORGANIZATION.md#escalation-is-not-failure): using an escalation trigger is the system working as designed. A decision owner who avoids escalation to "look decisive" has committed an anti-pattern (Section 31, "escalation avoidance"), not demonstrated leadership.

### Escalation SLA by trigger severity

| Severity | Example trigger | Response SLA |
|---|---|---|
| **Immediate** | Operational incident (severity 1); AI guardrail breach with external impact | Same day, per [Organization's escalation paths](03_ORGANIZATION.md#escalation-paths-by-trigger) |
| **Same-day** | Liquidity below policy; Reserve-bucket shortfall risk | Same day |
| **Before commitment** | New portfolio asset; irreversible contract; principle exception | Before the binding action is taken — never after |
| **Standard** | Blocked > 48 hours; ownership dispute | 48 hours to initiate; resolution timeline per [Organization](03_ORGANIZATION.md#escalation-paths-by-trigger) |

A decision-specific escalation (Section 17's triggers) inherits the severity of whatever underlying trigger fired — a hurdle-rate miss with no Reserve impact is Standard severity; the same miss compounded with a Reserve-adequacy breach is Same-day.

### De-escalation

Not every escalated item needs the full weight of the escalation target's continued attention once initial direction is given. A Brain-approved decision can be **de-escalated** back to the original owner for execution and logging, provided:

- The core decision (Decide/Approve, stages 7–8) is already resolved
- What remains is execution and routine logging, not further judgment calls
- The de-escalation is noted in the DR so a future reader understands why Brain's name appears at Approve but the owner's name appears at Execute/Log

De-escalation prevents the anti-pattern of every decision that ever touched Brain remaining "Brain's problem" indefinitely, which would quietly recreate the "management middleware" failure mode Atlas explicitly rejects (see [Why Software Is Replacing Management](01_WHY_ATLAS_EXISTS.md#why-software-is-replacing-management)).

### Escalation and the pipeline stages, precisely

To avoid ambiguity: escalation can be initiated at *any* pipeline stage (Section 8) the moment a trigger fires — an owner does not need to complete Evidence and Options before escalating a blocker. What changes is *what* is escalated: a blocker escalated at Frame carries only the framing; a blocker escalated at Score carries the full evidence and scoring work product completed so far.

### Illustrative escalation walkthrough

A department head (Operations) owns a decision to change a customer-facing SLA commitment. Midway through Evidence-gathering, it becomes clear this would also require a pricing change — which crosses into Finance's domain and carries reputational risk if communicated poorly.

1. **Trigger identified:** "Decision affects 2+ departments" (Section 17's trigger table) fires the moment the pricing implication surfaces — the owner does not wait until Score to notice this.
2. **Packet assembled:** Using [Appendix F](#appendix-f--escalation-packet-template), the owner states the problem, the two options considered so far, a recommendation (change the SLA and absorb the pricing impact short-term), the evidence gathered, a decision-needed-by date (before the next billing cycle), and the specific authority requested (Finance sign-off on the pricing impact; Brain awareness given reputational exposure).
3. **Escalation target responds:** Finance reviews the pricing evidence, either concurs with the owner's recommendation, requests more evidence (returning to Gate 2), or proposes an alternative.
4. **Resolution:** Say Finance concurs. The DR is updated with Finance's name in the `Escalation approval` field, and ownership of *execution* (stage 10) returns to the original Operations owner — a clean example of de-escalation (see above) once the judgment call itself is resolved.
5. **Logged:** Within 24 hours of Approve, per the standard SLA — the DR shows both the original owner and the escalation approver, with the full evidence trail intact.

---

## One-Way vs Two-Way Decisions

Atlas borrows reversible decision theory directly: [One-way vs two-way doors](00_ATLAS_BRAIN.md#one-way-vs-two-way-doors). This section makes the classification a **formal, repeatable test** rather than a judgment call made fresh each time.

### The classification test

Answer these four questions. Any "yes" defaults the decision to **one-way**:

1. **Cost to reverse** — Would undoing this cost more than 20% of the value at stake, in money, time, or relationships?
2. **Speed to reverse** — Would reversing take longer than the decision's own review window (Section 5)?
3. **External commitment** — Does this bind Atlas to a third party (contract, public statement, hire, brand) who did not agree to an easy unwind?
4. **Precedent lock-in** — Would reversing this contradict a pattern Atlas has now set for similar future decisions, creating a credibility cost beyond this one instance?

| Test result | Door type | Default authority | Default rigor |
|---|---|---|---|
| All four "no" | **Two-way** | Delegate to DL-0/DL-1 band (L0–L1) | Minimal — light DR if any at all |
| Any one "yes" | **One-way** | DL-3 minimum (L3) | Full pipeline, full evidence, Brain visibility |
| Genuinely uncertain | **Treat as one-way** | DL-3 minimum | Full pipeline until proven otherwise |

This directly implements [Organization's rule](03_ORGANIZATION.md#two-way-vs-one-way-doors): "When uncertain, treat as one-way."

### Door type is a DR field, not a footnote

Per [Decision Templates](#decision-templates), every Full DR states its door type explicitly. This is what allows the [Decision Register](#decision-register) to be filtered and pattern-matched later — "show me every one-way door decision from the last year" is a query the Register must support (see [Decision Quality Metrics](#decision-quality-metrics)).

### Reclassification

A decision initially framed as two-way can be reclassified one-way mid-pipeline if Evidence (stage 4) surfaces a fact that fails one of the four test questions — e.g., a vendor contract turns out to have a 24-month minimum term. This reclassification re-triggers the higher rigor level retroactively for the remaining stages; it never grandfathers the lighter path.

### Two-way doors used to move fast, deliberately

The entire point of correctly identifying two-way doors is **permission to move fast without guilt**. Per [Long-term thinking, in practice](00_ATLAS_BRAIN.md#long-term-thinking): "Reversible decisions are preferred over irreversible ones when upside is comparable." A decision owner who runs a full DL-3 pipeline on a genuinely two-way decision has wasted organizational time that should have gone to the actually-hard decisions — this is its own anti-pattern (Section 31, "over-classification drag").

### Extended examples table

| Decision | Cost to reverse | Speed to reverse | External commitment? | Precedent lock-in? | Door type |
|---|---|---|---|---|---|
| Try a new project-management tool, monthly plan | Low | Fast | No | No | Two-way |
| Sign a 3-year office lease | High | Slow | Yes | No | One-way |
| Publish a blog post under the Atlas name | Medium (retraction cost) | Fast to remove, slow to undo perception | Yes, public | Some | One-way (reputational) |
| Give a contractor a 2-week trial project | Low | Fast | Minimal | No | Two-way |
| Grant a customer an exclusive pricing arrangement | High | Slow, contractual | Yes | Yes (sets pattern for other customers) | One-way |
| A/B test a landing page headline | Low | Instant | No | No | Two-way |
| Rebrand the company name | Very high | Effectively never fully | Yes | Yes | One-way |
| Add a new field to an internal tracking spreadsheet | Low | Instant | No | No | Two-way |

### Borderline cases

Some decisions genuinely sit near the boundary and deserve explicit discussion rather than a confident snap classification:

- **A hire on a probationary/trial basis** — cheaper to reverse than a permanent hire, but still carries real human and reputational cost; Atlas treats this as one-way by default (per the canonical categories in [Irreversible Decisions](#irreversible-decisions)) even though the *contractual* reversal cost is lower than a typical one-way door.
- **A short-term vendor contract with an automatic renewal clause** — looks two-way at signing, becomes one-way if the renewal window is missed; the DR should flag the renewal date explicitly so it doesn't silently convert door types without anyone noticing.
- **A public beta launch with an "opt-in, no promises" framing** — the *product* decision may be two-way (easy to shut down), but the *relationship* decision (having told early users to trust you) carries a reputational one-way component worth naming separately.

When a decision is genuinely borderline, name both readings in the DR and default to the more conservative (one-way) classification per the standard rule, but do not let the borderline discussion itself become the anti-pattern "analysis paralysis" (Section 31) — the classification test has an explicit default for exactly this reason.

---

## Reversible Decisions

### Definition

A **reversible decision** (two-way door, per Section 18) can be undone at acceptable cost within its own review window. Reversibility is a property of the decision, not of the decision-maker's confidence.

### Default treatment

| Attribute | Default |
|---|---|
| Authority | Delegate down to the lowest capable owner (DL-0/DL-1) |
| Evidence | Light — cite the SOP or precedent; full evidence gathering is optional |
| Options | One alternative is enough; scoring table is optional |
| Approval | Self-approve within owner's own band |
| Logging | Optional at DL-0; short-form at DL-1 if any resource commitment |
| Review | Light-touch — a 30-day check-in is enough unless something breaks |

### Why Atlas defaults to speed here

Slowing down a genuinely reversible decision does not reduce risk — it only delays learning. Per [Action over perfection](02_FOUNDING_PRINCIPLES.md#action-over-perfection) and [Speed with rigor](00_ATLAS_BRAIN.md#speed-with-rigor), the rigor budget Atlas has is finite and should concentrate on decisions that are actually hard to undo.

### Examples of reversible decisions

- Adopting a new internal tool with a monthly (not annual) contract and no data lock-in
- A pricing experiment run on a subset of customers with an easy rollback
- Reassigning a project contributor for a sprint
- Testing a new AI agent in supervised (L1–L2) mode before wider rollout
- A short-term vendor trial below the department spend threshold

### When "reversible" is used to avoid rigor it doesn't deserve

If a decision is labeled reversible specifically to dodge the classification test in Section 18 rather than because it genuinely passes it, this is the anti-pattern "reversibility laundering" (Section 31). The four-question test exists precisely to prevent this rationalization.

### Speed benchmarks for reversible decisions

As a rough calibration, not a hard rule: a genuinely two-way DL-0 decision should be decidable in the time it takes to read this sentence twice. A two-way DL-1 decision with a real (if small) resource commitment should be decidable within a single working session — hours, not days. If a decision believed to be reversible is taking longer than that, either it is not actually as reversible as assumed (revisit Section 18's test) or the owner is over-gathering evidence for the stakes involved (revisit [Evidence sufficiency](#required-evidence)).

### Reversible decisions still deserve a review date

Even at the lightest end (DL-1 with any resource commitment), a review date exists. The point of a review on a reversible decision is not to catch a catastrophe — it's to build the habit of closing the loop, and to accumulate the kind of small, low-stakes hit-rate data that makes [Decision Quality Metrics](#decision-quality-metrics) meaningful in aggregate long before any DL-3+ decision has had time to mature to review.

---

## Irreversible Decisions

### Definition

An **irreversible decision** (one-way door, per Section 18) cannot be undone at acceptable cost, speed, or without external/precedent consequence. Per [Organization](03_ORGANIZATION.md#two-way-vs-one-way-doors): default authority is L3 minimum, and when uncertain, treat as irreversible.

### Default treatment

| Attribute | Default |
|---|---|
| Authority | DL-3 minimum (L3); DL-4 if it touches principles or governance documents |
| Evidence | Full — every category in [Required Evidence](#required-evidence) |
| Options | ≥2, fully scored per [Risk](#risk-assessment) and [Opportunity](#opportunity-assessment) Assessment |
| Approval | Escalation target or Brain; never self-approved below L3 |
| Logging | Full DR, logged within the SLA (Section 23), Brain notified |
| Review | Full cadence — 30/90/180 days, quarterly until stable for DL-4 |

### Canonical categories of irreversible decisions at Atlas

| Category | Why it's one-way | Cross-reference |
|---|---|---|
| Equity issuance or cap table change | Permanently dilutes/restructures ownership | [Capital Allocation](#capital-allocation) |
| Exclusivity or non-compete commitments | Forecloses future counterparties by contract | [Escalation](00_ATLAS_BRAIN.md#escalation) — "Contract > 12 months, exclusivity" |
| IP transfer or licensing-out of core IP | Cannot be un-transferred without a new negotiated deal | [Escalation](00_ATLAS_BRAIN.md#escalation) |
| Acquiring or divesting a portfolio asset | Deal costs, relationship costs, and reputational costs of reversal are high | [Company Lifecycle](00_ATLAS_BRAIN.md#company-lifecycle) |
| Hiring or separating a person | Reversal has real human and reputational cost regardless of legal reversibility | [Personnel class](#decision-classes) |
| Permanent data deletion | Cannot be undone by definition | [Data and security principles](00_ATLAS_BRAIN.md#data-and-security-principles) |
| Public commitments (press, investor, partner statements) | Retraction carries a credibility cost beyond the original claim | [Communication Principles](00_ATLAS_BRAIN.md#external-communication) |
| Entity formation, jurisdiction, legal structure | Expensive and slow to restructure | Flagged as open in [Current Infrastructure](05_CURRENT_STATE.md#current-infrastructure) |
| Founding/Core Principle exceptions | Sets precedent that erodes the principle for future decisions | [Principle exception](00_ATLAS_BRAIN.md#escalation) |
| T1/T2 governance document changes | Redefines the rules other decisions are judged against | [Versioning Policy](00_ATLAS_BRAIN.md#versioning-policy) |

### The "irreversible until proven otherwise" default

If the four-question test in Section 18 cannot be answered confidently, the decision is treated as irreversible **immediately**, without waiting for further analysis to confirm it. Downgrading from one-way to two-way requires positive evidence (a demonstrated cheap, fast, unwind path); upgrading requires none.

### Irreversible decisions still move fast — they just move deep

Full rigor does not mean slow by design. A well-evidenced DL-4 decision with clean data can still clear all seven gates (Section 10) in days, not months. What is non-negotiable is depth, not duration.

### A cooling-off pattern for high-stakes one-way doors

For DL-4 decisions with a high headline risk rating (Section 12), consider a deliberate cooling-off interval between Score (stage 6) and Decide (stage 7) — even 24–48 hours — specifically to let overconfidence and narrative-fallacy effects (Section 26) settle before committing. This is a recommended practice, not a mandatory gate: it should never be used as a stalling tactic on a decision that is genuinely ready and time-sensitive, and it never applies when the do-nothing cost (from Frame, stage 2) itself grows materially during the cooling-off window.

### Irreversible decisions and the Register's precedent value

Because one-way doors are, by definition, the decisions Atlas cannot cheaply undo, they are also the decisions where getting the *precedent search* right (Section 11) matters most — a prior one-way decision's postmortem (Section 28) is the highest-value input available for a new one-way decision in the same class. This is why [Decision Quality Metrics](#decision-quality-metrics)'s precedent reuse rate is tracked separately for one-way vs. two-way decisions: a low reuse rate on one-way doors specifically is a more urgent signal than a low reuse rate overall.

### Irreversibility is a spectrum in practice, a binary in classification

Some one-way doors are "somewhat" reversible at high cost (a bad hire can be separated, expensively) and some are truly absolute (permanently deleted data cannot be recovered at any cost). This document intentionally keeps the *classification* binary (Section 18) to keep the authority and rigor rules simple and enforceable, while the DR's worst-realistic-case narrative (Section 12) is where the actual *degree* of irreversibility gets captured in prose, for the humans who need that nuance.

### Side-by-side summary: reversible vs. irreversible

| Attribute | Reversible (two-way) | Irreversible (one-way) |
|---|---|---|
| Default Decision Level | Same as sizing test result, no adjustment | Sizing test result, minimum DL-3 |
| Default authority | Delegated down (L0–L1) | Escalated up (L3 minimum) |
| Evidence depth | Light, SOP-referenced | Full, every category |
| Options required | 1 alternative sufficient | ≥2, scored |
| Scoring | Optional | Mandatory (Risk + Opportunity) |
| Approval | Self | Escalation target or Brain |
| Logging | Optional to short-form | Full DR, SLA-bound |
| Review depth | Light 30-day check-in | Full 30/90/180-day or quarterly cadence |
| Postmortem | Not required | Required at DL-3+ |
| Speed default | Move fast, deliberately | Move deep, not necessarily slow |
| Default when uncertain | Never — uncertainty defaults to irreversible | Always the safe default |

This table is a **navigation aid**, not a new rule — every row traces back to a specific rule already stated in Sections 18–20 above.

---

## Delegation Rules

Authority can be delegated downward temporarily or permanently. This section defines how, so delegation strengthens the system instead of creating shadow authority.

### What can be delegated

| Delegable | Not delegable |
|---|---|
| Authority to decide within a named scope, up to the delegator's own band | Authority above the delegator's own band |
| Time-boxed authority (e.g., "L2 authority for vendor decisions under $X, for Q3") | Governance-level (L4) authority — Brain cannot delegate away principle-exception or T1-document authority |
| Approval authority (Gate 4) for a specific, named decision class | The delegator's own accountability for having delegated appropriately |
| Execution authority (stage 10) broadly and routinely | Log/Review certification for DL-3+ decisions (Gate 5/6 stay with Brain oversight even if execution is delegated) |

### Delegation record requirements

A delegation is itself logged — as a lightweight DR, Personnel/Governance class, containing:

| Field | Content |
|---|---|
| Delegator | Who is delegating |
| Delegate | Who receives the authority |
| Scope | Exact decision class/level the delegation covers |
| Duration | Start date and end date, or explicit "until revoked" |
| Revocation trigger | What automatically ends the delegation (date, event, or delegator's discretion) |
| Escalation path if delegate is unsure | Defaults to the delegator |

### Delegation cannot exceed the delegator's own authority

Per [Organization's authority bands](03_ORGANIZATION.md#authority-bands): a department head with L1 authority cannot delegate L2 authority to anyone, even temporarily. Attempting to do so is void, and any decision made under a void delegation is treated as unauthorized (Gate 4 failure, retroactively).

### Delegation is not abdication

The delegator remains accountable for the *quality* of the delegation itself — choosing an unprepared delegate, an unreasonably broad scope, or failing to define a revocation trigger is itself a decision the delegator owns and that can appear in a postmortem (Section 28) if things go wrong.

### Delegation at Stage 0

At Stage 0 (one operator holding every band — see [Current Organization](05_CURRENT_STATE.md#current-organization)), delegation mechanically has no target and therefore does not occur. This section exists now specifically so it is ready to use the moment a second operator or department head is named — see [Organizational Scaling](03_ORGANIZATION.md#organizational-scaling).

### Worked delegation examples

| Scenario | Valid delegation? | Why |
|---|---|---|
| Brain delegates all Operational-class DL-1 decisions to the Operations head, indefinitely | Yes | Within Brain's own authority; scope and duration ("indefinitely," revocable at will) are both stated |
| Operations head delegates DL-2 authority over vendor decisions to a contributor | No | Operations head holds L1, not L2 — cannot delegate above their own band |
| Finance head delegates hurdle-rate-override approval to Assets | No | Hurdle-rate overrides are always at least DL-3/Brain-adjacent per [Capital Allocation](#capital-allocation); Finance cannot delegate away a threshold that itself requires Brain |
| Brain delegates T1 document editing rights to Knowledge for typo-level, non-substantive fixes only | Yes, narrowly | Scope is explicitly limited to non-substantive changes, which per [Versioning Policy](00_ATLAS_BRAIN.md#versioning-policy) don't require a version bump or Brain approval regardless |
| A department head delegates their own decision authority to an AI agent | No | Never valid at any scope — see [AI-Assisted Decisions](#ai-assisted-decisions)'s governing rule; authority cannot be delegated to a non-human |

### Delegation vs. escalation — not the same direction

Delegation moves authority **down** the org for a defined scope, ahead of time. Escalation moves a specific decision **up** the org, in the moment, because it exceeds the current owner's authority. A well-functioning system uses both continuously and they are not substitutes: an over-delegated organization with no escalation discipline accumulates unauthorized decisions quietly; an under-delegated organization with heavy escalation discipline bottlenecks on whoever holds the highest bands.

### Revoking a delegation

Revocation is immediate and requires only the delegator's decision (logged as a lightweight update to the original delegation DR, not a fresh DR) — no cause needs to be proven, though stating one is good practice. Any decision the delegate made validly before revocation remains valid; decisions attempted after revocation are void per the same logic as decisions attempted above one's authority band.

---

## Ownership Rules

### The single-owner rule, applied to decisions

Every decision has exactly one **decision owner (DRI)**, per [Single Owner Principle](03_ORGANIZATION.md#single-owner-principle). This is true even when many people contribute evidence, scoring input, or dissent — see [Believability-weighted input](03_ORGANIZATION.md#believability-weighted-input).

### What the owner is accountable for

| Owner is accountable for | Owner is not accountable for |
|---|---|
| Correctly classifying the decision (Level, Class, Door type) | Guaranteeing the outcome — decisions are hypotheses (see [Decision Philosophy](#decision-philosophy)) |
| Gathering sufficient evidence and generating real options | Contributors' input being correct — only for weighing it appropriately |
| Choosing an option and documenting rationale | Escalation targets' final call once escalated |
| Logging within the SLA (Section 23) | Events outside the decision's stated scope |
| Scheduling and running the review (Section 28 if it becomes a postmortem) | Perfect foresight — only for honest postmortem participation |

### Ownership defaults when no one has claimed it

If a decision point is identified (Intake, stage 1) with no obvious owner, ownership defaults to the department head whose domain the decision most affects, per [Organization's default owners table](03_ORGANIZATION.md#default-owners-by-decision-type). If two departments have equal claim, Brain assigns ownership — this itself is a lightweight Governance-class decision.

### Ownership transfer

Ownership can transfer mid-pipeline (e.g., original owner leaves, or the decision is reclassified to a level outside the current owner's band). Transfer requires:

1. A one-line note in the DR: "Ownership transferred from X to Y on [date], reason: [reason]"
2. The new owner re-confirming (not necessarily redoing) the stages already passed
3. No loss of the original owner's contributed evidence or rationale — it stays attributed in the record

### Ownership across the decision's full life, not just at Decide

Ownership does not end at Approve. The same owner (or their confirmed successor, per the transfer process above) is accountable for Execute, Log, and Review — a decision owner who decides and then disappears until the review date, leaving execution and logging to whoever happens to pick it up, has not actually exercised ownership in the sense this section requires. If execution genuinely needs a different person (a common and healthy pattern — see the Roles table above, "Executor"), ownership of the *decision itself* still tracks back to one name, and that person remains accountable for confirming execution matched what was decided and for scheduling the review.

### Ownership is not co-ownership

"Co-owner" fields exist in Brain's default-owners table (e.g., "Finance (financial), Brain (strategic approval)") to describe **input and approval roles**, not shared decision authority. Exactly one name goes in the DR's `Owner` field. Everyone else is a contributor, an approver, or an escalation target — never a second owner. See [Decision Anti-patterns](#decision-anti-patterns), "committee ownership."

### Roles around a decision, precisely defined

| Role | Definition | How many per decision |
|---|---|---|
| **Owner (DRI)** | Accountable for the decision existing, being evidenced, and being logged and reviewed | Exactly 1 |
| **Contributor** | Provides evidence, scoring input, or domain expertise | 0 or more |
| **Approver / escalation target** | Holds the authority band the decision requires, if above the owner's own | 0 or 1 (only when escalation is required) |
| **Executor** | Carries out the chosen option, if different from the owner | 0 or more |
| **Reviewer** | Assesses outcome vs. success metric at the review date, if different from the owner (e.g., Brain for DL-3/DL-4) | 0 or 1 |

Only the **Owner** field is mandatory and singular in the DR. All other roles are named where relevant but never compete with the Owner field for the single-decision-maker slot.

### Ownership and the "who does the actual writing" question

The person who physically drafts the DR (which may be an AI agent, per [AI-Assisted Decisions](#ai-assisted-decisions)) is not thereby the owner. Ownership is about accountability for the judgment, not about who typed the document. An owner who has AI or a contributor draft the entire DR is still fully accountable for its accuracy and for the decision itself.

### What happens if the owner is unavailable at review time

If the named owner has left the role, the department head who now owns that domain inherits review responsibility, per the same default-assignment logic as an unclaimed decision (Section 22's "Ownership defaults" above). This is noted explicitly in the postmortem/review record so the change of reviewer is itself transparent.

---

## Decision Logging

### The core rule

Per [Communication Principles](00_ATLAS_BRAIN.md#internal-communication): "Write it down. Verbal agreements are provisional until documented." Applied to decisions: **a decision that is not logged has not, for organizational purposes, been made** — it exists only as an individual's private intention, which cannot be delegated against, audited, or learned from.

### Logging SLA by level

| Level | Logging deadline from Decide (stage 7) | Enforcement |
|---|---|---|
| DL-0 | No deadline — logging optional | N/A |
| DL-1 | Within 7 days if any resource/spend commitment exists | Self-enforced; spot-checked at Quarterly Review |
| DL-2 | Within 24 hours of Decide, per [Meeting standards](00_ATLAS_BRAIN.md#meeting-standards) ("decisions made in meetings are logged within 24 hours") | Flagged overdue at Quarterly Review |
| DL-3 | Within 24 hours; Brain notified at logging | Brain spot-checks; overdue items are a standing Quarterly Review agenda item |
| DL-4 | Within 24 hours; Brain notified at logging; changelog entry drafted same day | Brain certifies directly |

### What "logged" means, mechanically

A decision is logged when its DR (at the correct template tier, Section 9) is added as a row/entry in the [Decision Register](#decision-register) below, with a unique `DR-YYYY-NNN` identifier, `Status` set correctly per the [Lifecycle](#decision-lifecycle), and a `Review date` populated.

### No-decision is a decision

Explicitly choosing to do nothing, keep the status quo, or decline every option is logged exactly like an Approved decision — with `Status: Rejected` and the rationale for inaction. Undocumented inaction on a real decision point is treated identically to an undocumented action: provisional and non-existent for scaling purposes, per [Documentation before execution](00_ATLAS_BRAIN.md#documentation-before-execution).

### Retroactive logging

Decisions made before this framework existed, or made informally under time pressure, are logged retroactively with an explicit note: `Logged retroactively on [date]; decided on [approximate date]`. Retroactive logging is encouraged, not penalized — an incomplete Register is worse than a Register with honestly-dated retroactive entries. [Current State](05_CURRENT_STATE.md#current-decision-system) tracks the specific backlog of decisions awaiting retroactive logging (see [Appendix E — Decision Record Backlog](05_CURRENT_STATE.md#appendix-e--decision-record-backlog)) — this document does not restate that backlog, only the mechanism for clearing it.

### Logging is not the same as publicizing

Logging populates the Register, which is internal Knowledge-department infrastructure per [Knowledge Management](00_ATLAS_BRAIN.md#knowledge-management). Whether a decision's *existence* or *content* is communicated externally is governed separately by [External communication](00_ATLAS_BRAIN.md#external-communication) and does not block or delay logging.

### AI-assisted logging

AI may draft the DR entry in full (see [AI-Assisted Decisions](#ai-assisted-decisions)) from the pipeline artifacts already produced; a human owner must confirm accuracy before the entry is marked Logged. AI never marks its own draft as the canonical logged record.

### Where and how logging physically happens

Logging means two coordinated edits, done together:

1. A new row appended to the [Decision Register](#decision-register) table in this document (or, once the [Register scaling](#register-scaling-note) transition occurs, in the index file that replaces it)
2. The full DR content, using [Appendix A](#appendix-a--decision-record-template-canonical)'s template, stored either inline immediately below the Register or in the linked per-decision archive

Both edits happen in the same sitting — a Register row with no corresponding DR content is an incomplete log entry, not a valid one.

### What if the logging SLA is missed

A missed SLA is not itself a decision failure — it is a **process** failure, logged as such. The decision's `Status` remains whatever it actually is (Approved, Implemented) with a note: "Logged on [actual date], [N] days after the [24-hour/7-day] SLA." Repeated SLA misses by the same owner or department surface at the [Quarterly Decision Review](#quarterly-decision-review) as a process signal, not as a mark against any individual decision's substance.

### Logging channel

At Stage 0 and through early scale, this document itself (`06_DECISIONS.md`, specifically the Register in Section 24) is the sole logging channel — there is no separate database, ticketing system, or spreadsheet to keep in sync. This deliberately avoids the "logged in two places, agrees in neither" failure mode. If a future tool (see [Future Expansion](00_ATLAS_BRAIN.md#future-expansion), "Atlas OS platform") eventually implements the Register programmatically, that tool becomes the source of truth and this document's Register table becomes its rendered view — but that migration is itself a Technical-class, Governance-adjacent decision, logged like any other.

---

## Decision Register

The Decision Register is the literal, append-only log of every logged decision — the place every cross-reference in this document set means when it says "logged in `06_DECISIONS.md`." It lives in this section, directly below.

### Register schema

Every entry uses this row structure (expanded fields live in the linked DR itself, per [Appendix A](#appendix-a--decision-record-template-canonical)):

| Field | Description |
|---|---|
| **ID** | `DR-YYYY-NNN`, sequential within year |
| **Date** | Date decided (Gate 3/4) |
| **Title** | Short descriptive title |
| **Type** | Investment / Operational / Strategic / Personnel / Technical |
| **Level** | DL-0 through DL-4 |
| **Door** | One-way / Two-way |
| **Owner** | Single named DRI |
| **Status** | Proposed / Rejected / Approved / Implemented / Reviewed / Superseded / Reopened |
| **Review date** | Scheduled review |
| **Link** | Full DR reference (below the Register, or in a linked archive once the Register grows large) |

### ID assignment

IDs are assigned sequentially per calendar year, `DR-YYYY-NNN`, starting at `001` each January 1. The next available ID is always `(count of entries this year) + 1` — the decision owner checks the Register before assigning their own ID to avoid collisions, since Atlas has no central ID-issuing service at Stage 0.

### The live Register

The table below is the actual, current Register. New entries are appended chronologically by ID. Do not reorder, renumber, or delete past entries — corrections happen via a new entry that supersedes the old one (per [Decision Lifecycle](#decision-lifecycle)), never by editing history.

| ID | Date | Title | Type | Level | Door | Owner | Status | Review date | Link |
|---|---|---|---|---|---|---|---|---|---|
| DR-2026-001 | 2026-08-08 | Build full Brain governance set before operating activity | Strategic | DL-4 | One-way | Антон (Brain) | Approved | 2026-11-08 | [Full DR below](#dr-2026-001-build-full-brain-governance-set-before-operating-activity) |
| DR-2026-002 | 2026-08-08 | Approve Phase P0→P1 transition (Operating Kernel entry) | Strategic | DL-4 | One-way | Антон (Brain) | Approved | 2026-11-08 | [Full DR below](#dr-2026-002-approve-phase-p0p1-transition-operating-kernel-entry) |
| DR-2026-003 | 2026-08-09 | Adopt Brain-default "Irreversible commitment" escalation threshold for Finance | Operational | DL-1 | Two-way | Антон (Finance hat) | Approved | 2027-02-09 | [Full DR below](#dr-2026-003-adopt-brain-default-irreversible-commitment-escalation-threshold-for-finance) |
| DR-2026-004 | 2026-08-09 | Set temporary Phase 1 "Capital commitment" escalation threshold at 10% of deployable capital | Operational | DL-2 | Two-way | Антон (Brain + Finance hats) | Approved | 2026-11-09 | [Full DR below](#dr-2026-004-set-temporary-phase-1-capital-commitment-escalation-threshold-at-10-of-deployable-capital) |
| DR-2026-010 | 2026-08-12 | Atlas Capital Engine + Atlas Foundry direction | Strategic | DL-4 | One-way | Антон (Brain) | Approved (provisional) | 2026-11-12 | [Full DR below](#dr-2026-010-atlas-capital-engine--atlas-foundry-direction) |

**Current entry count: 5.**

### DR-2026-001: Build full Brain governance set before operating activity

**Date:** 2026-08-08
**Owner:** Антон (Brain Lead)
**Status:** Approved
**Type:** Strategic
**Sub-class:** Holding OS / governance substrate
**Level:** DL-4
**Door type:** One-way
**AI-assistance flag:** Drafting (Brain document set drafted with AI assistance under human review)
**Escalation approval:** N/A — within Brain band; self-approved at Stage 0

**Logged retroactively on 2026-08-08; decided in substance during August 2026.**

### Context

Should Atlas invest its first months in writing the full governance document set (Brain, Principles, Organization, Roadmap, Current State, Decisions framework, Glossary) before acquiring or building any revenue-generating asset? Deadline: soft — driven by founder bandwidth, not an external date. Do-nothing cost: begin sourcing deals/building immediately with no documented operating system.

### Evidence

- **Financial:** Opportunity cost of delayed deal sourcing — bounded by founder time; zero capital deployed.
- **Principle alignment:** Directly supported by [Documentation before execution](00_ATLAS_BRAIN.md#documentation-before-execution) and [Why Documentation Is Infrastructure](01_WHY_ATLAS_EXISTS.md#why-documentation-is-infrastructure).
- **Precedent:** Register search performed: no — this is the first entry.
- **Operational feasibility:** Single operator (Stage 0); all seven department hats worn by Brain lead.

### Options considered

1. **Full Brain set first, then source deals** — Encode identity, principles, organization, and roadmap before any operating activity.
2. **Source deals immediately, backfill documentation later** — Maximize speed to first asset; accept governance debt.
3. **Hybrid — minimum viable Brain set (Brain + Principles only), then parallelize** — Partial substrate with continued documentation.

### Risk score

| Category | Likelihood (1-5) | Impact (1-5) | Mitigation if Medium+ |
|---|---|---|---|
| Strategic | 2 | 2 | Monitor — delay to first asset is acceptable at zero capital |
| Financial | 3 | 2 | Monitor — time cost only, no capital at risk |
| Operational | 2 | 1 | Accept |
| Technical | 1 | 1 | Accept |
| Compliance/legal | 1 | 1 | Accept |
| Reputational | 1 | 1 | Accept |

**Worst-realistic-case narrative:** Months spent on documentation with no asset closed; mission drift into "docs as theater." Mitigated by explicit P0 exit criteria and Current State honesty discipline.

### Opportunity score

| Criterion | Score (1-5) | Justification |
|---|---|---|
| Return potential | 3 | Long-horizon holding OS compounding; no near-term revenue |
| Operational leverage | 5 | Entire document set becomes reusable infrastructure |
| Time to impact | 2 | Slow to first revenue |
| Knowledge contribution | 5 | This document set *is* the reusable system |
| Optionality created | 4 | Enables disciplined Build/Acquire/Operate decisions later |

**Opportunity cost named:** Founder time not spent on deal sourcing or venture building during the documentation period.

### Decision

**Option 1 chosen** — full Brain set first, then source deals. At zero capital deployed and zero portfolio companies, the cost of delay is time, not capital. [Founding Principles](02_FOUNDING_PRINCIPLES.md) rank documentation before execution when both compete for scarce founder attention at Stage 0.

### Success metrics

- P0.1–P0.9 exit criteria met by 2026-11-08 review date
- Brain document set 8/8 Active (`00`–`07`)
- ≥1 Decision Record logged in Register

### Review date

2026-11-08

### Related documents / precedent

- [Phase 0 — Brain Substrate](04_ROADMAP.md#phase-0--brain-substrate)
- [Current Strategic Position](05_CURRENT_STATE.md#current-strategic-position)
- Example walkthrough: [EX-1](#example-ex-1--strategic-dl-4-build-the-full-brain-document-set-before-any-operating-activity) (superseded by this entry for authoritative status)

### DR-2026-002: Approve Phase P0→P1 transition (Operating Kernel entry)

**Date:** 2026-08-08
**Owner:** Антон (Brain Lead)
**Status:** Approved
**Type:** Strategic
**Sub-class:** Governance / phase gate
**Level:** DL-4
**Door type:** One-way
**AI-assistance flag:** None
**Escalation approval:** N/A — Brain band; self-approved at Stage 0

### Context

P0 exit criteria are met or acceptably partial. Request formal approval to enter [Phase P1 — Operating Kernel](04_ROADMAP.md#phase-1--operating-kernel) per [Phase transition protocol](04_ROADMAP.md#phase-transition-protocol). Milestone M-G-007.

### Evidence — P0 exit criteria

| # | Criterion | Verdict | Evidence |
|---|---|---|---|
| P0.1–P0.6 | Brain docs 00–05 Active | ✅ Met | All Active |
| P0.7 | Decision log initialized | ✅ Met | DR-2026-001 logged |
| P0.8 | Glossary initialized | ✅ Met | v1.0, ~150 terms |
| P0.9 | Seven departments labeled | 🟡 Accepted partial | Dual-hat labeling in Current State; dept tracker deferred to P1 |

**CM-1 gate interpretation:** **Narrow reading adopted** — aggregate governance documentation is real and in active use (CM-1 "Docs real"); strict per-dimension CM-1 across all ten dimensions deferred — seven dimensions remain at CM-0 because underlying activity has not started, which is expected at Stage 0.

### Options considered

1. **Approve unconditional P1 entry** — Begin Operating Kernel work (playbooks, registry, project lifecycle).
2. **Stay in P0** — Require dept tracker and strict CM-1 before transition.
3. **Conditional approve** — P1 entry with mandatory playbook skeleton within 30 days.

### Risk score

| Category | Likelihood (1-5) | Impact (1-5) | Mitigation |
|---|---|---|---|
| Strategic | 2 | 3 | P1 exit criteria gate further work; quarterly review |
| Operational | 2 | 2 | Playbook skeleton ×7 is P1.1 exit criterion |

### Opportunity score

| Criterion | Score (1-5) | Justification |
|---|---|---|
| Operational leverage | 5 | Converts governance substrate into executable playbooks |
| Knowledge contribution | 4 | Phase transition sets precedent for future gates |
| Time to impact | 4 | P1 work can begin immediately |

### Decision

**Option 1 chosen** — approve unconditional P1 entry. P0.9 partial acceptance is explicit and documented; dept tagging tracker is first P1 deliverable, not a P0 blocker at Stage 0.

### Success metrics

- P1.1 (playbook skeleton ×7) started within 90 days
- M-G-007 marked Met in Current State
- Phase field updated to P1 in [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md)

### Review date

2026-11-08

### Related documents / precedent

- DR-2026-001
- [Phase 1 — Operating Kernel](04_ROADMAP.md#phase-1--operating-kernel)
- M-G-007

---

### DR-2026-003: Adopt Brain-default "Irreversible commitment" escalation threshold for Finance

**Date:** 2026-08-09
**Owner:** Антон (Finance hat)
**Status:** Approved
**Type:** Operational
**Level:** DL-1 — Routine
**Door:** Two-way

**Summary:**
Formally adopt, without modification, the existing Brain-default "Irreversible commitment" escalation trigger — "Contract > 12 months, exclusivity, IP transfer → Brain" ([`00_ATLAS_BRAIN.md` § Escalation](00_ATLAS_BRAIN.md#escalation)) — as Finance's live threshold value in [`05_CURRENT_STATE.md` § Current Governance](05_CURRENT_STATE.md#current-governance), replacing the current "TBD — no contracts exist" placeholder. No new numeric value is introduced; this decision only confirms Finance has not customized the default and will use it as-is, per Brain's own instruction to "customize per department" (or retain the default if no customization is made).

**Options considered:**
1. Leave the row TBD until a real contract exists to test it against.
2. Adopt the Brain-default threshold as-is now, without waiting for a real contract.
3. Set a Finance-specific customized threshold different from the Brain default (e.g., a shorter contract-length trigger).

**Decision:**
Option 2 — adopt the Brain-default as-is. Option 1 leaves this row unnecessarily unpublished despite the answer already existing canonically. Option 3 would require inventing a new number with no evidence basis to justify deviating from the default, contradicting [Truth over comfort](02_FOUNDING_PRINCIPLES.md#truth-over-comfort).

**Success metric:**
`05_CURRENT_STATE.md` § Current Governance's "Irreversible commitment" row shows a live, non-TBD value citing this DR; any future real contract review can be checked against it without further decision-making.

**Review date:** 2027-02-09 (aligned to the quarterly "Escalation threshold freshness" KPI, [`03_ORGANIZATION.md` § Department: Finance § KPIs](03_ORGANIZATION.md#department-finance)).

### Related documents / precedent

- [`00_ATLAS_BRAIN.md` § Escalation](00_ATLAS_BRAIN.md#escalation) — canonical default this decision adopts
- [Phase 1 exit criterion P1.7](04_ROADMAP.md#phase-1--operating-kernel) — this decision advances, but does not by itself satisfy, since Current State is not yet updated to reflect it
- `finance_playbook.md` § Execution guidance — the escalation threshold update procedure this decision is the first exercise of

---

### DR-2026-004: Set temporary Phase 1 "Capital commitment" escalation threshold at 10% of deployable capital

**Date:** 2026-08-09
**Owner:** Антон (Brain + Finance hats)
**Status:** Approved
**Type:** Operational
**Sub-class:** Governance / escalation threshold
**Level:** DL-2 — Significant
**Door type:** Two-way
**AI-assistance flag:** Yes — AI drafted the candidate options and comparative analysis; the numeric choice and approval are the human owner's
**Escalation approval:** N/A — Brain band; self-approved at Stage 0

### Context

[`00_ATLAS_BRAIN.md` § Escalation](00_ATLAS_BRAIN.md#escalation) defines the "Capital commitment" trigger as "> defined % of available deployable capital" but deliberately leaves the number unset (unlike the Irreversible commitment row, which had a concrete Brain default already adopted via `DR-2026-003`). This is the last unresolved row in [`05_CURRENT_STATE.md` § Current Governance § Escalation thresholds — live values](05_CURRENT_STATE.md#current-governance), and the sole remaining gap in [Phase 1 exit criterion P1.7](04_ROADMAP.md#phase-1--operating-kernel).

### Evidence

No real deployable-capital figure, revenue, or transaction history exists yet (per [`05_CURRENT_STATE.md` § Current Finance](05_CURRENT_STATE.md#current-finance)) — this decision is necessarily made from general capital-allocation and decision-governance principles already in canon ([Capital Efficiency](02_FOUNDING_PRINCIPLES.md#capital-efficiency), [Risk Management](00_ATLAS_BRAIN.md#risk-management), [Decision Levels sizing test](06_DECISIONS.md#decision-levels)), not from Atlas-specific financial data.

### Options considered

1. **5% of deployable capital** — most conservative; highest escalation frequency, lowest single-commitment exposure.
2. **10% of deployable capital** — low-moderate exposure; small experiments stay delegated; larger commitments still escalate.
3. **15% of deployable capital** — moderate autonomy; meaningfully larger single commitments could clear without Brain review.
4. **20% of deployable capital** — substantial autonomy; elevated single-commitment exposure.
5. **25% of deployable capital** — highest autonomy; highest single-commitment exposure before mandatory review.

### Risk score

| Category | Likelihood (1–5) | Impact (1–5) | Mitigation |
|---|---|---|---|
| Financial | 2 | 3 | Independent [Irreversible commitment rule](06_DECISIONS.md#dr-2026-003-adopt-brain-default-irreversible-commitment-escalation-threshold-for-finance) (`DR-2026-003`) still catches long-duration/exclusive/IP-transfer risk regardless of size; quarterly re-review cadence |
| Strategic | 2 | 2 | Explicitly temporary — see Review date; does not lock in a permanent policy without real evidence |

### Opportunity score

| Criterion | Score (1–5) | Justification |
|---|---|---|
| Operational leverage | 4 | Closes the last open row of P1.7 without waiting on real capital data |
| Knowledge contribution | 3 | Establishes a reusable, documented pattern for future threshold-setting decisions |
| Time to impact | 5 | Immediate — no dependency on any other unresolved Phase 1 item |

### Decision

**10% of deployable capital**, chosen over the more conservative 5% (which risks escalation fatigue on routine, well-understood small commitments) and the more permissive 15–25% options (which expose a materially larger share of capital to a single unreviewed judgment before any second review is forced) — appropriate specifically because, at [Org Stage 0](03_ORGANIZATION.md#stage-0-one-operator), escalating to Brain costs no real coordination friction (same person), so there is little reason not to lean conservative while zero track record exists.

**Explicitly a temporary Phase 1 default, not a permanent threshold.** It does not redefine "deployable capital" (still the capital-not-already-committed-or-reserved reading implicit in [`05_CURRENT_STATE.md` § Current Finance](05_CURRENT_STATE.md#current-finance)), and it does not modify, override, or interact conditionally with the Irreversible commitment rule — the two triggers remain fully independent; either can fire on its own.

### Success metrics

`05_CURRENT_STATE.md` § Current Governance's "Capital commitment" row shows a live 10% value citing this DR; [Phase 1 exit criterion P1.7](04_ROADMAP.md#phase-1--operating-kernel) evidence reaches 5 of 5 rows.

### Review date

2026-11-09 (aligned to the quarterly "Escalation threshold freshness" KPI), or sooner, at the first point a real deployable-capital figure exists — whichever comes first.

### Related documents / precedent

- `DR-2026-003` — the sibling decision this completes the escalation-threshold table alongside; kept fully independent per its own terms
- [`00_ATLAS_BRAIN.md` § Escalation](00_ATLAS_BRAIN.md#escalation) — canonical trigger type this decision sets a value for
- [Phase 1 exit criterion P1.7](04_ROADMAP.md#phase-1--operating-kernel) — the criterion this decision, once reflected in Current State, would fully satisfy

---

### DR-2026-010: Atlas Capital Engine + Atlas Foundry direction

**Date:** 2026-08-12
**Owner:** Антон (Brain Lead)
**Status:** Approved (provisional)
**Type:** Strategic
**Sub-class:** Holding direction / commercial sequencing / capability charter
**Level:** DL-4
**Door type:** One-way
**AI-assistance flag:** Yes — AI assisted drafting under Founder review; substance and approval are the Founder's
**Escalation approval:** N/A — Brain band; self-approved at Stage 0

### Context

Atlas has exited P0 and is in Phase P1 with governance substrate, Draft playbooks, an automation registry, and early project evidence — but still without external revenue, customers, production L2 automations, or a completed operating cycle. The Founder needs a clear near-term commercial direction that:

1. Prefers generating external capital through digital-first, remotely deliverable work before materially expanding compute or organizational complexity.
2. Names **Atlas Foundry** as a capability (not a new department) for converting validated problems into reusable AI-enabled products and delivery systems.
3. Keeps Founder personal capital conceptually distinct from Atlas-generated capital.
4. Avoids overbuilding departments, speculative infrastructure, or automation ahead of real workflow evidence.

This decision records strategic direction only. It does **not** complete P1.2 / P1.4 / P1.5, exit Phase 1, promote any automation maturity, create revenue, claim Foundry is already operational, or approve any listed AI Office as a shipped product.

### Evidence

- **Operating constraint:** Founder operates from Ukraine; early revenue strategy should avoid unnecessary dependency on local offline market structure, local relationship networks, or geography-bound operations when stronger international / digital opportunities are available. (Operating preference only — not a factual claim about Ukrainian businesses.)
- **Current State:** No customers, no revenue, no production L2 automations; Phase 1 exit = No; P1.2 / P1.4 / P1.5 remain Not Met.
- **Principle alignment:** [Simple before complex](02_FOUNDING_PRINCIPLES.md#simple-before-complex), [Capital efficiency](02_FOUNDING_PRINCIPLES.md#capital-efficiency), [Action over perfection](02_FOUNDING_PRINCIPLES.md#action-over-perfection), [Human accountability](02_FOUNDING_PRINCIPLES.md#human-accountability), [Evidence over opinion](02_FOUNDING_PRINCIPLES.md#evidence-over-opinion). (DL-4 Principle category — present; still subject to Brain re-confirmation at unconditional promotion.)
- **Precedent:** DR-2026-001 (governance before premature operating scale); DR-2026-002 (P1 entry without inventing maturity). Register search: no prior live DR defines Capital Engine / Foundry direction. (DL-4 Precedent category — present and cited.)
- **Risk / Opportunity:** Scored tables in this DR. (DL-4 Risk/Opportunity category — present as scored; still subject to re-confirmation when Financial/Market/Operational evidence is attached.)
- **Pending for unconditional Approved (mandatory DL-4 categories still unmet):** Per the [Evidence requirement matrix](#evidence-requirement-matrix-by-level), the following required DL-4 evidence categories remain **pending** and must be attached or validly resolved under existing governance rules before this DR may move from **Approved (provisional)** to unconditional **Approved**: **Financial**; **Market / competitive**; **Operational feasibility**; **Stakeholder input** (affected-department / Brain review input with any dissent logged). No Financial, Market, Operational, or Stakeholder evidence is invented here.

### Options considered

1. **Digital-first Capital Engine + Foundry-as-capability (chosen)** — Prefer remotely deliverable opportunities; earn reusable modules from real delivery; defer material compute/org expansion until economics justify it.
2. **Local / geography-bound first** — Prioritize nearby offline markets and relationship-heavy delivery before digital packaging.
3. **Infrastructure-first** — Expand servers / AI workstations / NAS / compute now so the architecture is “ready,” then find demand.
4. **Foundry-as-department now** — Create a new department and governance surface for Foundry before any paid external result.

### Risk score

| Category | Likelihood (1–5) | Impact (1–5) | Mitigation |
|---|---|---|---|
| Strategic | 3 | 3 | Explicit anti-overbuild rule; Foundry earned by real projects; review in ~90 days |
| Financial | 2 | 3 | Revenue-before-compute; distinguish Founder vs Atlas capital conceptually; no new legal/accounting rules invented here |
| Operational | 3 | 2 | Commercial sequencing loop; no major automation before understanding the real workflow |
| Technical | 2 | 2 | Human-control boundaries for high-stakes actions; AI Office examples are not products yet |
| Compliance/legal | 2 | 3 | Legal/Document AI Office must not claim independent final legal judgment or replace required professional responsibility |
| Reputational | 2 | 2 | Do not claim revenue, operational Foundry, or shipped AI Offices that do not exist |

### Opportunity score

| Criterion | Score (1–5) | Justification |
|---|---|---|
| Return potential | 4 | Path to external paid results and reusable product leverage |
| Operational leverage | 5 | ~80% reusable / ~20% customization design target compounds delivery speed |
| Time to impact | 3 | Requires real demand validation; not instant |
| Knowledge contribution | 4 | Creates a reusable commercial sequencing doctrine |
| Optionality created | 5 | Keeps digital/international paths open; avoids premature geography lock-in |

### Decision

**Option 1 chosen.** Atlas Lab’s near-term priority is to become capable of generating **external capital** through **digital-first, remotely deliverable** opportunities before materially expanding compute infrastructure or organizational complexity.

#### Atlas Foundry (capability, not department)

**Atlas Foundry** is established as a **capability**, not yet a standalone department. Its purpose is to convert validated opportunities and customer problems into reusable AI-enabled products and delivery systems.

Illustrative domains (examples only — not approved products):

- AI managers
- AI mini-offices
- research and analytics systems
- document-processing systems
- verification / review systems
- sales and lead-support systems
- workflow automation
- bots
- internal business tools
- small software products
- design/content production systems
- local/private AI deployments where appropriate

**Productization principle (design target, not a rigid formula):** approximately **80% reusable core** / **20% customer or domain customization**. The Foundry should progressively accumulate reusable modules so later client projects can be delivered faster, cheaper, and with more predictable quality.

#### First-wave strategy

Prefer digital-first and geographically flexible opportunities that can be developed and delivered remotely. Given the Founder’s Ukraine operating base, early revenue strategy should avoid unnecessary dependency on local offline market structure, local relationship networks, or geography-bound operations when stronger international / digital opportunities are available.

#### Revenue before compute

Do **not** materially expand into servers, AI workstations, NAS infrastructure, or other significant compute spending merely because the architecture could use it. Infrastructure expansion should follow demonstrated economic need, preferably funded from Atlas-generated revenue.

#### Commercial sequencing loop

1. Find an opportunity or painful workflow.
2. Research the market / user / company.
3. Define a measurable desired result.
4. Validate real demand.
5. Build the smallest useful prototype.
6. Seek a paid pilot or paid implementation.
7. Deliver initially manually or semi-manually where useful.
8. Measure customer value and economics.
9. Convert repeated delivery components into reusable Foundry modules.
10. Improve and scale only with evidence.

Do not build major automation before understanding the real workflow.

#### Capital distinction

Founder personal capital and Atlas-generated capital must remain **conceptually distinguishable**. Founder capital may fund carefully selected experiments. Revenue generated by Atlas becomes evidence of economic capability and may then be reinvested into further Atlas development. This decision does **not** create accounting rules or legal structures.

#### AI Office concept

Atlas intends to develop reusable **AI Office** foundations: configurable packages of AI roles, workflows, knowledge access, tools, controls, logging, and human approval boundaries designed around a real job or business function.

Potential examples (not approved products): Legal / Document AI Office; Research & Intelligence Office; Analytics Office; Sales / Lead Office; Operations Office; Content / Design Office.

A Legal / Document AI Office may assist with document review, transcription, audio analysis, information extraction, comparison, classification, summarization, and draft preparation. It must **not** be described as independently making final legal judgments or replacing required professional responsibility.

#### Human control (explicit)

Keep explicit human approval for:

- contracts
- pricing commitments
- payments and movement of capital
- external customer commitments
- legally consequential decisions
- access to sensitive customer data
- credentials / permissions
- irreversible actions
- production deployment where risk is material

Low-risk internal research, drafting, classification, testing, and analysis may progressively become more autonomous once controls are proven.

#### Anti-overbuild rule

This decision is **not** permission to create many new departments, governance frameworks, or speculative infrastructure. Atlas Foundry should be earned through real projects. Reusable components should normally be created because they were needed in a real experiment or delivery, not merely because they might become useful someday.

### Success metrics

- **Economic validation signal:** at least one external paid result generated through the commercial sequencing loop above.
- **Long-term goal (directional):** Atlas learns to discover opportunities, build digital assets/products, operate them, and compound the resulting capital — broader than client services alone.
- **Non-claims preserved:** does not by itself complete P1.2 / P1.4 / P1.5, exit Phase 1, promote automation maturity, invent revenue, declare Foundry operational, or ship any listed AI Office.

### Review date

2026-11-12 (≈90 days), or sooner upon first external paid result or any proposed material compute expansion.

### Related documents / precedent

- DR-2026-001 — governance substrate before premature operating scale
- DR-2026-002 — Phase P1 entry
- [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) — live Phase 1 / automation / project facts this direction must not contradict
- [`04_ROADMAP.md` § Phase 1](04_ROADMAP.md#phase-1--operating-kernel) — Phase 1 exit criteria remain independently evidenced
- P-001 / Market Screen artifacts — early opportunity screening context; do not treat as completed Capital Engine proof

---

### How to add an entry

1. Complete the pipeline (Section 8) through at least Gate 4 (Approve).
2. Assign the next sequential `DR-YYYY-NNN` ID.
3. Add a row to the table above with all ten fields populated.
4. Attach the full DR (using [Appendix A](#appendix-a--decision-record-template-canonical)) either inline below the Register table or in a linked decision archive file once this document's length makes inline storage impractical (see [Register scaling](#register-scaling-note) below).
5. Notify Brain if DL-3+ or if the decision sets a cross-department precedent.

### Register scaling note

At low entry counts, full DRs may be stored inline immediately below the Register table. As the count grows (expected around 50–100 entries, watch for this document approaching an unwieldy length), Brain should decide — and log, as a Governance-class DR — a transition to per-decision files under a `06_Decisions/` archive directory, with the Register table here retained as the searchable index. This transition is itself anticipated, not yet executed; see [Appendix H](#appendix-h--candidate-glossary-terms) and [Future Expansion](00_ATLAS_BRAIN.md#future-expansion) posture on infrastructure that scales without a rewrite.

### Register integrity

The Register is Knowledge-department infrastructure per [Knowledge architecture](00_ATLAS_BRAIN.md#knowledge-architecture). Its backup and redundancy approach is tracked as an open item in [Current Risks](05_CURRENT_STATE.md#current-risks) — this document defines the schema; Current State and Operations own the actual storage reliability.

### Register query patterns

The Register is designed to answer specific recurring questions. Even before it is populated, the schema (Section 24's field table) is chosen so these queries are mechanically answerable once entries exist:

| Question | How to answer it from the schema |
|---|---|
| What decisions are overdue for review? | Filter `Status` in {Approved, Implemented} where `Review date` < today |
| What has Atlas decided about vendor X before? | Text search `Title` and linked DR content for "vendor X"; check `Type = Operational` |
| How many one-way doors has Atlas committed to? | Filter `Door = One-way`, count by `Status` |
| Which decisions has Brain personally approved? | Filter `Level` in {DL-3, DL-4} |
| What's the reversal rate for Investment-class decisions? | Filter `Type = Investment`, compute (`Status = Reopened`) ÷ (`Status = Implemented` or later) |
| Has anything like this been decided before? (precedent search) | Text search `Title` and `Type`/sub-class combination, then read the linked DR's Evidence/Decision sections |

### Register as AI retrieval corpus

Per [Knowledge lifecycle § Surface](00_ATLAS_BRAIN.md#knowledge-lifecycle), the Register is designed to be a retrieval corpus for AI agents doing precedent search (Section 11) — which is why every field is structured (not free text) and every DR follows the identical template (Appendix A). An unstructured or inconsistently-formatted Register would be unfindable, and per [Knowledge Management](00_ATLAS_BRAIN.md#knowledge-management), "unfindable knowledge is lost knowledge."

### Interfaces with other Atlas systems

The Register does not operate in isolation — it is one node in the broader holding-OS nervous system described in [Knowledge architecture](00_ATLAS_BRAIN.md#knowledge-architecture). Its interfaces:

| System | Direction | Nature of the interface |
|---|---|---|
| [Current State](05_CURRENT_STATE.md) | Register → Current State | Current State's [Current Decision System](05_CURRENT_STATE.md#current-decision-system) and [Snapshot Dashboard](05_CURRENT_STATE.md#snapshot-dashboard) read entry counts and computed metrics from the Register; it never writes back |
| [Roadmap](04_ROADMAP.md) | Register ↔ Roadmap | Capital and Strategic decisions cite milestone IDs (per [Capital Allocation § Capital decisions and the milestone register](#capital-allocation)); Roadmap's Capability Maturity Model reads the Register's population and quality as a scoring input |
| Automation registry ([Automation Standards](00_ATLAS_BRAIN.md#automation-portfolio-review)) | Register ↔ Automation registry | Technical-class decisions that approve a new automation reference the resulting automation's entry in the AI department's registry, and vice versa |
| [Organization](03_ORGANIZATION.md) | Register → Organization | Ownership disputes and authority-band precedents resolved via a logged DR inform future application of [Decision Authority](03_ORGANIZATION.md#decision-authority) |
| Finance reporting ([Current Finance](05_CURRENT_STATE.md#current-finance)) | Register ↔ Finance reporting | Investment-class decisions' success metrics (ROI, IRR, MOIC) feed into portfolio-level return reporting; Finance's live hurdle rate and bucket figures feed into new Investment DRs |
| [`07_GLOSSARY.md`](07_GLOSSARY.md) | Register → Glossary | Postmortems and Quarterly Reviews surface new candidate terms (per [Appendix H](#appendix-h--candidate-glossary-terms)) for Glossary formalization |

None of these interfaces require new tooling to exist conceptually at Stage 0 — they describe how a human (or, later, an automated process) should read across documents by hand today, and what a future "Atlas OS platform" (per [Future Expansion](00_ATLAS_BRAIN.md#future-expansion)) would eventually automate.

---

## Decision Quality Metrics

Decisions are hypotheses (Section 3); hypotheses are only useful if their track record is measured. This section defines what Atlas measures about its own decision-making, distinct from measuring the outcomes of individual portfolio companies or projects.

### Core metrics

| Metric | Definition | Formula / Method | Target |
|---|---|---|---|
| **Time-to-decision** | Elapsed time from Frame (stage 2) to Decide (stage 7) | Date(Decide) − Date(Frame), by level | Faster for lower DL; no target for DL-3/4 beyond "not blocked past 48h without escalation" |
| **Time-to-log** | Elapsed time from Decide to Logged | Date(Logged) − Date(Decide) | Within SLA (Section 23) for ≥ 95% of DL-2+ decisions |
| **On-time review rate** | Share of decisions reviewed by their stated review date | (Reviewed on/before date) ÷ (Total due for review) | ≥ 90% |
| **Hit rate** | Share of decisions whose outcome met or exceeded the stated success metric | (Metric met) ÷ (Total reviewed) | Tracked, not targeted — a 100% hit rate signals under-ambitious bets, not skill (per [Failed hypotheses are celebrated](00_ATLAS_BRAIN.md#5-execute-measure-and-iterate)) |
| **Reversal rate** | Share of Implemented decisions later Reopened | (Reopened) ÷ (Implemented) | Tracked by Class and Level; a rising rate on DL-3+ triggers a Failure Analysis (Section 27) |
| **Escalation accuracy** | Share of escalated decisions that, in retrospect, genuinely needed escalation (vs. could have been resolved at the original level) | Qualitative tag at Quarterly Review | Directional — watch for systematic over- or under-escalation |
| **Evidence completeness** | Share of DL-2+ DRs with every Required Evidence category populated (Section 11) | Checklist completion at Gate 2 | 100% — this is a gate criterion, not an aspiration |
| **AI-assistance contribution** | Share of logged decisions where AI materially contributed (Section 15), and hit rate for that subset vs. the non-AI-assisted subset | Comparison at Quarterly/Annual Review | Directional — informs [Measure AI ROI explicitly](00_ATLAS_BRAIN.md#ai-strategy) |
| **Precedent reuse rate** | Share of DL-2+ decisions whose DR cites a prior Register entry as precedent | Presence of "Precedent check" field (Section 9) | Rising over time as the Register grows — near-zero is expected and correct at low Register counts |

### Why hit rate is tracked, not maximized

A decision framework optimized purely for a high hit rate systematically avoids the well-evidenced, asymmetric bets Atlas explicitly wants (Section 13, "asymmetric bets"). Brain reviews hit rate **alongside** the risk/opportunity scores the decision carried at the time — a low-probability, high-asymmetric-upside bet that failed exactly as its own scoring predicted is a successful use of this framework, even though its hit-rate contribution is negative.

### Where metrics are computed and reported

This document defines the metrics. Their **current computed values** are instance data and belong in [Current Decision System](05_CURRENT_STATE.md#current-decision-system) and the [Snapshot Dashboard](05_CURRENT_STATE.md#snapshot-dashboard), refreshed on the cadence defined in [Quarterly Decision Review](#quarterly-decision-review).

### Metrics feed the framework, not just the record

A metric trending badly (e.g., on-time review rate falling below 90%) is itself evidence that should produce a Governance-class decision to amend this document — e.g., shortening the logging SLA, adding an automated reminder, or simplifying the DL-1 template. Metrics are inputs to this document's own evolution (Section 35), not just a report card.

### Leading vs. lagging metrics

| Leading (predicts future quality) | Lagging (reports past outcomes) |
|---|---|
| Evidence completeness | Hit rate |
| Time-to-log | Reversal rate |
| Precedent reuse rate | Escalation accuracy (only knowable in retrospect) |
| Bias-checklist completion rate (Appendix D usage) | On-time review rate for decisions already past their date |

Brain weights leading metrics more heavily in the Quarterly Decision Review (Section 29), because they are actionable *now* — a lagging metric like hit rate on a DL-4 decision may not resolve for 180 days, by which point the leading indicators have already told the story about whether the decision was well-run.

### How metrics get gamed, and how to notice

| Metric | How it could be gamed | Detection |
|---|---|---|
| On-time review rate | Setting artificially short review windows that get trivially "reviewed" with a rubber-stamp | Annual Audit (Section 30) samples review content quality, not just timestamp presence |
| Hit rate | Setting deliberately easy, low-ambition success metrics | Cross-check success metrics against the Opportunity score at logging time — an ambitious Opportunity score paired with a trivial success metric is inconsistent |
| Evidence completeness | Checking every box with minimal, low-quality content just to pass Gate 2 | [Evidence quality bar](#required-evidence) spot-checked at Quarterly Review, not just checklist presence |
| Time-to-log | Logging a stub entry immediately, then never filling in the substantive DR content | Register scaling note's inline-DR requirement makes a stub visible immediately, not hidden behind a separate system |

Noticing a gamed metric is itself Failure Analysis input (Section 27) on the *framework*, not on the individual decision.

### Who owns collecting each metric

| Metric | Collection owner | Source |
|---|---|---|
| Time-to-decision, Time-to-log | Decision owner (self-reported via DR timestamps) | The DR itself |
| On-time review rate | Brain, at Quarterly Review | Register `Status` and `Review date` fields |
| Hit rate, Reversal rate | Decision owner at Review; aggregated by Brain | DR outcome sections + Register |
| Escalation accuracy | Brain, qualitative tag at Quarterly Review | Escalation packets + outcomes |
| Evidence completeness | Self-certified at Gate 2; spot-checked by Brain at Quarterly/Annual Review | DR Evidence section vs. Appendix C checklist |
| AI-assistance contribution | Decision owner (AI-assistance flag) + Brain (comparative analysis) | DR flag + Register filter |
| Precedent reuse rate | Brain, at Quarterly/Annual Review | DR precedent-check field, aggregated |

At Stage 0, all of these collapse to the same single person wearing every hat — the table exists so that as roles differentiate, collection responsibility differentiates cleanly with them rather than remaining vaguely "everyone's job."

### A minimum viable metrics dashboard

Once the Register has enough entries to be meaningful (a handful is enough to start), the minimum dashboard Brain should be able to produce at any time, without new tooling, is: open decisions past review date, decisions logged late this quarter, hit rate by Class, and reversal rate by Door type. This is exactly the [Snapshot Dashboard](05_CURRENT_STATE.md#snapshot-dashboard)'s decision-system section — this document defines what belongs on it; Current State reports the actual numbers.

### Sample calculation walkthrough (illustrative numbers, not real data)

To make the formulas in the Core metrics table concrete, suppose — purely hypothetically — a future quarter's Register contained 12 decisions reaching a review-eligible state, of which 10 were reviewed on time and 2 were overdue; of the 10 reviewed, 7 met their stated success metric and 3 did not; of the 3 that missed, 1 was later Reopened.

| Metric | Calculation | Result |
|---|---|---|
| On-time review rate | 10 ÷ 12 | 83% (below the 90% target — a Quarterly Review flag) |
| Hit rate | 7 ÷ 10 | 70% |
| Reversal rate | 1 ÷ 10 (of reviewed decisions that reached Implemented) | 10% |

The on-time review rate falling below target here is exactly the kind of trend that should generate a specific, named action item at the next Quarterly Decision Review (Section 29) — for example, checking whether the 2 overdue decisions share a common owner, department, or Decision Level, which would point to where the SLA is actually breaking down.

---

## Bias Detection

Evidence over opinion (see [Founding Principles](02_FOUNDING_PRINCIPLES.md#evidence-over-opinion)) fails quietly when the evidence itself is distorted by predictable cognitive biases. This section names the biases Atlas actively watches for and the mechanism that catches each one.

### Named biases and mitigations

| Bias | Definition | Detection signal | Mitigation |
|---|---|---|---|
| **Confirmation bias** | Evidence-gathering that seeks support rather than truth | Evidence section cites only sources favoring one option | Gate 2 explicitly requires evidence "for" and "against" the leading option; AI can be prompted to argue the opposing case |
| **Sunk-cost fallacy** | Continuing because of past investment rather than future value | Rationale references money/time already spent as a reason to continue | Explicitly excluded as valid evidence in [Capital Allocation](#capital-allocation) and [Opportunity Assessment](#opportunity-assessment) |
| **Anchoring** | Over-weighting the first number or option seen | Final decision matches the first-proposed option with no real comparison | Options stage (5) requires ≥2 genuinely distinct options before Score |
| **Overconfidence / optimism bias** | Systematically underestimating downside or overestimating probability of success | Risk score consistently low across many decisions from the same owner | [Risk Assessment](#risk-assessment) mandates a worst-realistic-case narrative, not just a number |
| **Groupthink / consensus bias** | Agreement substituting for evidence, especially under social pressure | No dissent recorded despite a cross-department decision with real stakes | [Believability-weighted input](03_ORGANIZATION.md#believability-weighted-input) requires written input, and dissent is explicitly loggable, not smoothed over |
| **Recency bias** | Over-weighting the most recent precedent or event | Precedent check cites only the most recent Register entry, ignoring older, more relevant ones | Precedent search (Section 11) is a Register-wide search, not "check the last one" |
| **Authority bias** | Deferring to a title rather than to evidence quality | A lower-believability input is discarded despite stronger evidence, with no rationale | [Human Override Rules](#human-override-rules) require the override rationale to address the evidence, not the org chart |
| **Automation bias** | Over-trusting an AI-generated score or recommendation without independent scrutiny | AI-proposed Risk/Opportunity score accepted unchanged, repeatedly, across many decisions | [AI-Assisted Decisions](#ai-assisted-decisions) flags unchanged AI scores for extra Quarterly Review scrutiny |
| **Narrative fallacy** | Constructing a compelling story that fits selected facts rather than testing against disconfirming ones | DR reads as persuasive prose with no explicit trade-off or rejected-alternative discussion | Brain's [option-scoring table](00_ATLAS_BRAIN.md#3-generate-and-evaluate-options) format forces structured comparison over narrative |
| **Survivorship bias** | Learning only from successful precedents; ignoring the Register's Rejected and failed entries | Precedent citations never reference Rejected or Reopened decisions | [Postmortem Process](#postmortem-process) and [Failure Analysis](#failure-analysis) explicitly mine failed decisions as first-class learning inputs |
| **Loss-aversion asymmetry** | Weighing a loss more heavily than an equivalent gain, distorting Risk vs. Opportunity comparison | Risk score dominates every decision regardless of Opportunity score magnitude | [Opportunity Assessment](#opportunity-assessment)'s asymmetric-bet framing exists specifically to counterweight this |

### Pre-mortem as a standing mitigation

For every DL-3+ decision, before Decide (stage 7), the owner runs a **pre-mortem**: assume the decision failed — write one paragraph on why. This single practice surfaces more of the biases above than any individual mitigation and is a mandatory Gate 3 input, not optional guidance.

### Bias detection is not personal criticism

Naming a bias in a DR or postmortem describes a pattern in the *decision*, not a character flaw in the *owner* — consistent with [Truth over comfort](02_FOUNDING_PRINCIPLES.md#truth-over-comfort) and the blameless posture of [Postmortem Process](#postmortem-process). Bias-flagging that becomes personal is itself an anti-pattern (Section 31).

### Bias interaction effects

Biases rarely occur in isolation, and some combinations are particularly dangerous:

- **Overconfidence + sunk cost** — a decision-maker who was confident at the outset is more likely to keep funding a failing bet rather than admit the initial confidence was miscalibrated. Watch for this specifically in [Capital Allocation](#capital-allocation)'s "cutting losers" cases.
- **Authority bias + groupthink** — once a senior figure states a preference, dissent quiets *and* the group converges, compounding a single-point error into an apparently unanimous one. Believability-weighted, written input (captured *before* a senior figure states their own view, where practical) mitigates this.
- **Automation bias + confirmation bias** — an AI recommendation that happens to match what the owner already wanted is far less likely to be scrutinized than one that surprises them. This is exactly why [AI-Assisted Decisions](#ai-assisted-decisions) asks AI to always present at least one option it does not itself recommend.

### A new bias worth naming: algorithmic aversion

The mirror image of automation bias — reflexively distrusting or discounting a correct AI-generated recommendation *because* it came from AI, even when its evidence and reasoning are sound. This is as much a distortion as over-trusting AI, and the same override-justification rule (Section 16: overriding a well-evidenced recommendation requires addressing the evidence, not just asserting disagreement) applies whether the recommendation came from a human or an AI.

### Debiasing checklist frequency

The full [Appendix D](#appendix-d--bias-self-audit-checklist) checklist is mandatory before Gate 3 for DL-3+ decisions (per Section 26's earlier text) and recommended, but not mandatory, for DL-2. Running it habitually even at DL-1 costs almost nothing and compounds into better calibration over time — this is a case where the marginal cost of extra rigor is low enough that erring toward more frequent use is reasonable.

### Illustrative bias caught in time

A DL-3 decision to expand into a new market is nearly ready for Decide (stage 7); the owner runs [Appendix D](#appendix-d--bias-self-audit-checklist) before Gate 3 as required. Question 1 ("Have I actively sought evidence that would argue against my leading option?") gives the owner pause — on reflection, every market-research source cited was found by searching for reasons the expansion would succeed, not by searching for reasons comparable expansions have failed elsewhere.

**Action taken:** The owner spends one additional hour specifically searching for failure cases of similar market expansions by comparable companies, finds two relevant cautionary examples, and adds them to the Evidence section with an updated Risk score reflecting a previously under-weighted operational risk (unfamiliarity with local regulatory requirements).

**Outcome:** The decision still proceeds — the additional evidence doesn't change the Decide outcome — but the DR now contains a documented mitigation plan for the regulatory risk that would otherwise have been discovered only after the fact. This is the checklist working exactly as intended: it did not block a good decision, it made a good decision more robust by surfacing a blind spot before it became a costly discovery during Execute.

---

## Failure Analysis

Failure Analysis is the structured process for understanding **why** a decision's outcome diverged from its stated success metric — feeding directly into the [Postmortem Process](#postmortem-process) below and into [Risk Management's incident response](00_ATLAS_BRAIN.md#incident-response) when the failure also constitutes an operational incident.

### Root-cause taxonomy

Every failed decision (Reviewed with metric missed, or Reopened) is classified into exactly one primary root cause:

| Root cause | Definition | Example |
|---|---|---|
| **Bad process** | The pipeline itself was skipped, compressed inappropriately, or gated incorrectly | A DL-3 decision was run at DL-1 rigor |
| **Bad information** | The evidence gathered was wrong, stale, or incomplete despite good-faith effort | Market data used was outdated by the time of execution |
| **Bad judgment** | Evidence and process were sound; the scoring or option selection itself was the weak link | Risk was correctly identified but under-weighted relative to Opportunity |
| **Bad execution** | The decision was well-made; implementation deviated from what was decided | Chosen vendor was correct; onboarding was executed poorly |
| **Bad luck** | Process, information, judgment, and execution were all sound; an unpredictable external event caused the miss | A well-evidenced, well-scored bet simply did not pay off — see [Decision Philosophy](#decision-philosophy) |
| **Wrong authority** | The decision was made at an authority band that should have escalated | An L1 owner made an irreversible commitment that should have been DL-3 |

### Why "bad luck" is a legitimate, first-class category

Per [Failed hypotheses are celebrated as information, not punished as mistakes](00_ATLAS_BRAIN.md#5-execute-measure-and-iterate): a correctly-run decision that fails due to genuine variance is evidence the framework is working as intended — it is not evidence the owner should have decided differently with the information available at the time. Conflating "bad luck" with "bad judgment" retroactively (see [Decision Anti-patterns](#decision-anti-patterns), "resulting") is explicitly rejected.

### Failure Analysis timeline

Mirrors [Risk Management's incident response](00_ATLAS_BRAIN.md#incident-response) timeline: root cause analysis is completed within **5 business days** of a decision reaching Reviewed status with its metric missed, or reaching Reopened status.

### Failure Analysis output

| Output | Destination |
|---|---|
| Root cause classification | Decision Register entry, `Status` remains Reviewed/Reopened with root-cause tag added |
| Any process gap identified | Feeds [Postmortem Process](#postmortem-process) if the decision is significant enough (DL-2+, or any decision with a notable divergence) |
| Any framework gap identified | Candidate item for the next [Quarterly Decision Review](#quarterly-decision-review) or, if urgent, an immediate Governance-class DR amending this document |
| Reusable heuristic | Captured in Knowledge per [Knowledge lifecycle](00_ATLAS_BRAIN.md#knowledge-lifecycle) — "Apply" stage |

### Failure severity tiers

Not every missed success metric deserves the same depth of Failure Analysis:

| Severity | Definition | Analysis depth |
|---|---|---|
| **Minor** | Missed by a small margin, no material harm, DL-0/DL-1 | A sentence in the review note; no formal root-cause classification required |
| **Moderate** | Missed materially, or DL-2, no external harm | Full root-cause classification (Section 27's taxonomy); no separate meeting required |
| **Severe** | DL-3+, or any harm to a third party, or a Reopened decision with real cost | Full root-cause classification plus a full [Postmortem](#postmortem-process) with attendees |
| **Critical** | Also constitutes an operational, financial, or reputational incident | Failure Analysis runs *alongside*, not instead of, [Risk Management's incident response](00_ATLAS_BRAIN.md#incident-response) — the two processes share the same 5-business-day root-cause timeline but serve different documents (this Register vs. an incident report in Knowledge) |

### When a decision failure is also an incident

A Critical-severity decision failure (e.g., a technical decision that caused an outage) triggers both processes simultaneously: [Risk Management's Contain → Communicate → Resolve → Analyze → Prevent → Record](00_ATLAS_BRAIN.md#incident-response) sequence handles the operational response, while this section's root-cause classification and the linked postmortem handle the decision-quality learning. The incident report and the DR's postmortem cross-reference each other rather than duplicating content.

### Distinguishing framework failure from decision failure

A Failure Analysis should explicitly ask: would a *correctly-run* version of this framework (right level, full evidence, honest scoring) have produced a different, better outcome? If yes, the root cause is process-related (Bad process, Bad information, or Wrong authority). If a correctly-run process would have made the same call with the same information, and it still failed, the root cause is Bad luck — and the framework itself gets no blame, per [Decision Philosophy](#decision-philosophy).

### Illustrative Failure Analysis

A DL-2 decision to adopt a new vendor for a core workflow is Reviewed at 90 days; the success metric (reduce processing time by 30%) was missed — actual improvement was only 8%.

**Root cause investigation:** The evidence at decision time (Gate 2) had correctly identified the vendor's claimed processing speed, sourced directly from vendor benchmarks — a "Medium" quality source per the [Evidence quality bar](#required-evidence), not independently verified against Atlas's actual data volume and format. The vendor's benchmark conditions turned out not to match Atlas's real usage pattern.

**Classification:** **Bad information** — the process was followed correctly (evidence was gathered, sourced, and cited), but the source itself was insufficiently rigorous for a claim this central to the decision's success metric. This is different from Bad luck (where correct information still leads to an unpredictable miss) and different from Bad judgment (where the evidence was fine but weighed incorrectly).

**Output:** The postmortem recommends an evidence-quality escalation rule — for Technical/Operational decisions where a vendor's own performance claim is the *primary* piece of evidence for the success metric, require either an independent benchmark or a time-boxed pilot before Gate 2 can pass at "Strong" rather than "Medium" quality. This becomes a candidate item for the next Quarterly Decision Review, and potentially a future amendment to [Appendix C](#appendix-c--evidence-checklists-by-class)'s Operational/Technical checklists.

---

## Postmortem Process

The Postmortem Process is the structured, blameless retrospective that turns a completed decision — successful or failed — into durable, reusable knowledge.

### When a postmortem is required

| Level | Postmortem required? |
|---|---|
| DL-0 | No |
| DL-1 | No, unless the outcome notably diverged from expectation |
| DL-2 | Lightweight postmortem (steps 1–4 below) at Review |
| DL-3 | Full postmortem at Review |
| DL-4 | Full postmortem at Review, attended by Brain |

### Postmortem steps

1. **Restate the original hypothesis** — the decision, its success metric, and its Risk/Opportunity scores as originally logged (never rewritten with hindsight).
2. **State the actual outcome** — measured against the same metric, using the same units.
3. **Run Failure Analysis if the metric was missed** (Section 27) — root cause classification.
4. **Ask what would change the decision next time** — not "was the person wrong," but "what evidence, gate, or process change would have produced a better decision with only the information available at the time."
5. **Extract reusable heuristics** — anything generalizable beyond this single decision, written for the Register's future precedent-search value.
6. **Flag candidate glossary terms or process changes** — anything discovered here that should update [`07_GLOSSARY.md`](07_GLOSSARY.md) or this document itself.
7. **Update the Register entry** — `Status` set to Reviewed (or Reopened, with a link to the new DR), postmortem summary attached.

### Blameless by design

Per [Truth over comfort](02_FOUNDING_PRINCIPLES.md#truth-over-comfort) and [Bad news fast](00_ATLAS_BRAIN.md#internal-communication): a postmortem investigates the **decision and the process**, never the person's character or effort. The output names root causes (Section 27's taxonomy), not culprits. A postmortem that assigns blame to an individual rather than a root-cause category has failed its own purpose regardless of how accurate its facts are.

### Postmortem timing

Aligned with [Brain's review cadences by decision size](00_ATLAS_BRAIN.md#5-execute-measure-and-iterate): postmortems run at the decision's scheduled review date(s) — 30 days (small), 90 days (medium), 30/90/180 days (large), quarterly until stable (strategic). A postmortem is never delayed waiting for a "better time" — the review date is the trigger, not a suggestion.

### Facilitation guidance

For DL-3/DL-4 postmortems run with more than one attendee, a facilitator (who may or may not be the decision owner) keeps the session anchored to the seven steps in order, specifically resisting two common derailments: re-litigating the original decision as if it could still be changed (it can't — the postmortem evaluates it, doesn't redo it), and drifting into unrelated grievances about the owner or department. A useful opening line: "We are here to make the *next* decision like this one better, not to re-decide this one."

### Common postmortem failure modes

| Failure mode | What it looks like | Fix |
|---|---|---|
| **The rubber-stamp postmortem** | "Metric was met, nothing to discuss" — even when it barely scraped by, or the win was due to an unrelated factor | Require the "what would change next time" step (4) even for decisions that hit their metric — success can still reveal a process gap that got lucky |
| **The blame-shifted postmortem** | Root cause quietly lands on "bad luck" by default, avoiding the harder categories | Facilitator explicitly checks whether a correctly-run process would have caught the issue before accepting "bad luck" |
| **The never-scheduled postmortem** | Review date passes with no postmortem convened at all | This is the "zombie decision" anti-pattern (Section 31), caught by the Quarterly Decision Review's overdue-items agenda item |
| **The over-long postmortem** | A DL-2 decision gets a two-hour retrospective meeting | Match facilitation depth to the "Postmortem required?" table above — lightweight for DL-2, full only for DL-3/DL-4 |

### The full template

See [Appendix E](#appendix-e--postmortem-template) for the fillable postmortem document.

---

## Quarterly Decision Review

Aligned with [Brain's quarterly cadence](00_ATLAS_BRAIN.md#continuous-improvement-as-a-system) ("Quarterly: Strategic review; principle and framework updates; threshold recalibration") and [Organization's T1 governance review cadence](03_ORGANIZATION.md#document-maintenance).

### Standing agenda

1. **Overdue items** — decisions past their review date with no Reviewed/Superseded status (Gate 6 failures); decisions Approved but unlogged past SLA (Gate 5 failures)
2. **Decision Quality Metrics trend** — the metrics in Section 25, compared quarter-over-quarter, sourced from [Current Decision System](05_CURRENT_STATE.md#current-decision-system)
3. **Bias pattern scan** — any bias from Section 26 appearing repeatedly across multiple decisions or a single owner
4. **Escalation threshold recalibration** — proposed changes to the numeric thresholds that live in [Current Governance](05_CURRENT_STATE.md#current-governance), based on the quarter's actual escalation volume and outcomes
5. **Anti-pattern scan** — any pattern from Section 31 observed this quarter, with a named fix owner
6. **Register health** — entry count, whether the [Register scaling note](#register-scaling-note) threshold is approaching, backup/redundancy status
7. **Open Governance-class proposals** — any pending amendments to this document itself

### Who attends

Brain always. Department heads attend when their department owned any DL-2+ decision that quarter. At Stage 0, this review is a structured solo exercise the single operator runs against themselves — still valuable, still logged, still on the calendar.

### Output

A short written summary (T5 record) filed in Knowledge, plus any resulting Governance-class DRs (threshold changes, framework amendments) logged in the Register per the normal pipeline. The Quarterly Decision Review does not itself decide anything outside its own agenda items — it is a review, not a shadow decision-making body (see [Decision Anti-patterns](#decision-anti-patterns), "review as backdoor decision").

### Relationship to other quarterly reviews

This review is one of several quarterly cadences defined across the Brain document set (Brain-level strategic review, Organization review checklist, Risk review, Roadmap phase-gate check). Where practical, run them in the same cycle to avoid a proliferation of separate quarterly meetings — see [Meeting standards](00_ATLAS_BRAIN.md#meeting-standards).

### Suggested time allocation

For a review covering a meaningful quarter of activity (illustrative split, adjust to actual volume):

| Agenda item | Share of session time |
|---|---|
| Overdue items | 15% |
| Metrics trend | 20% |
| Bias pattern scan | 15% |
| Escalation threshold recalibration | 15% |
| Anti-pattern scan | 15% |
| Register health | 10% |
| Open Governance proposals | 10% |

### Inputs required before the review starts

To avoid the review itself becoming a data-gathering exercise (which belongs in stage 4 of the pipeline, not in a review meeting), the following should exist *before* the session: an exported or filtered view of the Register for the quarter, the current [Decision Quality Metrics](#decision-quality-metrics) values from [Current State](05_CURRENT_STATE.md#current-decision-system), and any postmortems completed that quarter. Assembling these is itself a small Operational-class task that can be delegated or automated as Atlas scales.

### What "good" looks like at this review, by maturity stage

| Maturity | What a healthy Quarterly Decision Review looks like |
|---|---|
| Stage 0 (pre-Register) | A structured check that the framework itself is understood and ready; no metrics yet to review — see [Current State](05_CURRENT_STATE.md#current-decision-system) |
| Early Register (few entries) | Mostly a calibration exercise — checking that logged entries actually use the template correctly, more than trend analysis |
| Mature Register | Genuine trend analysis across the metrics in Section 25, with specific, named framework amendments proposed when trends warrant it |

---

## Annual Decision Audit

A deeper, once-a-year pass that the Quarterly Decision Review (Section 29) is not designed to catch — patterns visible only at a full-year timescale, and a meta-review of whether the framework itself still fits Atlas's current scale.

### Audit scope

| Area | Question the audit answers |
|---|---|
| **Compliance sampling** | Of a random sample of the year's logged decisions, what fraction fully satisfied their required gates and evidence at the time? |
| **Logging completeness** | What fraction of decisions later discovered to have been made (via other documents, e.g. Current State's retroactive-logging backlog) were ever logged at all? |
| **Bias trend over the year** | Which biases from Section 26 recurred most, and did the quarterly mitigations actually reduce them? |
| **Metric trend over the year** | Full-year trend on every metric in Section 25 — not just quarter-over-quarter noise |
| **Framework fit** | Has Atlas's scale (headcount, capital, portfolio size, per [Current Organizational Maturity](05_CURRENT_STATE.md#current-organizational-maturity)) outgrown any mechanism in this document — e.g., does the Register need the archive-file transition noted in [Register scaling](#register-scaling-note)? |
| **Precedent value realized** | Are decision owners actually citing the Register for precedent (Section 25's precedent reuse rate), or is the corpus going unused? |
| **Escalation calibration over the year** | Full-year view of escalation accuracy — systematic over/under-escalation invisible at quarterly granularity |

### Audit process

1. Brain (or a designated auditor, once that role exists) samples decisions per the compliance sampling method above.
2. Findings are compared against the prior year's audit (once one exists) to detect drift, not just point-in-time state.
3. Findings that indicate a framework gap become Governance-class DRs — potentially a MAJOR version bump to this document (Section 35).
4. Findings that indicate a principle-level tension are routed to the next [Founding Principles review](02_FOUNDING_PRINCIPLES.md#principle-evolution).
5. Findings that indicate a maturity gap update the relevant [Capability Maturity](04_ROADMAP.md#capability-maturity-model) dimension score in Current State.

### Output

A written annual audit report (T5 record), archived in Knowledge, referenced by the next year's Roadmap and Founding Principles reviews. The audit's own findings are themselves subject to this document's pipeline if they propose a decision (e.g., "raise the logging SLA from 24 to 48 hours") — an audit finding is evidence, not an automatic mandate.

### First audit

Atlas's first Annual Decision Audit cannot run meaningfully until at least one full year of Register data exists. Until then, this section defines the *method*; [Current State](05_CURRENT_STATE.md#current-decision-system) tracks whether the precondition (a populated Register spanning a year) has been met.

### Audit sampling method, in more detail

Once a meaningful Register exists, a workable sampling approach: pull every DL-3/DL-4 decision from the year (small numbers are expected early on, so this may be a full census rather than a true sample), plus a random sample of roughly 20% of DL-2 decisions, plus a spot-check of 5–10% of DL-1 decisions with any resource commitment attached. For each sampled decision, verify: was the assigned Level consistent with the sizing test given the facts at the time; was the required evidence checklist actually satisfied, not just checked; was the logging SLA met; and was the review actually completed with a genuine outcome comparison rather than a rubber stamp. This sampling depth scales naturally — a Register with thousands of entries would use a smaller sampling percentage; a Register with a handful of entries, as expected in Atlas's first audited year, may as well review all of them.

### Audit report structure

A written annual audit report follows this shape:

```markdown
# Annual Decision Audit — [Year]

## Summary
[One paragraph: overall health of the decision system this year]

## Compliance sampling results
[Sample size, methodology, % fully compliant with gates/evidence at the time]

## Year-over-year metric trends
[Table: each Decision Quality Metric, this year vs. last year]

## Bias trend analysis
[Which biases recurred most; whether quarterly mitigations reduced them]

## Framework fit assessment
[Has Atlas outgrown any mechanism? Register scaling, new decision classes needed, etc.]

## Precedent value assessment
[Is the Register actually being used for precedent search?]

## Findings and recommendations
1. [Finding] → [Recommended action] → [Proposed DR if applicable]
2. ...

## Sign-off
Brain, [date]
```

### How this audit differs from a financial audit

This is not a financial or compliance audit in the accounting sense — no external auditor, no attestation, no regulatory requirement (unless one is later imposed by an investor or regulator, at which point that requirement is layered on top, not substituted). It is an internal quality audit of Atlas's own judgment infrastructure, owned entirely by Brain, in the same spirit as [Risk Management's annual comprehensive risk audit](00_ATLAS_BRAIN.md#risk-review-cadence).

### Quarterly Review vs. Annual Audit — the distinction

Both cadences examine the same underlying Register, but at different resolutions and for different purposes:

| Dimension | Quarterly Decision Review | Annual Decision Audit |
|---|---|---|
| Primary question | "Are we keeping up with the process this quarter?" | "Is the process itself still the right one?" |
| Timescale examined | The quarter just completed | The full year, compared to prior years once they exist |
| Depth | Checklist-driven, agenda-timeboxed | Sampling-based, deeper investigation |
| Typical output | Overdue items resolved, thresholds tuned | Framework amendments, version bumps |
| Attendance | Brain + relevant department heads | Brain (+ designated auditor once that role exists) |
| Relationship to this document's own versioning | Rarely triggers a version bump directly | The primary mechanism by which this document evolves (Section 35) |

Neither cadence substitutes for the other — a year with four healthy Quarterly Reviews can still surface a structural gap only visible at the Annual Audit's longer timescale, and vice versa, a single bad quarter should be caught well before the Annual Audit if the Quarterly Review is functioning.

### Escalating audit findings that reveal a principle-level gap

If the audit surfaces a finding that isn't really about decision mechanics but about a genuine principle tension (e.g., "we consistently under-invest in asymmetric bets despite the stated preference for them") — that finding is routed to the next [Founding Principles review](02_FOUNDING_PRINCIPLES.md#principle-evolution) rather than resolved unilaterally inside this document, since it may reflect something deeper than a process fix.

---

## Decision Anti-patterns

Named failure patterns, in the same spirit as [Organization's Anti-Patterns](03_ORGANIZATION.md#organizational-anti-patterns) — recognizable, nameable, and paired with a fix, so a pattern can be called out in one word instead of re-explained every time it recurs.

| Anti-pattern | Symptom | Fix |
|---|---|---|
| **Decision by silence** | No one explicitly decided; the status quo persisted by default and is later treated as if it were a deliberate choice | Ownership Rules' default-assignment mechanism (Section 22); log the default explicitly as a Rejected/no-action decision |
| **Analysis paralysis** | A DL-1 or DL-2 decision accumulates evidence indefinitely without reaching Decide | Sizing test (Section 5) and gate timeboxing (Section 10) — evidence sufficiency, not volume |
| **Consensus-seeking on a one-way door** | Waiting for unanimous agreement on an irreversible decision that only needs the correctly-authorized owner to decide | [Believability-weighted input](03_ORGANIZATION.md#believability-weighted-input) — input is gathered, not voted; the owner decides |
| **Verbal-only decision** | A real decision was made in conversation and acted on, with no DR | [Decision Logging](#decision-logging)'s core rule — retroactively log immediately upon discovery |
| **Retroactive rationalization ("resulting")** | Judging the *decision* as good or bad purely by how the outcome turned out, ignoring the quality of process/evidence at decision time | [Failure Analysis](#failure-analysis)'s "bad luck" category; postmortems restate the original hypothesis before looking at outcome |
| **Escalation avoidance** | Owner keeps a decision at their own level to "look decisive" despite a clear escalation trigger (Section 17) | Reinforce that [escalating is correct behavior](03_ORGANIZATION.md#escalation-is-not-failure), not a failure signal |
| **Authority mismatch** | Someone decides above or below their authorized band (Section 4) | Gate 4 enforcement; Failure Analysis roots-cause as "wrong authority" |
| **Zombie decision** | Approved and Implemented, but never reaches Reviewed — sits indefinitely with a lapsed review date | Quarterly Decision Review's overdue-items agenda item (Section 29) |
| **Evidence shopping** | Gathering evidence until a batch supports the preferred conclusion, then stopping | Bias Detection's confirmation-bias mitigation (Section 26); Gate 2 requires evidence "for and against" |
| **Committee ownership** | A group is listed as the decision owner; no individual is accountable when it goes wrong | Ownership Rules (Section 22) — exactly one name in the `Owner` field, always |
| **Silent reversal** | A decision is quietly undone or ignored without logging the reversal as a new decision | [Decision Lifecycle](#decision-lifecycle)'s Superseded/Reopened states — reversal is itself a logged decision |
| **Sunk-cost persistence** | Continuing to fund or pursue something because of resources already spent, not because of forward-looking value | [Capital Allocation](#capital-allocation)'s explicit exclusion of sunk cost as valid evidence |
| **Reversibility laundering** | Labeling a decision "reversible" specifically to avoid the rigor its actual door type requires | The four-question classification test (Section 18) — mechanical, not self-assessed on vibes |
| **Over-classification drag** | Running full DL-3/DL-4 rigor on a decision that genuinely passes the two-way door test | Sizing test (Section 5) and door-type test (Section 18) applied honestly in both directions |
| **Gate laundering** | Repeatedly re-submitting a decision to a gate with cosmetic changes rather than actually fixing the deficiency | Named explicitly at the second consecutive failure; escalates to the owner's manager/Brain for a process check-in |
| **Review as backdoor decision** | The Quarterly/Annual Review body starts making new object-level decisions instead of reviewing the framework and past decisions | Section 29/30 scope limits — review outputs are findings and framework proposals, routed through the normal pipeline like any other decision |
| **Unexamined trade-off** | Two high-order principles genuinely conflict and the DR picks a side without naming the tension | [Decision Philosophy](#decision-philosophy) — log the tension explicitly as evidence, even if the resolution follows the standard [Principle Hierarchy](02_FOUNDING_PRINCIPLES.md#principle-hierarchy) |
| **Automation without an owner** | A decision-support agent operates in the pipeline with no named human accountable for its outputs | [AI-Assisted Decisions](#ai-assisted-decisions) and [Agent design standards](00_ATLAS_BRAIN.md#agent-design-standards) — disable until an owner is named |
| **Metric gaming** | Success metrics or review windows set deliberately easy to guarantee a high hit rate | [Decision Quality Metrics](#decision-quality-metrics)'s gaming-detection cross-checks; Annual Audit sampling |
| **Precedent blindness** | A decision is made with no Register search at all, despite a near-identical prior entry existing | Required Evidence's mandatory precedent check at DL-2+ (Section 11) |
| **Postmortem theater** | A postmortem is held and documented, but changes nothing about future behavior — same mistake recurs unaddressed | Postmortem Process's "what would change next time" step is mandatory, and its outputs are tracked at the next Quarterly Review |
| **Threshold creep** | Escalation thresholds are quietly loosened over time, one small exception at a time, without ever being formally re-decided | Threshold changes are themselves Governance-class DRs (Section 17); Quarterly Review's threshold-recalibration agenda item catches drift |
| **Framework worship** | Following every gate and template mechanically while losing sight of the actual judgment the framework exists to support | [Decision Philosophy](#decision-philosophy)'s framing — the machinery serves judgment, it does not replace it |

---

## Worked Examples

The examples below are **illustrative walkthroughs**, not entries in the [Decision Register](#decision-register). Each is tagged `EX-N` (never `DR-YYYY-NNN`) specifically so it can never be confused with a real logged decision. They are built from decision points [Current State](05_CURRENT_STATE.md#current-decision-system) has already flagged as real, pending, unlogged decisions facing Atlas today — the framework is demonstrated against Atlas's actual situation, not a hypothetical company. If and when these are formally decided, they will be logged in the Register above under their own real `DR-YYYY-NNN` IDs, at which point these examples become historical illustrations only. See [Current State § Appendix E — Decision Record Backlog](05_CURRENT_STATE.md#appendix-e--decision-record-backlog) for the authoritative status of each underlying decision.

### Example EX-1 — Strategic, DL-4: "Build the full Brain document set before any operating activity"

This walks through the decision Current State names as "the nearest thing to a decision made so far" ([Current Decision System](05_CURRENT_STATE.md#current-decision-system)) — made in substance, not yet formally run through this pipeline.

**1. Intake / Frame** — Problem: should Atlas invest its first months in writing the full governance document set (Brain, Principles, Organization, Roadmap, Current State, this document, Glossary) before acquiring or building any revenue-generating asset? Deadline: soft — driven by founder bandwidth, not an external date. Owner: Brain (the founder, wearing the Brain hat). Do-nothing cost: begin sourcing deals/building immediately with no documented operating system.

**2. Classify** — Type: **Strategic**. Level: **DL-4** (direction-changing, sets the operating pattern for everything after it). Door type: leans **one-way** — months of foundational time cannot be recovered, and the *pattern* it sets (documentation-first) is a precedent for every future initiative.

**3. Evidence** — Financial: opportunity cost of delayed deal sourcing, roughly bounded by founder time. Principle: directly supported by [Documentation before execution](00_ATLAS_BRAIN.md#documentation-before-execution) and [Why Documentation Is Infrastructure](01_WHY_ATLAS_EXISTS.md#why-documentation-is-infrastructure). Precedent: none in the Register yet (this would be entry `DR-2026-001` if logged). Risk: delay risk to first revenue/asset.

**4. Options** — (a) Full Brain set first, then source deals. (b) Source deals immediately, backfill documentation later. (c) Hybrid — minimum viable Brain set (Brain + Principles only), then parallelize deal sourcing with continued documentation.

**5. Score** — Strategic fit: 5 (directly the holding-OS thesis in [Why Atlas Exists](01_WHY_ATLAS_EXISTS.md#why-atlas-exists)). Risk: Medium likelihood of delay cost, Low impact given no capital yet deployed → "Monitor" cell. Opportunity: knowledge contribution 5 (this entire document set *is* the reusable system), time-to-impact 2 (slow to first revenue).

**6. Decide** — Option (a), full Brain set first, chosen. Rationale: at zero capital deployed and zero portfolio companies, the cost of delay is time, not capital — and the [Founding Principles](02_FOUNDING_PRINCIPLES.md) explicitly rank documentation before execution when both compete for scarce founder attention at this stage.

**7–8. Approve** — Self-approved at Brain band (DL-4, and the founder currently holds Brain).

**9. Log** — If formally logged, this becomes `DR-2026-001`, Type: Strategic, Level: DL-4, Door: One-way, Status: Approved (retroactively), Review date: at Phase P0 exit (see [Roadmap](04_ROADMAP.md#major-phases)).

**10–11. Execute / Review** — In progress; review is naturally gated to the Phase P0 exit criteria already defined in [Current Strategic Position](05_CURRENT_STATE.md#current-strategic-position).

### Example EX-2 — Technical, DL-2: "Register the AI-assisted-drafting pattern as a production automation"

Based on the open item Current State Appendix E flags as `DR-2026-008 (proposed)` (unused future ID). Live `DR-2026-003` is the irreversible-commitment escalation threshold and must not be reused here.

**1. Frame** — Should the pattern of using AI to draft Brain documents (this document included) be formally registered as a production automation under [Automation Standards](00_ATLAS_BRAIN.md#automation-standards), rather than remaining an ad hoc practice?

**2. Classify** — Type: **Technical**, sub-class AI/automation deployment. Level: **DL-2** (affects Knowledge and AI department scope; reversible). Door: **two-way** — the practice can be un-registered or re-scoped cheaply.

**3. Evidence** — Frequency: document drafting recurs well above the automation eligibility frequency bar ([Automation eligibility criteria](00_ATLAS_BRAIN.md#automation-eligibility-criteria)). Definition: inputs (prompts, source documents) and outputs (drafted markdown) are clear. Measurement: no formal baseline metrics collected yet — a gap this decision would need to close.

**4. Options** — (a) Register formally now, at L1 (Assisted) maturity, with a named owner and eval criteria. (b) Continue informally, revisit after more usage data. (c) Register at L2 (Supervised automation) immediately, given AI-Assisted Decisions rules already cap decision-support at L2.

**5. Score** — Risk: Low/Low ("Accept" cell) — human review of every draft is already the norm. Opportunity: knowledge contribution 4, time-to-impact 5 (immediate).

**6. Decide** — Option (a): register at L1 now, with a defined path to L2 once baseline metrics (time saved, revision rate) exist, per the standard [AI adoption process](00_ATLAS_BRAIN.md#ai-adoption-process).

**7. Log (if made real)** — Proposed ID `DR-2026-008` (not yet live), Type: Technical, Level: DL-2, Door: Two-way, AI-assistance flag: Yes (this decision is itself about AI drafting), Review date: 90 days.

### Example EX-3 — Investment, DL-4 (illustrative, not yet applicable): "First acquisition target"

No real target exists yet ([Current Assets](05_CURRENT_STATE.md#current-assets) shows an empty pipeline), so this example is fully hypothetical, included to demonstrate how [Capital Allocation](#capital-allocation) and [Risk](#risk-assessment)/[Opportunity Assessment](#opportunity-assessment) compose for the highest-stakes decision class Atlas will eventually face.

**1. Frame** — Should Atlas acquire Company X, a small SaaS business with $Y ARR, using capital from the Growth bucket?

**2. Classify** — Type: **Investment** (M&A sub-class). Level: **DL-4** (capital deployment + new portfolio asset, both independently trigger Brain escalation per [Escalation Rules](#escalation-rules)). Door: **one-way** (acquisition costs, integration costs, and reputational cost of an unwind are all high).

**3. Evidence** — Full due-diligence packet (financial, market, operational per [Company Lifecycle § Evaluate](00_ATLAS_BRAIN.md#company-lifecycle)), integration-scorecard forecast per [Integration standards](00_ATLAS_BRAIN.md#integration-standards-acquire--build--integrate), build-vs-acquire comparison per [Brain's framework](00_ATLAS_BRAIN.md#build-vs-acquire-framework).

**4. Options** — (a) Acquire at asking valuation. (b) Acquire with renegotiated terms (earnout structure). (c) Decline; redirect capital to Reserve or a competing opportunity. (d) Build a comparable capability in-house instead.

**5. Score — Risk** — Financial: capital-at-risk stated as an absolute dollar figure and as a percentage of the Growth bucket (values from [Current Finance](05_CURRENT_STATE.md#current-finance) at decision time). Operational: key-person dependency risk in the target's team, scored explicitly. Worst-realistic-case narrative: written out per [Risk Assessment](#risk-assessment).

**5. Score — Opportunity** — Return potential scored against the [hurdle rate](00_ATLAS_BRAIN.md#capital-allocation-philosophy) (current value in [Current Finance](05_CURRENT_STATE.md#current-finance)); operational leverage scored on how much Atlas's AI/knowledge infrastructure could improve the target's unit economics post-close; optionality — does this open a sector Atlas wants a platform in, or foreclose flexibility.

**6. Decide** — Whichever option scores highest, with explicit rejected-alternative rationale for the other three — this is the step real due diligence would fill in; the framework does not predetermine the answer.

**7–8. Approve** — Assets deal owner + Finance draft; **Brain approval mandatory** regardless of deal size, per [Escalation](00_ATLAS_BRAIN.md#escalation) ("New portfolio asset — Any acquisition or new venture launch").

**9–11. Log / Execute / Review** — Logged immediately on Approve; review cadence 30/90/180 days per [Brain's review cadence table](00_ATLAS_BRAIN.md#5-execute-measure-and-iterate), feeding the [Integration standards](00_ATLAS_BRAIN.md#integration-standards-acquire--build--integrate) scorecard on the same timeline.

### Example EX-4 — Operational, DL-1: "Adopt a new project-tracking tool"

A minimal example at the light end of the spectrum, to show the framework does not impose DL-4 weight on everyday choices.

**1. Frame** — Should Atlas start using a specific lightweight tool to track the milestone register instead of a plain markdown file?

**2. Classify** — Type: **Operational** (tooling sub-class). Level: **DL-1**. Door: **two-way** — monthly contract, exportable data, no lock-in.

**3–5. Evidence / Options / Score** — Light-touch per the [Evidence requirement matrix](#required-evidence): cost is trivial relative to any threshold; one alternative (status quo markdown file) is enough; no formal scoring table required at DL-1.

**6–8. Decide / Approve** — Self-decided and self-approved within the owner's own L0–L1 band; no escalation needed.

**9. Log** — Short-form DR only if there is a recurring spend commitment; otherwise a one-line note in a status update satisfies this level, per [Decision Templates](#decision-templates)'s micro-log tier.

**11. Review** — 30 days, informal — "is this actually getting used and is it worth the subscription."

### Example EX-5 — Personnel, DL-3: "First hire — Operations generalist"

Illustrative, since [Current Roles](05_CURRENT_STATE.md#current-roles) shows zero hires to date. Demonstrates how Personnel-class decisions compose with delegation and organizational scaling.

**1. Frame** — Should Atlas make its first hire, an Operations generalist, to begin offloading routine execution from the founder?

**2. Classify** — Type: **Personnel**, hire/role-creation sub-class. Level: **DL-3** — precedent-setting (first hire ever), affects budget (Operating bucket), and is costly to reverse even though legally an at-will separation is possible (per the canonical irreversible category "hiring or separating a person," Section 20). Door: **one-way**.

**3. Evidence** — Role charter drafted per [Hiring philosophy](03_ORGANIZATION.md#hiring-philosophy) ("hire for judgment... not for task volume capacity"). Budget source: Operating bucket, confirmed sufficient in [Current Finance](05_CURRENT_STATE.md#current-finance). Fit check: does this role reduce coordination tax or add to it? Precedent: none in the Register (first Personnel decision).

**4. Options** — (a) Hire a full-time generalist now. (b) Engage a part-time contractor first, as a lower-commitment trial. (c) Delay hiring further and continue automating before adding headcount, per [Automation first](00_ATLAS_BRAIN.md#automation-first) and [Default to the system](00_ATLAS_BRAIN.md#default-to-the-system) ("document; automate; then hire," per [Organization's anti-patterns table](03_ORGANIZATION.md#organizational-anti-patterns), "Hiring ahead of workflow").

**5. Score — Risk** — Operational: Low likelihood of a bad hire given a structured process, Medium impact given it's the first hire and sets cultural precedent → Monitor. Financial: capital-at-risk is the salary commitment against the Operating bucket, explicitly bounded and low relative to bucket size → Accept.

**5. Score — Opportunity** — Operational leverage: Medium — this specific role does not itself compound across the portfolio the way a system or automation would, which is explicitly named as a trade-off against option (c). Knowledge contribution: naming this the first hire also means designing the **first role charter and onboarding path**, which is reusable — scored higher than the hire itself in isolation.

**6. Decide** — Illustrative outcome: option (b), a part-time contractor trial first, chosen specifically because [Organization's hiring-ahead-of-workflow anti-pattern](03_ORGANIZATION.md#organizational-anti-patterns) flags exactly this risk at Atlas's current stage, and a trial engagement converts a one-way door into something closer to two-way before fully committing.

**7–8. Approve** — Self-approved at Brain band, since at Stage 0 Brain and the hiring authority are the same person; the DR still documents this explicitly rather than skipping the Approve stage silently.

**9. Log** — Would be `DR-2026-XXX`, Type: Personnel, Level: DL-3, Door: One-way (softened by the trial structure — noted explicitly in the DR), Review date: 90 days into the trial.

**10–11. Execute / Review** — Onboarding uses the standard [Role Lifecycle](03_ORGANIZATION.md#role-lifecycle) and [Onboarding](03_ORGANIZATION.md#onboarding) processes; review compares actual coordination-tax reduction against the Opportunity score's stated expectation.

### Example EX-6 — Strategic, DL-4: "Principle exception request — accept a below-hurdle-rate deal for strategic knowledge gain"

Demonstrates the Principle Exception pathway (Section 6's Strategic sub-class), which is the highest-friction, most tightly-gated decision type in this framework.

**1. Frame** — A specific opportunity fails the [hurdle rate](00_ATLAS_BRAIN.md#capital-allocation-philosophy) test but would give Atlas its first hands-on experience integrating an acquisition — valuable per [Knowledge gain](00_ATLAS_BRAIN.md#3-generate-and-evaluate-options) even if the financial return is sub-hurdle.

**2. Classify** — Type: **Strategic**, principle-exception sub-class. Level: **DL-4** — any deviation from a Core or Founding Principle is Brain-level by definition ([Escalation](00_ATLAS_BRAIN.md#escalation), "Principle exception — Any deviation from Core Principles — Escalate to Brain"). Door: **one-way** (sets a precedent for how strictly hurdle rates are enforced going forward).

**3. Evidence** — The [Capital Allocation](#capital-allocation) hurdle-rate override procedure is followed exactly: the strategic (non-financial) rationale is named explicitly (first integration experience), scored honestly in Opportunity Assessment rather than used to bypass scoring, and Brain approval is sought regardless of deal size.

**4. Options** — (a) Grant the exception, proceed with the deal. (b) Decline; wait for a hurdle-rate-clearing opportunity to gain the same experience. (c) Grant a *narrower* exception — proceed, but cap the capital committed well below what the deal ideally wants, limiting downside while still capturing the learning.

**5. Score** — Opportunity: knowledge contribution scored high (5) with the specific future reuse named ("informs the integration scorecard timelines in Company Lifecycle, currently untested against real data"); return potential scored honestly low, reflecting the actual sub-hurdle economics — not inflated to justify the decision. Risk: Financial risk scored against the *narrower*, capped exposure in option (c), not the full deal size.

**6. Decide** — Illustrative outcome: option (c) — grant a narrow, capped exception, explicitly reasoned as preserving the hurdle-rate principle's integrity (a full, uncapped exception would set a precedent that erodes it) while still capturing the stated knowledge-gain rationale.

**7–8. Approve** — Brain approval is mandatory and explicit; the DR states a **sunset framing** — this specific exception does not create a standing policy that future sub-hurdle deals are approvable on knowledge-gain grounds without an equally explicit, equally scrutinized case each time.

**9. Log** — Would be `DR-2026-XXX`, Type: Strategic, Level: DL-4, Door: One-way, tagged as a **Principle Exception** in [Current Governance's exception tracking](05_CURRENT_STATE.md#current-governance) ("Principle exceptions on record").

**10–11. Execute / Review** — Reviewed on the DL-4 quarterly-until-stable cadence; the postmortem explicitly re-evaluates whether the knowledge-gain rationale actually materialized as claimed, since an unrealized "strategic rationale" that becomes a habitual excuse for missing the hurdle rate is exactly the failure mode the narrow, capped, explicitly-sunset structure is designed to prevent.

### Counter-examples — what running the framework badly looks like

The positive examples above (EX-1 through EX-6) show the framework working. It is equally instructive to see it fail — these two counter-examples walk through decisions run *badly*, each triggering a named [Decision Anti-pattern](#decision-anti-patterns), so a reader can recognize the pattern in their own work before it produces a costly postmortem.

**Counter-example CX-1 — "We'll just wing it, it's obviously fine"**

A decision to switch the holding's primary cloud provider is made verbally in a single conversation, acted on the same day, and never written down. Three months later, a migration issue surfaces and no one can reconstruct why the original provider was dropped, what alternatives were considered, or what the expected cost savings were supposed to be.

- **What went wrong:** Stages 2–6 (Frame through Score) may well have happened *in someone's head*, but nothing left a trace. This is the **verbal-only decision** anti-pattern (Section 31), compounded by **decision by silence** on the question of who actually owned it.
- **What the framework would have caught:** Gate 1 requires the five framing questions answered in writing; Gate 5 requires logging within 24 hours of Decide for a decision this size (almost certainly DL-2, given it's a holding-wide infrastructure change). Neither gate was ever engaged.
- **The fix, after the fact:** Retroactive logging per [Decision Logging](#decision-logging) — even a late, reconstructed DR is better than none, explicitly dated as retroactive so the gap itself is visible and not disguised as contemporaneous rigor.

**Counter-example CX-2 — "The data was inconvenient, so we found better data"**

An Investment-class decision to follow on into an existing portfolio company is evaluated. The first pass of Evidence-gathering turns up a concerning unit-economics trend. The owner, having already informally committed to the deal socially, re-runs the market analysis with a narrower comparison set that excludes the concerning trend, and the revised evidence section supports the deal.

- **What went wrong:** This is **evidence shopping** (Section 26/31) — gathering evidence until it supports a pre-existing conclusion, not to find the truth. It is compounded by **sunk-cost persistence** if the "informal commitment" itself was driven by prior capital or relationship investment.
- **What the framework would have caught:** [Appendix D](#appendix-d--bias-self-audit-checklist)'s confirmation-bias question ("Have I actively sought evidence that would argue against my leading option?") is designed to be asked *before* Gate 3, precisely to catch a narrowing-the-comparison-set maneuver like this one. Gate 2's "evidence for and against" requirement should also have flagged the discarded concerning trend as unaddressed.
- **The fix:** The original, wider comparison set is restored; the concerning trend is scored honestly in Risk Assessment with a stated mitigation plan, or the deal is Rejected with the concerning trend named as the reason — either is an acceptable outcome, but both are more defensible than the laundered version.

---

## Appendices

### Appendix A — Decision Record Template (Canonical)

This extends Brain's [Decision Record template](00_ATLAS_BRAIN.md#decision-record-template) with the fields this document adds (Section 9). Copy this block to draft a new Full DR; strike fields not required at your Decision Level per Section 9's tier table.

```markdown
## DR-YYYY-NNN: [Decision title]

**Date:** YYYY-MM-DD
**Owner:** [Single named DRI]
**Status:** Proposed | Rejected | Approved | Implemented | Reviewed | Superseded | Reopened
**Type:** Investment | Operational | Strategic | Personnel | Technical
**Sub-class:** [see Section 6]
**Level:** DL-0 | DL-1 | DL-2 | DL-3 | DL-4
**Door type:** One-way | Two-way
**AI-assistance flag:** None | Drafting | Evidence-gathering | Scoring | Multiple (specify)
**Escalation approval:** [Name / role, or "N/A — within owner's own band"]

### Context
[What prompted this decision? What is the deadline? What happens if we do nothing?]

### Evidence
- Financial: [...]
- Market / competitive: [...]
- Operational feasibility: [...]
- Principle alignment: [...]
- Precedent (Register search performed: yes/no; citations): [...]

### Options considered
1. [Option A] — [description, trade-offs]
2. [Option B] — [description, trade-offs]
3. [Option C, if any]

### Risk score
| Category | Likelihood (1-5) | Impact (1-5) | Mitigation if Medium+ |
|---|---|---|---|
| Strategic | | | |
| Financial | | | |
| Operational | | | |
| Technical | | | |
| Compliance/legal | | | |
| Reputational | | | |

**Worst-realistic-case narrative:** [...]

### Opportunity score
| Criterion | Score (1-5) | Justification |
|---|---|---|
| Return potential | | |
| Operational leverage | | |
| Time to impact | | |
| Knowledge contribution | | |
| Optionality created | | |

**Opportunity cost named:** [What else could this capital/time/attention achieve?]

### Decision
[Chosen option and why alternatives were rejected]

### Success metrics
- [Metric 1]: [target] by [date]

### Review date
YYYY-MM-DD

### Postmortem (completed at review)
[Filled in at Review stage — see Appendix E]

### Related documents / precedent
- [Links to prior Register entries, sibling Brain documents, or external sources]
```

### Appendix B — Decision Classification Flowchart

A text-based decision tree implementing Sections 5, 6, and 18 in sequence. Walk it top to bottom for any new decision.

```
START
  │
  ▼
Is this fully reversible, no capital, no external party, no precedent? ──YES──▶ DL-0. Decide and move on.
  │ NO
  ▼
Is it inside one department's documented budget/SOP AND reversible? ──YES──▶ DL-1. Short-form DR if any commitment.
  │ NO
  ▼
Does it affect 2+ departments OR create a reusable precedent? ──YES──▶ at least DL-2. Continue below.
  │ NO (still ambiguous)
  ▼
Default to DL-2 and let Evidence stage confirm or downgrade.
  │
  ▼
Does real capital move, or is it hard to reverse within 90 days? ──YES──▶ at least DL-3.
  │
  ▼
Is it irreversible, principle-level, or capital/precedent-setting at the holding level? ──YES──▶ DL-4.
  │
  ▼
Run the four-question door-type test (Section 18):
  1. Cost to reverse > 20% of value at stake?
  2. Reversal slower than the review window?
  3. Binds Atlas to an external party without easy unwind?
  4. Locks in a precedent for future decisions?
  │
  ├── Any YES, or genuinely uncertain ──▶ ONE-WAY DOOR. Minimum DL-3 authority, full pipeline.
  │
  └── All NO ──▶ TWO-WAY DOOR. Delegate to DL-0/DL-1, minimal rigor.
  │
  ▼
Assign Type (Investment / Operational / Strategic / Personnel / Technical) and sub-class (Section 6).
  │
  ▼
Proceed to Decision Pipeline (Section 8), Stage 4 — Evidence.
```

### Appendix C — Evidence Checklists by Class

Instantiates the [Required Evidence matrix](#required-evidence) at the level of a literal checklist, organized by the five canonical Types.

**Investment**
- [ ] Financial model / projections attached
- [ ] Hurdle rate test result stated ([Capital Allocation](#capital-allocation))
- [ ] Capital bucket named and reserve-adequacy checked
- [ ] Market / competitive context summarized
- [ ] Build-vs-acquire comparison (if new venture or acquisition)
- [ ] Precedent search of the Register performed
- [ ] Risk score and worst-realistic-case narrative
- [ ] Opportunity score and opportunity cost named
- [ ] Return-measurement metric selected ([Brain's return measurement](00_ATLAS_BRAIN.md#return-measurement))

**Operational**
- [ ] Baseline metrics (time, cost, error rate) stated if this changes an existing process
- [ ] Affected-department sign-off or input captured
- [ ] SOP or playbook reference, if one exists
- [ ] Automation eligibility considered ([Automation Standards](00_ATLAS_BRAIN.md#automation-eligibility-criteria))
- [ ] Rollback / reversal path stated

**Strategic**
- [ ] Roadmap impact assessed ([Roadmap](04_ROADMAP.md))
- [ ] Principle alignment stated explicitly, citing the specific principle(s)
- [ ] Cross-department impact list, if any
- [ ] Precedent search of the Register performed
- [ ] If a principle exception: sunset date and Brain approval path named

**Personnel**
- [ ] Role charter or scope defined
- [ ] Budget source identified
- [ ] Fit against [Hiring philosophy](03_ORGANIZATION.md#hiring-philosophy)
- [ ] Knowledge-transfer / offboarding plan, if a separation
- [ ] Delegation scope and duration, if an authority delegation (Section 21)

**Technical**
- [ ] Agent Design Standard fields completed, if AI/automation ([Agent design standards](00_ATLAS_BRAIN.md#agent-design-standards))
- [ ] Target AI maturity level (L0–L4) stated
- [ ] Security / data-segmentation review, if applicable ([Data and security principles](00_ATLAS_BRAIN.md#data-and-security-principles))
- [ ] Rollback / migration plan
- [ ] Evaluation criteria and baseline for success

### Sub-class checklist supplements

For the sub-classes most likely to recur (per [Decision Classes](#decision-classes)), these items supplement — never replace — the top-level Type checklist above.

**M&A / acquisition (Investment)**
- [ ] Full due-diligence packet per [Company Lifecycle § Evaluate](00_ATLAS_BRAIN.md#company-lifecycle)
- [ ] Integration-scorecard forecast against [Integration standards](00_ATLAS_BRAIN.md#integration-standards-acquire--build--integrate) timelines
- [ ] Key-person dependency assessment of the target's team
- [ ] Post-close 30/45/60-day integration milestones drafted before Approve, not after

**New venture / build (Investment)**
- [ ] Build-vs-acquire comparison per [Brain's framework](00_ATLAS_BRAIN.md#build-vs-acquire-framework)
- [ ] MVP definition and validation plan
- [ ] Minimum viable team/resourcing named

**Exit / divestiture (Investment)**
- [ ] Exit criteria check against [Company Lifecycle § Exit criteria](00_ATLAS_BRAIN.md#exit-criteria)
- [ ] Alternative-use-of-capital comparison (what the freed capital funds instead)
- [ ] Sunk-cost exclusion confirmed explicitly in the rationale (per [Capital Allocation](#capital-allocation))

**Vendor / tooling (Operational)**
- [ ] Contract term length and renewal/auto-renewal clauses (door-type relevant, per [One-Way vs Two-Way Decisions](#one-way-vs-two-way-decisions))
- [ ] Data portability / export path if switching away later
- [ ] Cost comparison against at least one alternative, including "do nothing"

**AI / automation deployment (Technical)**
- [ ] Guardrails field explicitly excludes Approve/Log authority per [AI-Assisted Decisions](#ai-assisted-decisions)
- [ ] Fallback behavior defined for uncertainty
- [ ] Named human owner for exceptions
- [ ] Target maturity level and the process to graduate from L1→L2→L3

**Principle exception (Strategic)**
- [ ] Explicit sunset date or re-review trigger
- [ ] Narrowest viable scope stated (per [Capital Allocation § Hurdle rate override](#capital-allocation)'s "narrow exception" pattern)
- [ ] Brain approval explicit, not implied
- [ ] Logged as an exception in [Current Governance's exception tracking](05_CURRENT_STATE.md#current-governance)

### Appendix D — Bias Self-Audit Checklist

Run before Gate 3 (Score/Decide) for any DL-3+ decision. Each "yes" is a flag to address before proceeding, not an automatic blocker.

- [ ] Have I actively sought evidence that would argue *against* my leading option? (confirmation bias)
- [ ] Does my rationale mention money or time already spent as a reason to proceed? (sunk-cost fallacy)
- [ ] Is my chosen option the first one anyone proposed, with no real comparison? (anchoring)
- [ ] Have I written a genuine worst-realistic-case narrative, not just a low risk score? (overconfidence)
- [ ] Is there zero recorded dissent on a decision with real stakes and multiple stakeholders? (groupthink)
- [ ] Did I only check the most recent Register entry for precedent, ignoring older ones? (recency bias)
- [ ] Did I discard a lower-authority contributor's input without addressing their evidence? (authority bias)
- [ ] Did I accept an AI-proposed score or recommendation unchanged without independent scrutiny? (automation bias)
- [ ] Does my DR read as a persuasive story with no structured trade-off table? (narrative fallacy)
- [ ] Did I only cite successful past decisions as precedent, ignoring Rejected/Reopened ones? (survivorship bias)
- [ ] Did my Risk score dominate my Opportunity score regardless of their relative magnitude? (loss-aversion asymmetry)
- [ ] Have I run a one-paragraph pre-mortem assuming this decision failed?

### Appendix E — Postmortem Template

```markdown
## Postmortem: DR-YYYY-NNN — [Decision title]

**Postmortem date:** YYYY-MM-DD
**Facilitator:** [Name — decision owner, or Brain for DL-4]
**Attendees:** [Names]

### Original hypothesis (verbatim from the DR, not rewritten with hindsight)
- Decision: [...]
- Success metric: [...]
- Risk score at decision time: [...]
- Opportunity score at decision time: [...]

### Actual outcome
[Measured against the same metric, same units]

### Metric met? 
Yes | No | Partially

### Failure Analysis (if metric missed or decision Reopened)
**Root cause (choose one primary):** Bad process | Bad information | Bad judgment | Bad execution | Bad luck | Wrong authority

**Explanation:** [...]

### What would change next time
[Specific to evidence, gates, or process — not personal performance]

### Reusable heuristics extracted
- [...]

### Candidate glossary / framework updates flagged
- [...]

### Register entry updated
- [ ] Status set to Reviewed / Superseded / Reopened
- [ ] Postmortem summary attached to DR
```

### Appendix F — Escalation Packet Template

Directly instantiates [Organization's escalation packet requirements](03_ORGANIZATION.md#escalation-packet-requirements) for a decision-specific escalation. This **is** the DR at whatever stage it has reached — no separate document.

```markdown
## Escalation: DR-YYYY-NNN — [Decision title]

**Escalated by:** [Owner]
**Escalated to:** [Target — department head / Brain / board]
**Escalation trigger:** [Which trigger from Section 17 fired]

### Problem statement
[One paragraph]

### Owner after escalation
[Who owns resolution — usually still the original owner, with the target holding Approve authority]

### Options
1. [Option A + trade-off]
2. [Option B + trade-off]

### Recommendation
[Owner's preference and why]

### Evidence
[Link to the DR's Evidence section; cite Register precedents]

### Decision needed by
[Date] — consequence of delay: [...]

### Authority requested
[Specific approval needed — e.g., "Approval to deploy $X from Growth bucket" or "Approval for principle exception, sunset [date]"]
```

### Appendix G — First-Time Decision Owner Quick-Start

A condensed path for someone facing their first non-trivial decision at Atlas, who has not yet internalized the full document.

1. **Size it** — run the sizing test in [Decision Levels](#decision-levels), Section 5. Takes under a minute.
2. **Classify it** — pick a Type from [Decision Classes](#decision-classes), Section 6.
3. **Run the door-type test** — [Appendix B](#appendix-b--decision-classification-flowchart)'s four questions.
4. **If DL-0/DL-1** — just decide, note it in your next status update if any resource commitment exists, done.
5. **If DL-2+** — copy [Appendix A](#appendix-a--decision-record-template-canonical), fill in Context and Evidence using [Appendix C](#appendix-c--evidence-checklists-by-class)'s checklist for your Type.
6. **Generate ≥2 real options** — not one option and a straw man.
7. **Score Risk and Opportunity** if DL-3+ — Sections 12–13.
8. **Run the bias checklist** — [Appendix D](#appendix-d--bias-self-audit-checklist) — before you finalize.
9. **Decide, and if above your authority band, escalate** using [Appendix F](#appendix-f--escalation-packet-template) — Sections 4, 17.
10. **Log it** in the [Decision Register](#decision-register) within the SLA (Section 23).
11. **Put the review date on your actual calendar** — not just in the document. This is the single most commonly skipped step.

### Appendix H — Candidate Glossary Terms

Terms this document coins or formalizes, proposed for [`07_GLOSSARY.md`](07_GLOSSARY.md) at its next update cycle — see [Current State's note](05_CURRENT_STATE.md#appendix-d--candidate-glossary-terms) that the Glossary is not yet initialized.

| Term | Proposed definition |
|---|---|
| **DR / Decision Record** | The canonical logged artifact for a decision, ID format `DR-YYYY-NNN` |
| **DL (Decision Level)** | DL-0 through DL-4; the decision-specific weight scale mapped onto Organization's L0–L4 authority bands |
| **Decision Register** | The append-only log of all logged decisions, held in `06_DECISIONS.md` |
| **Door type** | One-way or two-way, per the four-question classification test in Section 18 |
| **Decision pipeline** | The eleven-stage sequence (Intake → Review) every decision moves through |
| **Decision gate** | A checkpoint between pipeline stages with explicit pass/fail criteria |
| **AI-assistance flag** | A DR field disclosing which pipeline stages AI materially contributed to |
| **Resulting** | The anti-pattern of judging a decision's quality purely by its outcome, ignoring process quality at decision time |
| **Reversibility laundering** | The anti-pattern of mislabeling a decision "reversible" specifically to avoid its warranted rigor |
| **Zombie decision** | A decision stuck Approved/Implemented that never reaches Reviewed |
| **EX-N (worked example)** | The tagging convention for illustrative, non-Register walkthroughs in this document, distinct from real `DR-YYYY-NNN` entries |
| **CX-N (counter-example)** | The tagging convention for illustrative walkthroughs of decisions run badly, demonstrating a named anti-pattern |
| **Decision gate** vs **phase gate** | A decision gate (this document) checks one decision's pipeline completeness; a phase gate ([Roadmap](04_ROADMAP.md)) checks Atlas's readiness to move between strategic horizons — related concepts, different scope |
| **Headline risk rating** | The single highest-severity category score across a decision's six risk categories, never an average |
| **De-escalation** | Returning execution and logging authority to the original decision owner once an escalated judgment call is resolved |

### Appendix I — One-Page Quick Reference Card

A single condensed view of the entire framework, for printing, pinning, or prompting an AI agent with the essential rules in one pass.

**Levels:** DL-0 trivial → DL-4 strategic/governance. Sizing test: irreversible/holding-strategic → DL-4; real capital/hard to reverse → DL-3; cross-department/precedent → DL-2; in-SOP/reversible → DL-1; else DL-0. When unsure, round up.

**Classes:** Investment · Operational · Strategic · Personnel · Technical (fixed set, per Brain).

**Door test (any "yes" → one-way; default to one-way if unsure):** (1) Costs > 20% of value at stake to reverse? (2) Slower to reverse than the review window? (3) Binds an external party without easy unwind? (4) Locks in a precedent?

**Pipeline:** Intake → Frame → Classify → Evidence → Options (≥2) → Score → Decide → Approve → Log (≤24h at DL-2+) → Execute → Review (on the due date, no exceptions).

**Gates:** 0 Worth deciding · 1 Framed · 2 Evidenced (both-sided) · 3 Scored & Decided (no unexplained veto scores) · 4 Approved (correct authority) · 5 Logged & Executing · 6 Reviewed.

**Evidence categories:** Financial · Market · Operational · Principle · Precedent · Risk · Opportunity · Stakeholder.

**Risk/Opportunity scoring:** 1–5 per category, worst-case and opportunity-cost narratives mandatory at DL-3+. Headline risk = highest single category, never an average.

**AI can:** draft, gather, score, recommend, at every stage. **AI cannot:** decide, approve, or self-certify a log entry.

**Override:** always available to a human, always logged when overriding well-evidenced input, never available to AI overriding a human.

**Escalate when:** blocked >48h, hurdle rate missed with no override, Reserve shortfall, principle exception, risk lands in "Escalate to Brain," cross-department disagreement.

**One-way default authority:** DL-3 minimum. **Two-way default authority:** delegate to DL-0/DL-1.

**Ownership:** exactly one name per decision, always. Committees advise; they do not own.

**Logging:** unlogged = provisional = doesn't count. SLA: 24h at DL-2+, 7 days at DL-1 if any commitment.

**Review cadence:** 30d (small) / 90d (medium) / 30-90-180d (large) / quarterly-until-stable (strategic).

**Postmortem:** restate the original hypothesis before looking at the outcome. Blameless. Root cause ∈ {Bad process, Bad information, Bad judgment, Bad execution, Bad luck, Wrong authority}.

**Cadence:** Quarterly Decision Review (metrics, overdue items, bias scan, thresholds) → Annual Decision Audit (compliance sampling, year-over-year trend, framework fit).

**When in doubt:** open [Appendix G](#appendix-g--first-time-decision-owner-quick-start) and follow the eleven steps.

### Appendix J — Frequently Asked Questions

Questions that don't fit neatly under a single numbered section, collected here for quick lookup.

| Question | Answer |
|---|---|
| What if I don't know the Decision Level until I've already gathered some evidence? | That's normal and expected — Classify (stage 3) is provisional until Evidence (stage 4) confirms it; see [Decision Levels § Level can be revised mid-pipeline](#decision-levels). |
| Can a decision have zero rejected options — i.e., only one option was ever real? | Only at DL-0/DL-1. At DL-2+, Gate 2 requires at least two genuinely viable options; if only one is truly viable, the DR should say so explicitly and explain why the "do nothing" option specifically was rejected, since that is always the implicit second option. |
| What if the decision owner and the escalation target are the same person (e.g., Brain deciding a Brain-level matter)? | The `Escalation approval` field states "N/A — decided directly at the required band" — no separate approval step is theatrically required when the owner already holds the necessary authority. |
| Is a Rejected decision still subject to the Quarterly Decision Review's overdue-items check? | No — Rejected and Superseded are terminal states with no pending review date, per the [Decision Lifecycle](#decision-lifecycle) transition table. |
| Can this document's own rules be an exception to itself (e.g., can Brain skip Gate 4 "just this once")? | No. This document's own amendment process (Section 35) is the only path to changing its rules, and even that runs through the pipeline it defines. |
| What happens to a decision made correctly under an *older version* of this document, before a later amendment? | It remains valid as logged — amendments are never applied retroactively to existing Register entries, per [Decision Templates § Template versioning](#decision-templates). |
| How does this framework apply to a decision made by an external party (e.g., a portfolio company's own leadership) rather than by Atlas directly? | Per [Company Lifecycle's autonomy spectrum](00_ATLAS_BRAIN.md#portfolio-company-autonomy-spectrum), the decision framework is a **required** Atlas standard for portfolio companies ("Decision framework — Required" in that table) once integrated — the portfolio company runs its own version of this pipeline, logged in its own local register, with escalation to Atlas Brain only for triggers that cross the thresholds in [Escalation Rules](#escalation-rules). |
| Does a decision need a DR if it was entirely AI-executed with pre-approved guardrails (e.g., a fully automated L3 workflow)? | If the automation itself was already approved as a production automation (with its own spec per [Automation Standards](00_ATLAS_BRAIN.md#automation-standards)), each individual execution is not a new decision — the *decision* was made once, when the automation was approved, and is logged once. A new DR is only needed if the automation encounters an exception outside its guardrails and a human has to intervene. |

### Appendix K — Master Checklist Index

Every checklist and checklist-shaped table in this document, indexed in one place so none get lost in the surrounding prose.

| Checklist | Location | Use it when |
|---|---|---|
| Sizing test (5 questions) | [Decision Levels](#decision-levels) | Starting any new decision |
| Door-type classification test (4 questions) | [One-Way vs Two-Way Decisions](#one-way-vs-two-way-decisions) | Any DL-2+ decision, before Score |
| Decision Record mandatory fields | [Decision Templates](#decision-templates) | Drafting any DR above micro-log tier |
| Evidence requirement matrix | [Required Evidence](#required-evidence) | Gate 2, for any DL-1+ decision |
| Type-level evidence checklists | [Appendix C](#appendix-c--evidence-checklists-by-class) | Gate 2, matched to the decision's Type |
| Sub-class evidence supplements | [Appendix C § Sub-class checklist supplements](#appendix-c--evidence-checklists-by-class) | Gate 2, matched to the decision's sub-class |
| Risk scoring categories (6) | [Risk Assessment](#risk-assessment) | Gate 3, DL-3+ (optional DL-2) |
| Opportunity scoring criteria (5) | [Opportunity Assessment](#opportunity-assessment) | Gate 3, DL-3+ (optional DL-2) |
| Bias self-audit (12 questions) | [Appendix D](#appendix-d--bias-self-audit-checklist) | Before Gate 3, DL-3+ mandatory |
| Escalation packet requirements | [Appendix F](#appendix-f--escalation-packet-template) | Any time a decision escalates |
| First-time owner quick-start (11 steps) | [Appendix G](#appendix-g--first-time-decision-owner-quick-start) | First non-trivial decision, or whenever a fast refresher is needed |
| Postmortem steps (7) | [Postmortem Process](#postmortem-process) | Every DL-2+ Review stage |
| Delegation record fields | [Delegation Rules](#delegation-rules) | Any time authority is delegated |
| Quarterly Decision Review standing agenda (7 items) | [Quarterly Decision Review](#quarterly-decision-review) | Every quarter |
| Annual Decision Audit scope (7 areas) | [Annual Decision Audit](#annual-decision-audit) | Every year |

### Appendix L — Delegation Record Template

Instantiates the fields listed in [Delegation Rules](#delegation-rules) as a fillable, lightweight record.

```markdown
## Delegation Record: [Short title]

**Date:** YYYY-MM-DD
**Delegator:** [Name/role — must hold the authority being delegated]
**Delegate:** [Name/role receiving authority]
**Scope:** [Exact Decision Class(es) and Level(s) covered — be specific, not "general authority"]
**Duration:** [Start date] to [End date, or "until revoked"]
**Revocation trigger:** [What automatically ends this — a date, an event, or "delegator's discretion, effective immediately upon notice"]
**Escalation path if delegate is uncertain:** [Defaults to the delegator unless stated otherwise]
**Logged as:** [Personnel-class DR ID, if this delegation is significant enough to warrant one per Section 21]
```

### Appendix M — Full Worked Evidence Packet (Illustrative DL-4 Capital Decision)

A complete, filled-out example combining [Required Evidence](#required-evidence), [Risk Assessment](#risk-assessment), and [Opportunity Assessment](#opportunity-assessment) into a single packet, for a hypothetical Investment-class decision — extending Example EX-3 with full documentation depth rather than a summary. This is illustrative only; all figures are fabricated placeholders.

```markdown
## Evidence Packet: Acquire Company X (illustrative — not a real decision)

### Financial
- Trailing-twelve-month revenue: $[X], growing [Y]% YoY (source: target's financials, reviewed by Finance)
- Proposed purchase price: $[Z], implying a [multiple]x revenue multiple
- Hurdle rate test: current hurdle rate is [see Current Finance]; projected IRR at base case is [above/below] that rate
- Capital source: Growth bucket; post-deployment bucket balance remains above policy minimum (confirmed against Current Finance)

### Market / competitive
- Target operates in [sector], estimated market size $[X]
- Three named comparable companies and their approximate valuations
- Competitive positioning: target's specific defensible advantage (or lack thereof) stated plainly

### Operational feasibility
- Target team size: [N] people; key-person dependency assessed for the [role] specifically
- Integration timeline estimate against [Integration standards](00_ATLAS_BRAIN.md#integration-standards-acquire--build--integrate)'s 30/45/60-day thresholds
- Atlas capacity check: who would own post-close integration, and is that capacity currently available

### Principle alignment
- Long-term thinking: 3-year value horizon stated explicitly, not just first-year returns
- Capital efficiency: comparison against at least one alternative use of the same capital
- Systems over heroes: does the deal depend on any single irreplaceable person surviving the transition

### Precedent
- Register search performed: [date], keywords used: [list]
- Result: no prior acquisition precedent exists (first of this class) — noted explicitly, not glossed over

### Risk score
| Category | Likelihood | Impact | Cell |
|---|---|---|---|
| Strategic | 2 | 3 | Monitor |
| Financial | 3 | 4 | Mitigate |
| Operational | 4 | 3 | Mitigate |
| Technical | 2 | 2 | Accept |
| Compliance/legal | 2 | 3 | Monitor |
| Reputational | 1 | 2 | Accept |

**Headline risk rating:** Mitigate. **Mitigation plans:** Financial — staged earnout structure ties a portion of purchase price to post-close performance; Operational — retention agreement for the key team member identified above, with a documented succession plan if retention fails.

**Worst-realistic-case narrative:** Key team member departs within 6 months despite retention terms; integration stalls; Atlas absorbs a partial write-down but the earnout structure limits total cash exposure to [X]% of the deal's headline value.

### Opportunity score
| Criterion | Score | Justification |
|---|---|---|
| Return potential | 4 | Projected IRR clears the hurdle rate with margin at base case |
| Operational leverage | 3 | Atlas's existing finance/reporting infrastructure reduces target's back-office costs measurably, though the core product still requires standalone expertise |
| Time to impact | 3 | Revenue accretive from close; full synergy realization takes ~2 quarters |
| Knowledge contribution | 5 | First acquisition — produces the first real-world test of the Integration standards and scorecard |
| Optionality created | 4 | Opens a sector adjacency Atlas has flagged as strategically interesting |

**Opportunity cost named:** Capital deployed here is unavailable for the competing follow-on opportunity being evaluated the same quarter (see the worked example in [Capital Allocation](#capital-allocation)) — both are compared explicitly in a single combined DR, not two independent ones, per that section's rule.

**Asymmetry check:** Downside is capped by the earnout structure; upside includes both the direct return and the non-financial knowledge-contribution value of proving the integration playbook works — flagged explicitly as a favorable asymmetric bet.
```

This packet is deliberately long — a real DL-4 capital decision should produce evidence at roughly this depth. A DL-4 DR with a packet substantially thinner than this example has very likely failed Gate 2 and should be returned to Evidence (stage 4) before proceeding.

### Appendix N — Decision Level and Class Quick Matrix

A cross-tabulation showing the *typical* Decision Level range for each Class, for fast sanity-checking during Classify (pipeline stage 3) — not a substitute for running the actual sizing test in Section 5.

| Class | Most common DL | Widest realistic range | Why the range is wide |
|---|---|---|---|
| Investment | DL-3 | DL-2 to DL-4 | A small follow-on can be DL-2; a first acquisition is always DL-4 |
| Operational | DL-1 | DL-0 to DL-2 | Most process tweaks are trivial; a holding-wide process change is DL-2 |
| Strategic | DL-4 | DL-3 to DL-4 | Strategic decisions are rarely small by definition, but not every one is a principle exception |
| Personnel | DL-2 | DL-1 to DL-3 | A minor role-scope tweak is DL-1; a first hire or a separation is DL-3 |
| Technical | DL-1 | DL-0 to DL-3 | Routine tooling changes are trivial; core architecture or AI deployment decisions with holding-wide reach are DL-3 |

If a decision's self-assigned Level falls outside the "widest realistic range" for its Class, that mismatch is itself worth a second look before proceeding — not because it's necessarily wrong, but because it's unusual enough to warrant confirming the sizing test (Section 5) was actually applied rather than guessed.

---

## Cross References

This document is the **decision-mechanics layer** of Atlas. Sibling documents provide strategy, philosophy, structure, sequencing, state, and vocabulary — **link rather than duplicate**.

### Relationship to every Brain document

| Document | Relationship |
|---|---|
| [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) | **Parent OS reference.** Brain defines the five-step Decision Framework, minimum DR fields, default owners by type, review cadences, and one-way/two-way doors at summary depth. **This document operationalizes** [Decision Framework](00_ATLAS_BRAIN.md#decision-framework) into the full pipeline, gates, scoring, register, and audit cadence. Brain points here for "decisions are logged in `06_DECISIONS.md`." |
| [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) | **Philosophical foundation.** Explains *why* every decision must become knowledge and why AI-native verification beats bureaucratic committee review. Read for conviction; this document reads for **mechanism**. See especially [Why Every Decision Must Become Knowledge](01_WHY_ATLAS_EXISTS.md#why-every-decision-must-become-knowledge). |
| [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) | **Judgment infrastructure.** The [Principle Hierarchy](02_FOUNDING_PRINCIPLES.md#principle-hierarchy) and [Decision Checklist](02_FOUNDING_PRINCIPLES.md#decision-checklist) are the judgment inputs this document's pipeline operationalizes into gates, evidence, and templates. This document does not re-derive principle rationale. |
| [`03_ORGANIZATION.md`](03_ORGANIZATION.md) | **Authority source.** The L0–L4 [Decision Authority](03_ORGANIZATION.md#decision-authority) bands, [Escalation Authority](03_ORGANIZATION.md#escalation-authority) paths, [Single Owner Principle](03_ORGANIZATION.md#single-owner-principle), and believability-weighted input are **applied, not redefined,** throughout this document — see especially Sections 4, 17, 22. |
| [`04_ROADMAP.md`](04_ROADMAP.md) | **Strategic sequencing.** Roadmap's [Capability Maturity Model](04_ROADMAP.md#capability-maturity-model) scores the decision system's own maturity (a CM dimension); this document defines what that dimension is scoring against. Phase-gate decisions use this document's pipeline like any other Strategic-class decision. |
| [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) | **Instance facts.** Actual Register entry count, current escalation threshold values, current Decision Quality Metrics, and the retroactive-logging backlog all live in [Current Decision System](05_CURRENT_STATE.md#current-decision-system) and [Current Governance](05_CURRENT_STATE.md#current-governance). **This document defines the type; Current State reports the instance.** |
| [`06_DECISIONS.md`](06_DECISIONS.md) | **This document.** Canonical source for decision mechanics and the live Decision Register. |
| [`07_GLOSSARY.md`](07_GLOSSARY.md) | **Shared vocabulary.** Terms used here (DRI, believability, one-way door, holding OS, CM, L-level) are defined canonically there once populated; this document is a major source of new candidate terms — see [Appendix H](#appendix-h--candidate-glossary-terms). |

### Relationship to Principles

| Principle | Expression in this document |
|---|---|
| Long-term thinking | Review cadences scale with Decision Level; strategic decisions reviewed quarterly until stable |
| Truth over comfort | Blameless postmortems name root causes, not culprits; "bad luck" is a legitimate category |
| Evidence over opinion | Required Evidence matrix; evidence-completeness is a hard gate, not a suggestion |
| Systems over heroes | The pipeline, gates, and templates work identically regardless of who the decision owner is |
| Compounding over optimization | The Decision Register and precedent-search requirement are the compounding mechanism |
| Ownership | Single Owner Principle applied without exception in Section 22 |
| Transparency | Escalation is explicitly not failure; dissent is loggable, not smoothed over |
| Extreme documentation | Every decision above DL-0 produces a written artifact; verbal decisions are provisional |
| AI-first thinking | AI participates at every pipeline stage except Decide and Approve |
| Automation by default | AI-assisted drafting, evidence-gathering, and scoring are the default, not the exception, above DL-1 |
| Simple before complex | DL-0/DL-1 compress the eleven-stage pipeline to near-zero overhead |
| Reversible decisions | The formal four-question door-type test in Section 18 |
| Human accountability | AI may recommend at any stage; AI may decide at none — the governing rule of Section 15 |
| Capital efficiency | Hurdle-rate testing and reserve-adequacy checks gate every capital decision |
| Integrity | Escalation packets always name the specific authority requested; no vague asks |
| Optionality | Opportunity Assessment's "optionality created" criterion; asymmetric bets named explicitly |
| Continuous improvement | Quarterly Decision Review and Annual Decision Audit feed back into this document's own versioning |
| Knowledge compounds | The Register is the literal compounding mechanism — precedent search is mandatory at DL-2+ |
| Build before buy | Build-vs-acquire comparison is mandatory evidence for new-venture/acquisition sub-classes |
| Acquire when leverage exists | Operational-leverage scoring in Opportunity Assessment |
| Data before intuition | Risk and Opportunity scoring rubrics convert intuition into comparable numbers with justification |
| Action over perfection | Gates check completeness, not duration; a clean DL-2 decision can clear every gate in under an hour |
| One source of truth | This document's entire non-duplication posture (Section 2) |

See [Principle-to-document map](02_FOUNDING_PRINCIPLES.md#cross-references) for the full sibling table.

### Relationship to Organization

- Every authority band this document references (Section 4) is defined once, in [Organization](03_ORGANIZATION.md#decision-authority) — never redefined here.
- Escalation paths (Section 17) extend, never replace, [Organization's Escalation Authority](03_ORGANIZATION.md#escalation-authority).
- Delegation (Section 21) is bounded by the same authority ceiling Organization defines; this document adds only the decision-specific logging requirement.
- Ownership (Section 22) is the decision-specific application of [Organization's Single Owner Principle](03_ORGANIZATION.md#single-owner-principle) and [Ownership vs Execution](03_ORGANIZATION.md#ownership-vs-execution).

### Relationship to Roadmap

| Roadmap element | This document's response |
|---|---|
| Phase-gate transitions | Run as Strategic-class, DL-4 decisions through the standard pipeline |
| Capability Maturity Model decision-system dimension | Scored against whether this document's mechanisms (gates, register, metrics, audit) are actually in use, per [Current State](05_CURRENT_STATE.md#current-capability-maturity) |
| Milestone dependencies affecting decision infrastructure | e.g., Glossary initialization (Section 33 candidate terms), Register archive-file transition ([Register scaling](#register-scaling-note)) |
| Multi-year evolution horizons | Strategic-class decisions that shift Atlas between horizons (per [Roadmap's Multi-Year Evolution](04_ROADMAP.md#multi-year-evolution)) are always DL-4 and always logged, since they are, by construction, precedent-setting |
| Success criteria definitions | Roadmap's phase-level success criteria inform, but do not replace, a decision's own success metrics (Section 9) — a decision can meet its own metric while the phase it belongs to still misses its criteria, and vice versa |
| Scaling plan | As headcount and department count grow per Roadmap's scaling plan, [Delegation Rules](#delegation-rules) and [Ownership Rules](#ownership-rules) are the mechanisms that absorb that growth without amending this document |

### Relationship to Current State

[`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) holds **instance values** for this document's **type definitions**:

| This document defines | Current State holds |
|---|---|
| Decision Level and Class taxonomy | How many decisions have been logged at each level/class to date |
| Escalation trigger categories | Actual current threshold percentages/dollar amounts |
| Decision Quality Metrics (formulas, targets) | Current computed values for each metric |
| The Decision Register schema (this document, Section 24) | The actual populated rows (currently zero) |
| Postmortem, Quarterly Review, Annual Audit processes | Whether any have actually been run yet, and their findings |
| The retroactive-logging mechanism (Section 23) | The actual backlog of decisions awaiting retroactive logging ([Appendix E — Decision Record Backlog](05_CURRENT_STATE.md#appendix-e--decision-record-backlog)) |
| Bias categories and detection methods | Whether any bias pattern has actually been observed and recorded yet |
| The CM decision-system scoring dimension's definition (indirectly, via Roadmap) | The actual current CM score for that dimension ([Current Capability Maturity](05_CURRENT_STATE.md#current-capability-maturity)) |

When Current State contradicts this document's invariant rules, **this document wins** — fix Current State's report, or amend this document via a logged Governance-class DR.

### Relationship to Glossary

Canonical definitions for decision-related terms live in [`07_GLOSSARY.md`](07_GLOSSARY.md). Key terms used throughout this document, pending formal Glossary entries (see [Appendix H](#appendix-h--candidate-glossary-terms) for this document's specific additions):

| Term | Glossary entry (when published) |
|---|---|
| DRI | Directly Responsible Individual |
| Believability | Decision weight from track record and evidence quality, not rank |
| One-way / two-way door | Irreversible / reversible decision, per reversible decision theory |
| Holding OS | Atlas operating system |
| CM | Capability Maturity (score dimension from Roadmap) |
| L-level | Authority band or AI maturity level (context-dependent — always read the prefix: L0–L4 for authority/AI, DL-0–DL-4 for decisions) |

### Terminology consistency check

Because Atlas uses parallel five-tier letter-and-number scales in three different places, this document maintains an explicit disambiguation table so no reader or agent ever conflates them:

| Prefix | Scale | Defined in | Measures |
|---|---|---|---|
| **L0–L4** | Authority bands | [Organization](03_ORGANIZATION.md#authority-bands) | Who may decide |
| **L0–L4** | AI maturity model | [Brain](00_ATLAS_BRAIN.md#ai-maturity-model) | How autonomous an automation is |
| **DL-0–DL-4** | Decision Levels | This document, [Section 5](#decision-levels) | How much rigor a decision needs |
| **T1–T5** | Document tiers | [Brain](00_ATLAS_BRAIN.md#documentation-standards) | How authoritative a document is |
| **CM (0–4, per dimension)** | Capability Maturity | [Roadmap](04_ROADMAP.md#capability-maturity-model) | How mature an organizational capability is, including the decision system itself |

Any future document that introduces a new numbered maturity or authority scale should register it in this table (via a Governance-class DR touching this document) specifically to prevent the letter/number-prefix collision this table exists to avoid.

### What this document explicitly leaves to future definition

Some terms used loosely throughout this document await formal Glossary treatment beyond the candidates in [Appendix H](#appendix-h--candidate-glossary-terms) — for example, precise numeric thresholds for "material," "significant," and "meaningful" as used in various tables above. These remain deliberately qualitative in this document because the numeric calibration is instance data that belongs in [Current Governance](05_CURRENT_STATE.md#current-governance), reviewed quarterly — hardcoding a number here would violate this document's own non-duplication rule (Section 2).

---

## Document Maintenance

| Field | Value |
|---|---|
| **Canonical owner** | Brain department (Brain lead) |
| **Suggested readers** | All operators facing a non-trivial decision; department heads (deep); AI agents (as the literal schema for drafting and logging decisions); future auditors |
| **Change process** | Propose via a Governance-class Decision Record (using this document's own Section 8 pipeline) → Brain review → version bump per [Versioning Policy](00_ATLAS_BRAIN.md#versioning-policy) → update the changelog below → notify department heads if evidence/gate requirements change |
| **Review cadence** | Quarterly (aligned with T1 governance schedule) plus the Annual Decision Audit (Section 30) |
| **AI retrieval note** | Agents use this document as the literal schema for Sections 9 (templates), 24 (register), and 15 (their own participation limits); defer to [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) for current counts and threshold values; defer to [`07_GLOSSARY.md`](07_GLOSSARY.md) for terms |

### Changelog

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-08-08 | Initial release — full decision framework: authority mapping, decision levels and classes, eleven-stage pipeline, gates, templates, evidence requirements, risk/opportunity scoring, capital allocation process, AI participation rules, human override rules, escalation mechanics, reversibility doctrine, delegation and ownership rules, logging mechanics and live Register, quality metrics, bias detection, failure analysis, postmortem process, quarterly review and annual audit cadences, anti-patterns, worked examples, and appendices |
| 1.1 | 2026-08-12 | Added live Register entry **DR-2026-010** (Atlas Capital Engine + Atlas Foundry direction; Strategic / DL-4 / One-way; **Approved (provisional)** pending unmet mandatory DL-4 Financial, Market, Operational, and Stakeholder evidence). Current State instance-count sync is handled separately in `05_CURRENT_STATE.md`. |

### This document versus a decision itself

Amending this document is, itself, a Governance-class, DL-4 decision, and must be logged in the Register above using its own template — this document practices what it defines. The first entry in a future, populated Register may well be the decision that formally activated this framework.

### Known limitations of version 1.0

Stated plainly, so a future amendment has a documented starting point rather than needing to rediscover these gaps independently:

| Limitation | Why it exists at v1.0 | What would resolve it |
|---|---|---|
| The Register has never been exercised end-to-end on a real decision | Atlas is at Stage 0 — see [Current Decision System](05_CURRENT_STATE.md#current-decision-system) | The first real logged decision, ideally the retroactive logging of the "build the Brain first" decision (Example EX-1) |
| No tooling automates gate checks, SLA tracking, or metric computation | No engineering capacity has been allocated to decision-system tooling yet | A future Technical-class decision to build lightweight tooling, per [Future Expansion's "Automated decision support"](00_ATLAS_BRAIN.md#future-expansion) |
| The Register-scaling transition (inline DRs → archive files) is specified but untested | Entry count is currently zero, far below the threshold that would trigger it | Revisit once entry count approaches the 50–100 range noted in [Register scaling](#register-scaling-note) |
| No portfolio company has yet run a localized version of this framework | Zero portfolio companies exist — see [Current Assets](05_CURRENT_STATE.md#current-assets) | First acquisition or build, per [Company Lifecycle's integration standards](00_ATLAS_BRAIN.md#integration-standards-acquire--build--integrate) |
| Believability scoring has no quantitative track record to draw on yet | Zero decisions logged means zero track record to weight | Accumulates naturally as the Register populates and postmortems complete |

### Amendment proposals in flight

None as of version 1.1. Future amendment proposals should be listed here with a status (Proposed / Under review / Merged / Declined) until they are either merged into a version bump (and removed from this list, replaced by a changelog entry) or formally declined (and removed, with the decision to decline itself logged as a Governance-class DR).

### A final orientation note

Everything above this line is machinery: levels, classes, gates, templates, scoring rubrics, a register, and a review cadence. None of it replaces judgment — [Decision Philosophy](#decision-philosophy) said this at the start and it is worth repeating at the end. What the machinery buys Atlas is that judgment, once exercised, does not evaporate. It becomes a dated, evidenced, ownable, reviewable, searchable artifact — one more entry in a Register that compounds, decision by decision, into the thing no competitor can quickly copy: an organization that remembers, honestly, what it decided, why, and what actually happened next.

---

*Decisions are how Atlas turns judgment into infrastructure. A decision that is not logged has not, for organizational purposes, happened.*

*For the five-step summary and default owners, return to [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md). For why this matters at all, see [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md). For the judgment this framework operationalizes, see [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md). For who holds which authority today, see [`03_ORGANIZATION.md`](03_ORGANIZATION.md). For what has actually been decided, see [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md).*
