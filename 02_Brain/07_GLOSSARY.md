# Atlas Glossary

> The canonical, single source of truth for Atlas terminology — every organizational, AI, governance, roadmap, decision, capability-maturity, workflow, automation, finance, infrastructure, and document-authority term used across the Brain document set, defined exactly once.

**Document ID:** `07_GLOSSARY.md`
**Location:** `02_Brain/`
**Status:** Active
**Version:** 1.0
**Owner:** Brain (curation); Knowledge (maintenance); all departments (term proposals)
**Classification:** Governance — shared vocabulary
**Last updated:** 2026-08-08
**Review date:** 2026-11-08
**Supersedes:** — (first populated version; document previously existed as an empty placeholder — see [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md#current-knowledge-system))
**Authority:** This document is the authoritative source for *what a term means* across Atlas. It does not hold strategy ([`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md)), philosophical rationale ([`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md)), principle depth ([`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md)), organizational structure ([`03_ORGANIZATION.md`](03_ORGANIZATION.md)), sequencing ([`04_ROADMAP.md`](04_ROADMAP.md)), current facts ([`05_CURRENT_STATE.md`](05_CURRENT_STATE.md)), or precedent ([`06_DECISIONS.md`](06_DECISIONS.md)). Where a sibling document already defines a term in depth, this document gives the **short, canonical definition** and links to the sibling for full treatment. It never restates what a sibling already owns.

---

## Table of Contents

1. [Purpose](#purpose)
2. [Glossary Philosophy](#glossary-philosophy)
3. [How to Use This Glossary](#how-to-use-this-glossary)
4. [Document Authority](#document-authority)
5. [Alphabetical Index](#alphabetical-index)
6. [Term Categories Overview](#term-categories-overview)
7. [Organizational Terms](#organizational-terms)
8. [AI Terms](#ai-terms)
9. [Governance Terms](#governance-terms)
10. [Roadmap Terms](#roadmap-terms)
11. [Decision Framework Terms](#decision-framework-terms)
12. [Capability Maturity Terms](#capability-maturity-terms)
13. [Workflow Terminology](#workflow-terminology)
14. [Automation Terminology](#automation-terminology)
15. [Finance Terminology](#finance-terminology)
16. [Infrastructure Terminology](#infrastructure-terminology)
17. [Document Authority Terminology](#document-authority-terminology)
18. [Aliases and Synonyms](#aliases-and-synonyms)
19. [Deprecated Terms](#deprecated-terms)
20. [Naming Conventions](#naming-conventions)
21. [Abbreviation Table](#abbreviation-table)
22. [Cross References](#cross-references)
23. [Maintenance Process](#maintenance-process)
24. [Appendices](#appendices)
25. [Versioning Policy](#versioning-policy)
26. [Document Maintenance](#document-maintenance)

**Related documents:** [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) · [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) · [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) · [`03_ORGANIZATION.md`](03_ORGANIZATION.md) · [`04_ROADMAP.md`](04_ROADMAP.md) · [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) · [`06_DECISIONS.md`](06_DECISIONS.md)

---

## Purpose

### What this document is

This document is the **single canonical dictionary** for every term of art used across the Atlas Brain document set. It exists so that "holding OS," "one-way door," "DRI," "CM-3," or "DL-2" mean exactly one thing, in exactly one place, for every human operator, portfolio leader, and AI agent that reads or retrieves from the Atlas knowledge base.

Per [Knowledge compounds](02_FOUNDING_PRINCIPLES.md#knowledge-compounds) and [One source of truth](02_FOUNDING_PRINCIPLES.md#one-source-of-truth), a term defined in five places with five slightly different shades of meaning is not five conveniences — it is five liabilities. This document is the deliberate fix: **one definition per term, everywhere else links to it.**

### What this document is not

| This document is not | It lives instead in |
|---|---|
| Strategy, mission, or operating philosophy | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) |
| Founding narrative or philosophical conviction | [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) |
| Extended principle rationale, examples, and failure modes | [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) |
| Department charters, authority boundaries, escalation mechanics | [`03_ORGANIZATION.md`](03_ORGANIZATION.md) |
| Strategic sequencing, phases, horizons, milestone detail | [`04_ROADMAP.md`](04_ROADMAP.md) |
| Live instance values — actual headcount, actual thresholds, actual scores | [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) |
| Decision precedent, pipeline mechanics, and the Decision Register | [`06_DECISIONS.md`](06_DECISIONS.md) |

This document never originates a principle, a department, a phase, or a framework. It **names and defines** concepts that sibling documents originate, and it routes the reader to the document that owns the depth. When a term appears here without a clear canonical home elsewhere, that is itself a signal — flagged explicitly in [Appendix D](#appendix-d--candidate-terms-not-yet-fully-canonical) rather than invented on the spot.

### Primary audience

| Audience | How to use this document |
|---|---|
| **New operators** | Read third in the [onboarding knowledge path](00_ATLAS_BRAIN.md#onboarding-knowledge-path) — after Brain and Why, before department playbooks |
| **AI agents** | Primary retrieval target for term disambiguation; resolve every ambiguous abbreviation (e.g., "L2") against this document before acting |
| **Department heads** | Reference when writing playbooks and SOPs, to reuse canonical terms rather than invent local synonyms |
| **Portfolio operators** | Reference for Atlas-wide vocabulary that appears in reporting templates, decision records, and integration scorecards |
| **Future leaders** | Structural invariant — the vocabulary layer that lets a new generation of operators read old decisions and documents without a translator |

### Design intent

This document is built the way a well-maintained API reference is built: scannable, alphabetized, cross-linked, versioned, and boring on purpose. Per [Documentation Standards](00_ATLAS_BRAIN.md#documentation-standards), it leads with structure over prose, names owners and sources explicitly, and treats a missing definition as more useful to surface than to paper over.

### Non-goals of this document

- It does not argue for a term's importance — that rationale lives in the term's canonical source.
- It does not narrate history — a term's evolution belongs in [`06_DECISIONS.md`](06_DECISIONS.md) if a decision changed it, or in this document's [Deprecated Terms](#deprecated-terms) section if it was retired.
- It does not invent terminology to fill category quotas. Every term below is drawn from actual usage in an active Brain document.
- It does not duplicate full definitions already owned by a sibling — it summarizes and links.

---

## Glossary Philosophy

### Why a glossary is infrastructure

Per [Why Documentation Is Infrastructure](01_WHY_ATLAS_EXISTS.md#why-documentation-is-infrastructure), documentation is the interface specification between human intent and machine execution. A glossary is the **narrowest, highest-leverage slice** of that infrastructure: it is the layer beneath every other document, the shared symbol table that makes every other document parseable by a newcomer or an agent without oral tradition filling the gaps.

Without a glossary, vocabulary drifts silently. "Owner" starts meaning one thing in [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md), something subtly different in a department playbook, and a third thing in a Decision Record. Each drift is small. Compounded across dozens of documents and years of operators, drift becomes the same **structural entropy** that [Why Atlas Exists](01_WHY_ATLAS_EXISTS.md#why-traditional-companies-fail) identifies as the root failure of traditional organizations — except applied to language instead of process.

### Why exactly one definition per term

Per [One source of truth](02_FOUNDING_PRINCIPLES.md#one-source-of-truth), each concept has one authoritative document or system. For terminology specifically, **this document is that system.** Every other Brain document that uses a term of art should link here rather than redefine it. When a sibling document appears to define a term (for example, [Founding Principles' distinction](02_FOUNDING_PRINCIPLES.md#what-is-a-principle) between opinion, value, policy, process, and principle), this glossary's entry is the **short-form pointer**, and the sibling remains the canonical depth — this document does not fork the definition, it echoes and redirects.

### Definition philosophy

Every entry in this document follows the same discipline:

1. **State the definition in the fewest words that remain precise** — per [Writing standards](00_ATLAS_BRAIN.md#documentation-standards), scannable beats elegant.
2. **Name the canonical source** — the document and section where the term originates or receives full treatment. If a term has no deeper home, this document is provisionally its home, flagged as such.
3. **Surface aliases and near-synonyms explicitly** — silent synonymy is how drift begins. If two words mean the same thing, this document says so once, in [Aliases and Synonyms](#aliases-and-synonyms), rather than leaving readers to guess.
4. **Mark status** — Active, Deprecated, or Proposed. A term without a status is an unmanaged term, and unmanaged terms are how the corpus rots.
5. **Link, never duplicate rationale** — a definition explains *what*; it does not re-argue *why*. The *why* stays in the canonical source.

### Term lifecycle

Terms move through a lifecycle mirroring [Knowledge Management § Knowledge lifecycle](00_ATLAS_BRAIN.md#knowledge-management):

```
Proposed → Reviewed → Active → (optionally) Superseded → Deprecated
```

| Stage | Meaning | Who moves it |
|---|---|---|
| **Proposed** | A department has flagged a term for inclusion but Knowledge/Brain has not yet ratified the definition | Proposing department |
| **Reviewed** | Knowledge has checked the definition against actual usage in canonical sources | Knowledge head |
| **Active** | Ratified; usable as a citation target; appears in the [Alphabetical Index](#alphabetical-index) | Brain (final approval for T1/T2-affecting terms) |
| **Superseded** | Replaced by a newer or merged term; old term still resolvable but points forward | Knowledge, on proposal |
| **Deprecated** | No longer in active use; retained for historical readability of old documents and decisions | Brain + Knowledge |

See [Maintenance Process](#maintenance-process) for the full proposal-to-ratification workflow.

### Why categories, not just an alphabet

An alphabetical list alone optimizes for "I know the word, give me the meaning." Atlas also needs "I am new to a domain, show me its vocabulary as a set." This document therefore provides **both**: an [Alphabetical Index](#alphabetical-index) for lookup, and eleven category sections ([Organizational](#organizational-terms) through [Document Authority](#document-authority-terminology)) for domain onboarding — matching the categories requested when this glossary was chartered: organizational, AI, governance, roadmap, decision framework, capability maturity, workflow, automation, finance, infrastructure, document authority, and abbreviations.

A term appears in exactly **one** category section (its primary domain) even if it is used across several documents, to avoid the duplication this document exists to prevent. The [Alphabetical Index](#alphabetical-index) tags every term with that single category so lookups stay unambiguous.

---

## How to Use This Glossary

### Reading rules

1. **Look up, don't read linearly.** This document is a reference, not a narrative. Use the [Alphabetical Index](#alphabetical-index) or your editor's search function.
2. **Follow the canonical source link for depth.** Every entry's short definition is intentionally incomplete — full rationale, examples, and failure modes live at the linked source.
3. **Check status before citing.** A `Deprecated` term should not appear in new documents; use its replacement per [Deprecated Terms](#deprecated-terms).
4. **When a term you need is missing, check [Appendix D](#appendix-d--candidate-terms-not-yet-fully-canonical) before assuming it doesn't exist**, then propose it per [Maintenance Process](#maintenance-process) rather than inventing a local synonym.

### Entry anatomy

Every entry in the [category sections](#organizational-terms) below follows this shape:

```markdown
#### Term Name

**Category:** <one of the eleven categories> · **Status:** Active | Deprecated | Proposed

One-to-four sentence definition. Precise, structured, no rhetorical framing.

**Aliases:** comma-separated list, or "None"
**Canonical source:** [`document.md` § Section](document.md#anchor)
**Related terms:** [Term A](#term-a) · [Term B](#term-b)
```

Some entries that describe an ordered series (maturity levels, phases, horizons, decision gates) include an embedded reference table beneath the definition rather than one entry per level — this keeps the series's internal structure visible in one place, matching how the canonical source itself presents it.

### Reading paths by audience

| If you are… | Start with |
|---|---|
| Brand new to Atlas | [Organizational Terms](#organizational-terms), then [Governance Terms](#governance-terms) |
| Onboarding into a decision-heavy role | [Decision Framework Terms](#decision-framework-terms), then [Governance Terms](#governance-terms) |
| Building or evaluating automations | [AI Terms](#ai-terms), then [Automation Terminology](#automation-terminology) |
| Assessing where Atlas stands today | [Roadmap Terms](#roadmap-terms), then [Capability Maturity Terms](#capability-maturity-terms) |
| Writing a playbook or SOP | [Workflow Terminology](#workflow-terminology), then [Document Authority Terminology](#document-authority-terminology) |
| An AI agent resolving an abbreviation | [Abbreviation Table](#abbreviation-table) directly |

---

## Document Authority

### Authority scope

This document has authority over **term definitions only** — the canonical, short-form meaning of a word or phrase used across the Brain document set. It does not have authority over:

- **Rationale** — why a term or the concept it names matters (owned by the term's canonical source).
- **Instance values** — live numbers, names, or statuses (owned by [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md)).
- **Structure** — departments, tiers, phases, or frameworks themselves (owned by [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md), [`03_ORGANIZATION.md`](03_ORGANIZATION.md), [`04_ROADMAP.md`](04_ROADMAP.md)).
- **Precedent** — how a term was applied in a specific past decision (owned by [`06_DECISIONS.md`](06_DECISIONS.md)).

### Conflict resolution

If this document and a sibling document appear to define the same term differently:

1. **The sibling's definition governs the concept; this document's entry must be corrected to match it.** This document is downstream of every sibling for definitional accuracy — it synthesizes, it does not originate.
2. If two siblings define the same term differently from each other, that is a **sibling-to-sibling conflict**, escalated to Brain per [Single source of truth](00_ATLAS_BRAIN.md#knowledge-management), not resolved unilaterally in this document.
3. Corrections are logged the same way any documentation fix is logged — materially significant corrections (changing what a widely-cited term means) warrant a [Decision Record](06_DECISIONS.md#decision-templates).

### Why this document can exist without contradicting "one source of truth"

A glossary does not violate [One source of truth](02_FOUNDING_PRINCIPLES.md#one-source-of-truth) — it **implements** it for vocabulary specifically. Every entry below is a **pointer with a short summary**, not a second authoritative copy. Where the short summary and the canonical source could ever diverge, the canonical source wins by construction (see Conflict resolution above), which is exactly the single-canon discipline [One source of truth](02_FOUNDING_PRINCIPLES.md#one-source-of-truth) requires applied recursively to the concept of definitions themselves.

### AI retrieval note

Agents retrieving Atlas context should treat this document as the **first stop for term disambiguation** — before inferring meaning from surrounding context in another document, especially for overloaded symbols. The most important disambiguation this document performs: **the same letter-number pattern means different things in different systems.** "L2" alone is ambiguous between [AI Maturity Level 2](00_ATLAS_BRAIN.md#ai-maturity-model), [Authority Band L2](03_ORGANIZATION.md#authority-bands), and — because Atlas deliberately used a different prefix to avoid this exact collision — is **not** a valid way to refer to [Decision Level 2](06_DECISIONS.md#decision-levels), which is always written `DL-2`. See the [Abbreviation Table](#abbreviation-table) and the [L-Prefix Disambiguation](#l-prefix-disambiguation) entry for the full resolution table.

---

## Alphabetical Index

Every Active term in this document, alphabetized, tagged by category, with a one-line gloss and a jump link to its full entry. Deprecated terms are listed separately in [Deprecated Terms](#deprecated-terms) and marked `(deprecated)` here for redirect purposes only.

| Term | Category | One-line gloss | Full entry |
|---|---|---|---|
| Abbreviation | Document Authority | A shortened form of a term or phrase standardized for reuse | [→](#abbreviation) |
| Advisor (contributor type) | Organizational | Provides input with no delivery obligation | [→](#contributor) |
| Agent | AI | Software entity that executes defined automation steps under a human owner | [→](#agent) |
| Agent Design Standards | AI | Required fields every Atlas agent must define before deployment | [→](#agent-design-standards) |
| Aggregate CM Score | Capability Maturity | Average across all ten CM dimensions, used diagnostically | [→](#aggregate-cm-score) |
| AI-Assisted Decision | Decision Framework | A decision drafted or scored with AI support, capped by Decision Level | [→](#ai-assisted-decision) |
| AI Evolution Stage | Roadmap | AI-0 through AI-5 roadmap targets for AI/automation maturity by phase | [→](#ai-evolution-stage) |
| AI Maturity Model | AI | The L0–L4 scale describing how much of a process AI executes | [→](#ai-maturity-model) |
| AI-Native | AI | Organizational form where AI is core infrastructure, not a bolted-on feature | [→](#ai-native) |
| AI ROI | Finance | Measured return (time saved, error reduction, cost, quality) from an automation | [→](#ai-roi) |
| Anti-Success | Roadmap | An outcome Atlas treats as roadmap failure even if revenue grows | [→](#anti-success) |
| Arc (Capability Arc) | Roadmap | One of five long-run evolution tracks (A–E) spanning multiple phases | [→](#capability-arc) |
| Authority Band | Organizational | The L0–L4 scale of who may decide what, independent of decision size | [→](#authority-band) |
| Automation | Automation | A machine-executed process replacing manual, repeated human work | [→](#automation) |
| Automation Eligibility Criteria | Automation | The five conditions that make a task ready for automation | [→](#automation-eligibility-criteria) |
| Automation Registry | Automation | The AI department's central catalog of all production automations | [→](#automation-registry) |
| Automation Retirement | Automation | The deliberate decommissioning of an automation whose value has ended | [→](#automation-retirement) |
| Automation Spec | Automation | The required documentation template for any production automation | [→](#automation-spec) |
| Automation Vanity | AI | Deploying agents for demo value without tracked ROI | [→](#automation-vanity) |
| Automation Wave | Roadmap | W0–W5 roadmap targets for automation scope and depth by phase | [→](#automation-wave) |
| Bad News Fast | Governance | The communication norm that problems escalate immediately, without softening | [→](#bad-news-fast) |
| BAU (Business As Usual) | Workflow | Ongoing operational work, distinguished from time-bound project work | [→](#bau-business-as-usual) |
| Believability-Weighted Decision Rights | Organizational | Authority follows demonstrated track record in a domain, not title | [→](#believability-weighted-decision-rights) |
| Bias Detection | Decision Framework | Checking that decision evidence is not one-sided before it clears a gate | [→](#bias-detection) |
| Black Box Trust | AI | The failure mode of accepting AI outputs without traceability to sources | [→](#black-box-trust) |
| Brain (department) | Organizational | The strategic command center; owns governance and holding-wide direction | [→](#department) |
| Build vs. Acquire | Finance | The framework for choosing between building a venture and acquiring one | [→](#build-vs-acquire) |
| Canonical Source | Document Authority | The one document a term, fact, or standard is authoritative in | [→](#canonical-source) |
| Capability Arc | Roadmap | See Arc | [→](#capability-arc) |
| Capability Maturity Model (CM) | Capability Maturity | The ten-dimension, six-level model scoring how mature Atlas's systems are | [→](#capability-maturity-model-cm) |
| Capital Bucket | Finance | One of five categories (Operating, Growth, Infrastructure, Reserve, Experimental) capital is allocated into | [→](#capital-bucket) |
| Capital Efficiency | Governance | The principle of maximizing return per unit of capital and attention | [→](#capital-efficiency-principle) |
| Chain of Custody (for facts) | Document Authority | The documented path by which a live fact enters Current State | [→](#chain-of-custody-for-facts) |
| Chart of Accounts | Finance | The standardized ledger categories every portfolio company maps into | [→](#chart-of-accounts) |
| Classification (document field) | Document Authority | Metadata tag describing a document's governance weight | [→](#classification-document-field) |
| CM Dimension | Capability Maturity | One of ten scored axes (D1–D10) of holding capability | [→](#cm-dimension) |
| CM Level | Capability Maturity | One of six levels (0–5) describing overall maturity on a dimension or in aggregate | [→](#cm-level) |
| Coordination Tax | Organizational | The cost of alignment that grows with headcount and layers | [→](#coordination-tax) |
| Company Lifecycle | Workflow | The seven-stage path every portfolio asset moves through | [→](#company-lifecycle) |
| Compounding | Governance | Preferring actions that accumulate advantage over time over local optimization | [→](#compounding-over-optimization) |
| Contributor | Organizational | A person, agent, or vendor who performs work toward an outcome owned by someone else | [→](#contributor) |
| Cost of Capital | Finance | The minimum return Atlas must clear before capital deployment creates value | [→](#cost-of-capital) |
| Cross-Portfolio Intelligence | AI | Pattern detection across multiple portfolio assets to inform strategy | [→](#cross-portfolio-intelligence) |
| Decade Checkpoint | Roadmap | A ten-year-interval strategic checkpoint on the long-term vision | [→](#decade-checkpoint) |
| Decision Class | Decision Framework | One of five canonical decision types: Investment, Operational, Strategic, Personnel, Technical | [→](#decision-class) |
| Decision Gate | Decision Framework | One of seven mandatory checkpoints (Gate 0–6) in the decision pipeline | [→](#decision-gate) |
| Decision Level (DL) | Decision Framework | The DL-0 to DL-4 scale of how much process a decision requires | [→](#decision-level-dl) |
| Decision Lifecycle | Decision Framework | The state machine (Proposed → ... → Reviewed/Superseded) every decision moves through | [→](#decision-lifecycle) |
| Decision Pipeline | Decision Framework | The eleven ordered stages a decision passes through from intake to review | [→](#decision-pipeline) |
| Decision Record (DR) | Governance | The structured written artifact capturing a decision, its rationale, and its review date | [→](#decision-record-dr) |
| Decision Register | Decision Framework | The running log of all logged Decision Records, searchable for precedent | [→](#decision-register) |
| Deputy | Organizational | A named backup who acts for an owner without becoming co-owner | [→](#deputy) |
| Directly Responsible Individual (DRI) | Organizational | The single named human accountable for an outcome | [→](#directly-responsible-individual-dri) |
| Document Hierarchy | Governance | The T1–T5 tier system classifying documents by governance weight | [→](#document-hierarchy) |
| Document ID | Document Authority | The canonical filename identifying a governance document | [→](#document-id) |
| Dry Powder | Finance | Undeployed capital reserved for opportunistic or defensive use | [→](#dry-powder) |
| Dual-Hatting | Organizational | One person formally holding more than one department role at once | [→](#dual-hatting) |
| Entry Criteria | Roadmap | The conditions that must hold before a phase can formally begin | [→](#entry-and-exit-criteria) |
| Era (Evolution Era) | Roadmap | A multi-year evolutionary period (E0, E1, E2, E3+) spanning several phases | [→](#evolution-era) |
| Escalation | Organizational | Moving a decision or blocker to the lowest authority level capable of resolving it | [→](#escalation) |
| Escalation Threshold | Governance | The defined trigger (capital, scope, irreversibility) above which escalation is mandatory | [→](#escalation-threshold) |
| Evidence Checklist | Decision Framework | The class-specific list of evidence required before a decision clears Gate 2 | [→](#evidence-checklist) |
| Executor | Organizational | See Contributor | [→](#contributor) |
| Exit Criteria | Roadmap | The conditions that must hold before a phase can be declared complete | [→](#entry-and-exit-criteria) |
| Expansion Mode | Roadmap | One of nine named ways Atlas grows (E-Build, E-Acquire, E-Integrate-deep, etc.) | [→](#expansion-mode) |
| Extreme Documentation | Governance | The principle of documenting before, during, and after execution, always | [→](#extreme-documentation-principle) |
| Fail Loudly | Automation | The design rule that automation errors must alert an owner, never fail silently | [→](#fail-loudly) |
| Fallback | AI | The defined behavior an agent follows when it fails or is uncertain | [→](#fallback) |
| Financial Close | Finance | The periodic process of finalizing and reporting accurate financial statements | [→](#financial-close) |
| Gate (Decision Gate) | Decision Framework | See Decision Gate | [→](#decision-gate) |
| Governance Boundary | Governance | The documented line describing which body may change which kind of standard | [→](#governance-boundary) |
| Governance Council | Organizational | An advisory-only body that emerges at Org Stage 3; never an ownership committee | [→](#governance-council) |
| Guardrail | AI | An action an agent must never take without explicit human approval | [→](#guardrail) |
| Handoff | Workflow | The formal transfer of a stable output from a project to its owning department | [→](#handoff) |
| Holding Operating System (Holding OS / HOS) | Organizational | The reusable infrastructure making every portfolio company faster and smarter | [→](#holding-operating-system-holding-os--hos) |
| Horizon (Vision Horizon) | Roadmap | A multi-year strategic band (H0–H4) anchored to the fifty-year vision | [→](#vision-horizon) |
| Hurdle Rate | Finance | The minimum required return an investment must clear before capital is committed | [→](#hurdle-rate) |
| Idempotent | Automation | Property of an automation that produces the same result whether run once or repeatedly | [→](#idempotent) |
| Immutable Principle | Governance | A core principle that changes only rarely, via Brain-level governance | [→](#principle-evolution-tiers) |
| Incident Response | Workflow | The six-step protocol (Contain → Record) for handling a materialized risk | [→](#incident-response) |
| Individual Contributor (IC) | Organizational | A staff member without direct reports, distinguished from a department head | [→](#individual-contributor-ic) |
| Infrastructure Layer | Infrastructure | One of seven technical substrate layers (L-Doc through L-Edge) of the holding OS | [→](#infrastructure-layer) |
| Instance Document | Document Authority | A document reporting current facts, as opposed to defining a framework | [→](#instance-vs-type-document) |
| Integration Scorecard | Workflow | The tracked checklist measuring a newly acquired asset's integration progress | [→](#integration-scorecard) |
| Interface (department) | Organizational | The defined inputs, outputs, and SLA between two departments | [→](#interface-department) |
| Knowledge (department) | Organizational | The institutional-memory department; owns documentation standards and the knowledge base | [→](#department) |
| Knowledge Base Architecture | Infrastructure | The structural design of how Atlas's documented knowledge is organized and retrieved | [→](#knowledge-base-architecture) |
| Knowledge Evolution Stage | Roadmap | K-0 through K-5 roadmap targets for the knowledge system's maturity by phase | [→](#knowledge-evolution-stage) |
| Knowledge Lifecycle | Workflow | The five-stage cycle (Capture → Organize → Surface → Validate → Apply) every piece of knowledge moves through | [→](#knowledge-lifecycle) |
| L-Prefix Disambiguation | Document Authority | The rule distinguishing AI Maturity L-levels, Authority L-bands, and Decision DL-levels | [→](#l-prefix-disambiguation) |
| Level Inflation / Deflation | Decision Framework | The two symmetric failure modes of mis-sizing a Decision Level | [→](#level-inflation--deflation) |
| Location (document field) | Document Authority | Metadata field naming a document's folder path | [→](#location-document-field) |
| M&A (Mergers & Acquisitions) | Finance | Transactions in which Atlas acquires or divests a portfolio company | [→](#ma-mergers--acquisitions) |
| Maintenance Process | Document Authority | The workflow by which glossary terms are proposed, reviewed, and retired | [→](#maintenance-process) |
| Management Middleware | Organizational | The relay/filter/approve layer of traditional hierarchy that Atlas replaces with departments | [→](#management-middleware) |
| Metadata Block | Governance | The required header fields (Document ID, Status, Version, etc.) on every T1–T3 document | [→](#metadata-block) |
| Milestone | Roadmap | A discrete, dated, evidenced marker of roadmap progress | [→](#milestone) |
| Milestone Health State | Roadmap | The color-coded status (Green/Yellow/Red/Blue) of a milestone's progress | [→](#milestone-health-state) |
| MOIC (Multiple on Invested Capital) | Finance | The ratio of total value returned to total capital invested | [→](#moic-multiple-on-invested-capital) |
| Model-Agnostic | AI | The principle of selecting AI models by task fit, not vendor loyalty | [→](#model-agnostic) |
| MVP (Minimum Viable Product) | Finance | The smallest version of a build that tests a strategic hypothesis | [→](#mvp-minimum-viable-product) |
| NIH (Not Invented Here) | Governance | The anti-pattern of rebuilding what already exists because it feels more "ours" | [→](#nih-not-invented-here) |
| North-Star Test | Roadmap | A short question used to check whether a roadmap item is worth pursuing | [→](#north-star-test) |
| One-Way Door | Governance | A decision that is expensive or impossible to reverse | [→](#one-way-and-two-way-doors) |
| One Source of Truth | Governance | The rule that every concept has exactly one authoritative document | [→](#one-source-of-truth-principle) |
| Onboarding Knowledge Path | Workflow | The prescribed reading sequence for new operators and agents | [→](#onboarding-knowledge-path) |
| Operations (department) | Organizational | The execution-discipline department; runs day-to-day process and KPIs | [→](#department) |
| Org Stage | Organizational | One of five scale bands (0–4) describing headcount and structural maturity | [→](#org-stage) |
| Owner | Organizational | See Directly Responsible Individual | [→](#directly-responsible-individual-dri) |
| Phase (Roadmap Phase) | Roadmap | One of seven major, sequential strategic periods (P0–P6) | [→](#major-phase) |
| Playbook | Workflow | A Tier-3 document giving step-by-step guidance for a domain of work | [→](#playbook) |
| Policy | Governance | A rule governing a specific domain, changing with business conditions | [→](#opinion-value-policy-process-principle) |
| Portal | Infrastructure | The planned self-serve software surface exposing the holding OS to operators | [→](#portal) |
| Portfolio Company | Organizational | A business Atlas builds, acquires, or holds within the portfolio | [→](#portfolio-company) |
| Postmortem | Decision Framework | The structured review comparing a decision's expected and actual outcomes | [→](#postmortem) |
| Principle | Governance | An immutable statement of what Atlas optimizes for, independent of circumstance | [→](#opinion-value-policy-process-principle) |
| Process (governance layer) | Governance | A repeatable sequence of steps producing a defined output | [→](#opinion-value-policy-process-principle) |
| Project Brief | Workflow | The required planning document (scope, owner, success criteria) before execution begins | [→](#project-brief) |
| Project Health Signal | Workflow | The color-coded status (Green/Yellow/Red/Blue) of an active project | [→](#project-health-signal) |
| Project Lifecycle | Workflow | The seven-stage path (Intake → Handoff) every initiative moves through | [→](#project-lifecycle) |
| Projects (department) | Organizational | The initiative-delivery department; owns the project lifecycle | [→](#department) |
| Prompt Engineering | AI | The discipline of designing inputs to AI models for reliable, evaluable outputs | [→](#prompt-engineering) |
| RAG (Retrieval-Augmented Generation) | AI | An AI pattern that retrieves corpus content before generating a response | [→](#rag-retrieval-augmented-generation) |
| RCA (Root Cause Analysis) | Workflow | The structured investigation identifying why an incident occurred | [→](#rca-root-cause-analysis) |
| Reliability Class | Infrastructure | One of three tiers (Critical, Important, Best-effort) describing required system robustness | [→](#reliability-class) |
| Reporting Line | Organizational | The functional accountability relationship between roles, distinct from political hierarchy | [→](#reporting-line) |
| Reserve Bucket | Finance | See Capital Bucket | [→](#capital-bucket) |
| Retrospective | Workflow | The structured post-project or post-incident review that produces captured learning | [→](#retrospective) |
| Review Date | Governance | The metadata field committing a document to a future re-examination | [→](#review-date-field) |
| Reversible Decision | Governance | A decision that can be undone or corrected cheaply | [→](#one-way-and-two-way-doors) |
| Role Charter | Organizational | The Tier-3 document defining a named seat's scope, authority, and interfaces | [→](#role-charter) |
| ROI (Return on Investment) | Finance | The ratio of value gained to cost, applied to an individual bet | [→](#roi-return-on-investment) |
| ROIC (Return on Invested Capital) | Finance | Holding-level return measured across the entire deployed capital base | [→](#roic-return-on-invested-capital) |
| Runbook | Workflow | A precise, step-by-step procedure for handling a specific operational or incident scenario | [→](#runbook) |
| Seven-Department Invariant | Organizational | The rule that Atlas maintains exactly seven departments absent Brain-approved change | [→](#seven-department-invariant) |
| Shadow Governance | Governance | Informal power structures or documents that bypass documented authority | [→](#shadow-governance) |
| Single Owner Principle | Organizational | The rule that every outcome, system, document, and decision has exactly one accountable owner | [→](#single-owner-principle) |
| Sizing Test | Decision Framework | The five-question test used to assign a Decision Level in under a minute | [→](#sizing-test) |
| SLA (Service Level Agreement) | Organizational | The committed response time or standard between two departments or systems | [→](#sla-service-level-agreement) |
| Skill Atrophy | AI | The failure mode of humans losing the ability to judge AI outputs over time | [→](#skill-atrophy) |
| SOP (Standard Operating Procedure) | Automation | A Tier-4 document giving precise step-by-step execution instructions | [→](#sop-standard-operating-procedure) |
| Status (document field) | Governance | Metadata field marking a document Active, Draft, or Deprecated | [→](#status-document-field) |
| Sub-Class (decision) | Decision Framework | A finer-grained category beneath one of the five canonical decision types | [→](#sub-class-decision) |
| Success Criteria | Roadmap | Auditable, ID-tagged tests (SC-Hx-NN) that define what "success" means per horizon | [→](#success-criteria) |
| Supersedes (document field) | Document Authority | Metadata field naming the prior document this one replaces | [→](#supersedes-document-field) |
| Systems Over Heroes | Governance | The principle that repeatable infrastructure should never depend on exceptional individuals | [→](#systems-over-heroes-principle) |
| Temporary Principle | Governance | A time-bound strategic emphasis that shifts weights without overriding immutable principles | [→](#principle-evolution-tiers) |
| Tier (document tier) | Governance | See Document Hierarchy | [→](#document-hierarchy) |
| Transparency | Governance | The principle that information is visible by default to those who need it | [→](#transparency-principle) |
| Truth Over Comfort | Governance | The principle of reporting reality as it is, regardless of discomfort | [→](#truth-over-comfort-principle) |
| Two-Way Door | Governance | A decision that can be reversed cheaply | [→](#one-way-and-two-way-doors) |
| Unit Economics | Finance | The per-unit profitability of a business, independent of scale | [→](#unit-economics) |
| Value (governance layer) | Governance | A cultural aspiration, important but not always measurable or enforced | [→](#opinion-value-policy-process-principle) |
| Version (document field) | Governance | Metadata field tracking a document's MAJOR.MINOR revision number | [→](#version-document-field) |
| Weakest-Link Method | Capability Maturity | Scoring the holding's overall CM level as the minimum across all ten dimensions | [→](#weakest-link-method) |

---

## Term Categories Overview

The eleven categories below organize every Active term by primary domain. A term's category assignment reflects where it is **most used**, not every document that mentions it — cross-references throughout each entry connect it to adjacent categories.

| # | Category | Scope | Primary canonical sources |
|---|---|---|---|
| 1 | [Organizational Terms](#organizational-terms) | Departments, ownership, authority, staffing, scaling | [`00`](00_ATLAS_BRAIN.md), [`03`](03_ORGANIZATION.md) |
| 2 | [AI Terms](#ai-terms) | AI maturity, agents, models, automation intelligence | [`00`](00_ATLAS_BRAIN.md), [`02`](02_FOUNDING_PRINCIPLES.md) |
| 3 | [Governance Terms](#governance-terms) | Principles, policy, document tiers, decision doctrine | [`00`](00_ATLAS_BRAIN.md), [`02`](02_FOUNDING_PRINCIPLES.md) |
| 4 | [Roadmap Terms](#roadmap-terms) | Horizons, eras, phases, milestones, success criteria | [`04`](04_ROADMAP.md) |
| 5 | [Decision Framework Terms](#decision-framework-terms) | Levels, classes, lifecycle, pipeline, gates | [`00`](00_ATLAS_BRAIN.md), [`06`](06_DECISIONS.md) |
| 6 | [Capability Maturity Terms](#capability-maturity-terms) | CM levels and dimensions | [`04`](04_ROADMAP.md), [`05`](05_CURRENT_STATE.md) |
| 7 | [Workflow Terminology](#workflow-terminology) | Project and company lifecycles, knowledge lifecycle | [`00`](00_ATLAS_BRAIN.md), [`03`](03_ORGANIZATION.md) |
| 8 | [Automation Terminology](#automation-terminology) | Automation standards, specs, registry | [`00`](00_ATLAS_BRAIN.md) |
| 9 | [Finance Terminology](#finance-terminology) | Capital, returns, unit economics, close | [`00`](00_ATLAS_BRAIN.md), [`03`](03_ORGANIZATION.md) |
| 10 | [Infrastructure Terminology](#infrastructure-terminology) | Technical substrate layers, platform, reliability | [`04`](04_ROADMAP.md) |
| 11 | [Document Authority Terminology](#document-authority-terminology) | Metadata, tiers, canonical sourcing, instance vs type | [`00`](00_ATLAS_BRAIN.md), [`05`](05_CURRENT_STATE.md) |

---

## Organizational Terms

Terms describing how Atlas is structured, staffed, and scaled — departments, ownership, authority, and organizational growth. Full structural depth lives in [`03_ORGANIZATION.md`](03_ORGANIZATION.md); this section defines the vocabulary that document, and every department playbook beneath it, relies on.

#### Holding Operating System (Holding OS / HOS)

**Category:** Organizational · **Status:** Active

The reusable infrastructure — shared playbooks, centralized AI, a unified knowledge base, standard financial and operational reporting, and common decision frameworks — that makes every portfolio company faster, smarter, and more durable than it could be alone. Atlas's primary product is the Holding OS itself, not any single portfolio company.

**Aliases:** Holding OS, HOS, "the OS," holding operating system
**Canonical source:** [`00_ATLAS_BRAIN.md` § The holding as product](00_ATLAS_BRAIN.md#the-holding-as-product)
**Related terms:** [Department](#department) · [Portfolio Company](#portfolio-company) · [Compounding](#compounding-over-optimization)

#### Department

**Category:** Organizational · **Status:** Active

A permanent ownership domain aligned to one layer of the Holding OS. Atlas maintains exactly seven: Brain (strategy, governance), Knowledge (institutional memory), AI (intelligent infrastructure), Finance (capital and economic truth), Operations (execution discipline), Assets (portfolio ownership), and Projects (initiative delivery). Departments are domains, not headcount containers — a department may be staffed by one dual-hatted person or fifty specialists without changing its mission.

**Aliases:** None
**Canonical source:** [`03_ORGANIZATION.md` § Department Architecture Overview](03_ORGANIZATION.md#department-architecture-overview)
**Related terms:** [Seven-Department Invariant](#seven-department-invariant) · [Holding Operating System](#holding-operating-system-holding-os--hos) · [Interface](#interface-department)

#### Directly Responsible Individual (DRI)

**Category:** Organizational · **Status:** Active

The single named human accountable for an outcome, system, document, decision, agent, or open issue — never a committee, never "the team." The DRI defines success criteria, assigns and unblocks contributors, makes final calls within their authority band, escalates when blocked, and captures lessons when outcomes diverge from plan.

**Aliases:** Owner, DRI
**Canonical source:** [`03_ORGANIZATION.md` § Single Owner Principle](03_ORGANIZATION.md#single-owner-principle)
**Related terms:** [Contributor](#contributor) · [Deputy](#deputy) · [Single Owner Principle](#single-owner-principle)

#### Single Owner Principle

**Category:** Organizational · **Status:** Active

The organizational rule that exactly one human owner exists per outcome, system, document, decision, agent, and open issue — not zero, not two. Committees advise; they do not own. This principle is the organizational implementation of the [Ownership](02_FOUNDING_PRINCIPLES.md#ownership) founding principle.

**Aliases:** Single-threaded ownership
**Canonical source:** [`03_ORGANIZATION.md` § Single Owner Principle](03_ORGANIZATION.md#single-owner-principle)
**Related terms:** [Directly Responsible Individual (DRI)](#directly-responsible-individual-dri) · [Committee Anti-Pattern](#single-owner-principle)

#### Contributor

**Category:** Organizational · **Status:** Active

A person, AI agent, vendor, or portfolio team that performs work toward an outcome owned by someone else. Contributors execute; they do not carry accountability for the outcome itself. Sub-types include human contributor, AI agent, vendor, advisory contributor (input only, no delivery obligation), and cross-department contributor (loaned expertise).

**Aliases:** Executor
**Canonical source:** [`03_ORGANIZATION.md` § Contributor Model](03_ORGANIZATION.md#contributor-model)
**Related terms:** [Directly Responsible Individual (DRI)](#directly-responsible-individual-dri) · [Ownership vs. Execution](#directly-responsible-individual-dri)

#### Deputy

**Category:** Organizational · **Status:** Active

A named backup who acts for an owner when the owner is unavailable. A deputy is not a co-owner — the owner retains full accountability, and the deputy relationship must be documented in writing, never implicit.

**Aliases:** None
**Canonical source:** [`03_ORGANIZATION.md` § Single Owner Principle](03_ORGANIZATION.md#single-owner-principle)
**Related terms:** [Directly Responsible Individual (DRI)](#directly-responsible-individual-dri) · [Org Stage](#org-stage)

#### Individual Contributor (IC)

**Category:** Organizational · **Status:** Active

A staff member who executes work directly within a department but does not hold department-head or DRI-level authority over the department's outcomes. Distinguished from a department head, who may still function as an IC in a small organization.

**Aliases:** IC
**Canonical source:** [`03_ORGANIZATION.md` § Organizational Scaling](03_ORGANIZATION.md#organizational-scaling)
**Related terms:** [Org Stage](#org-stage) · [Reporting Line](#reporting-line)

#### Authority Band

**Category:** Organizational · **Status:** Active

The five-tier scale (L0–L4) describing **who may decide what**, independent of how large the decision is. Distinct from [Decision Level](#decision-level-dl), which describes how much process a specific decision requires — Authority Band describes standing decision rights.

| Band | Scope | Typical holder |
|---|---|---|
| **L0 — Operational** | Reversible, within SOP, below spend threshold | Process owner, operator |
| **L1 — Departmental** | Affects one department, reversible | Department head |
| **L2 — Cross-department** | Affects 2+ departments or portfolio | Relevant heads + sponsor |
| **L3 — Holding** | Strategic, capital, irreversible | Brain + Finance/Assets as needed |
| **L4 — Governance** | Principles, structure, T1 documents | Brain (+ board if applicable) |

**Aliases:** L-band
**Canonical source:** [`03_ORGANIZATION.md` § Decision Authority](03_ORGANIZATION.md#decision-authority)
**Related terms:** [Decision Level (DL)](#decision-level-dl) · [AI Maturity Model](#ai-maturity-model) · [L-Prefix Disambiguation](#l-prefix-disambiguation)

#### Believability-Weighted Decision Rights

**Category:** Organizational · **Status:** Active

The organizational principle — borrowed explicitly from Ray Dalio's Bridgewater — that authority in a domain follows demonstrated competence documented in outcomes, not tenure, title, or proximity to power. A portfolio operator with a strong multi-year track record has believability on product decisions for their asset; Finance has believability on capital structure.

**Aliases:** Believability
**Canonical source:** [`03_ORGANIZATION.md` § The Ray Dalio principle applied to Atlas](03_ORGANIZATION.md#organizational-philosophy)
**Related terms:** [Decision Authority](#authority-band) · [Evidence Over Opinion](#evidence-over-opinion-principle)

#### Escalation

**Category:** Organizational · **Status:** Active

The act of moving a decision or blocker to the **lowest authority level capable of resolving it** — not the highest title available. Escalation is a designed feature of the system, not evidence of failure; suppressing legitimate escalation trains silence and is itself a named anti-pattern.

**Aliases:** None
**Canonical source:** [`03_ORGANIZATION.md` § Escalation Authority](03_ORGANIZATION.md#escalation-authority)
**Related terms:** [Escalation Threshold](#escalation-threshold) · [Authority Band](#authority-band)

#### Coordination Tax

**Category:** Organizational · **Status:** Active

The cost of alignment — meetings, handoff friction, reconciliation — that grows with every additional person, department, and location in a traditional hierarchy. Atlas's department model and single-owner discipline exist specifically to keep this tax sublinear as headcount grows; it is monitored via periodic "coordination tax audits" at scale.

**Aliases:** None
**Canonical source:** [`01_WHY_ATLAS_EXISTS.md` § The coordination tax](01_WHY_ATLAS_EXISTS.md#why-traditional-companies-fail)
**Related terms:** [Management Middleware](#management-middleware) · [Org Stage](#org-stage)

#### Dual-Hatting

**Category:** Organizational · **Status:** Active

The practice of one person formally holding more than one department role at once, typical at early Org Stages. Dual-hatting requires labeling which "hat" is worn in writing for any material action, to preserve single-owner clarity even when the owner is the same human across roles.

**Aliases:** Dual-hat
**Canonical source:** [`03_ORGANIZATION.md` § Stage 0: One operator](03_ORGANIZATION.md#organizational-scaling)
**Related terms:** [Org Stage](#org-stage) · [Directly Responsible Individual (DRI)](#directly-responsible-individual-dri)

#### Org Stage

**Category:** Organizational · **Status:** Active

One of five bands (0–4) describing an organization's headcount and structural maturity, distinct from [Capability Maturity](#capability-maturity-model-cm) (which measures system quality, not headcount) and [AI Maturity](#ai-maturity-model) (which measures automation depth). The seven departments remain invariant across every stage; only staffing and interface complexity scale.

| Stage | Approx. headcount | Profile |
|---|---|---|
| **Stage 0** | 1 | Founder/holding lead; possibly zero employees; all seven hats worn by one person |
| **Stage 1** | ~10 | One human per core department (or dual-hatted); first portfolio asset live |
| **Stage 2** | ~50 | Multiple ICs per department; 3–8 portfolio assets; integration playbook proven |
| **Stage 3** | ~200 | Full department benches; international portfolio; holding OS mature |
| **Stage 4** | 1000+ | Multi-sector portfolio; Atlas OS licensed or replicated; generational leadership transition |

**Aliases:** Scale stage
**Canonical source:** [`03_ORGANIZATION.md` § Organizational Scaling](03_ORGANIZATION.md#organizational-scaling)
**Related terms:** [Coordination Tax](#coordination-tax) · [Dual-Hatting](#dual-hatting) · [Major Phase](#major-phase)

#### Seven-Department Invariant

**Category:** Organizational · **Status:** Active

The structural rule that Atlas maintains exactly seven canonical departments (Brain, Knowledge, AI, Finance, Operations, Assets, Projects) at every scale, unless Brain explicitly approves a structural change via Decision Record. Sub-teams, squads, and portfolio-local organizations exist inside or adjacent to these seven; they never replace them.

**Aliases:** None
**Canonical source:** [`03_ORGANIZATION.md` § Why Departments Instead of Management Layers](03_ORGANIZATION.md#why-departments-instead-of-management-layers)
**Related terms:** [Department](#department) · [Governance Boundary](#governance-boundary)

#### Management Middleware

**Category:** Organizational · **Status:** Active

The relay-filter-approve function performed by middle managers in traditional hierarchies — aggregating status, routing information, enforcing compliance, escalating exceptions. Atlas treats this function as software-replaceable and structurally rejects it as a default, replacing it with documented departments, ownership, and AI-assisted routing.

**Aliases:** Middleware management, relay layer
**Canonical source:** [`01_WHY_ATLAS_EXISTS.md` § Why Software Is Replacing Management](01_WHY_ATLAS_EXISTS.md#why-software-is-replacing-management)
**Related terms:** [Coordination Tax](#coordination-tax) · [Seven-Department Invariant](#seven-department-invariant)

#### Interface (department)

**Category:** Organizational · **Status:** Active

The defined inputs, outputs, and service-level agreement between two departments, used instead of standing sync meetings to coordinate work. Every department pair in the [Cross-department interaction matrix](00_ATLAS_BRAIN.md#cross-department-interaction-matrix) has a documented interface.

**Aliases:** None
**Canonical source:** [`03_ORGANIZATION.md` § Department Interfaces](03_ORGANIZATION.md#department-brain)
**Related terms:** [SLA (Service Level Agreement)](#sla-service-level-agreement) · [Department](#department)

#### SLA (Service Level Agreement)

**Category:** Organizational · **Status:** Active

The committed response time or quality standard governing an interface between two departments, an automation and its users, or a vendor relationship. Used internally between departments, not only externally with vendors.

**Aliases:** None
**Canonical source:** [`03_ORGANIZATION.md` § Interfaces with other departments](03_ORGANIZATION.md#department-brain)
**Related terms:** [Interface (department)](#interface-department)

#### Reporting Line

**Category:** Organizational · **Status:** Active

The functional accountability relationship between roles — who a role answers to for outcomes — distinct from political hierarchy or title seniority. Reporting lines are flat at Org Stage 0–1 and grow only as demonstrated need requires, per [Scaling Without Changing Principles](03_ORGANIZATION.md#scaling-without-changing-principles).

**Aliases:** None
**Canonical source:** [`03_ORGANIZATION.md` § Reporting Relationships](03_ORGANIZATION.md#organizational-scaling)
**Related terms:** [Org Stage](#org-stage) · [Individual Contributor (IC)](#individual-contributor-ic)

#### Role Charter

**Category:** Organizational · **Status:** Active

A Tier-3 document defining a named seat's scope, authority, interfaces, and success criteria. Role charters become mandatory at Org Stage 1 and are the mechanism by which "the org chart lives in documents, not in meetings."

**Aliases:** None
**Canonical source:** [`03_ORGANIZATION.md` § The Stripe principle applied to Atlas](03_ORGANIZATION.md#organizational-philosophy)
**Related terms:** [Document Hierarchy](#document-hierarchy) · [Org Stage](#org-stage)

#### Governance Council

**Category:** Organizational · **Status:** Active

An advisory-only body that typically emerges around Org Stage 3, providing counsel and challenge to Brain. It is explicitly **not** an ownership committee — it never holds a Single Owner Principle exemption, per [Committee Anti-Pattern](03_ORGANIZATION.md#single-owner-principle).

**Aliases:** None
**Canonical source:** [`03_ORGANIZATION.md` § Stage 3: ~200 people](03_ORGANIZATION.md#organizational-scaling)
**Related terms:** [Single Owner Principle](#single-owner-principle) · [Org Stage](#org-stage)

#### Portfolio Company

**Category:** Organizational · **Status:** Active

A business Atlas builds, acquires, or holds within the portfolio, connected to the Holding OS but retaining local autonomy within holding standards. See [Company Lifecycle](#company-lifecycle) for the stages a portfolio company moves through, and [Portfolio Company Autonomy Spectrum](00_ATLAS_BRAIN.md#portfolio-company-autonomy-spectrum) for what is standardized versus locally controlled.

**Aliases:** Portfolio asset, asset (in the M&A sense)
**Canonical source:** [`00_ATLAS_BRAIN.md` § Company Lifecycle](00_ATLAS_BRAIN.md#company-lifecycle)
**Related terms:** [Company Lifecycle](#company-lifecycle) · [Holding Operating System](#holding-operating-system-holding-os--hos)

---

## AI Terms

Terms describing how AI functions as core infrastructure inside Atlas — maturity, agents, models, and the guardrails that keep humans accountable. Strategic depth lives in [AI Strategy](00_ATLAS_BRAIN.md#ai-strategy) and [AI-first thinking](02_FOUNDING_PRINCIPLES.md#ai-first-thinking).

#### AI-Native

**Category:** AI · **Status:** Active

An organizational form in which AI is designed into every workflow, role, and system as core infrastructure from the start — equivalent to finance systems — rather than added as a feature after humans burn out. Distinguished explicitly from "bolt-on AI," which retains human bureaucracy with a chatbot interface.

**Aliases:** AI-first
**Canonical source:** [`01_WHY_ATLAS_EXISTS.md` § Why AI-Native Organizations Outperform Human Bureaucracy](01_WHY_ATLAS_EXISTS.md#why-ai-native-organizations-outperform-human-bureaucracy)
**Related terms:** [AI Maturity Model](#ai-maturity-model) · [AI-First Thinking](#ai-native)

#### AI Maturity Model

**Category:** AI · **Status:** Active

The five-level scale (L0–L4) describing how much of a process AI executes versus a human. This is a **process-level** scale — it describes one workflow at a time, not the whole organization (contrast with [Capability Maturity Model](#capability-maturity-model-cm), which scores the holding overall).

| Level | Name | Description |
|---|---|---|
| **L0** | Manual | No AI involvement; acceptable only for novel or high-stakes work |
| **L1** | Assisted | AI drafts, suggests, or analyzes; human executes and approves |
| **L2** | Supervised automation | AI executes routine steps; human reviews exceptions and outputs |
| **L3** | Autonomous | AI executes end-to-end within guardrails; human monitors metrics |
| **L4** | Self-improving | AI detects degradation, suggests improvements, adapts within bounds |

Default target for any repeated process: **L2 or higher within 90 days** of process stabilization.

**Aliases:** AI L-level, process maturity level
**Canonical source:** [`00_ATLAS_BRAIN.md` § AI Strategy](00_ATLAS_BRAIN.md#ai-maturity-model)
**Related terms:** [Authority Band](#authority-band) · [Decision Level (DL)](#decision-level-dl) · [L-Prefix Disambiguation](#l-prefix-disambiguation)

#### Agent

**Category:** AI · **Status:** Active

A software entity that executes defined automation steps on behalf of Atlas, under a named human owner. Every Atlas agent must define its purpose, trigger, inputs, outputs, guardrails, owner, evaluation method, and fallback behavior before deployment.

**Aliases:** AI agent
**Canonical source:** [`00_ATLAS_BRAIN.md` § Agent design standards](00_ATLAS_BRAIN.md#ai-strategy)
**Related terms:** [Agent Design Standards](#agent-design-standards) · [Guardrail](#guardrail) · [Fallback](#fallback)

#### Agent Design Standards

**Category:** AI · **Status:** Active

The required set of fields — purpose, trigger, inputs, outputs, guardrails, owner, evaluation, fallback — that every Atlas agent must define before it is deployed to production. No production agent exists without a human owner and a documented fallback path.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Agent design standards](00_ATLAS_BRAIN.md#ai-strategy)
**Related terms:** [Agent](#agent) · [Automation Spec](#automation-spec) · [Human Accountability Principle](#human-accountability-principle)

#### Guardrail

**Category:** AI · **Status:** Active

An action an agent must never take without explicit human approval, defined as part of every agent's design specification. Guardrails are the primary mechanism by which autonomy (higher AI Maturity levels) coexists with [Human Accountability](#human-accountability-principle).

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Agent design standards](00_ATLAS_BRAIN.md#ai-strategy)
**Related terms:** [Agent Design Standards](#agent-design-standards) · [Fallback](#fallback)

#### Fallback

**Category:** AI · **Status:** Active

The defined behavior an agent follows when it fails, encounters an edge case, or is uncertain — typically escalation to a named human owner. Every production agent must have a documented fallback path; "the algorithm decided" is never an acceptable postmortem conclusion.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Agent design standards](00_ATLAS_BRAIN.md#ai-strategy)
**Related terms:** [Guardrail](#guardrail) · [Human Accountability Principle](#human-accountability-principle)

#### Model-Agnostic

**Category:** AI · **Status:** Active

The principle of selecting AI models by task fit, cost, latency, and accuracy — not by vendor loyalty — and evaluating that fit continuously rather than once. Atlas maintains no permanent commitment to any single model provider.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § AI Strategy](00_ATLAS_BRAIN.md#ai-strategy)
**Related terms:** [Model Evaluation](#model-evaluation)

#### Model Evaluation

**Category:** AI · **Status:** Active

The structured comparison of AI models against task-specific benchmarks (accuracy, cost, latency) that precedes any model selection or vendor change, per the [Model-Agnostic](#model-agnostic) principle.

**Aliases:** None
**Canonical source:** [`03_ORGANIZATION.md` § Department: AI](03_ORGANIZATION.md#department-ai)
**Related terms:** [Model-Agnostic](#model-agnostic)

#### Prompt Engineering

**Category:** AI · **Status:** Active

The discipline of designing inputs to AI models so that outputs are reliable, evaluable, and traceable to sources — one of the AI department's core responsibilities.

**Aliases:** None
**Canonical source:** [`03_ORGANIZATION.md` § Department: AI § Scope](03_ORGANIZATION.md#department-ai)
**Related terms:** [Agent](#agent) · [RAG (Retrieval-Augmented Generation)](#rag-retrieval-augmented-generation)

#### RAG (Retrieval-Augmented Generation)

**Category:** AI · **Status:** Active

An AI architecture pattern in which a model retrieves relevant corpus content — playbooks, decisions, glossary entries — before generating a response, so outputs are grounded in Atlas's actual documented knowledge rather than the model's unaided memory.

**Aliases:** Retrieval-augmented generation
**Canonical source:** [`03_ORGANIZATION.md` § Department: Knowledge § Interfaces](03_ORGANIZATION.md#department-knowledge)
**Related terms:** [Knowledge Base Architecture](#knowledge-base-architecture) · [Cross-Portfolio Intelligence](#cross-portfolio-intelligence)

#### AI Adoption Process

**Category:** AI · **Status:** Active

The six-stage path (Identify → Spec → Prototype → Evaluate → Deploy → Document) an automation candidate follows from first observation to production maturity.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § AI adoption process](00_ATLAS_BRAIN.md#ai-adoption-process)
**Related terms:** [Automation Eligibility Criteria](#automation-eligibility-criteria) · [AI Maturity Model](#ai-maturity-model)

#### AI ROI

**Category:** AI · **Status:** Active

The measured return from an automation — combining time saved, error reduction, cost impact, and quality improvement — tracked explicitly for every deployed agent rather than assumed from its existence.

**Aliases:** Automation ROI
**Canonical source:** [`00_ATLAS_BRAIN.md` § Strategic objectives](00_ATLAS_BRAIN.md#ai-strategy)
**Related terms:** [Automation Vanity](#automation-vanity) · [ROI (Return on Investment)](#roi-return-on-investment)

#### Cross-Portfolio Intelligence

**Category:** AI · **Status:** Active

Pattern detection across multiple portfolio assets — which integrations succeed, which operational changes stick, which market entries exceed projections — that no single asset's data alone could reveal. A planned late-phase capability, not a current one; see [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) for live status.

**Aliases:** Portfolio intelligence
**Canonical source:** [`01_WHY_ATLAS_EXISTS.md` § Network effects of institutional memory](01_WHY_ATLAS_EXISTS.md#why-compounding-knowledge-is-the-greatest-competitive-advantage)
**Related terms:** [AI Evolution Stage](#ai-evolution-stage) · [RAG (Retrieval-Augmented Generation)](#rag-retrieval-augmented-generation)

#### Automation Vanity

**Category:** AI · **Status:** Active

The failure mode of deploying agents for demo value or optics rather than tracked, positive ROI. Guarded against by requiring an evaluation period before any automation is promoted in maturity level.

**Aliases:** Automation theater
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § AI-first thinking § Failure modes](02_FOUNDING_PRINCIPLES.md#ai-first-thinking)
**Related terms:** [AI ROI](#ai-roi) · [Anti-Success](#anti-success)

#### Skill Atrophy

**Category:** AI · **Status:** Active

The failure mode of humans gradually losing the ability to critically judge AI outputs as automation deepens, guarded against through training, sampling, and periodic manual runs.

**Aliases:** None
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § AI-first thinking § Failure modes](02_FOUNDING_PRINCIPLES.md#ai-first-thinking)
**Related terms:** [Black Box Trust](#black-box-trust) · [Human Accountability Principle](#human-accountability-principle)

#### Black Box Trust

**Category:** AI · **Status:** Active

The failure mode of accepting AI outputs without traceability to sources or evaluation metrics. Guarded against by requiring source citation and confidence/evaluation data on any AI output that informs a decision.

**Aliases:** None
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § AI-first thinking § Failure modes](02_FOUNDING_PRINCIPLES.md#ai-first-thinking)
**Related terms:** [Skill Atrophy](#skill-atrophy) · [Human Accountability Principle](#human-accountability-principle)

#### AI-Assisted Decision

**Category:** Decision Framework · **Status:** Active

A decision whose drafting, evidence-gathering, or scoring was supported by an AI agent, capped at Supervised (L2) AI Maturity for any decision at DL-2 or above — meaning AI may draft and score, but a human must review before the decision advances past evidence-gathering. See [`06_DECISIONS.md` § AI-Assisted Decisions](06_DECISIONS.md#decision-levels) for the full cap rule.

**Aliases:** None
**Canonical source:** [`06_DECISIONS.md` § AI-Assisted Decisions](06_DECISIONS.md#decision-pipeline)
**Related terms:** [AI Maturity Model](#ai-maturity-model) · [Decision Level (DL)](#decision-level-dl)

---

## Governance Terms

Terms describing how Atlas defines, layers, and enforces judgment — principles, policy, document tiers, and the doctrines that keep decisions consistent across time and operators. Full depth lives in [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) and [Documentation Standards](00_ATLAS_BRAIN.md#documentation-standards).

#### Opinion, Value, Policy, Process, Principle

**Category:** Governance · **Status:** Active

The five layers of organizational guidance Atlas distinguishes explicitly, ordered from least to most durable:

| Layer | Definition | Changes when |
|---|---|---|
| **Opinion** | One person's current belief, unsupported by evidence or precedent | New information arrives |
| **Value** | A cultural aspiration; important but not always measurable | Rarely; signals identity |
| **Policy** | A rule governing a specific domain or situation | Business conditions, regulation, scale |
| **Process** | A repeatable sequence of steps producing a defined output | Optimization, tooling, scale |
| **Principle** | An immutable optimization target for judgment | Almost never; requires Brain-level governance |

Confusing these layers causes either rigidity (treating policy as immutable) or drift (treating principles as suggestions).

**Aliases:** None
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § What Is a Principle](02_FOUNDING_PRINCIPLES.md#what-is-a-principle)
**Related terms:** [Principle Hierarchy](#principle-hierarchy) · [Principle Evolution Tiers](#principle-evolution-tiers)

#### Principle Hierarchy

**Category:** Governance · **Status:** Active

The resolution order Atlas applies when two principles conflict: (1) Long-term thinking, (2) Evidence over opinion / Data before intuition, (3) Extreme documentation, (4) Systems over heroes, (5) Automation by default. Non-obvious resolutions are logged in [`06_DECISIONS.md`](06_DECISIONS.md).

**Aliases:** None
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § Principle Hierarchy](02_FOUNDING_PRINCIPLES.md#principle-hierarchy)
**Related terms:** [Opinion, Value, Policy, Process, Principle](#opinion-value-policy-process-principle) · [Conflicts Between Principles](#principle-hierarchy)

#### Principle Evolution Tiers

**Category:** Governance · **Status:** Active

The three mutation-rate classes Atlas sorts guidance into, to prevent both dangerous drift and sclerotic rigidity:

| Tier | What | Change authority | Expected frequency |
|---|---|---|---|
| **Immutable principle** | Core principles — the identity of Atlas | Brain-level governance + Decision Record | Rare — years, not quarters |
| **Slow-changing principle / decision rule** | Framework weights, thresholds, capital policy, AI maturity defaults | Brain + relevant department owner | Adjustments annually |
| **Temporary principle** | Time-bound strategic emphasis that shifts weights without overriding immutable principles | Brain; mandatory end date | Per strategic phase |

A "temporary" exception to an immutable principle (e.g., a temporary truth delay) is never acceptable.

**Aliases:** None
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § Principle Evolution](02_FOUNDING_PRINCIPLES.md#principle-evolution)
**Related terms:** [Principle Exception](#principle-exception) · [Governance Boundary](#governance-boundary)

#### Principle Exception

**Category:** Governance · **Status:** Active

An explicitly documented, Brain-approved deviation from a Core or Founding Principle, always requiring written rationale and a review/sunset date. Principle exceptions are, by design, rare — normalized exceptions are a named roadmap anti-success (identity erosion).

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Core Principles](00_ATLAS_BRAIN.md#core-principles)
**Related terms:** [Principle Evolution Tiers](#principle-evolution-tiers) · [Anti-Success](#anti-success)

#### One-Way and Two-Way Doors

**Category:** Governance · **Status:** Active

Borrowed from reversible decision theory: a **two-way door** is a decision that can be reversed cheaply (default: decide quickly, delegate down, document lightly). A **one-way door** is a decision that is expensive or impossible to reverse (default: full decision framework, Brain involvement, comprehensive documentation). When uncertain which applies, Atlas treats a decision as one-way until proven otherwise.

**Aliases:** Reversible decision (two-way door), irreversible commitment (one-way door)
**Canonical source:** [`00_ATLAS_BRAIN.md` § One-way vs. two-way doors](00_ATLAS_BRAIN.md#one-way-vs-two-way-doors)
**Related terms:** [Escalation Threshold](#escalation-threshold) · [Decision Level (DL)](#decision-level-dl)

#### One Source of Truth Principle

**Category:** Governance · **Status:** Active

The founding principle that each concept has exactly one authoritative document or system; every other reference links to it rather than duplicating or contradicting it. This glossary is itself an application of this principle to vocabulary specifically.

**Aliases:** Single source of truth
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § One source of truth](02_FOUNDING_PRINCIPLES.md#one-source-of-truth)
**Related terms:** [Shadow Governance](#shadow-governance) · [Canonical Source](#canonical-source)

#### Truth Over Comfort Principle

**Category:** Governance · **Status:** Active

The founding principle of seeking and reporting reality as it is, not as anyone wishes it were — bad news travels fast, narrative is subordinate to evidence, and discomfort is never a reason to delay truth.

**Aliases:** Truth over narrative
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § Truth over comfort](02_FOUNDING_PRINCIPLES.md#truth-over-comfort)
**Related terms:** [Bad News Fast](#bad-news-fast) · [Transparency Principle](#transparency-principle)

#### Human Accountability Principle

**Category:** Governance · **Status:** Active

The founding principle that a human, never an algorithm, is always accountable for AI-assisted outcomes — "the algorithm decided" is never an acceptable postmortem conclusion. Every agent has a named human owner; every AI-assisted decision has a human who reviewed and could have stopped it.

**Aliases:** Human accountability, human-in-the-loop accountability
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § AI-first thinking](02_FOUNDING_PRINCIPLES.md#ai-first-thinking)
**Related terms:** [Agent Design Standards](#agent-design-standards) · [Guardrail](#guardrail) · [Fallback](#fallback) · [Skill Atrophy](#skill-atrophy)

#### Bad News Fast

**Category:** Governance · **Status:** Active

The communication norm that problems escalate immediately, without waiting for a recovery plan or more certainty — surprises are treated as failures of communication, not merely of the underlying problem.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Communication Principles](00_ATLAS_BRAIN.md#communication-principles)
**Related terms:** [Truth Over Comfort Principle](#truth-over-comfort-principle)

#### Evidence Over Opinion Principle

**Category:** Governance · **Status:** Active

The founding principle that opinions are hypotheses to be tested, not conclusions to be defended — decisions above trivial impact require written evidence before commitment.

**Aliases:** Data before intuition, data-driven decisions
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § Evidence over opinion](02_FOUNDING_PRINCIPLES.md#evidence-over-opinion)
**Related terms:** [Believability-Weighted Decision Rights](#believability-weighted-decision-rights) · [Evidence Checklist](#evidence-checklist)

#### Systems Over Heroes Principle

**Category:** Governance · **Status:** Active

The founding principle that repeatable, improvable infrastructure should produce excellent outcomes without requiring exceptional individuals. A heroic save is treated as a system-failure signal, triggering a postmortem asking what system should exist so heroics are never required again.

**Aliases:** Systems over heroics
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § Systems over heroes](02_FOUNDING_PRINCIPLES.md#systems-over-heroes)
**Related terms:** [Extreme Documentation Principle](#extreme-documentation-principle) · [Playbook](#playbook)

#### Compounding Over Optimization

**Category:** Governance · **Status:** Active

The founding principle of preferring actions that accumulate advantage over time over actions that maximize immediate local efficiency — building knowledge, systems, relationships, and capabilities that grow in value with reuse.

**Aliases:** Compounding
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § Compounding over optimization](02_FOUNDING_PRINCIPLES.md#compounding-over-optimization)
**Related terms:** [Holding Operating System](#holding-operating-system-holding-os--hos) · [Knowledge Lifecycle](#knowledge-lifecycle)

#### Extreme Documentation Principle

**Category:** Governance · **Status:** Active

The founding principle of documenting before, during, and after execution — nothing important lives only in someone's head. Documentation is treated as infrastructure and, in an AI-native organization, as the interface specification for intelligence.

**Aliases:** Documentation before execution
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § Extreme documentation](02_FOUNDING_PRINCIPLES.md#extreme-documentation)
**Related terms:** [Systems Over Heroes Principle](#systems-over-heroes-principle) · [Document Hierarchy](#document-hierarchy)

#### Transparency Principle

**Category:** Governance · **Status:** Active

The founding principle that information is visible by default to those who need it for good decisions; secrecy requires justification, not the reverse. Bounded by legitimate legal, contractual, and privacy obligations.

**Aliases:** None
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § Transparency](02_FOUNDING_PRINCIPLES.md#transparency)
**Related terms:** [Transparency vs. Security](#shadow-governance) · [Bad News Fast](#bad-news-fast)

#### Capital Efficiency Principle

**Category:** Governance · **Status:** Active

The founding principle of deploying financial resources to maximize return per unit of capital and attention — not to maximize spending, headcount, or activity.

**Aliases:** None
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § Capital efficiency](02_FOUNDING_PRINCIPLES.md#capital-efficiency)
**Related terms:** [Hurdle Rate](#hurdle-rate) · [Build vs. Acquire](#build-vs-acquire)

#### NIH (Not Invented Here)

**Category:** Governance · **Status:** Active

The anti-pattern of rebuilding a capability that already exists — internally or via a vendor — because it "feels more ours," rather than because differentiation is real. Named explicitly as a counter-example under both [Build before buy](02_FOUNDING_PRINCIPLES.md#build-before-buy) and [Compounding over optimization](02_FOUNDING_PRINCIPLES.md#compounding-over-optimization).

**Aliases:** Not Invented Here syndrome
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § Build before buy § Counter-examples](02_FOUNDING_PRINCIPLES.md#build-before-buy)
**Related terms:** [Build vs. Acquire](#build-vs-acquire)

#### Metadata Block

**Category:** Governance · **Status:** Active

The required header fields — Document ID, Location, Status, Version, Owner, Last updated, Review date, and (for T1/T2 documents) Classification, Supersedes, and Authority — that every Tier-1 through Tier-3 document must carry. Skipping the metadata block is treated as skipping documentation itself.

**Aliases:** Header block
**Canonical source:** [`00_ATLAS_BRAIN.md` § Required metadata](00_ATLAS_BRAIN.md#documentation-standards)
**Related terms:** [Document Hierarchy](#document-hierarchy) · [Status (document field)](#status-document-field)

#### Status (document field)

**Category:** Governance · **Status:** Active

The metadata field marking a document `Active`, `Draft`, or `Deprecated`. A deprecated document is never deleted — it is marked, pointed to its replacement, and retained for historical context.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Deprecation](00_ATLAS_BRAIN.md#documentation-standards)
**Related terms:** [Metadata Block](#metadata-block) · [Supersedes (document field)](#supersedes-document-field)

#### Version (document field)

**Category:** Governance · **Status:** Active

The metadata field tracking a document's MAJOR.MINOR revision number. A structural change, new section, or principle change bumps MAJOR; a content expansion or clarification bumps MINOR; a typo or formatting fix requires no bump but a changelog note.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Versioning Policy](00_ATLAS_BRAIN.md#versioning-policy)
**Related terms:** [Metadata Block](#metadata-block) · [Review Date (field)](#review-date-field)

#### Review Date (field)

**Category:** Governance · **Status:** Active

The metadata field committing a document to a future re-examination. A document past its review date is flagged by Knowledge as stale and prioritized for update or deprecation — it is not simply left as-is.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Review schedule](00_ATLAS_BRAIN.md#versioning-policy)
**Related terms:** [Metadata Block](#metadata-block) · [Knowledge Lifecycle](#knowledge-lifecycle)

#### Decision Record (DR)

**Category:** Governance · **Status:** Active

The structured written artifact capturing a decision's context, options considered, chosen option and rationale, success metrics, and review date. Every significant decision produces a Decision Record, logged in [`06_DECISIONS.md`](06_DECISIONS.md). See [Decision Framework Terms](#decision-framework-terms) for the surrounding taxonomy (Level, Class, Lifecycle, Pipeline).

**Aliases:** DR
**Canonical source:** [`00_ATLAS_BRAIN.md` § Decision Record template](00_ATLAS_BRAIN.md#documentation-standards)
**Related terms:** [Decision Register](#decision-register) · [Decision Level (DL)](#decision-level-dl)

#### Escalation Threshold

**Category:** Governance · **Status:** Active

The defined trigger — a capital amount, a scope of impact, a degree of irreversibility — above which escalation to a higher authority band is mandatory rather than discretionary. Default holding-wide thresholds are set by Brain and customized quarterly in [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md).

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Escalation](00_ATLAS_BRAIN.md#escalation)
**Related terms:** [Escalation](#escalation) · [Authority Band](#authority-band)

#### Governance Boundary

**Category:** Governance · **Status:** Active

The documented line describing which body may change which kind of standard — for example, only Brain may approve a Tier-1 document change or create an eighth department. Crossing a governance boundary without the required approval is organizational debt, surfaced and fixed in quarterly org reviews.

**Aliases:** None
**Canonical source:** [`03_ORGANIZATION.md` § Governance Boundaries](03_ORGANIZATION.md#organization-executes-the-brain)
**Related terms:** [Shadow Governance](#shadow-governance) · [Seven-Department Invariant](#seven-department-invariant)

#### Shadow Governance

**Category:** Governance · **Status:** Active

Informal power structures, unofficial documents, or de facto decision-making that bypass documented authority. Named explicitly as organizational debt; the fix is to make the official path easier to use than the unofficial one, not merely to prohibit the unofficial one.

**Aliases:** Shadow wiki (documentation-specific variant)
**Canonical source:** [`03_ORGANIZATION.md` § Rules of engagement](03_ORGANIZATION.md#organization-executes-the-brain)
**Related terms:** [Governance Boundary](#governance-boundary) · [One Source of Truth Principle](#one-source-of-truth-principle)

---

## Roadmap Terms

Terms describing where Atlas is going and in what order — horizons, eras, phases, milestones, and success criteria. Full sequencing lives in [`04_ROADMAP.md`](04_ROADMAP.md); this glossary defines the vocabulary the Roadmap uses so it does not need to redefine it inline in every section.

#### Vision Horizon

**Category:** Roadmap · **Status:** Active

One of five multi-year strategic bands (H0–H4) anchored to the fifty-year vision in [The Long-Term Vision](01_WHY_ATLAS_EXISTS.md#the-long-term-vision-50-years). A horizon is the longest-duration unit on the roadmap's time axis, spanning multiple [Eras](#evolution-era) and [Phases](#major-phase).

| Horizon | Years | Character |
|---|---|---|
| **H0 — Foundation** | 0–2 | Brain substrate, first execution loop, first capital discipline |
| **H1 — Leverage** | 2–5 | Integration speed, automation depth, financial honesty at scale |
| **H2 — Repeatability** | 5–10 | Declining marginal integration effort, platform pull, headcount leverage |
| **H3 — Institution** | 10–20 | Succession, precedent power, cross-portfolio intelligence |
| **H4 — Infrastructure** | 20+ | Permanence, stewardship, sustained compounding |

**Aliases:** Horizon
**Canonical source:** [`04_ROADMAP.md` § Vision Horizon](04_ROADMAP.md#vision-horizon)
**Related terms:** [Evolution Era](#evolution-era) · [Major Phase](#major-phase) · [Success Criteria](#success-criteria)

#### Evolution Era

**Category:** Roadmap · **Status:** Active

A multi-year evolutionary period (E0, E1, E2, E3+) inside a [Vision Horizon](#vision-horizon), used to describe the holding's overall character across several [Phases](#major-phase) at once — e.g., E0 "Substrate" spans the years in which Atlas builds its governance layer before operating anything.

**Aliases:** Era
**Canonical source:** [`04_ROADMAP.md` § Multi-Year Evolution](04_ROADMAP.md#multi-year-evolution)
**Related terms:** [Vision Horizon](#vision-horizon) · [Capability Arc](#capability-arc)

#### Capability Arc

**Category:** Roadmap · **Status:** Active

One of five long-run evolution tracks describing a specific dimension of Atlas's growth across multiple phases, independent of the Phase model's calendar-agnostic gates:

| Arc | Track |
|---|---|
| **Arc A** | From documents to executable operating system |
| **Arc B** | From first asset to portfolio organism |
| **Arc C** | From assisted AI to self-improving systems |
| **Arc D** | From founder memory to institutional memory |
| **Arc E** | From lean team to scaled organism without bureaucracy |

**Aliases:** Arc
**Canonical source:** [`04_ROADMAP.md` § Multi-year capability arcs](04_ROADMAP.md#multi-year-evolution)
**Related terms:** [Evolution Era](#evolution-era) · [Major Phase](#major-phase)

#### Major Phase

**Category:** Roadmap · **Status:** Active

One of seven sequential, gate-based strategic periods (P0–P6) that Atlas moves through based on met exit criteria, not calendar time. Unlike Horizons and Eras (time-anchored), Phases only advance when their exit criteria are evidenced.

| Phase | Name | Intent |
|---|---|---|
| **P0** | Brain Substrate | Establish governance documents, decision log, and glossary |
| **P1** | Operating Kernel | First real decisions, first playbooks, first production agents |
| **P2** | Leverage Demonstration | Prove Atlas infrastructure creates disproportionate uplift on ≥1 asset |
| **P3** | Repeatable Machine | Integration and build playbooks work across multiple assets |
| **P4** | Platform Organism | Holding OS becomes software; self-serve for operators |
| **P5** | Institutional Form | Succession-ready; recognized as a durable organizational form |
| **P6** | Infrastructure Era | Functions as durable economic infrastructure across generations |

**Aliases:** Phase, Roadmap Phase
**Canonical source:** [`04_ROADMAP.md` § Major Phases](04_ROADMAP.md#major-phases)
**Related terms:** [Entry and Exit Criteria](#entry-and-exit-criteria) · [Org Stage](#org-stage) · [CM to Phase Mapping](#weakest-link-method)

#### Entry and Exit Criteria

**Category:** Roadmap · **Status:** Active

The documented conditions that must hold before a [Phase](#major-phase) can formally begin (**entry criteria**) or be declared complete (**exit criteria**). Exit criteria are evidenced, not assumed — a phase with unmet exit criteria remains open regardless of elapsed time.

**Aliases:** Phase gate criteria
**Canonical source:** [`04_ROADMAP.md` § Phase 0 — Brain Substrate § Exit criteria](04_ROADMAP.md#major-phases)
**Related terms:** [Major Phase](#major-phase) · [Milestone](#milestone)

#### Milestone

**Category:** Roadmap · **Status:** Active

A discrete, dated, evidenced marker of roadmap progress, ID-tagged by cluster (e.g., `M-K-001` for the first Knowledge-cluster milestone, `M-A-003` for an AI-cluster milestone). Milestones are grouped into clusters (Governance, Knowledge, AI/Automation, Finance, Operations, Assets/Portfolio, Projects, Infrastructure/Platform) in the [Milestone Register](04_ROADMAP.md#strategic-milestones).

**Aliases:** None
**Canonical source:** [`04_ROADMAP.md` § Strategic Milestones](04_ROADMAP.md#strategic-milestones)
**Related terms:** [Milestone Health State](#milestone-health-state) · [Success Criteria](#success-criteria)

#### Milestone Health State

**Category:** Roadmap · **Status:** Active

The color-coded status of a milestone's progress, using the same palette as [Project Health Signal](#project-health-signal): 🟢 Green (on track), 🟡 Yellow (minor delay), 🔴 Red (material miss), 🔵 Blue (deprioritized).

**Aliases:** None
**Canonical source:** [`04_ROADMAP.md` § Milestone health states](04_ROADMAP.md#strategic-milestones)
**Related terms:** [Milestone](#milestone) · [Project Health Signal](#project-health-signal)

#### Success Criteria

**Category:** Roadmap · **Status:** Active

Auditable, ID-tagged tests (format `SC-Hx-NN`, e.g., `SC-H0-01`) that define what "success" concretely means for a given [Vision Horizon](#vision-horizon) — each paired with a metric or evidence type, not a vague aspiration. Complemented by [Anti-Success](#anti-success), the explicit list of outcomes Atlas treats as failure even if revenue grows.

**Aliases:** SC
**Canonical source:** [`04_ROADMAP.md` § Success Criteria](04_ROADMAP.md#success-criteria)
**Related terms:** [Anti-Success](#anti-success) · [Vision Horizon](#vision-horizon)

#### Anti-Success

**Category:** Roadmap · **Status:** Active

An outcome Atlas explicitly treats as a roadmap failure mode even if revenue or headcount grows — for example, portfolio growth without integration, automation vanity metrics, narrative over truth, or headcount mistaken for progress.

**Aliases:** None
**Canonical source:** [`04_ROADMAP.md` § Anti-success (explicit failures)](04_ROADMAP.md#success-criteria)
**Related terms:** [Success Criteria](#success-criteria) · [Automation Vanity](#automation-vanity)

#### North-Star Test

**Category:** Roadmap · **Status:** Active

A short question used to check whether a roadmap item is worth pursuing at all before it is scheduled into a phase — the roadmap-level analog of the Brain's three [mission questions](00_ATLAS_BRAIN.md#mission-in-practice).

**Aliases:** None
**Canonical source:** [`04_ROADMAP.md` § North-star tests for any roadmap item](04_ROADMAP.md#roadmap-architecture)
**Related terms:** [Success Criteria](#success-criteria)

#### Decade Checkpoint

**Category:** Roadmap · **Status:** Active

A ten-year-interval strategic checkpoint used to assess Atlas's progress against [The Long-Term Vision (50+ Years)](01_WHY_ATLAS_EXISTS.md#the-long-term-vision-50-years), distinct from the quarterly and annual review cadences used for operational course-correction.

**Aliases:** None
**Canonical source:** [`04_ROADMAP.md` § Decade checkpoints](04_ROADMAP.md#multi-year-evolution)
**Related terms:** [Vision Horizon](#vision-horizon)

#### Expansion Mode

**Category:** Roadmap · **Status:** Active

One of nine named ways Atlas grows, each with an earliest eligible phase and a preferred-when condition — used to sequence *when* a growth mode is appropriate, distinct from [Build vs. Acquire](#build-vs-acquire), which decides *which* mode for a specific opportunity.

| Mode | Description | Earliest phase |
|---|---|---|
| **E-Build** | New venture from first principles | P1 |
| **E-Acquire** | Purchase existing business | P2 |
| **E-Integrate-deep** | Deeper OS penetration in existing assets | P2+ |
| **E-Shared-services** | Centralize a function across assets | P3 |
| **E-Platform** | Productize the OS for operators | P4 |
| **E-Sector** | Enter a new sector cluster | P3+ |
| **E-Geo** | Enter a new geography | P3+ |
| **E-External-knowledge** | Publish frameworks selectively | P5+ |
| **E-Operator-network** | Community of portfolio leaders | P4+ |

**Aliases:** None
**Canonical source:** [`04_ROADMAP.md` § Expansion modes](04_ROADMAP.md#expansion-strategy)
**Related terms:** [Build vs. Acquire](#build-vs-acquire) · [Major Phase](#major-phase)

#### AI Evolution Stage

**Category:** Roadmap · **Status:** Active

The roadmap targets (AI-0 through AI-5) for AI and automation maturity by phase — distinct from the [AI Maturity Model](#ai-maturity-model), which scores one process at a time. AI Evolution Stage describes the holding's overall automation posture at a given phase (e.g., AI-1 at Phase P1: "Registry; specs; first production agents; L1–L2").

**Aliases:** None
**Canonical source:** [`04_ROADMAP.md` § AI evolution stages](04_ROADMAP.md#ai-evolution)
**Related terms:** [AI Maturity Model](#ai-maturity-model) · [Automation Wave](#automation-wave)

#### Knowledge Evolution Stage

**Category:** Roadmap · **Status:** Active

The roadmap targets (K-0 through K-5) for the knowledge system's maturity by phase, ranging from K-0 ("Fragments; founder memory") to K-5 ("Knowledge-as-product; powers portal").

**Aliases:** None
**Canonical source:** [`04_ROADMAP.md` § Knowledge evolution stages](04_ROADMAP.md#knowledge-evolution)
**Related terms:** [Knowledge Lifecycle](#knowledge-lifecycle) · [Major Phase](#major-phase)

#### Automation Wave

**Category:** Roadmap · **Status:** Active

The roadmap targets (W0 through W5) for automation scope and depth by phase, from W0 ("None systematic; manual OK") to W5 ("Selective L4; self-improving within bounds").

**Aliases:** None
**Canonical source:** [`04_ROADMAP.md` § Automation maturity wave plan](04_ROADMAP.md#automation-evolution)
**Related terms:** [AI Evolution Stage](#ai-evolution-stage) · [Automation Eligibility Criteria](#automation-eligibility-criteria)

#### Expansion Thesis

**Category:** Roadmap · **Status:** Active

The written explanation of *why* a specific expansion strengthens the Holding OS rather than merely increasing "logos under a brand." Required for any [Expansion Mode](#expansion-mode) beyond deepening existing integration.

**Aliases:** None
**Canonical source:** [`04_ROADMAP.md` § Expansion thesis](04_ROADMAP.md#expansion-strategy)
**Related terms:** [Expansion Mode](#expansion-mode) · [Acquire When Leverage Exists](#build-vs-acquire)

---

## Decision Framework Terms

Terms describing how a specific decision is sized, classified, moved through its lifecycle, and reviewed. High-level framing lives in [Decision Framework](00_ATLAS_BRAIN.md#decision-framework); full mechanics live in [`06_DECISIONS.md`](06_DECISIONS.md).

#### Decision Level (DL)

**Category:** Decision Framework · **Status:** Active

The five-tier scale (DL-0 to DL-4) answering "how much process does this decision actually need?" Decision Level maps onto, but is a distinct scale from, [Authority Band](#authority-band) — Atlas deliberately uses the **DL** prefix instead of a bare "L" so a reader is never unsure whether "L2" means an AI Maturity level, an Authority band, or a Decision Level.

| Level | Trigger | Pipeline depth | Review cadence |
|---|---|---|---|
| **DL-0 — Trivial** | Fully reversible, no capital, no external party, no precedent | Frame + Decide only | None required |
| **DL-1 — Routine** | Reversible, within a documented SOP or department budget | Frame → light Evidence → Decide → Log | 30 days if spend/commitment involved |
| **DL-2 — Significant** | Affects 2+ departments, meaningful resource commitment, or sets precedent | Full pipeline, all gates | 30 / 90 days |
| **DL-3 — Major** | Portfolio-level impact, real capital at risk, costly to reverse | Full pipeline + scoring + Brain sign-off | 30 / 90 / 180 days |
| **DL-4 — Strategic** | Direction-changing, principle-level, or structurally irreversible | Full pipeline + scoring + Brain approval + version bump if governance-affecting | Quarterly until stable |

Use the [Sizing Test](#sizing-test) to assign a level in under a minute; when two levels could apply, take the higher one.

**Aliases:** DL
**Canonical source:** [`06_DECISIONS.md` § Decision Levels](06_DECISIONS.md#decision-levels)
**Related terms:** [Authority Band](#authority-band) · [AI Maturity Model](#ai-maturity-model) · [L-Prefix Disambiguation](#l-prefix-disambiguation)

#### Sizing Test

**Category:** Decision Framework · **Status:** Active

The five-question test used to assign a [Decision Level](#decision-level-dl) quickly: is it irreversible or holding-level precedent-setting (DL-4)? Does real capital move or is it hard to reverse within 90 days (DL-3)? Does it affect more than one department or create a reusable pattern (DL-2)? Is it inside one department's documented budget/SOP and reversible (DL-1)? Otherwise, DL-0. Stop at the first "yes"; when uncertain, take the higher level.

**Aliases:** None
**Canonical source:** [`06_DECISIONS.md` § Sizing test](06_DECISIONS.md#decision-levels)
**Related terms:** [Decision Level (DL)](#decision-level-dl) · [Level Inflation / Deflation](#level-inflation--deflation)

#### Level Inflation / Deflation

**Category:** Decision Framework · **Status:** Active

The two symmetric failure modes of mis-sizing a decision: **inflation** classifies a decision one notch higher than warranted (usually for social cover), costing speed for no rigor benefit; **deflation** classifies it one notch lower (usually to dodge evidence burden), costing rigor and hiding risk until a postmortem traces a bad outcome back to it. Deflation is the more dangerous of the two because it is invisible until reviewed.

**Aliases:** None
**Canonical source:** [`06_DECISIONS.md` § Level inflation and level deflation](06_DECISIONS.md#decision-levels)
**Related terms:** [Sizing Test](#sizing-test) · [Quarterly Decision Review](#postmortem)

#### Decision Class

**Category:** Decision Framework · **Status:** Active

One of exactly five canonical types every decision is classified into, fixed by Brain and treated as immutable so that precedent comparisons remain meaningful over time:

| Class | Definition | Typical DL range | Default owner |
|---|---|---|---|
| **Investment** | Capital deployed expecting a return | DL-2 to DL-4 | Assets deal owner (+ Finance, + Brain) |
| **Operational** | Process, tooling, vendor, or workflow change | DL-0 to DL-2 | Operations process owner |
| **Strategic** | Direction, priority, or structural change to the holding | DL-3 to DL-4 | Brain |
| **Personnel** | Hiring, role change, compensation, separation, authority delegation | DL-1 to DL-3 | Relevant department head |
| **Technical** | System, architecture, AI/automation, or data decision | DL-0 to DL-3 | Agent owner + AI head, or domain owner |

Each class has documented **sub-classes** (e.g., Investment → M&A, New venture, Follow-on, Exit) that route evidence checklists without expanding the five-type taxonomy itself.

**Aliases:** Decision type
**Canonical source:** [`06_DECISIONS.md` § Decision Classes](06_DECISIONS.md#decision-classes)
**Related terms:** [Sub-Class (decision)](#sub-class-decision) · [Decision Level (DL)](#decision-level-dl)

#### Sub-Class (decision)

**Category:** Decision Framework · **Status:** Active

A finer-grained category beneath one of the five canonical [Decision Classes](#decision-class) — for example, "M&A / acquisition" and "Exit / divestiture" are sub-classes of Investment. Sub-classes may be added over time via a Governance-class Decision Record; the five top-level classes never expand.

**Aliases:** None
**Canonical source:** [`06_DECISIONS.md` § Sub-classes](06_DECISIONS.md#decision-classes)
**Related terms:** [Decision Class](#decision-class) · [Evidence Checklist](#evidence-checklist)

#### Decision Lifecycle

**Category:** Decision Framework · **Status:** Active

The state machine every decision moves through regardless of [Level](#decision-level-dl) or [Class](#decision-class) — the vocabulary used in a Decision Record's `Status` field and the [Decision Register](#decision-register)'s `Status` column. States include Proposed, Approved, Implemented, Reviewed, and the two terminal states Rejected and Superseded.

**Aliases:** None
**Canonical source:** [`06_DECISIONS.md` § Decision Lifecycle](06_DECISIONS.md#decision-lifecycle)
**Related terms:** [Decision Record (DR)](#decision-record-dr) · [Decision Register](#decision-register)

#### Decision Pipeline

**Category:** Decision Framework · **Status:** Active

The eleven ordered stages a decision passes through from intake to review, gated by the seven [Decision Gates](#decision-gate). Pipeline depth scales with [Decision Level](#decision-level-dl) — a DL-0 decision may compress to two stages, while a DL-4 decision runs the full eleven with Brain sign-off.

**Aliases:** None
**Canonical source:** [`06_DECISIONS.md` § Decision Pipeline](06_DECISIONS.md#decision-pipeline)
**Related terms:** [Decision Gate](#decision-gate) · [Decision Level (DL)](#decision-level-dl)

#### Decision Gate

**Category:** Decision Framework · **Status:** Active

One of seven mandatory checkpoints (Gate 0 through Gate 6) between pipeline stages, each with a pass/fail checklist. Gates are not waivable — a decision can only pass a gate or be re-routed to a lower Decision Level if reclassification genuinely applies. Failing a gate routes the decision back to the prior stage; it is not an escalation-worthy event unless the same gate fails repeatedly.

| Gate | Sits between | Pass criteria |
|---|---|---|
| **Gate 0 — Worth deciding** | Intake → Frame | A real decision point exists with an identifiable "do nothing" alternative |
| **Gate 1 — Framed** | Frame/Classify → Evidence | Brain's five framing questions answered; Level and Class assigned |
| **Gate 2 — Evidenced** | Evidence/Options → Score | Evidence checklist satisfied; ≥2 options with trade-offs stated |
| **Gate 3 — Scored & Decided** | Score/Decide → Approve | Criteria table complete; no unexplained veto-triggering score of 1 |
| **Gate 4 — Approved** | Approve → Log | Decision approved within the correct authority band |
| **Gate 5 — Logged & Executing** | Log/Execute → Review | DR entered in the Register within the logging SLA; execution started |
| **Gate 6 — Reviewed** | Review → close | Outcome compared to the stated success metric; status resolved |

**Aliases:** Gate
**Canonical source:** [`06_DECISIONS.md` § Decision Gates](06_DECISIONS.md#decision-gates)
**Related terms:** [Decision Pipeline](#decision-pipeline) · [Bias Detection](#bias-detection)

#### Evidence Checklist

**Category:** Decision Framework · **Status:** Active

The class-specific list of evidence required before a decision clears Gate 2 — for example, an Investment/M&A decision requires a due diligence packet, valuation model, and integration scorecard forecast, while an Operational/vendor decision requires a cost comparison and switching-cost analysis.

**Aliases:** None
**Canonical source:** [`06_DECISIONS.md` § Required Evidence](06_DECISIONS.md#decision-classes)
**Related terms:** [Decision Class](#decision-class) · [Decision Gate](#decision-gate)

#### Bias Detection

**Category:** Decision Framework · **Status:** Active

The Gate 2 check confirming that decision evidence is not one-sided — for example, that an evidence section does not cite only sources favorable to the preferred option. Failure requires the owner (or AI, prompted) to add at least one countervailing consideration before proceeding.

**Aliases:** None
**Canonical source:** [`06_DECISIONS.md` § Bias Detection](06_DECISIONS.md#decision-gates)
**Related terms:** [Decision Gate](#decision-gate) · [Evidence Over Opinion Principle](#evidence-over-opinion-principle)

#### Decision Register

**Category:** Decision Framework · **Status:** Active

The running, searchable log of every logged Decision Record — the structure underlying [`06_DECISIONS.md`](06_DECISIONS.md) — used for precedent search, pattern analysis, and the [Quarterly Decision Review](#postmortem). Value compounds only if [Decision Class](#decision-class) is applied consistently across every entry.

**Aliases:** None
**Canonical source:** [`06_DECISIONS.md` § Decision Register](06_DECISIONS.md#decision-classes)
**Related terms:** [Decision Record (DR)](#decision-record-dr) · [Postmortem](#postmortem)

#### Postmortem

**Category:** Decision Framework · **Status:** Active

The structured review comparing a decision's stated success metrics against actual outcomes at its scheduled review date, feeding lessons back into the Brain and, where relevant, into a heuristic or principle update. Postmortems are blameless but not excuse-laden — "market conditions" alone is not a complete root cause.

**Aliases:** Decision review, Quarterly Decision Review (aggregate form)
**Canonical source:** [`00_ATLAS_BRAIN.md` § Execute, measure, and iterate](00_ATLAS_BRAIN.md#decision-framework)
**Related terms:** [RCA (Root Cause Analysis)](#rca-root-cause-analysis) · [Decision Register](#decision-register)

---

## Capability Maturity Terms

Terms describing how mature Atlas's holding-level systems are, independent of headcount ([Org Stage](#org-stage)) or any single process's automation depth ([AI Maturity Model](#ai-maturity-model)). Full rubrics live in [Capability Maturity Model](04_ROADMAP.md#capability-maturity-model); live scores live in [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md#current-capability-maturity).

#### Capability Maturity Model (CM)

**Category:** Capability Maturity · **Status:** Active

A ten-dimension, six-level model scoring how mature Atlas's holding-level systems are — the **only** framework that scores the holding as a whole, as opposed to one process ([AI Maturity](#ai-maturity-model)) or one org's headcount ([Org Stage](#org-stage)). Scored quarterly (light) and annually (deep), with evidence packs required, not opinions.

**Aliases:** CM, Holding Capability Maturity
**Canonical source:** [`04_ROADMAP.md` § Capability Maturity Model](04_ROADMAP.md#capability-maturity-model)
**Related terms:** [CM Level](#cm-level) · [CM Dimension](#cm-dimension) · [Weakest-Link Method](#weakest-link-method)

#### CM Level

**Category:** Capability Maturity · **Status:** Active

One of six levels (0–5) describing overall maturity, either per [CM Dimension](#cm-dimension) or in aggregate for the whole holding. Each Phase transition (P0→P1, P1→P2, etc.) requires a minimum CM level to be met before the gate opens.

| Level | Name | Meaning |
|---|---|---|
| **CM-0** | Implicit | No or minimal system; activity is ad hoc or has not started |
| **CM-1** | Docs real | Documentation exists and reflects reality, even if rarely used live |
| **CM-2** | Managed execution | Systems are used by default in live decisions/operations |
| **CM-3** | Leverage shown | Systems demonstrably create leverage; reuse and retrieval work |
| **CM-4** | Industrialized | Automated, templated, and reliable at scale |
| **CM-5** | Institutional | Self-sustaining, cross-portfolio, continuously improving |

**Aliases:** None
**Canonical source:** [`04_ROADMAP.md` § CM levels](04_ROADMAP.md#capability-maturity-model)
**Related terms:** [CM Dimension](#cm-dimension) · [Major Phase](#major-phase)

#### CM Dimension

**Category:** Capability Maturity · **Status:** Active

One of ten scored axes (D1–D10) of holding capability, each with its own 0–5 rubric and departmental owner:

| ID | Dimension | Owner focus |
|---|---|---|
| **CM-D1** | Governance & judgment | Brain |
| **CM-D2** | Knowledge compounding | Knowledge |
| **CM-D3** | AI & automation | AI |
| **CM-D4** | Financial truth | Finance |
| **CM-D5** | Operational integration | Operations |
| **CM-D6** | Portfolio stewardship | Assets |
| **CM-D7** | Delivery system | Projects |
| **CM-D8** | Organizational clarity | Brain + Organization |
| **CM-D9** | Platform / infrastructure | AI + Operations |
| **CM-D10** | Learning loop | All departments |

**Aliases:** None
**Canonical source:** [`04_ROADMAP.md` § CM dimensions](04_ROADMAP.md#capability-maturity-model)
**Related terms:** [CM Level](#cm-level) · [Weakest-Link Method](#weakest-link-method) · [Aggregate CM Score](#aggregate-cm-score)

#### Weakest-Link Method

**Category:** Capability Maturity · **Status:** Active

The rule that the holding's overall, **gating** CM level is the **minimum** score across all ten [CM Dimensions](#cm-dimension) — not an average. A holding cannot claim CM-3 overall while any dimension sits at CM-0; the weakest dimension is the honest overall score, and becomes the next quarter's priority.

**Aliases:** None
**Canonical source:** [`04_ROADMAP.md` § Capability Maturity Model § Purpose of CM levels](04_ROADMAP.md#capability-maturity-model)
**Related terms:** [Aggregate CM Score](#aggregate-cm-score) · [CM Dimension](#cm-dimension)

#### Aggregate CM Score

**Category:** Capability Maturity · **Status:** Active

The **average** across all ten CM dimensions, used diagnostically alongside the [Weakest-Link Method](#weakest-link-method)'s gating score. The average shows genuine partial progress that the weakest-link score, by design, does not credit.

**Aliases:** Diagnostic CM score
**Canonical source:** [`05_CURRENT_STATE.md` § Aggregate scores](05_CURRENT_STATE.md#current-capability-maturity)
**Related terms:** [Weakest-Link Method](#weakest-link-method) · [CM Level](#cm-level)

---

## Workflow Terminology

Terms describing the repeatable sequences Atlas moves work, companies, and knowledge through — project and company lifecycles, knowledge flow, and incident handling. Full mechanics live in [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) sections on lifecycle and in [`03_ORGANIZATION.md`](03_ORGANIZATION.md#execution-flow).

#### Project Lifecycle

**Category:** Workflow · **Status:** Active

The seven-stage path every time-bound initiative moves through: **Intake → Triage → Brief → Plan → Execute → Review → Handoff.** No project enters Execute without an approved [Project Brief](#project-brief); no project closes without a confirmed [Handoff](#handoff).

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Project Lifecycle](00_ATLAS_BRAIN.md#project-lifecycle)
**Related terms:** [Project Brief](#project-brief) · [Handoff](#handoff) · [Retrospective](#retrospective)

#### Project Brief

**Category:** Workflow · **Status:** Active

The Tier-3 planning document required before any project enters execution — scope, non-goals, success metrics, milestones, timeline, team and roles, budget, risks, dependencies, and a handoff plan. Every brief names exactly one DRI.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Brief (Project Lifecycle)](00_ATLAS_BRAIN.md#project-lifecycle)
**Related terms:** [Project Lifecycle](#project-lifecycle) · [Directly Responsible Individual (DRI)](#directly-responsible-individual-dri)

#### Project Health Signal

**Category:** Workflow · **Status:** Active

The color-coded status of an active project: 🟢 Green (on track, metrics met), 🟡 Yellow (minor recoverable delay), 🔴 Red (material scope/budget/timeline miss, triggers Brain review), 🔵 Blue (strategic priority changed; pause or redirect). Shared palette with [Milestone Health State](#milestone-health-state).

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Project health signals](00_ATLAS_BRAIN.md#project-lifecycle)
**Related terms:** [Milestone Health State](#milestone-health-state) · [Project Lifecycle](#project-lifecycle)

#### Handoff

**Category:** Workflow · **Status:** Active

The formal transfer of a stable project output to its owning department — operational processes to Operations, automations to AI (maintain) plus Operations (use), new portfolio assets to Assets, documentation to Knowledge, financial models to Finance. A project does not close until handoff is confirmed.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Handoff (Project Lifecycle)](00_ATLAS_BRAIN.md#project-lifecycle)
**Related terms:** [Project Lifecycle](#project-lifecycle) · [Ownership Transfer](#directly-responsible-individual-dri)

#### Company Lifecycle

**Category:** Workflow · **Status:** Active

The seven-stage path every portfolio asset moves through: **Prospect → Evaluate → Acquire/Build → Integrate → Operate → Optimize → Exit/Hold.** Each stage has a primary owner and key output — for example, Integrate is owned by Operations + AI and produces an [Integration Scorecard](#integration-scorecard).

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Company Lifecycle](00_ATLAS_BRAIN.md#company-lifecycle)
**Related terms:** [Portfolio Company](#portfolio-company) · [Integration Scorecard](#integration-scorecard) · [Build vs. Acquire](#build-vs-acquire)

#### Integration Scorecard

**Category:** Workflow · **Status:** Active

The tracked checklist measuring a newly acquired or built asset's progress against minimum integration thresholds — financial reporting, operational KPIs, documentation, knowledge base entry, AI/automation audit, and decision-framework adoption — each with a target timeline (e.g., 30 days for financial reporting mapping).

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Integration standards](00_ATLAS_BRAIN.md#company-lifecycle)
**Related terms:** [Company Lifecycle](#company-lifecycle) · [Portfolio Company Autonomy Spectrum](#portfolio-company)

#### BAU (Business As Usual)

**Category:** Workflow · **Status:** Active

Ongoing operational work that is not a time-bound project — the steady-state execution a system settles into once its [Project Lifecycle](#project-lifecycle) has completed and [Handoff](#handoff) occurred. Atlas requires that project work be explicitly separated from BAU in briefs, even at Org Stage 0.

**Aliases:** Business as usual
**Canonical source:** [`03_ORGANIZATION.md` § Stage 0: One operator](03_ORGANIZATION.md#organizational-scaling)
**Related terms:** [Project Lifecycle](#project-lifecycle) · [Handoff](#handoff)

#### Onboarding Knowledge Path

**Category:** Workflow · **Status:** Active

The prescribed reading sequence for new operators and agents: Brain → Why Atlas Exists → Glossary → relevant department playbooks → Current State and Roadmap. Executing this path is itself a tracked milestone.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Onboarding knowledge path](00_ATLAS_BRAIN.md#knowledge-management)
**Related terms:** [Knowledge Lifecycle](#knowledge-lifecycle) · [Document Hierarchy](#document-hierarchy)

#### Knowledge Lifecycle

**Category:** Workflow · **Status:** Active

The five-stage cycle every piece of institutional knowledge moves through: **Capture → Organize → Surface → Validate → Apply.** Knowledge that is captured but never surfaced, or surfaced but never applied, is treated as lost knowledge despite existing on disk.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Knowledge lifecycle](00_ATLAS_BRAIN.md#knowledge-management)
**Related terms:** [Onboarding Knowledge Path](#onboarding-knowledge-path) · [Knowledge Evolution Stage](#knowledge-evolution-stage)

#### Retrospective

**Category:** Workflow · **Status:** Active

The structured post-project or post-incident review producing captured learning — what worked, what didn't, what to change — transferred to Knowledge within a defined window of the initiative's close. A retrospective without action-item owners and dates is treated as improvement theater, not improvement.

**Aliases:** Postmortem (project sense; see [Postmortem](#postmortem) for the decision-specific sense)
**Canonical source:** [`00_ATLAS_BRAIN.md` § Review (Project Lifecycle)](00_ATLAS_BRAIN.md#project-lifecycle)
**Related terms:** [Project Lifecycle](#project-lifecycle) · [Knowledge Lifecycle](#knowledge-lifecycle)

#### Incident Response

**Category:** Workflow · **Status:** Active

The six-step protocol for handling a materialized risk: **Contain → Communicate → Resolve → Analyze → Prevent → Record.** Root cause analysis is required within 5 business days of containment.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Incident response](00_ATLAS_BRAIN.md#risk-management)
**Related terms:** [RCA (Root Cause Analysis)](#rca-root-cause-analysis) · [Escalation](#escalation)

#### RCA (Root Cause Analysis)

**Category:** Workflow · **Status:** Active

The structured investigation identifying *why* an incident or decision failure occurred, distinguishing genuine causes from surface-level excuses. "Market conditions" alone is never treated as a complete root cause.

**Aliases:** Root cause analysis
**Canonical source:** [`00_ATLAS_BRAIN.md` § Incident response](00_ATLAS_BRAIN.md#risk-management)
**Related terms:** [Incident Response](#incident-response) · [Postmortem](#postmortem)

#### Runbook

**Category:** Workflow · **Status:** Active

A precise, step-by-step procedure for handling a specific operational or incident scenario, closely related to but narrower in scope than a full [SOP](#sop-standard-operating-procedure) — typically written for a single failure mode or recurring exception.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Knowledge types and ownership](00_ATLAS_BRAIN.md#knowledge-management)
**Related terms:** [SOP (Standard Operating Procedure)](#sop-standard-operating-procedure) · [Incident Response](#incident-response)

---

## Automation Terminology

Terms describing how Atlas designs, documents, and governs automation specifically — as distinct from [AI Terms](#ai-terms), which cover AI's broader intelligence role. Full standards live in [Automation Standards](00_ATLAS_BRAIN.md#automation-standards).

#### Automation

**Category:** Automation · **Status:** Active

A machine-executed process that replaces manual, repeated human work, governed by the same documentation and ownership discipline as any other system. Automation is the highest-leverage layer in the [Principle Hierarchy](#principle-hierarchy)'s stack (Principles → Decision Rules → Processes → Automation) — and, per that stack, only appropriate once the underlying process is stable and documented.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Automation Standards](00_ATLAS_BRAIN.md#automation-standards)
**Related terms:** [Agent](#agent) · [Automation Eligibility Criteria](#automation-eligibility-criteria)

#### Automation Eligibility Criteria

**Category:** Automation · **Status:** Active

The five conditions that make a task ready for automation: it occurs ≥3 times per month (or is high-stakes and error-prone); its inputs, steps, and outputs are clearly defined; an SOP or playbook already documents it; baseline metrics exist; and a human owner is assigned for maintenance and exceptions.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Automation eligibility criteria](00_ATLAS_BRAIN.md#automation-standards)
**Related terms:** [SOP (Standard Operating Procedure)](#sop-standard-operating-procedure) · [Automation Spec](#automation-spec)

#### Automation Spec

**Category:** Automation · **Status:** Active

The required documentation template for any production automation: name, owner, SOP reference, trigger, inputs, steps, outputs, error handling, monitoring, maturity level, and last-tested date. An automation without a spec is treated as undocumented and therefore non-existent for scaling purposes.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Automation spec template](00_ATLAS_BRAIN.md#automation-standards)
**Related terms:** [Agent Design Standards](#agent-design-standards) · [Automation Registry](#automation-registry)

#### Automation Registry

**Category:** Automation · **Status:** Active

The AI department's central catalog of all production automations and agents, reviewed quarterly for ROI, flakiness, and cross-portfolio reuse potential. Automations below expected ROI are improved or retired from this registry, not left to run unmonitored.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Automation portfolio review](00_ATLAS_BRAIN.md#automation-standards)
**Related terms:** [Automation Spec](#automation-spec) · [Automation Retirement](#automation-retirement) · [AI ROI](#ai-roi)

#### Idempotent

**Category:** Automation · **Status:** Active

A design property of an automation such that re-running it produces the same result whether it runs once or many times — no duplicate or corrupt outputs from a retry. One of the five core [automation design principles](00_ATLAS_BRAIN.md#automation-standards).

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Automation design principles](00_ATLAS_BRAIN.md#automation-standards)
**Related terms:** [Fail Loudly](#fail-loudly) · [Automation Spec](#automation-spec)

#### Fail Loudly

**Category:** Automation · **Status:** Active

The design rule that automation errors must trigger alerts to a named owner — silent failure is unacceptable regardless of an automation's maturity level. Paired with logging every input, output, timestamp, and error for debugging and audit.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Automation design principles](00_ATLAS_BRAIN.md#automation-standards)
**Related terms:** [Idempotent](#idempotent) · [Guardrail](#guardrail)

#### Automation Retirement

**Category:** Automation · **Status:** Active

The deliberate decommissioning of an automation whose value has ended — negative ROI after improvement attempts, obsolete process, risk exceeding value, or superseded by a better template. Retirement is logged as a hygiene success, never treated as a failure.

**Aliases:** None
**Canonical source:** [`04_ROADMAP.md` § Automation retirement](04_ROADMAP.md#automation-evolution)
**Related terms:** [Automation Registry](#automation-registry) · [AI ROI](#ai-roi)

#### SOP (Standard Operating Procedure)

**Category:** Automation · **Status:** Active

A Tier-4 document giving precise, step-by-step execution instructions for a process, owned by the process owner (typically in Operations). SOPs are the required documentation precondition before any [Automation Eligibility Criteria](#automation-eligibility-criteria) can be met.

**Aliases:** SOP
**Canonical source:** [`00_ATLAS_BRAIN.md` § Document hierarchy](00_ATLAS_BRAIN.md#documentation-standards)
**Related terms:** [Playbook](#playbook) · [Runbook](#runbook) · [Document Hierarchy](#document-hierarchy)

#### Playbook

**Category:** Automation · **Status:** Active

A Tier-3 document giving step-by-step guidance for executing a specific domain of work — narrower than a T2 standard, broader than a T4 SOP — owned by the relevant domain department head. Examples include the integration playbook and the hiring playbook.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Document hierarchy](00_ATLAS_BRAIN.md#documentation-standards)
**Related terms:** [SOP (Standard Operating Procedure)](#sop-standard-operating-procedure) · [Document Hierarchy](#document-hierarchy)

---

## Finance Terminology

Terms describing how Atlas allocates, measures, and reports capital. Full philosophy lives in [Capital Allocation Philosophy](00_ATLAS_BRAIN.md#capital-allocation-philosophy); live instance values (actual bucket percentages, actual hurdle rates) live in [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md#current-finance).

#### Capital Bucket

**Category:** Finance · **Status:** Active

One of five categories capital is allocated into, each with distinct purpose and deployment guidance:

| Bucket | Purpose | Allocation guidance |
|---|---|---|
| **Operating** | Day-to-day portfolio and holding expenses | Fully funded from revenue |
| **Growth** | Build, acquire, and expand portfolio assets | Deploy against hurdle rate and strategic fit |
| **Infrastructure** | Holding OS — AI, systems, knowledge, automation | Fund projects with measurable leverage |
| **Reserve** | Opportunistic and defensive capital | Maintain minimum % of total capital |
| **Experimental** | Small bets on novel opportunities | Capped at a defined % of the Growth bucket |

Exact percentages are instance values, set and reviewed quarterly by Finance + Brain, and live in [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md).

**Aliases:** Reserve bucket (specific instance)
**Canonical source:** [`00_ATLAS_BRAIN.md` § Capital buckets](00_ATLAS_BRAIN.md#capital-allocation-philosophy)
**Related terms:** [Dry Powder](#dry-powder) · [Hurdle Rate](#hurdle-rate)

#### Hurdle Rate

**Category:** Finance · **Status:** Active

The minimum required return, adjusted for risk and liquidity, that an investment must clear before capital is committed. Hurdle rates are non-negotiable per [Capital Efficiency](#capital-efficiency-principle) — a lower rate is not accepted merely because capital sits idle.

**Aliases:** None
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § Hurdle rates are non-negotiable](02_FOUNDING_PRINCIPLES.md#capital-efficiency)
**Related terms:** [Capital Bucket](#capital-bucket) · [Build vs. Acquire](#build-vs-acquire)

#### Dry Powder

**Category:** Finance · **Status:** Active

Undeployed capital reserved for exceptional opportunities and portfolio resilience. Fully deployed capital is treated as fully exposed capital — dry powder is a strategic asset, not a failure of ambition.

**Aliases:** Reserves
**Canonical source:** [`00_ATLAS_BRAIN.md` § Allocation principles](00_ATLAS_BRAIN.md#capital-allocation-philosophy)
**Related terms:** [Capital Bucket](#capital-bucket) · [Optionality Principle](#one-way-and-two-way-doors)

#### Cost of Capital

**Category:** Finance · **Status:** Active

The minimum return Atlas must clear on any deployment before that deployment creates rather than destroys value — the baseline against which [Hurdle Rate](#hurdle-rate) and growth-vs-profit trade-offs are measured.

**Aliases:** None
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § Growth vs Profit](02_FOUNDING_PRINCIPLES.md#conflicts-between-principles)
**Related terms:** [Hurdle Rate](#hurdle-rate) · [Capital Efficiency Principle](#capital-efficiency-principle)

#### Build vs. Acquire

**Category:** Finance · **Status:** Active

The evaluation framework for choosing between building a venture from first principles and acquiring an existing business, scored across market timing, operational leverage, speed to revenue, capital efficiency, knowledge gain, and risk profile. Neither path is a default — each opportunity is scored on its merits.

**Aliases:** Build vs. buy vs. acquire
**Canonical source:** [`00_ATLAS_BRAIN.md` § Build vs. acquire framework](00_ATLAS_BRAIN.md#capital-allocation-philosophy)
**Related terms:** [NIH (Not Invented Here)](#nih-not-invented-here) · [Expansion Mode](#expansion-mode) · [Company Lifecycle](#company-lifecycle)

#### Unit Economics

**Category:** Finance · **Status:** Active

The per-unit profitability of a business — revenue and cost per customer, transaction, or comparable unit — measured independent of overall scale, tracked for every operating portfolio asset.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Return measurement](00_ATLAS_BRAIN.md#capital-allocation-philosophy)
**Related terms:** [ROI (Return on Investment)](#roi-return-on-investment) · [Financial Close](#financial-close)

#### ROI (Return on Investment)

**Category:** Finance · **Status:** Active

The ratio of value gained to cost, applied to an individual bet — "did this specific investment pay off?" Distinguished from [ROIC](#roic-return-on-invested-capital) (holding-wide) and [IRR](#roi-return-on-investment)/[MOIC](#moic-multiple-on-invested-capital) (time- and multiple-sensitive variants).

**Aliases:** Return on investment
**Canonical source:** [`00_ATLAS_BRAIN.md` § Return measurement](00_ATLAS_BRAIN.md#capital-allocation-philosophy)
**Related terms:** [AI ROI](#ai-roi) · [ROIC (Return on Invested Capital)](#roic-return-on-invested-capital)

#### IRR (Internal Rate of Return)

**Category:** Finance · **Status:** Active

A time-sensitive return metric that accounts for the timing of cash flows, applied to investments where cash arrives or is deployed unevenly over time.

**Aliases:** Internal rate of return
**Canonical source:** [`00_ATLAS_BRAIN.md` § Return measurement](00_ATLAS_BRAIN.md#capital-allocation-philosophy)
**Related terms:** [MOIC (Multiple on Invested Capital)](#moic-multiple-on-invested-capital) · [ROI (Return on Investment)](#roi-return-on-investment)

#### MOIC (Multiple on Invested Capital)

**Category:** Finance · **Status:** Active

The ratio of total value returned to total capital invested, applied to private holdings where a simple multiple is more legible than a time-weighted rate.

**Aliases:** Multiple on invested capital
**Canonical source:** [`00_ATLAS_BRAIN.md` § Return measurement](00_ATLAS_BRAIN.md#capital-allocation-philosophy)
**Related terms:** [IRR (Internal Rate of Return)](#irr-internal-rate-of-return) · [ROIC (Return on Invested Capital)](#roic-return-on-invested-capital)

#### ROIC (Return on Invested Capital)

**Category:** Finance · **Status:** Active

A holding-level return measure applied across the entire deployed capital base — "is Atlas creating value overall?" — published quarterly by Finance, distinct from any single asset's ROI.

**Aliases:** Holding ROIC
**Canonical source:** [`00_ATLAS_BRAIN.md` § Return measurement](00_ATLAS_BRAIN.md#capital-allocation-philosophy)
**Related terms:** [ROI (Return on Investment)](#roi-return-on-investment) · [Unit Economics](#unit-economics)

#### Financial Close

**Category:** Finance · **Status:** Active

The periodic (monthly or quarterly) process of finalizing and reporting accurate financial statements for the holding and portfolio, owned by Finance, with a target close timeline of ≤10 business days after period end.

**Aliases:** Monthly close, quarterly close
**Canonical source:** [`03_ORGANIZATION.md` § Department: Finance § KPIs](03_ORGANIZATION.md#department-finance)
**Related terms:** [Chart of Accounts](#chart-of-accounts) · [Unit Economics](#unit-economics)

#### Chart of Accounts

**Category:** Finance · **Status:** Active

The standardized ledger categories every portfolio company must map its books into as part of integration, enabling consolidated holding-level financial reporting within 30 days of close.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Integration standards](00_ATLAS_BRAIN.md#company-lifecycle)
**Related terms:** [Financial Close](#financial-close) · [Integration Scorecard](#integration-scorecard)

#### M&A (Mergers & Acquisitions)

**Category:** Finance · **Status:** Active

Transactions in which Atlas acquires or divests a portfolio company — the Investment-class sub-class covering deal sourcing, valuation, and closing, distinct from post-close [Integration](#integration-scorecard).

**Aliases:** Mergers and acquisitions
**Canonical source:** [`06_DECISIONS.md` § Sub-classes](06_DECISIONS.md#decision-classes)
**Related terms:** [Decision Class](#decision-class) · [Company Lifecycle](#company-lifecycle)

#### MVP (Minimum Viable Product)

**Category:** Finance · **Status:** Active

The smallest version of a build that tests a strategic hypothesis with real feedback, favored over a fully polished launch per [Action Over Perfection](02_FOUNDING_PRINCIPLES.md#action-over-perfection).

**Aliases:** Minimum viable product
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § Action over perfection](02_FOUNDING_PRINCIPLES.md#action-over-perfection)
**Related terms:** [Build vs. Acquire](#build-vs-acquire) · [Two-Way Door](#one-way-and-two-way-doors)

---

## Infrastructure Terminology

Terms describing the technical and operational substrate of the Holding OS — distinct from portfolio product infrastructure, which belongs to individual portfolio companies. Full detail lives in [Infrastructure Evolution](04_ROADMAP.md#infrastructure-evolution).

#### Infrastructure Layer

**Category:** Infrastructure · **Status:** Active

One of seven technical substrate layers making up the Holding OS's infrastructure, each with primary departmental owners:

| Layer | Contents | Primary owners |
|---|---|---|
| **L-Doc** | Docs, templates, versioning | Knowledge + Brain |
| **L-Access** | Identity, permissions, secrets | Operations + AI |
| **L-Data** | Storage, segmentation, pipelines | AI + Finance + Operations |
| **L-Automation** | Agents, workflows, registry | AI |
| **L-Observe** | Logging, metrics, alerts | AI + Operations |
| **L-Platform** | Atlas OS software + portal | AI + Projects |
| **L-Edge** | Portfolio connectors | Operations + Assets |

**Aliases:** None
**Canonical source:** [`04_ROADMAP.md` § Infrastructure layers](04_ROADMAP.md#infrastructure-evolution)
**Related terms:** [Atlas OS Platform](#atlas-os-platform) · [Data Segmentation](#data-segmentation)

#### Reliability Class

**Category:** Infrastructure · **Status:** Active

One of three tiers describing the required robustness of a system: **Critical** (financial truth, access, decision log integrity — high robustness, tested restores), **Important** (automations, dashboards — monitored with manual fallback), and **Best-effort** (experimental agents — clearly labeled, easy to disable).

**Aliases:** None
**Canonical source:** [`04_ROADMAP.md` § Reliability posture](04_ROADMAP.md#infrastructure-evolution)
**Related terms:** [Infrastructure Layer](#infrastructure-layer) · [Fail Loudly](#fail-loudly)

#### Data Segmentation

**Category:** Infrastructure · **Status:** Active

The default practice of isolating portfolio company data from other portfolio companies unless an explicit cross-portfolio access policy exists — a security principle applied to both human and AI access.

**Aliases:** Portfolio data segmentation
**Canonical source:** [`00_ATLAS_BRAIN.md` § Data and security principles](00_ATLAS_BRAIN.md#ai-strategy)
**Related terms:** [Cross-Portfolio Intelligence](#cross-portfolio-intelligence) · [Guardrail](#guardrail)

#### Atlas OS Platform

**Category:** Infrastructure · **Status:** Active

The planned software layer implementing the Holding OS's standards programmatically — the Phase P4 ("Platform Organism") deliverable, distinct from the current document-based Holding OS. Not yet built as of the current [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) snapshot.

**Aliases:** Atlas OS, OS platform
**Canonical source:** [`00_ATLAS_BRAIN.md` § Long-term (12+ months)](00_ATLAS_BRAIN.md#future-expansion)
**Related terms:** [Portal](#portal) · [Major Phase](#major-phase)

#### Portal

**Category:** Infrastructure · **Status:** Active

The planned self-serve software surface exposing the Holding OS's playbooks, automations, reporting, and knowledge directly to portfolio operators, targeted for Phase P4 and beyond.

**Aliases:** Portfolio company self-serve portal
**Canonical source:** [`00_ATLAS_BRAIN.md` § Long-term (12+ months)](00_ATLAS_BRAIN.md#future-expansion)
**Related terms:** [Atlas OS Platform](#atlas-os-platform) · [HOS Product Stage](#holding-operating-system-holding-os--hos)

#### Knowledge Base Architecture

**Category:** Infrastructure · **Status:** Active

The structural design of how Atlas's documented knowledge is organized, tagged, and retrieved — index, taxonomy, and search — owned by Knowledge, distinct from the content of any individual document.

**Aliases:** None
**Canonical source:** [`03_ORGANIZATION.md` § Department: Knowledge § Ownership](03_ORGANIZATION.md#department-knowledge)
**Related terms:** [RAG (Retrieval-Augmented Generation)](#rag-retrieval-augmented-generation) · [Knowledge Lifecycle](#knowledge-lifecycle)

---

## Document Authority Terminology

Terms describing how Atlas documents are identified, tiered, and made authoritative over one another — the metadata and sourcing discipline that lets any document in the Brain set be trusted at a glance. Full standards live in [Documentation Standards](00_ATLAS_BRAIN.md#documentation-standards).

#### Abbreviation

**Category:** Document Authority · **Status:** Active

A shortened form of a term or phrase, standardized for reuse so it always expands to exactly one meaning (or, where a short form is deliberately reused across systems, is resolved by an explicit disambiguation rule). Every abbreviation used in an Active Brain document must appear in this document's [Abbreviation Table](#abbreviation-table).

**Aliases:** Acronym (used loosely; not every abbreviation here is a true acronym)
**Canonical source:** This document (provisional home — abbreviation governance has no deeper sibling home)
**Related terms:** [Abbreviation Table](#abbreviation-table) · [L-Prefix Disambiguation](#l-prefix-disambiguation) · [Naming Conventions](#naming-conventions)

#### Document ID

**Category:** Document Authority · **Status:** Active

The canonical filename identifying a governance document — e.g., `00_ATLAS_BRAIN.md`. Document IDs are numbered to encode reading order and never reused, even if a document is deprecated.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Required metadata](00_ATLAS_BRAIN.md#documentation-standards)
**Related terms:** [Metadata Block](#metadata-block) · [Location (document field)](#location-document-field)

#### Location (document field)

**Category:** Document Authority · **Status:** Active

The metadata field naming a document's folder path — currently `02_Brain/` for every Tier-1 document in the Atlas vault.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Required metadata](00_ATLAS_BRAIN.md#documentation-standards)
**Related terms:** [Document ID](#document-id) · [Metadata Block](#metadata-block)

#### Classification (document field)

**Category:** Document Authority · **Status:** Active

A metadata tag describing a document's governance weight beyond its Tier — for example, "Immutable governance" ([`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md)) or "Governance — current state snapshot" ([`05_CURRENT_STATE.md`](05_CURRENT_STATE.md)). Optional for T3–T5 documents, expected for T1–T2.

**Aliases:** None
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` metadata block](02_FOUNDING_PRINCIPLES.md)
**Related terms:** [Document Hierarchy](#document-hierarchy) · [Metadata Block](#metadata-block)

#### Supersedes (document field)

**Category:** Document Authority · **Status:** Active

The metadata field naming the prior document or version this one replaces — `—` (em dash) when a document has no predecessor. Used to preserve historical traceability without deleting superseded material.

**Aliases:** None
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` metadata block](02_FOUNDING_PRINCIPLES.md)
**Related terms:** [Status (document field)](#status-document-field) · [Decision Lifecycle](#decision-lifecycle)

#### Document Hierarchy

**Category:** Document Authority · **Status:** Active

The five-tier system classifying every Atlas document by governance weight and required approval:

| Tier | Purpose | Examples | Approval |
|---|---|---|---|
| **T1 — Governance** | How Atlas thinks and decides | Brain, principles, frameworks | Brain |
| **T2 — Standards** | How Atlas builds and operates | Doc standards, automation specs, templates | Brain + Knowledge |
| **T3 — Playbooks** | How to execute specific domains | Integration playbook, hiring playbook | Department head |
| **T4 — SOPs** | Precise step-by-step procedures | Monthly close SOP, onboarding checklist | Process owner |
| **T5 — Records** | Point-in-time logs and artifacts | Decision records, meeting notes, reports | Author |

**Aliases:** Document tier, T1–T5
**Canonical source:** [`00_ATLAS_BRAIN.md` § Document hierarchy](00_ATLAS_BRAIN.md#documentation-standards)
**Related terms:** [Metadata Block](#metadata-block) · [Playbook](#playbook) · [SOP (Standard Operating Procedure)](#sop-standard-operating-procedure)

#### Canonical Source

**Category:** Document Authority · **Status:** Active

The one document that is authoritative for a given term, fact, or standard. Every glossary entry names its canonical source explicitly; where a canonical source does not yet exist for a concept in active use, that gap is flagged in [Appendix D](#appendix-d--candidate-terms-not-yet-fully-canonical) rather than filled ad hoc.

**Aliases:** Canonical document, source of truth
**Canonical source:** [`02_FOUNDING_PRINCIPLES.md` § One source of truth](02_FOUNDING_PRINCIPLES.md#one-source-of-truth)
**Related terms:** [One Source of Truth Principle](#one-source-of-truth-principle) · [Sibling Document](#sibling-document)

#### Sibling Document

**Category:** Document Authority · **Status:** Active

Any other Tier-1 Brain document (`00` through `06`) relative to a given document — used to describe the peer relationship between, e.g., this glossary and [`06_DECISIONS.md`](06_DECISIONS.md), as opposed to a parent/child or superseding relationship.

**Aliases:** None
**Canonical source:** [`03_ORGANIZATION.md`](03_ORGANIZATION.md) metadata block, `Authority` field
**Related terms:** [Root Node](#root-node) · [Instance vs. Type Document](#instance-vs-type-document)

#### Root Node

**Category:** Document Authority · **Status:** Active

The description of [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) as the originating document of the Brain department and the document every other Brain document ultimately derives from.

**Aliases:** None
**Canonical source:** [`00_ATLAS_BRAIN.md` § Executive Summary](00_ATLAS_BRAIN.md#executive-summary)
**Related terms:** [Sibling Document](#sibling-document) · [Document Hierarchy](#document-hierarchy)

#### Instance vs. Type Document

**Category:** Document Authority · **Status:** Active

The distinction between documents that define a **type** — a framework, principle, or structure that changes rarely ([`00`](00_ATLAS_BRAIN.md), [`01`](01_WHY_ATLAS_EXISTS.md), [`02`](02_FOUNDING_PRINCIPLES.md), [`03`](03_ORGANIZATION.md), [`04`](04_ROADMAP.md)) — and documents that report **instance values**, the actual, current, dated facts filling in those types ([`05_CURRENT_STATE.md`](05_CURRENT_STATE.md)). Where a type document and an instance document appear to disagree, the type document wins on *what should be true or how something is defined*, and the instance document wins on *what is true today*.

**Aliases:** Type document, instance document
**Canonical source:** [`05_CURRENT_STATE.md` § Document Authority](05_CURRENT_STATE.md#document-authority)
**Related terms:** [Chain of Custody](#chain-of-custody-for-facts) · [Canonical Source](#canonical-source)

#### Chain of Custody (for facts)

**Category:** Document Authority · **Status:** Active

The documented path by which a live fact — a headcount number, a threshold, a CM score — enters [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md): its source of truth (e.g., a Finance system or a direct observation) and the trigger that updates it (e.g., "on any hiring/offboarding event").

**Aliases:** None
**Canonical source:** [`05_CURRENT_STATE.md` § Chain of custody for facts in this document](05_CURRENT_STATE.md#document-authority)
**Related terms:** [Instance vs. Type Document](#instance-vs-type-document)

#### L-Prefix Disambiguation

**Category:** Document Authority · **Status:** Active

The explicit rule for resolving the ambiguous letter-number pattern "L" + digit across three unrelated scales that all happen to use the same shorthand. Atlas deliberately gave Decision Level a different prefix (`DL`) specifically to prevent this collision from being silently unresolvable.

| Pattern | Scale | Meaning of "2" |
|---|---|---|
| `L2` | [AI Maturity Model](#ai-maturity-model) | Supervised automation — AI executes routine steps, human reviews exceptions |
| `L2` | [Authority Band](#authority-band) | Departmental authority — a department head may decide |
| `DL-2` | [Decision Level](#decision-level-dl) | Significant decision — affects 2+ departments, full pipeline |
| `CM-2` (as a level) | [CM Level](#cm-level) | Managed execution — systems used by default in live decisions |

When any Atlas document or agent output uses a bare "L2" without further context, the reader must check which system is under discussion before assuming meaning — this glossary's category tags exist partly to make that check fast.

**Aliases:** None
**Canonical source:** This document (provisional home; no single sibling owns the disambiguation itself)
**Related terms:** [AI Maturity Model](#ai-maturity-model) · [Authority Band](#authority-band) · [Decision Level (DL)](#decision-level-dl) · [CM Level](#cm-level)

---

## Aliases and Synonyms

Atlas prefers exactly one canonical term per concept, but usage across documents, departments, and time inevitably produces near-synonyms. This section is the **single place** those synonyms are reconciled, so that a reader encountering the alias in an older document or an informal conversation can resolve it to the canonical term without guessing.

### Consolidated alias table

| Alias / informal term | Canonical term | Category |
|---|---|---|
| Owner | [Directly Responsible Individual (DRI)](#directly-responsible-individual-dri) | Organizational |
| DRI | [Directly Responsible Individual (DRI)](#directly-responsible-individual-dri) | Organizational |
| Single-threaded ownership | [Single Owner Principle](#single-owner-principle) | Organizational |
| Executor | [Contributor](#contributor) | Organizational |
| L-band | [Authority Band](#authority-band) | Organizational |
| Believability | [Believability-Weighted Decision Rights](#believability-weighted-decision-rights) | Organizational |
| Scale stage | [Org Stage](#org-stage) | Organizational |
| Dual-hat | [Dual-Hatting](#dual-hatting) | Organizational |
| Middleware management / relay layer | [Management Middleware](#management-middleware) | Organizational |
| Portfolio asset / asset (M&A sense) | [Portfolio Company](#portfolio-company) | Organizational |
| AI-first | [AI-Native](#ai-native) | AI |
| AI L-level / process maturity level | [AI Maturity Model](#ai-maturity-model) | AI |
| AI agent | [Agent](#agent) | AI |
| Automation ROI | [AI ROI](#ai-roi) | AI |
| Automation theater | [Automation Vanity](#automation-vanity) | AI |
| Portfolio intelligence | [Cross-Portfolio Intelligence](#cross-portfolio-intelligence) | AI |
| Retrieval-augmented generation | [RAG (Retrieval-Augmented Generation)](#rag-retrieval-augmented-generation) | AI |
| Truth over narrative | [Truth Over Comfort Principle](#truth-over-comfort-principle) | Governance |
| Data before intuition / data-driven decisions | [Evidence Over Opinion Principle](#evidence-over-opinion-principle) | Governance |
| Systems over heroics | [Systems Over Heroes Principle](#systems-over-heroes-principle) | Governance |
| Documentation before execution | [Extreme Documentation Principle](#extreme-documentation-principle) | Governance |
| Single source of truth | [One Source of Truth Principle](#one-source-of-truth-principle) | Governance |
| Reversible decision | [One-Way and Two-Way Doors](#one-way-and-two-way-doors) (two-way) | Governance |
| Irreversible commitment | [One-Way and Two-Way Doors](#one-way-and-two-way-doors) (one-way) | Governance |
| Header block | [Metadata Block](#metadata-block) | Governance |
| Not Invented Here syndrome | [NIH (Not Invented Here)](#nih-not-invented-here) | Governance |
| Shadow wiki | [Shadow Governance](#shadow-governance) | Governance |
| DR | [Decision Record (DR)](#decision-record-dr) | Governance |
| Horizon | [Vision Horizon](#vision-horizon) | Roadmap |
| Era | [Evolution Era](#evolution-era) | Roadmap |
| Arc | [Capability Arc](#capability-arc) | Roadmap |
| Phase / Roadmap Phase | [Major Phase](#major-phase) | Roadmap |
| Phase gate criteria | [Entry and Exit Criteria](#entry-and-exit-criteria) | Roadmap |
| SC | [Success Criteria](#success-criteria) | Roadmap |
| DL | [Decision Level (DL)](#decision-level-dl) | Decision Framework |
| Decision type | [Decision Class](#decision-class) | Decision Framework |
| Gate | [Decision Gate](#decision-gate) | Decision Framework |
| Decision review / Quarterly Decision Review | [Postmortem](#postmortem) | Decision Framework |
| CM | [Capability Maturity Model (CM)](#capability-maturity-model-cm) | Capability Maturity |
| Holding Capability Maturity | [Capability Maturity Model (CM)](#capability-maturity-model-cm) | Capability Maturity |
| Diagnostic CM score | [Aggregate CM Score](#aggregate-cm-score) | Capability Maturity |
| Business as usual | [BAU (Business As Usual)](#bau-business-as-usual) | Workflow |
| Postmortem (project sense) | [Retrospective](#retrospective) | Workflow |
| Root cause analysis | [RCA (Root Cause Analysis)](#rca-root-cause-analysis) | Workflow |
| SOP | [SOP (Standard Operating Procedure)](#sop-standard-operating-procedure) | Automation |
| Reserve bucket (specific instance) | [Capital Bucket](#capital-bucket) | Finance |
| Return on investment | [ROI (Return on Investment)](#roi-return-on-investment) | Finance |
| Holding ROIC | [ROIC (Return on Invested Capital)](#roic-return-on-invested-capital) | Finance |
| Monthly close / quarterly close | [Financial Close](#financial-close) | Finance |
| Mergers and acquisitions | [M&A (Mergers & Acquisitions)](#ma-mergers--acquisitions) | Finance |
| Minimum viable product | [MVP (Minimum Viable Product)](#mvp-minimum-viable-product) | Finance |
| Build vs. buy vs. acquire | [Build vs. Acquire](#build-vs-acquire) | Finance |
| Atlas OS / OS platform | [Atlas OS Platform](#atlas-os-platform) | Infrastructure |
| Portfolio data segmentation | [Data Segmentation](#data-segmentation) | Infrastructure |
| Document tier / T1–T5 | [Document Hierarchy](#document-hierarchy) | Document Authority |
| Canonical document / source of truth | [Canonical Source](#canonical-source) | Document Authority |
| Type document / instance document | [Instance vs. Type Document](#instance-vs-type-document) | Document Authority |

### Why aliases are tracked rather than banned

Banning natural variation in speech is unenforceable and counterproductive — operators will say "owner" long after "DRI" is written into templates. The discipline Atlas enforces instead is **resolvability**: every alias resolves to exactly one canonical term, and every canonical term's full entry is the place new documentation should cite from, even when casual writing uses the alias.

### Alias proposal rule

A new alias is added to this table, not a new competing definition, whenever a department reports that a term is being used informally with a meaning that already matches an existing canonical entry. If the informal usage means something **genuinely different**, it is a new term proposal, not an alias — see [Maintenance Process](#maintenance-process).

---

## Deprecated Terms

Deprecated terms are retained here — never deleted — so that older Decision Records, playbooks, or retrospectives that used them remain readable. Per [Deprecation](00_ATLAS_BRAIN.md#deprecation), a deprecated term is marked, pointed to its replacement, and never used in new documentation.

### Currently deprecated terms

As of this document's first version, Atlas has **zero deprecated terms** — this glossary is being populated for the first time, and no term has yet been retired or replaced. This section exists as active infrastructure for the first deprecation, not as a placeholder to be filled decoratively.

| Deprecated term | Replacement | Deprecated on | Reason | Decision Record |
|---|---|---|---|---|
| *(none yet)* | — | — | — | — |

### How a term becomes deprecated

1. A department or Brain identifies that a term is no longer accurate, has been superseded by a better term, or was found to conflict with a sibling document's usage.
2. A proposal is filed per [Maintenance Process](#maintenance-process), naming the replacement term (if any).
3. Every canonical-source document using the old term is checked for required updates.
4. The term's entry is moved from its category section into this section, with `Status: Deprecated`, a `Deprecated on` date, and a `Reason`.
5. If the deprecation is governance-significant (the term appeared in a Tier-1 or Tier-2 document), a Decision Record is logged in [`06_DECISIONS.md`](06_DECISIONS.md) and referenced here.

### What deprecation is not

- **Not deletion.** The old entry remains readable in this section indefinitely, so historical documents stay interpretable.
- **Not a value judgment on past usage.** A term can be perfectly correct at the time it was written and still be deprecated later because the concept evolved or merged with another.
- **Not silent.** A deprecated term without a documented replacement and reason is itself a documentation defect.

### Anticipated future deprecation candidates

None are currently flagged. When a term is used inconsistently across two or more Active sibling documents, Knowledge should flag it here as a **deprecation watch** item before it is formally deprecated, so that inconsistent usage does not silently compound. This watch list starts empty and is expected to be the first practical use of this section.

---

## Naming Conventions

Consistent naming is what makes IDs, filenames, and terms machine-legible — searchable by both humans and AI agents without a lookup table for every individual case. This section documents the **patterns**, not a list of every ID (those live in their respective canonical sources).

### Document filenames

| Rule | Example | Rationale |
|---|---|---|
| Two-digit zero-padded prefix + underscore + SCREAMING_SNAKE_CASE name + `.md` | `00_ATLAS_BRAIN.md`, `07_GLOSSARY.md` | Prefix encodes reading order; case signals "this is a governance document," not a casual note |
| Prefix numbers are never reused, even if a document is deprecated | — | Preserves historical reference stability |
| Department playbooks (once created) live under a `departments/` subfolder, not the root `02_Brain/` | `02_Brain/departments/knowledge_playbook.md` (planned) | Keeps the seven root T1 documents visually distinct from T3 material |

### Decision Record IDs

| Format | Example | Meaning |
|---|---|---|
| `DR-YYYY-NNN` | `DR-2026-001` | Year of logging + sequential number within that year, reset each January 1 |

See [`00_ATLAS_BRAIN.md` § Decision Record template](00_ATLAS_BRAIN.md#documentation-standards) for the full template this ID prefixes.

### Milestone IDs

| Format | Example | Meaning |
|---|---|---|
| `M-<cluster>-NNN` | `M-K-001`, `M-A-003` | Cluster letter (G=Governance, K=Knowledge, A=AI/Automation, F=Finance, O=Operations, P=Assets/Portfolio, J=Projects, I=Infrastructure/Platform) + sequential number within that cluster |

See [`04_ROADMAP.md` § Milestone register](04_ROADMAP.md#strategic-milestones) for the canonical register these IDs index.

### Success Criteria IDs

| Format | Example | Meaning |
|---|---|---|
| `SC-H<n>-NN` | `SC-H0-01`, `SC-H2-05` | Horizon number + sequential number within that horizon |

### CM Dimension IDs

| Format | Example | Meaning |
|---|---|---|
| `CM-D<n>` | `CM-D1`, `CM-D10` | Fixed set of ten, D1 through D10, never renumbered — see [CM Dimension](#cm-dimension) |

### Decision Level, Phase, Horizon, and Era prefixes

| Prefix | Range | Meaning | Never confuse with |
|---|---|---|---|
| `DL-` | 0–4 | [Decision Level](#decision-level-dl) | Bare `L` (AI Maturity or Authority Band) |
| `P` | 0–6 | [Major Phase](#major-phase) | `CM` levels (also 0–5-ish but a different axis) |
| `H` | 0–4 | [Vision Horizon](#vision-horizon) | `L`-levels or `DL`-levels |
| `E` | 0–3+ | [Evolution Era](#evolution-era) | `CM-D` dimension IDs (unrelated letter reuse) |
| `CM-` | 0–5 | [CM Level](#cm-level) | `L0`–`L4` AI Maturity (different scale, overlapping range) |
| `L` (bare) | 0–4 | [AI Maturity Model](#ai-maturity-model) **or** [Authority Band](#authority-band) — context-dependent | Everything above; see [L-Prefix Disambiguation](#l-prefix-disambiguation) |

### Series-stage prefixes (roadmap evolution tracks)

| Prefix | Series | Range |
|---|---|---|
| `AI-` | [AI Evolution Stage](#ai-evolution-stage) | AI-0 to AI-5 |
| `K-` | [Knowledge Evolution Stage](#knowledge-evolution-stage) | K-0 to K-5 |
| `W` | [Automation Wave](#automation-wave) | W0 to W5 |
| `F-` | Finance evolution stage | F-1 to F-4 |
| `HOS-` | Holding OS product stage | HOS-1 to HOS-5 |
| `G` | Geographic expansion stage | G0 to G3 |
| `M-ORG-` | Organization evolution milestone | M-ORG-001 and up |

These roadmap-evolution prefixes are deliberately distinct in letter choice from the governance-scale prefixes (`DL-`, `L`, `CM-`) precisely so a reader scanning `04_ROADMAP.md` never mistakes an evolution-track stage for a governance authority level.

### Capitalization rules

- **Department names** are capitalized as proper nouns when referring to the department itself: "Finance owns the close process," not "the finance department owns it" mid-sentence (though "the Finance department" is acceptable when clarity requires the word "department").
- **Principle names** are capitalized in title case when referenced as a named principle: "per Long-term thinking," not "per long term thinking."
- **Term-of-art phrases defined in this glossary** are capitalized consistently with their entry heading on first use in a document, then may be lowercased in casual subsequent prose within the same document if unambiguous.
- **Status values** (`Active`, `Draft`, `Deprecated`, `Proposed`, `Reviewed`, `Superseded`) are always capitalized exactly as shown, never lowercased, to keep them visually distinct from prose.

### Version number format

`MAJOR.MINOR` — a structural change, new section, or principle change bumps MAJOR; a content expansion or clarification bumps MINOR; a non-substantive edit (typo, formatting) requires no bump but a changelog note. See [`00_ATLAS_BRAIN.md` § Versioning Policy](00_ATLAS_BRAIN.md#versioning-policy) for full rules, inherited unchanged by this document.

### Date format

All dates in Atlas documents use ISO 8601 (`YYYY-MM-DD`) — never locale-ambiguous formats like `MM/DD/YYYY`. This is a silent convention observed across every sibling document and inherited here without a separate governance decision, because it was never actually a matter of choice once the first document set the pattern.

---

## Abbreviation Table

Every abbreviation and acronym used across the Brain document set, alphabetized, with full expansion, category, and — where the abbreviation is a scale or ID prefix rather than a single fixed meaning — a pointer to the series it belongs to. This table is the fastest lookup path for an AI agent resolving an unfamiliar short-form in retrieved text.

| Abbreviation | Expansion | Category | Notes |
|---|---|---|---|
| **AI** | Artificial Intelligence | AI | Core infrastructure department and discipline; see [AI-Native](#ai-native) |
| **AI-0…AI-5** | AI Evolution Stage 0 through 5 | Roadmap | See [AI Evolution Stage](#ai-evolution-stage) |
| **Arc A…Arc E** | Capability Arc A through E | Roadmap | See [Capability Arc](#capability-arc) |
| **BAU** | Business As Usual | Workflow | See [BAU](#bau-business-as-usual) |
| **CFO** | Chief Financial Officer | Organizational | Default title band for Head of Finance, per [`03_ORGANIZATION.md`](03_ORGANIZATION.md#department-architecture-overview) |
| **CM** | Capability Maturity (Model) | Capability Maturity | See [Capability Maturity Model (CM)](#capability-maturity-model-cm) |
| **CM-D1…CM-D10** | Capability Maturity Dimension 1 through 10 | Capability Maturity | See [CM Dimension](#cm-dimension) |
| **COO** | Chief Operating Officer | Organizational | Default title band for Head of Operations |
| **DD** | Due Diligence | Finance | Evidence-gathering process for Investment-class decisions, especially M&A |
| **DL** | Decision Level | Decision Framework | Always hyphenated with its number, e.g., `DL-2` — see [Decision Level (DL)](#decision-level-dl) |
| **DR** | Decision Record | Governance | See [Decision Record (DR)](#decision-record-dr) |
| **DRI** | Directly Responsible Individual | Organizational | See [Directly Responsible Individual (DRI)](#directly-responsible-individual-dri) |
| **E0, E1, E2, E3+** | Evolution Era 0 through 3-plus | Roadmap | See [Evolution Era](#evolution-era) |
| **E-Build, E-Acquire, etc.** | Expansion Mode (Build, Acquire, Integrate-deep, Shared-services, Platform, Sector, Geo, External-knowledge, Operator-network) | Roadmap | See [Expansion Mode](#expansion-mode) |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization | Finance | Referenced implicitly in [Long-term thinking examples](02_FOUNDING_PRINCIPLES.md#long-term-thinking); not yet formally defined as an Atlas-specific metric |
| **F-1…F-4** | Finance Evolution Stage 1 through 4 | Roadmap | See [`04_ROADMAP.md` § Finance evolution stages](04_ROADMAP.md#finance-and-capital-evolution) |
| **G0…G3** | Geographic expansion stage 0 through 3 | Roadmap | See [`04_ROADMAP.md` § Geographic expansion](04_ROADMAP.md#expansion-strategy) |
| **HOS** | Holding Operating System | Organizational | See [Holding Operating System](#holding-operating-system-holding-os--hos) |
| **HOS-1…HOS-5** | Holding OS Product Stage 1 through 5 | Roadmap | See [`04_ROADMAP.md` § Holding OS product evolution](04_ROADMAP.md#product-evolution) |
| **IC** | Individual Contributor | Organizational | See [Individual Contributor (IC)](#individual-contributor-ic) |
| **IP** | Intellectual Property | Finance | Referenced in irreversible-commitment triggers (IP transfer) — see [Escalation](00_ATLAS_BRAIN.md#escalation) |
| **IRR** | Internal Rate of Return | Finance | See [IRR (Internal Rate of Return)](#irr-internal-rate-of-return) |
| **K-0…K-5** | Knowledge Evolution Stage 0 through 5 | Roadmap | See [Knowledge Evolution Stage](#knowledge-evolution-stage) |
| **KPI** | Key Performance Indicator | Workflow | Used throughout department, project, and portfolio reporting |
| **L0…L4** | Level 0 through 4 (context-dependent) | AI / Organizational | Ambiguous by itself — resolves to either [AI Maturity Model](#ai-maturity-model) or [Authority Band](#authority-band); see [L-Prefix Disambiguation](#l-prefix-disambiguation) |
| **L-Doc, L-Access, L-Data, L-Automation, L-Observe, L-Platform, L-Edge** | Infrastructure Layer names | Infrastructure | See [Infrastructure Layer](#infrastructure-layer) |
| **M&A** | Mergers & Acquisitions | Finance | See [M&A (Mergers & Acquisitions)](#ma-mergers--acquisitions) |
| **M-<cluster>-NNN** | Milestone ID | Roadmap | See [Naming Conventions § Milestone IDs](#naming-conventions) |
| **MOIC** | Multiple on Invested Capital | Finance | See [MOIC (Multiple on Invested Capital)](#moic-multiple-on-invested-capital) |
| **MVP** | Minimum Viable Product | Finance | See [MVP (Minimum Viable Product)](#mvp-minimum-viable-product) |
| **NIH** | Not Invented Here | Governance | See [NIH (Not Invented Here)](#nih-not-invented-here) |
| **OS** | Operating System | Organizational | Almost always appears as part of "Holding OS" or "Atlas OS" — see [Holding Operating System](#holding-operating-system-holding-os--hos) |
| **P0…P6** | Roadmap Phase 0 through 6 | Roadmap | See [Major Phase](#major-phase) |
| **P&L** | Profit and Loss (statement) | Finance | Standard financial statement referenced in [Organizational Architecture](00_ATLAS_BRAIN.md#organizational-architecture) |
| **RAG** | Retrieval-Augmented Generation | AI | See [RAG (Retrieval-Augmented Generation)](#rag-retrieval-augmented-generation) |
| **RCA** | Root Cause Analysis | Workflow | See [RCA (Root Cause Analysis)](#rca-root-cause-analysis) |
| **ROI** | Return on Investment | Finance | See [ROI (Return on Investment)](#roi-return-on-investment) |
| **ROIC** | Return on Invested Capital | Finance | See [ROIC (Return on Invested Capital)](#roic-return-on-invested-capital) |
| **SC-H<n>-NN** | Success Criteria ID | Roadmap | See [Success Criteria](#success-criteria) |
| **SLA** | Service Level Agreement | Organizational | See [SLA (Service Level Agreement)](#sla-service-level-agreement) |
| **SOP** | Standard Operating Procedure | Automation | See [SOP (Standard Operating Procedure)](#sop-standard-operating-procedure) |
| **T1…T5** | Document Tier 1 through 5 | Governance | See [Document Hierarchy](#document-hierarchy) |
| **TBD** | To Be Decided | Document Authority | Used in [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) to mark a field with no owner or target date yet assigned, distinct from "Unknown" (no decision pending, only information-gathering) |
| **VP** | Vice President | Organizational | Referenced only as an example of traditional-hierarchy titling that Atlas's department model replaces; not an Atlas title |
| **W0…W5** | Automation Wave 0 through 5 | Roadmap | See [Automation Wave](#automation-wave) |

### Abbreviations deliberately not assigned a single meaning

A small number of short forms are **intentionally polysemous** across Atlas documents, and this table resolves them by pointing to disambiguation guidance rather than picking one meaning:

- **"L2"** — see [L-Prefix Disambiguation](#l-prefix-disambiguation).
- **"P0"** in casual speech could mean [Major Phase](#major-phase) P0 or, in an incident-severity context borrowed from common industry usage, "priority zero" — Atlas does not use severity-numbered incident priorities as of this version, so "P0" should always resolve to the roadmap phase unless a future incident-management standard introduces the other meaning explicitly.

---

## Cross References

This section maps, in the opposite direction from every individual entry's "Canonical source" link, **which glossary terms each sibling document depends on** — useful when revising a sibling document, to know which glossary entries must be checked for continued accuracy.

### `00_ATLAS_BRAIN.md` depends on

[Holding Operating System](#holding-operating-system-holding-os--hos) · [Department](#department) · [AI Maturity Model](#ai-maturity-model) · [Agent](#agent) · [Agent Design Standards](#agent-design-standards) · [Decision Level (DL)](#decision-level-dl) · [Document Hierarchy](#document-hierarchy) · [Metadata Block](#metadata-block) · [Company Lifecycle](#company-lifecycle) · [Project Lifecycle](#project-lifecycle) · [Onboarding Knowledge Path](#onboarding-knowledge-path) · [AI Adoption Process](#ai-adoption-process) · [Version (document field)](#version-document-field)

### `01_WHY_ATLAS_EXISTS.md` depends on

[Coordination Tax](#coordination-tax) · [Management Middleware](#management-middleware) · [AI-Native](#ai-native) · [Cross-Portfolio Intelligence](#cross-portfolio-intelligence) · [Holding Operating System](#holding-operating-system-holding-os--hos)

### `02_FOUNDING_PRINCIPLES.md` depends on

[Opinion, Value, Policy, Process, Principle](#opinion-value-policy-process-principle) · [Principle Evolution Tiers](#principle-evolution-tiers) · [Truth Over Comfort Principle](#truth-over-comfort-principle) · [Systems Over Heroes Principle](#systems-over-heroes-principle) · [Extreme Documentation Principle](#extreme-documentation-principle) · [One Source of Truth Principle](#one-source-of-truth-principle) · [Compounding Over Optimization](#compounding-over-optimization) · [Evidence Over Opinion Principle](#evidence-over-opinion-principle) · [Capital Efficiency Principle](#capital-efficiency-principle) · [Transparency Principle](#transparency-principle) · [One-Way and Two-Way Doors](#one-way-and-two-way-doors) · [Skill Atrophy](#skill-atrophy) · [Black Box Trust](#black-box-trust) · [Automation Vanity](#automation-vanity)

### `03_ORGANIZATION.md` depends on

[Department](#department) · [Directly Responsible Individual (DRI)](#directly-responsible-individual-dri) · [Single Owner Principle](#single-owner-principle) · [Contributor](#contributor) · [Deputy](#deputy) · [Authority Band](#authority-band) · [Believability-Weighted Decision Rights](#believability-weighted-decision-rights) · [Escalation](#escalation) · [Escalation Threshold](#escalation-threshold) · [Org Stage](#org-stage) · [Seven-Department Invariant](#seven-department-invariant) · [Role Charter](#role-charter) · [Governance Council](#governance-council) · [Interface (department)](#interface-department) · [SLA (Service Level Agreement)](#sla-service-level-agreement)

### `04_ROADMAP.md` depends on

[Vision Horizon](#vision-horizon) · [Evolution Era](#evolution-era) · [Capability Arc](#capability-arc) · [Major Phase](#major-phase) · [Entry and Exit Criteria](#entry-and-exit-criteria) · [Milestone](#milestone) · [Milestone Health State](#milestone-health-state) · [Success Criteria](#success-criteria) · [Anti-Success](#anti-success) · [North-Star Test](#north-star-test) · [Decade Checkpoint](#decade-checkpoint) · [Capability Maturity Model (CM)](#capability-maturity-model-cm) · [CM Dimension](#cm-dimension) · [CM Level](#cm-level) · [Weakest-Link Method](#weakest-link-method) · [Aggregate CM Score](#aggregate-cm-score) · [Expansion Mode](#expansion-mode) · [AI Evolution Stage](#ai-evolution-stage) · [Knowledge Evolution Stage](#knowledge-evolution-stage) · [Automation Wave](#automation-wave) · [Infrastructure Layer](#infrastructure-layer) · [Reliability Class](#reliability-class) · [Portal](#portal) · [Atlas OS Platform](#atlas-os-platform)

### `05_CURRENT_STATE.md` depends on

[Instance vs. Type Document](#instance-vs-type-document) · [Chain of Custody](#chain-of-custody-for-facts) · [CM Level](#cm-level) · [Org Stage](#org-stage) · [Decision Level (DL)](#decision-level-dl) — plus every term whose live value it reports against a framework defined elsewhere

### `06_DECISIONS.md` depends on

[Decision Level (DL)](#decision-level-dl) · [Decision Class](#decision-class) · [Sub-Class (decision)](#sub-class-decision) · [Decision Lifecycle](#decision-lifecycle) · [Decision Pipeline](#decision-pipeline) · [Decision Gate](#decision-gate) · [Evidence Checklist](#evidence-checklist) · [Bias Detection](#bias-detection) · [Sizing Test](#sizing-test) · [Level Inflation / Deflation](#level-inflation--deflation) · [Postmortem](#postmortem) · [Decision Register](#decision-register) · [AI-Assisted Decision](#ai-assisted-decision) · [Decision Record (DR)](#decision-record-dr)

### How to keep cross-references accurate

Whenever a term's canonical source changes (the term moves to a different sibling, or a sibling adds a new term of art), update **both**:

1. The term's entry in this document's category section (its `Canonical source` line).
2. The relevant sibling's list in this section.

This is a manual synchronization step today; it is a natural candidate for automation once Atlas's knowledge base tooling ([`04_ROADMAP.md` § Knowledge Evolution Stage](04_ROADMAP.md#knowledge-evolution-stage)) reaches a stage where document dependency graphs are machine-derived rather than hand-maintained.

---

## Maintenance Process

This document is only as trustworthy as its update discipline. This section defines exactly how a term enters, changes, or leaves this glossary — mirroring the rigor [`06_DECISIONS.md`](06_DECISIONS.md) applies to decisions, because an unmanaged vocabulary change is itself a decision with holding-wide blast radius.

### Who owns what

| Responsibility | Owner |
|---|---|
| Final ratification of new or changed Active terms | Brain |
| Day-to-day curation, alphabetization, cross-link integrity | Knowledge |
| Proposing new terms from lived usage | Any department |
| Verifying a term's short definition still matches its canonical source | Knowledge, on every sibling document revision |
| Flagging drift between two siblings' usage of the same term | Any department, escalated to Brain |

Per [Document Authority § Authority scope](#document-authority), this document's owner curates definitions; it does not originate the concepts those definitions describe.

### Proposal workflow

```
1. PROPOSE   → Department opens a proposal: term, draft definition, category,
               proposed canonical source (existing sibling section or "new,
               owned by this glossary provisionally").
2. CHECK     → Knowledge checks: does this term already exist under a
               different name (→ becomes an alias, not a new entry)? Does
               its meaning conflict with existing usage in a sibling
               document (→ resolve conflict before proceeding)?
3. DRAFT     → Knowledge drafts the full entry per Entry Anatomy
               (see How to Use This Glossary), in the correct category
               section, in alphabetical position within that section.
4. INDEX     → Knowledge adds the term to the Alphabetical Index and,
               if it is an abbreviation, to the Abbreviation Table.
5. RATIFY    → Brain reviews and marks the term Active. For terms whose
               canonical source is a T1 document, Brain approval is
               mandatory before the term is usable as a citation target.
6. PUBLISH   → Version bump per Versioning Policy; changelog entry added.
```

A term may be used informally in conversation or draft documents before it completes this workflow, but should not be cited authoritatively (e.g., in a Decision Record or Role Charter) until it reaches **Active** status.

### Change workflow (editing an existing Active term)

1. Propose the change with the specific text diff and the reason (usage drift, sibling document update, correction of an error).
2. If the change is **non-substantive** (typo, formatting, link fix), Knowledge may apply it directly and log it in the changelog with no Brain review required.
3. If the change is **substantive** (meaning shifts, category changes, canonical source changes), it follows the same Check → Draft → Ratify → Publish steps as a new term.
4. If the change affects a term that appears in a **T1 or T2 document's own text** (not just this glossary), the sibling document is flagged for a corresponding update.

### Deprecation workflow

See [Deprecated Terms § How a term becomes deprecated](#deprecated-terms) for the full deprecation sequence. Deprecation is a Change workflow with a mandatory Brain review step, regardless of how small the wording change looks, because removing a term from active use has downstream effects on every document that cites it.

### Conflict resolution during proposal

If two departments propose different definitions for what turns out to be the same underlying concept:

1. Knowledge attempts to reconcile by identifying which department's usage is closer to the term's actual canonical source (if one already exists in a sibling document).
2. If no canonical source exists yet, Brain adjudicates which definition becomes canonical, and the other becomes a documented alias or a distinguished, separately named term if the concepts are subtly but genuinely different.
3. The adjudication itself, if material, is logged as a Decision Record per [`06_DECISIONS.md`](06_DECISIONS.md#decision-templates).

### Review cadence

This document follows the same review cadence as its siblings: a full pass every quarter, checking every entry's canonical-source link still resolves and every definition still matches current usage, plus an ad hoc check any time a sibling document undergoes a MAJOR version bump. See [`Review date`](#review-date-field) in this document's own metadata block for the next scheduled review.

### Quality bar for a new entry

Before ratification, every new entry must pass:

- [ ] Definition is 1–4 sentences, precise, no rhetorical framing.
- [ ] Canonical source link resolves to a real section in a real document (or is explicitly flagged as provisionally owned by this glossary).
- [ ] Category assignment matches the term's dominant usage domain.
- [ ] Aliases field is populated (with "None" if there truly are none) — never left blank.
- [ ] At least one Related terms link, unless the term is genuinely freestanding.
- [ ] Term appears in the Alphabetical Index in correct alphabetical position.
- [ ] If the term is an abbreviation or has one, it appears in the Abbreviation Table.

---

## Appendices

### Appendix A — Full category-to-document map

A denser restatement of [Term Categories Overview](#term-categories-overview), listing every canonical source document each category draws from, in priority order:

| Category | Primary source | Secondary sources |
|---|---|---|
| Organizational | [`03_ORGANIZATION.md`](03_ORGANIZATION.md) | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md), [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) |
| AI | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) § AI Strategy | [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) § AI-first thinking, [`06_DECISIONS.md`](06_DECISIONS.md) § AI-Assisted Decisions |
| Governance | [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) § Documentation Standards |
| Roadmap | [`04_ROADMAP.md`](04_ROADMAP.md) | [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) for live values |
| Decision Framework | [`06_DECISIONS.md`](06_DECISIONS.md) | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) § Decision Framework (short form) |
| Capability Maturity | [`04_ROADMAP.md`](04_ROADMAP.md) § Capability Maturity Model | [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) for live scores |
| Workflow | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) § Project/Company Lifecycle | [`03_ORGANIZATION.md`](03_ORGANIZATION.md) § Onboarding/Offboarding |
| Automation | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) § Automation Standards | [`03_ORGANIZATION.md`](03_ORGANIZATION.md) § Department: AI |
| Finance | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) § Capital Allocation | [`03_ORGANIZATION.md`](03_ORGANIZATION.md) § Department: Finance |
| Infrastructure | [`04_ROADMAP.md`](04_ROADMAP.md) § Infrastructure Evolution | — |
| Document Authority | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) § Documentation Standards | [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) § Document Authority |

### Appendix B — Term count by category

A structural snapshot as of this version, useful for spotting category imbalance at a glance during quarterly review:

| Category | Active term count (approx.) |
|---|---|
| Organizational | 20 |
| AI | 17 |
| Governance | 24 |
| Roadmap | 20 |
| Decision Framework | 13 |
| Capability Maturity | 6 |
| Workflow | 12 |
| Automation | 8 |
| Finance | 15 |
| Infrastructure | 7 |
| Document Authority | 15 |

Counts are approximate and intentionally not treated as a KPI — a glossary is not improved by adding terms for their own sake, per [Non-goals of this document](#non-goals-of-this-document). This table exists only to help Knowledge notice if one category is growing suspiciously faster than the underlying document it draws from, which usually signals term duplication rather than real growth.

### Appendix C — Retired abbreviation collisions

A log of abbreviation collisions caught and resolved **before** they caused confusion in a live document, kept here as institutional memory of why certain prefix choices were made deliberately:

| Collision | Resolution | Rationale |
|---|---|---|
| Decision Level using bare "L" (would collide with AI Maturity and Authority Band) | Adopted `DL-` prefix instead | See [L-Prefix Disambiguation](#l-prefix-disambiguation) |
| Roadmap Phase using "L" (would collide with the above three) | Adopted `P` prefix instead | Kept roadmap sequencing visually distinct from any governance-scale prefix |
| CM Level using bare "L" (would collide with AI Maturity, which shares the same 0–5-ish numeric range) | Adopted `CM-` prefix instead | Prevents "L3" from being read as a capability score |

### Appendix D — Candidate terms not yet fully canonical

Terms in active informal use across Atlas conversation and drafts, which this glossary has deliberately **not yet promoted to Active status**, because their canonical source is still forming. Per [How to Use This Glossary](#how-to-use-this-glossary), check here before assuming a term does not exist.

| Candidate term | Where it's used informally | Why not yet Active | Tracking |
|---|---|---|---|
| "Integration playbook" | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) Future Expansion, [`03_ORGANIZATION.md`](03_ORGANIZATION.md) | The playbook itself does not yet exist as a written document; the term describes a planned artifact, not yet a ratified concept with stable content | [`00_ATLAS_BRAIN.md` § Future Expansion](00_ATLAS_BRAIN.md#future-expansion) |
| "Atlas OS platform" (as a shipped product, distinct from the Holding OS concept) | [`04_ROADMAP.md`](04_ROADMAP.md), [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) Future Expansion | Defined in this glossary as a roadmap target (see [Atlas OS Platform](#atlas-os-platform)), but its eventual production feature set is not yet fixed enough to fully canonicalize sub-terms (e.g., specific portal modules) | [`04_ROADMAP.md` § Infrastructure Evolution](04_ROADMAP.md#infrastructure-evolution) |
| "Operator network" | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) Future Expansion | Long-term (12+ month) planned concept with no current structure, membership model, or governance defined | [`00_ATLAS_BRAIN.md` § Future Expansion](00_ATLAS_BRAIN.md#future-expansion) |
| "Vendor management framework" | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) Future Expansion | Not yet written; would need its own standard before this glossary defines vendor-specific vocabulary | [`00_ATLAS_BRAIN.md` § Future Expansion](00_ATLAS_BRAIN.md#future-expansion) |
| "Coordination tax audit" | [`03_ORGANIZATION.md`](03_ORGANIZATION.md) § Stage 3/4 | Named as a future practice at scale, without a defined method or cadence yet | [`03_ORGANIZATION.md` § Organizational Scaling](03_ORGANIZATION.md#organizational-scaling) |

When any row in this table gains a stable canonical source, it should be promoted to a full entry in its category section and removed from this appendix, per [Maintenance Process](#maintenance-process).

### Appendix E — Worked disambiguation examples

Three worked examples showing how to use this glossary to resolve a genuinely ambiguous phrase encountered in the wild:

**Example 1 — "The project is at L2."**
Check context: is this a project status update (would use [Project Health Signal](#project-health-signal), which is color-coded, not numeric) or an automation status update (would use [AI Maturity Model](#ai-maturity-model), L2 = Supervised automation)? A bare "L2" attached to "the project" most likely means the *automation supporting* the project is at AI Maturity L2 — resolve by asking the author, and flag the sentence as a documentation defect for using an ambiguous shorthand.

**Example 2 — "That's a DL-3, get Brain involved."**
Unambiguous: `DL-` prefix always means [Decision Level (DL)](#decision-level-dl). DL-3 = Major decision, full pipeline, Brain-level sign-off — the sentence is using the term correctly.

**Example 3 — "Our CM is basically a 2 right now."**
Check whether "our CM" refers to the [Aggregate CM Score](#aggregate-cm-score) (holding-wide average) or a specific [CM Dimension](#cm-dimension) (e.g., CM-D4, Automation). If unspecified, default to assuming Aggregate CM Score, per [Weakest-Link Method](#weakest-link-method) guidance that aggregate scores without a named dimension should be treated cautiously, since [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) reports both the weakest-link level and the aggregate, and they can differ significantly.

---

## Versioning Policy

This document inherits the holding-wide versioning policy defined in [`00_ATLAS_BRAIN.md` § Versioning Policy](00_ATLAS_BRAIN.md#versioning-policy) without modification. Restated here for convenience:

### Version format

**MAJOR.MINOR**

| Change type | Version bump | Example |
|---|---|---|
| Structural change (new category section, new required entry field, TOC reorganization) | MAJOR | 1.0 → 2.0 |
| Content expansion (new term, expanded definition, new appendix row) | MINOR | 1.0 → 1.1 |
| Typo, formatting, broken-link fix | No bump | Note in changelog |

### What counts as a MAJOR change specifically for this document

- Adding or removing one of the eleven term categories.
- Changing the required fields in [Entry Anatomy](#how-to-use-this-glossary) (e.g., adding a mandatory "Introduced in version" field to every entry).
- Re-deriving the Alphabetical Index generation method (e.g., moving from manual to automated generation) in a way that changes existing anchors.

### What counts as a MINOR change specifically for this document

- Adding a new Active term to any category section.
- Promoting a term from Proposed to Active.
- Deprecating a term (also logged in [Deprecated Terms](#deprecated-terms) directly).
- Adding a new alias, abbreviation, or cross-reference.

### Current version

| Field | Value |
|---|---|
| Document | `07_GLOSSARY.md` |
| Location | `02_Brain/` |
| Status | Active |
| Version | 1.0 |
| Last updated | 2026-08-08 |
| Next review | 2026-11-08 |

---

## Document Maintenance

| Field | Value |
|---|---|
| **Canonical owner** | Knowledge department (curation and maintenance); Brain (ratification of Active status for governance-significant terms) |
| **Suggested readers** | All operators (reference); AI agents (primary disambiguation target); department heads (playbook and SOP authoring); new hires (onboarding, third document read) |
| **Change process** | Propose per [Maintenance Process](#maintenance-process) → Knowledge draft → Brain ratification for T1-linked terms → version bump per [Versioning Policy](#versioning-policy) → notify departments if a widely-cited term's meaning changed |
| **Review cadence** | Quarterly (aligned with T1/T2 governance schedule), plus ad hoc on any sibling document MAJOR version bump |
| **AI retrieval note** | Agents should treat this document as the first-stop disambiguation target for any term-of-art or abbreviation before inferring meaning from surrounding context — see [AI retrieval note](#document-authority) under Document Authority above |

### Changelog

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-08-08 | Initial release — full canonical glossary: purpose, philosophy, alphabetical index, eleven category sections with complete term definitions, aliases and synonyms, deprecated terms (empty, tracked), naming conventions, abbreviation table, cross-references, maintenance process, appendices, versioning policy |

---

*This glossary is infrastructure, not decoration — every term here exists because it is actually used, and every definition here points back to the document that earned the right to define it.*

*For strategy, see [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md). For conviction, see [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md). For principle depth, see [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md). For structure, see [`03_ORGANIZATION.md`](03_ORGANIZATION.md). For sequencing, see [`04_ROADMAP.md`](04_ROADMAP.md). For today's facts, see [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md). For precedent, see [`06_DECISIONS.md`](06_DECISIONS.md).*
