# Atlas Roadmap

> The canonical multi-horizon roadmap for Atlas — vision, phases, capability maturity, evolution tracks, planning models, and ownership. This document sequences *where Atlas is going*; it does not redefine *why* or *how* Atlas thinks.

**Document ID:** `04_ROADMAP.md`  
**Location:** `02_Brain/`  
**Status:** Active  
**Version:** 1.0  
**Owner:** Brain  
**Classification:** Governance — strategic roadmap  
**Last updated:** 2026-08-08  
**Review date:** 2026-11-08  
**Supersedes:** —  
**Authority:** This document is the authoritative source for *strategic horizons*, *phased evolution*, *capability maturity targets*, *milestone sequencing*, and *roadmap governance*. Principles live in sibling Brain documents — link to them; do not duplicate.

---

## Table of Contents

1. [Purpose](#purpose)
2. [How to Read This Roadmap](#how-to-read-this-roadmap)
3. [Relationship to Other Brain Documents](#relationship-to-other-brain-documents)
4. [Vision Horizon](#vision-horizon)
5. [Roadmap Architecture](#roadmap-architecture)
6. [Multi-Year Evolution](#multi-year-evolution)
7. [Major Phases](#major-phases)
8. [Strategic Milestones](#strategic-milestones)
9. [Capability Maturity Model](#capability-maturity-model)
10. [Success Criteria](#success-criteria)
11. [Expansion Strategy](#expansion-strategy)
12. [AI Evolution](#ai-evolution)
13. [Infrastructure Evolution](#infrastructure-evolution)
14. [Knowledge Evolution](#knowledge-evolution)
15. [Organization Evolution](#organization-evolution)
16. [Product Evolution](#product-evolution)
17. [Automation Evolution](#automation-evolution)
18. [Finance and Capital Evolution](#finance-and-capital-evolution)
19. [Portfolio and Assets Evolution](#portfolio-and-assets-evolution)
20. [Operations Evolution](#operations-evolution)
21. [Projects Evolution](#projects-evolution)
22. [Scaling Plan](#scaling-plan)
23. [Milestone Dependencies](#milestone-dependencies)
24. [Long-Term Risks](#long-term-risks)
25. [What Is NOT on the Roadmap](#what-is-not-on-the-roadmap)
26. [Quarterly Planning Model](#quarterly-planning-model)
27. [Annual Planning Model](#annual-planning-model)
28. [Roadmap Review Process](#roadmap-review-process)
29. [Roadmap Ownership](#roadmap-ownership)
30. [Change Control](#change-control)
31. [Measurement and Scorecards](#measurement-and-scorecards)
32. [Horizon Checklists](#horizon-checklists)
33. [Scenario Planning](#scenario-planning)
34. [Anti-Patterns](#anti-patterns)
35. [Practical Examples](#practical-examples)
36. [Cross References](#cross-references)
37. [Document Maintenance](#document-maintenance)

**Related documents:** [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) · [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) · [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) · [`03_ORGANIZATION.md`](03_ORGANIZATION.md) · [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) · [`06_DECISIONS.md`](06_DECISIONS.md) · [`07_GLOSSARY.md`](07_GLOSSARY.md)

---

## Purpose

### What this document is

This document defines **where Atlas is going across time** — the strategic sequencing layer that converts vision and principles into horizons, phases, milestones, maturity targets, and planning cadences.

It answers:

- **What horizons matter** — near-term foundation through multi-decade institution
- **What phases Atlas must pass through** — ordered capability build, not wishful parallelism
- **What "done" means at each stage** — success criteria and maturity gates
- **How capabilities evolve** — AI, infrastructure, knowledge, organization, product, automation
- **How Atlas expands** — build, acquire, integrate, and scale without abandoning form
- **How planning works** — quarterly and annual models, review process, ownership
- **What is deliberately excluded** — scope discipline so the roadmap stays executable

### What this document is not

| This document | Lives elsewhere |
|---|---|
| Mission, vision statements, operating philosophy | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) |
| Why Atlas exists; 50-year philosophical horizon | [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) |
| Immutable principles and judgment infrastructure | [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) |
| Departments, ownership, authority, escalation | [`03_ORGANIZATION.md`](03_ORGANIZATION.md) |
| Decision scoring, one-way doors, capital philosophy | [Decision Framework](00_ATLAS_BRAIN.md#decision-framework), [Capital Allocation](00_ATLAS_BRAIN.md#capital-allocation-philosophy) |
| Current headcount, active thresholds, live priorities | [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) |
| Logged decisions and precedents | [`06_DECISIONS.md`](06_DECISIONS.md) |
| Canonical term definitions | [`07_GLOSSARY.md`](07_GLOSSARY.md) |
| AI maturity levels L0–L4 (definition) | [AI Strategy](00_ATLAS_BRAIN.md#ai-strategy) |
| Project and company lifecycle stages (definition) | [Project Lifecycle](00_ATLAS_BRAIN.md#project-lifecycle), [Company Lifecycle](00_ATLAS_BRAIN.md#company-lifecycle) |

### Primary audience

| Audience | How to use this document |
|---|---|
| **Brain / leadership** | Set and recalibrate horizons; gate phase transitions |
| **Department heads** | Align department roadmaps to holding phases and maturity targets |
| **Portfolio leaders** | Understand what infrastructure arrives when; plan local work accordingly |
| **Project DRIs** | Sequence initiatives against milestone dependencies |
| **AI agents** | Resolve phase gates, maturity targets, and planning cadence rules |
| **Future leaders** | Continuity of strategic intent across generations of operators |

### Design intent

Atlas is an **AI-native holding company** designed to compound over decades. A roadmap that only lists near-term features is inadequate. This document is **executable strategy over time** — as durable as principles, as measurable as financial statements, and as legible to machines as to humans.

The roadmap exists to **sequence the Brain's intent**, not replace it. When roadmap and principles conflict, principles win. When roadmap and current state conflict, update the roadmap or the plan — never silently ignore either.

### Non-goals of this document

- Does not invent new principles (see [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md)).
- Does not redefine department ownership (see [`03_ORGANIZATION.md`](03_ORGANIZATION.md)).
- Does not hold live numeric thresholds (see [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md)).
- Does not replace quarterly OKRs or project briefs — it constrains them.
- Does not promise specific portfolio companies, markets, or product names.

---

## How to Read This Roadmap

### Layers of time

Read this document as five nested time layers:

```
┌─────────────────────────────────────────────────────────────┐
│  VISION HORIZON (decades)                                   │
│  What Atlas becomes as institutional infrastructure         │
└──────────────────────────┬──────────────────────────────────┘
                           │ informs
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  MULTI-YEAR EVOLUTION (1–20+ years)                         │
│  Eras and capability arcs                                   │
└──────────────────────────┬──────────────────────────────────┘
                           │ sequences
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  MAJOR PHASES (gated stages)                                │
│  Entry criteria · exit criteria · milestone bundles         │
└──────────────────────────┬──────────────────────────────────┘
                           │ drives
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  ANNUAL PLAN (12 months)                                    │
│  Theme · capital buckets · phase focus                      │
└──────────────────────────┬──────────────────────────────────┘
                           │ decomposes
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  QUARTERLY PLAN (90 days)                                   │
│  Priorities · projects · maturity deltas · reviews          │
└─────────────────────────────────────────────────────────────┘
```

### How Current State interacts

| Document | Role | Update cadence |
|---|---|---|
| This roadmap | Stable strategic sequencing | Semi-annual major; quarterly minor |
| [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) | Live snapshot of where we are | Quarterly or on material change |
| Department playbooks | How we execute in each domain | On process change |
| Project briefs | Time-bound delivery | Per project |

**Rule:** The roadmap says *what phase we are building toward*. Current State says *what phase we are in and what is true today*. Never treat Current State as strategy or the roadmap as a status report.

### Reading paths

| If you need… | Read… |
|---|---|
| Why we exist before planning | [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) then this doc § Vision Horizon |
| What phase we should prioritize now | § Major Phases + [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) |
| Whether a project fits the roadmap | § What Is NOT on the Roadmap + § Milestone Dependencies |
| How to plan next quarter | § Quarterly Planning Model |
| How AI should mature | § AI Evolution + [AI Strategy](00_ATLAS_BRAIN.md#ai-strategy) |
| How org headcount should grow | § Organization Evolution + [Organizational Scaling](03_ORGANIZATION.md#organizational-scaling) |
| How to change this document | § Change Control + § Roadmap Ownership |

### Terminology used here

Terms follow [`07_GLOSSARY.md`](07_GLOSSARY.md) when defined. Until the glossary is complete, this document uses:

| Term | Meaning in this roadmap |
|---|---|
| **Horizon** | A time band of strategic intent (e.g., H0–H4) |
| **Phase** | A gated stage with entry/exit criteria |
| **Milestone** | A verifiable outcome that advances a phase |
| **Maturity level** | Measured capability state (CM-0–CM-5 for holding; L0–L4 for AI processes) |
| **Track** | A parallel evolution stream (AI, Knowledge, Org, etc.) |
| **Gate** | A go/no-go review before phase transition |
| **Theme** | Annual focus that constrains quarterly priorities |

---

## Relationship to Other Brain Documents

### Authority stack

```
Principles (02)  →  constrain  →  Brain OS (00)  →  constrain  →  Organization (03)
        │                              │                              │
        └──────────────┬───────────────┴──────────────┬───────────────┘
                       ▼                              ▼
                 Why Exists (01)                 Roadmap (04)  ← this document
                       │                              │
                       └──────────────┬───────────────┘
                                      ▼
                         Current State (05) · Decisions (06) · Glossary (07)
```

### Hard rules for cross-document consistency

1. **Do not restate principles.** Link to [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md).
2. **Do not redefine departments.** Link to [`03_ORGANIZATION.md`](03_ORGANIZATION.md).
3. **Do not redefine AI L0–L4.** Link to [AI maturity model](00_ATLAS_BRAIN.md#ai-maturity-model); this roadmap only sets *targets by phase*.
4. **Do not hold live metrics.** Put current numbers in [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md).
5. **Material roadmap changes** require a Decision Record in [`06_DECISIONS.md`](06_DECISIONS.md).
6. **Philosophical 50-year context** lives in [The Long-Term Vision](01_WHY_ATLAS_EXISTS.md#the-long-term-vision-50-years); this roadmap operationalizes eras into phases and gates.

### What Brain Future Expansion maps to here

The Brain's [Future Expansion](00_ATLAS_BRAIN.md#future-expansion) near/medium/long lists are **inputs** to this roadmap. This document is the authoritative sequencing and maturity model those lists feed into.

| Brain Future Expansion band | Roadmap home |
|---|---|
| Near-term (next 90 days) | Phase 0–1 quarterly work; see § Quarterly Planning Model |
| Medium-term (3–12 months) | Phase 1–2 milestones |
| Long-term (12+ months) | Phase 2–4+ tracks |

---

## Vision Horizon

### Anchor vision

Atlas's vision is defined in the Brain: [Vision](00_ATLAS_BRAIN.md#vision).

**Roadmap implication:** Every horizon below must increase the holding's capacity to make building and operating businesses limited by imagination, not operational friction — through shared systems, AI-native operations, and compounding knowledge.

### Horizon bands

| Band | Name | Approximate span | Character |
|---|---|---|---|
| **H0** | Foundation | Years 0–2 | Prove form; build Brain OS substrate; first assets |
| **H1** | Proof of leverage | Years 2–5 | Repeatable integration; measurable OS leverage on real portfolio |
| **H2** | Scaled organism | Years 5–10 | Multi-asset OS; majority routine work automated; external pull |
| **H3** | Institution | Years 10–25 | Form recognized; succession by systems; cross-portfolio intelligence |
| **H4** | Infrastructure | Years 25–50+ | Durable economic infrastructure; outlives leaders by design |

These bands align with the philosophical eras in [The Long-Term Vision (50+ Years)](01_WHY_ATLAS_EXISTS.md#the-long-term-vision-50-years) and the Brain's [Long-term Purpose](00_ATLAS_BRAIN.md#long-term-purpose) horizons — without restating their rationale.

### Vision horizon success posture

| Horizon | Success posture (evidence, not slogans) |
|---|---|
| H0 | Brain docs complete; departments labeled; first build/acquire path live; decisions logged |
| H1 | Integration weeks not years; L2+ on majority of repeated holding processes; hurdle-rate returns with honest reporting |
| H2 | New assets inherit OS day one; operators choose Atlas for infrastructure; headcount grows slower than capability |
| H3 | Leadership transitions without oral tradition; knowledge corpus drives decision quality; form studied externally |
| H4 | Atlas functions as institutional infrastructure; stewardship norms durable; OS still compounding |

### Vision constraints

Across all horizons, the roadmap remains constrained by enduring commitments in the Brain ([Enduring commitments](00_ATLAS_BRAIN.md#enduring-commitments)) and founding principles — especially long-term thinking, systems over heroes, human accountability, and knowledge compounds.

| Constraint | Roadmap effect |
|---|---|
| Truth over narrative | Horizon claims require measurable gates |
| Systems over heroics | Milestones prefer reusable infrastructure over one-off wins |
| Optionality over optimization | Phases preserve reversible paths; avoid premature lock-in |
| Stewardship over extraction | Expansion strategy rejects extractive portfolio growth |
| Human accountability | AI autonomy never removes named human owners |

### What "horizon" is not

- Not a forecast of markets or macro conditions.
- Not a promise of portfolio size or valuation.
- Not a substitute for annual capital plans.
- Not a license to skip current-phase gates because a later horizon sounds exciting.

---

## Roadmap Architecture

### Three axes

Atlas roadmap work is planned on three axes simultaneously:

1. **Time** — horizons, phases, years, quarters
2. **Capability** — maturity of holding OS subsystems
3. **Scope** — holding core vs portfolio surface area

```
         SCOPE →
         Holding core ─────── Shared services ─────── Portfolio edge
TIME ↓
H0     Brain+docs           Templates               First asset
H1     Standards+agents     Integration playbook    Multi-asset ops
H2     Atlas OS platform    Self-serve portal       Sector clusters
H3     Institutional gov    Cross-portfolio intel   Operator network
H4     Durable infra        External knowledge      Civilization-scale stewardship
```

### Evolution tracks

The following tracks run in parallel inside each phase. Each has its own section later in this document.

| Track | Primary owner | Consumes from | Produces for |
|---|---|---|---|
| AI evolution | AI | Knowledge, Operations | All departments |
| Infrastructure evolution | AI + Operations | Brain standards | Portfolio + holding |
| Knowledge evolution | Knowledge | All departments | AI retrieval, onboarding |
| Organization evolution | Brain + Org | Principles | Hiring, scaling stages |
| Product evolution | Assets + Projects | Brain, AI | Portfolio products / HOS product |
| Automation evolution | AI + Operations | SOPs | Scale without headcount |
| Finance / capital evolution | Finance | Brain capital philosophy | Deployable capital plans |
| Portfolio / assets evolution | Assets | Finance, Operations | Integration & exits |
| Operations evolution | Operations | Standards, AI | KPI discipline |
| Projects evolution | Projects | Brain priorities | Capability delivery |

### Planning artifacts

| Artifact | Owner | Cadence | Relates to |
|---|---|---|---|
| This roadmap (T1) | Brain | Semi-annual review | Strategy |
| Annual plan memo | Brain + Finance | Annual | Theme + capital |
| Quarterly priorities | Brain | Quarterly | Phase focus |
| Department roadmap appendix | Dept head | Quarterly | Track deltas |
| Project portfolio | Projects | Weekly/monthly | Execution |
| Current State | Brain | Quarterly | Truth snapshot |
| Decision Records | Decision owners | On decision | Precedent |

### North-star tests for any roadmap item

Every proposed milestone or initiative must answer yes to at least two of the Brain's three mission questions ([Mission in practice](00_ATLAS_BRAIN.md#mission-in-practice)):

1. Does this make the holding OS stronger?
2. Does this create durable value?
3. Does this align with AI-native operations?

If none: out of scope. If one weakly: defer or redesign.

---

## Multi-Year Evolution

### Overview

Multi-year evolution describes how Atlas's form compounds across decades. It is the connective tissue between Vision Horizon bands and gated Major Phases.

Philosophical context: [Phases of evolution](01_WHY_ATLAS_EXISTS.md#the-long-term-vision-50-years) in Why Atlas Exists. Operational targets below are roadmap-owned.

### Evolution eras (operational)

| Era | Years | Horizon | Dominant question | Dominant risk |
|---|---|---|---|---|
| **E0 — Substrate** | 0–2 | H0 | Can we encode judgment into docs and systems? | Oral culture; heroics |
| **E1 — Leverage proof** | 2–5 | H1 | Does the OS make assets better measurably? | Fake synergy; vanity automation |
| **E2 — Repeatability** | 5–10 | H2 | Can we add assets without linear pain? | Coordination tax; silo relapse |
| **E3 — Institutionalization** | 10–25 | H3 | Does the OS survive leadership change? | Bureaucracy regression |
| **E4 — Infrastructure** | 25–50+ | H4 | Is Atlas durable economic infrastructure? | Mission drift; extraction pressure |

### Multi-year capability arcs

#### Arc A — From documents to executable OS

| Stage | Years | State |
|---|---|---|
| A1 | 0–1 | Brain documents and org model exist |
| A2 | 1–3 | Playbooks + SOPs + automation registry live |
| A3 | 3–7 | Software platform encodes standards |
| A4 | 7–15 | Self-serve portal; agents execute majority of BAU |
| A5 | 15+ | OS is the primary product surface for operators |

#### Arc B — From first asset to portfolio organism

| Stage | Years | State |
|---|---|---|
| B1 | 0–2 | First build or acquire closes; integration scorecard invented |
| B2 | 2–4 | 2–5 assets; integration playbook versioned |
| B3 | 4–8 | Multi-sector or multi-geo clusters; shared services real |
| B4 | 8–15 | Portfolio operators pull OS capabilities self-serve |
| B5 | 15+ | External operators seek Atlas as platform, not only capital |

#### Arc C — From assisted AI to self-improving systems

| Stage | Years | State | Maps to AI levels |
|---|---|---|---|
| C1 | 0–1 | L1 assisted on knowledge work | L1 |
| C2 | 1–3 | L2 supervised on repeated processes | L2 default |
| C3 | 3–7 | L3 autonomous within guardrails for majority BAU | L3 common |
| C4 | 7–15 | L4 self-improving on select domains | L4 selective |
| C5 | 15+ | Continuous evaluation + adaptation as culture | L4 institutionalized |

AI level definitions remain in [AI maturity model](00_ATLAS_BRAIN.md#ai-maturity-model).

#### Arc D — From founder memory to institutional memory

| Stage | Years | State |
|---|---|---|
| D1 | 0–1 | Decision log started; onboarding path defined |
| D2 | 1–3 | Staleness detection; retrieval usable |
| D3 | 3–7 | Precedent search influences most material decisions |
| D4 | 7–15 | Cross-portfolio pattern detection |
| D5 | 15+ | Knowledge compounds faster than individual turnover |

#### Arc E — From lean team to scaled organism without bureaucracy

| Stage | Org stage (see Organization) | Years (indicative) |
|---|---|---|
| E1 | Stage 0–1 (1–10 people) | 0–2 |
| E2 | Stage 2 (~50) | 2–6 |
| E3 | Stage 3 (~200) | 6–12 |
| E4 | Stage 4 (1000+) | 12+ |

Org stage definitions: [Organizational Scaling](03_ORGANIZATION.md#organizational-scaling). Years are indicative; **gates are maturity-based, not calendar-based**.

### Multi-year capital posture

Capital philosophy is owned by the Brain ([Capital Allocation Philosophy](00_ATLAS_BRAIN.md#capital-allocation-philosophy)). Roadmap posture by era:

| Era | Capital posture |
|---|---|
| E0 | Heavy infrastructure + experimental; preserve reserve; few large bets |
| E1 | Growth capital to prove leverage; measure OS contribution to returns |
| E2 | Scale winners; standardize hurdle application; deepen reserve discipline |
| E3 | Institutional capital process; multi-year dry powder policy stable |
| E4 | Stewardship capital; optionality preserved across cycles |

Exact bucket percentages live in [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md).

### Multi-year evolution principles (roadmap-specific)

These are planning rules, not founding principles:

1. **Maturity before scale** — Do not add portfolio surface area faster than OS maturity can absorb.
2. **Reuse before novelty** — Prefer milestones that strengthen shared systems.
3. **Gates before calendars** — Slip the calendar before skipping a gate.
4. **Evidence before narrative** — Horizon advancement requires scorecard evidence.
5. **Parallel tracks, serial gates** — Tracks run in parallel; phase exits are serial go/no-go.
6. **Document the fork** — If strategy forks, log a Decision Record; update this roadmap.

### Decade checkpoints

| Checkpoint | Question | Required artifacts |
|---|---|---|
| Year 1 | Is the Brain real? | T1 docs, org model, decision log, current state |
| Year 3 | Is leverage real? | Integration scorecards, AI ROI, return vs plan |
| Year 5 | Is repeatability real? | Playbook versions ≥2, multi-asset reuse metrics |
| Year 10 | Is the organism real? | Self-serve OS usage, org stage ≥3 or equivalent maturity |
| Year 20 | Is the institution real? | Succession exercise passed; external recognition optional |
| Year 50 | Is infrastructure real? | Continuity across ≥2 leadership generations |

---

## Major Phases

### Phase model

Atlas advances through gated phases. **Calendar dates are planning aids; gates are authority.**

| Phase | Name | Typical horizon | Primary outcome |
|---|---|---|---|
| **P0** | Brain Substrate | H0 early | Holding can think in writing |
| **P1** | Operating Kernel | H0–H1 | Holding can execute as a system |
| **P2** | Leverage Demonstration | H1 | Holding proves OS advantage on real assets |
| **P3** | Repeatable Machine | H1–H2 | Holding adds assets with declining marginal chaos |
| **P4** | Platform Organism | H2 | Holding OS is productized for operators |
| **P5** | Institutional Form | H3 | Holding survives people; form is durable |
| **P6** | Infrastructure Era | H4 | Holding is economic infrastructure |

### Phase 0 — Brain Substrate

#### Intent

Encode identity, principles, organization, and roadmap so Atlas is legible to humans and machines.

#### Entry criteria

- Decision to build Atlas as holding OS (founding intent)
- Willingness to document before scaling portfolio

#### Exit criteria (all required)

| # | Criterion | Evidence |
|---|---|---|
| P0.1 | Brain root document active | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) Active |
| P0.2 | Why document active | [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) Active |
| P0.3 | Principles active | [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) Active |
| P0.4 | Organization active | [`03_ORGANIZATION.md`](03_ORGANIZATION.md) Active |
| P0.5 | Roadmap active | This document Active |
| P0.6 | Current State initialized | [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) has snapshot |
| P0.7 | Decision log initialized | [`06_DECISIONS.md`](06_DECISIONS.md) has format + ≥1 record or template |
| P0.8 | Glossary initialized | [`07_GLOSSARY.md`](07_GLOSSARY.md) started |
| P0.9 | Seven departments labeled in practice | Work tagged by department even if dual-hatted |

#### Primary work

- Complete T1 Brain set
- Establish documentation standards usage
- Define first Current State thresholds
- Name owners (even if same human) per [Single Owner Principle](03_ORGANIZATION.md#single-owner-principle)

#### Explicit non-goals in P0

- Large acquisition volume
- Building Atlas OS software platform
- Hiring to org Stage 2+
- External brand campaigns

#### Phase 0 risks

| Risk | Mitigation |
|---|---|
| Docs as theater | Require Current State + decisions to use docs |
| Premature portfolio scale | Gate P1 before multi-asset expansion |
| Principle drift while writing | Keep principles immutable; roadmap adjusts |

### Phase 1 — Operating Kernel

#### Intent

Make Atlas executable: playbooks, SOPs, first automations, financial truth, project lifecycle in use.

#### Entry criteria

- P0 exit criteria met
- Brain review approves P1 entry

#### Exit criteria

| # | Criterion | Evidence |
|---|---|---|
| P1.1 | Department playbook skeleton ×7 | T3 docs exist or explicit dual-hat charters |
| P1.2 | Project lifecycle used on ≥3 initiatives | Briefs + retrospectives in Knowledge |
| P1.3 | Automation registry exists | AI owns registry; ≥5 candidates tracked |
| P1.4 | ≥3 processes at L2 | Per [AI maturity model](00_ATLAS_BRAIN.md#ai-maturity-model) |
| P1.5 | Monthly financial close process documented | Finance SOP + actual closes |
| P1.6 | Integration scorecard v1 | Assets + Operations |
| P1.7 | Escalation thresholds published | In Current State |
| P1.8 | Onboarding path executed once | New operator or simulated dry-run |

#### Primary work

- Convert Brain standards into department playbooks
- Stand up automation eligibility pipeline ([Automation Standards](00_ATLAS_BRAIN.md#automation-standards))
- Implement decision framework on real decisions
- First portfolio asset path (build or acquire) may start but integration maturity is P2 focus

#### Phase 1 risks

| Risk | Mitigation |
|---|---|
| Playbooks unread | Tie playbooks to project gates |
| Automation without SOPs | Enforce eligibility criteria |
| Thresholds never updated | Quarterly Current State review |

### Phase 2 — Leverage Demonstration

#### Intent

Prove that Atlas infrastructure creates disproportionate operational leverage on real assets.

#### Entry criteria

- P1 exit met
- At least one asset in Integrate/Operate stage ([Company Lifecycle](00_ATLAS_BRAIN.md#company-lifecycle))

#### Exit criteria

| # | Criterion | Evidence |
|---|---|---|
| P2.1 | ≥1 asset integrated to scorecard thresholds | Integration scorecard complete |
| P2.2 | Measured time-to-integrate vs baseline | Before/after or peer comparison |
| P2.3 | Shared automation reused across ≥2 contexts | Registry shows reuse |
| P2.4 | Portfolio reporting package live | Finance templates in use |
| P2.5 | AI ROI tracked for production agents | Time/error/cost metrics |
| P2.6 | Decision reviews completed on large decisions | Per review cadence in Brain |
| P2.7 | Honest miss documented | ≥1 failed hypothesis logged without narrative cover-up |

#### Primary work

- Run full acquire/build → integrate loop
- Instrument OS contribution to unit economics
- Harden integration playbook from scars
- Expand L2 coverage on holding BAU

#### Phase 2 risks

| Risk | Mitigation |
|---|---|
| Claiming leverage without metrics | Require P2.2–P2.5 |
| Integrating poorly then scaling | Block P3 until scorecard green |
| Local heroics credited as OS | Attribute outcomes to systems in retros |

### Phase 3 — Repeatable Machine

#### Intent

Make integration and build playbooks repeatable; declining chaos per added asset.

#### Entry criteria

- P2 exit met
- Integration playbook ≥ v2

#### Exit criteria

| # | Criterion | Evidence |
|---|---|---|
| P3.1 | ≥3 assets through Integrate | Scorecards archived |
| P3.2 | Marginal integration effort declining | Measured hours/cost per integrate |
| P3.3 | Agent templates library | Reusable patterns with eval benchmarks |
| P3.4 | 90% of repeated holding processes ≥ L2 | Automation portfolio review |
| P3.5 | Cross-dept interface SLAs reviewed | Org quarterly review |
| P3.6 | Org stage ≥2 or equivalent maturity | [Organizational Scaling](03_ORGANIZATION.md#organizational-scaling) |
| P3.7 | Knowledge staleness process live | Flags + remediation cadence |

#### Primary work

- Templetize everything that worked in P2
- Build shared services where leverage is clear
- Formalize portfolio operator model
- Kill one-off tools that resist reuse

### Phase 4 — Platform Organism

#### Intent

Productize the holding OS: software layer, self-serve portal, operator experience.

#### Entry criteria

- P3 exit met
- Clear demand from portfolio operators for self-serve

#### Exit criteria

| # | Criterion | Evidence |
|---|---|---|
| P4.1 | Atlas OS platform MVP in production | Used weekly by operators |
| P4.2 | Self-serve access to playbooks/automations/reporting | Portal or equivalent |
| P4.3 | Automated decision support for scoring | Assists [Decision Framework](00_ATLAS_BRAIN.md#decision-framework) |
| P4.4 | Majority BAU at L3 where eligible | Guardrails + owners |
| P4.5 | External pull signal | Operators or partners seek Atlas for OS not only capital |
| P4.6 | Coordination tax audit passed | [Org anti-bureaucracy controls](03_ORGANIZATION.md#organizational-anti-patterns) |

#### Primary work

- Build platform capabilities listed in Brain long-term expansion
- Shift Projects capacity toward infrastructure product
- Maintain human accountability on one-way doors

### Phase 5 — Institutional Form

#### Intent

Make Atlas independent of founding operators through systems, succession, and precedent depth.

#### Entry criteria

- P4 exit met or equivalent maturity
- Multi-year decision corpus

#### Exit criteria

| # | Criterion | Evidence |
|---|---|---|
| P5.1 | Succession exercise: new lead operates 90 days via docs | Retrospective |
| P5.2 | Cross-portfolio intelligence in production | Pattern detection used in decisions |
| P5.3 | Governance council advisory only (if exists) | No ownership committees |
| P5.4 | Knowledge-as-product internal | Retrieval is default work interface |
| P5.5 | Principles still binding under stress | Stress-test DR review |

### Phase 6 — Infrastructure Era

#### Intent

Operate as durable economic infrastructure — permanence through systems.

#### Entry criteria

- P5 exit met
- Multi-generational leadership transition completed or simulated at high fidelity

#### Exit criteria

P6 has no terminal exit. Success is continued compounding under stewardship norms. Review every 5 years against [What Success Looks Like](01_WHY_ATLAS_EXISTS.md#what-success-looks-like).

### Phase transition protocol

1. Department heads submit track evidence against exit criteria.
2. Knowledge assembles evidence pack.
3. Brain conducts gate review (see § Roadmap Review Process).
4. Decision Record: approve transition, conditional approve, or reject.
5. Update [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) phase field.
6. Update annual theme if needed.
7. Communicate one voice per [Communication Principles](00_ATLAS_BRAIN.md#communication-principles).

### Phase vs calendar discipline

| Situation | Correct response |
|---|---|
| Exit criteria unmet; calendar says "time to scale" | Stay in phase; adjust plan |
| Exit criteria met early | May advance; do not invent busywork |
| One track ahead, others behind | Advance track work; do not skip phase gate |
| Market opportunity requires early scale | Explicit principle/roadmap exception DR; raise reserve risk |

---

## Strategic Milestones

### Milestone taxonomy

| Class | Description | Example |
|---|---|---|
| **M-G** | Governance milestone | T1 docs complete |
| **M-K** | Knowledge milestone | Retrieval live; glossary v1 |
| **M-A** | AI / automation milestone | Registry; L2 coverage target |
| **M-F** | Finance milestone | Reporting package; hurdle policy published |
| **M-O** | Operations milestone | Integration scorecard; KPI dictionary |
| **M-S** | Assets / portfolio milestone | First close; third integrate |
| **M-P** | Projects / delivery milestone | Lifecycle compliance rate |
| **M-I** | Infrastructure / platform milestone | Portal MVP |
| **M-X** | Cross-cutting milestone | Phase gate passed |

### Milestone register (canonical)

Milestones below are strategic. Delivery dates live in Current State / annual plan — not frozen here.

#### Governance cluster

| ID | Milestone | Phase | Depends on | Success test |
|---|---|---|---|---|
| M-G-001 | Brain OS document set Active | P0 | — | All 00–04 Active |
| M-G-002 | Current State v1 published | P0 | M-G-001 | Thresholds filled |
| M-G-003 | Decision log operational | P0 | M-G-001 | Template + process used |
| M-G-004 | Escalation thresholds live | P1 | M-G-002 | Current State table |
| M-G-005 | Quarterly Brain review running | P1 | M-G-001 | Minutes + actions |
| M-G-006 | Annual planning model executed once | P1 | M-G-005 | Annual memo filed |
| M-G-007 | Phase gate P0→P1 passed | P0/P1 | P0 exits | DR recorded |
| M-G-008 | Phase gate P1→P2 passed | P1/P2 | P1 exits | DR recorded |
| M-G-009 | Phase gate P2→P3 passed | P2/P3 | P2 exits | DR recorded |
| M-G-010 | Phase gate P3→P4 passed | P3/P4 | P3 exits | DR recorded |
| M-G-011 | Succession exercise designed | P4 | Org stage ≥2 | Spec approved |
| M-G-012 | Succession exercise passed | P5 | M-G-011 | Retro filed |

#### Knowledge cluster

| ID | Milestone | Phase | Depends on | Success test |
|---|---|---|---|---|
| M-K-001 | Glossary v1 | P0–P1 | M-G-001 | Terms used in docs |
| M-K-002 | Onboarding path executed | P1 | Brain reading path | Checklist complete |
| M-K-003 | Playbook skeleton ×7 | P1 | Org model | Files exist |
| M-K-004 | SOP quality bar defined | P1 | Doc standards | Rubric published |
| M-K-005 | Staleness flags live | P2–P3 | Corpus exists | Weekly report |
| M-K-006 | Retrieval for operators | P2 | Corpus tagged | Findability study |
| M-K-007 | Precedent search for decisions | P3 | Decision corpus | Used in ≥5 DRs |
| M-K-008 | Cross-portfolio research briefs cadence | P3 | Multi-asset | Monthly briefs |
| M-K-009 | Knowledge-as-product UX | P4 | Platform | Adoption metric |
| M-K-010 | Selective external knowledge products | P5+ | Quality bar | Brain approval |

#### AI / Automation cluster

| ID | Milestone | Phase | Depends on | Success test |
|---|---|---|---|---|
| M-A-001 | Automation registry v1 | P1 | Eligibility criteria | Registry doc |
| M-A-002 | First 3 agents in production | P1 | Specs + owners | Eval baselines |
| M-A-003 | L2 default on repeated holding processes | P2 | M-A-001 | Coverage % |
| M-A-004 | Agent template library | P3 | Reuse ≥2 | Templates + benchmarks |
| M-A-005 | AI ROI dashboard | P2 | Production agents | Quarterly report |
| M-A-006 | Model-agnostic eval harness | P2–P3 | Multi-model use | Harness doc |
| M-A-007 | L3 on majority eligible BAU | P4 | Guardrails | Maturity report |
| M-A-008 | L4 pilot domain | P4–P5 | Strong eval | Pilot retro |
| M-A-009 | Automated decision support | P4 | Decision corpus | Assistive scoring live |
| M-A-010 | Cross-portfolio intelligence | P5 | Multi-asset data policy | Patterns used |

#### Finance cluster

| ID | Milestone | Phase | Depends on | Success test |
|---|---|---|---|---|
| M-F-001 | Chart of accounts / close SOP | P1 | — | Monthly close |
| M-F-002 | Capital bucket policy published | P1 | Capital philosophy | Current State % |
| M-F-003 | Hurdle rate policy published | P1 | Finance + Brain | Written policy |
| M-F-004 | Portfolio reporting package | P2 | ≥1 asset | Templates used |
| M-F-005 | Unit economics standard | P2 | Reporting package | Dashboard |
| M-F-006 | Investment memo standard | P1–P2 | Decision framework | Memo template |
| M-F-007 | Automated reporting L2+ | P3 | Package stable | Automation spec |
| M-F-008 | Holding ROIC published quarterly | P2+ | Portfolio data | Finance pack |

#### Operations cluster

| ID | Milestone | Phase | Depends on | Success test |
|---|---|---|---|---|
| M-O-001 | KPI dictionary v1 | P1 | — | Definitions doc |
| M-O-002 | Integration scorecard v1 | P1 | Company lifecycle | Scorecard |
| M-O-003 | Vendor management framework | P2 | Shared services need | Framework doc |
| M-O-004 | Incident response drills | P2 | Risk section | Drill report |
| M-O-005 | Integration playbook v2 | P3 | ≥2 integrates | Versioned playbook |
| M-O-006 | Shared services catalog | P3 | Multi-asset | Catalog + SLAs |
| M-O-007 | Portfolio dashboard spec live | P2–P3 | KPI dictionary | Dashboard |
| M-O-008 | Coordination tax audit v1 | P4 | Org scale | Audit report |

#### Assets / Portfolio cluster

| ID | Milestone | Phase | Depends on | Success test |
|---|---|---|---|---|
| M-S-001 | Build-vs-acquire checklist in use | P1 | Brain framework | Used on live opp |
| M-S-002 | First asset Acquire or Build complete | P1–P2 | M-S-001 | Close/launch |
| M-S-003 | First Integrate complete | P2 | M-O-002 | Scorecard green |
| M-S-004 | Second asset integrated | P2–P3 | Playbook v1 | Scorecard |
| M-S-005 | Third asset integrated | P3 | Playbook v2 | Declining effort |
| M-S-006 | Exit/hold rationale standard | P2 | Exit criteria | Template used |
| M-S-007 | Portfolio operator model live | P3 | Org stage | Charters |
| M-S-008 | Sector or geo cluster model | P4 | Multi-asset | Cluster charter |

#### Projects cluster

| ID | Milestone | Phase | Depends on | Success test |
|---|---|---|---|---|
| M-P-001 | Intake/triage process live | P1 | Project lifecycle | Tracker |
| M-P-002 | 100% approved projects have briefs | P1 | M-P-001 | Audit |
| M-P-003 | Retrospective compliance ≥90% | P2 | Closed projects | Knowledge |
| M-P-004 | Handoff confirmation gate | P2 | Lifecycle | Sign-off |
| M-P-005 | Infrastructure project portfolio visible | P3 | Platform intent | Roadmap link |

#### Infrastructure / Platform cluster

| ID | Milestone | Phase | Depends on | Success test |
|---|---|---|---|---|
| M-I-001 | Tooling inventory + preferred stack | P1 | Ops + AI | Inventory |
| M-I-002 | Identity/access baseline | P1 | Security principles | Policy |
| M-I-003 | Data segmentation policy | P2 | Multi-asset | Policy enforced |
| M-I-004 | Atlas OS platform MVP | P4 | P3 exits | Production use |
| M-I-005 | Self-serve portal | P4 | M-I-004 | Adoption |
| M-I-006 | Operator network (internal) | P4–P5 | Multi-operator | Cadence |

### Milestone health states

| State | Meaning | Action |
|---|---|---|
| Not started | No work | Schedule if phase-relevant |
| In progress | Active project/BAU | Weekly status |
| Blocked | Dependency or resource | Escalate per Org |
| Met | Evidence filed | Knowledge archive |
| Waived | Explicit DR exception | Rare; time-boxed |
| Retired | No longer strategic | Changelog |

Live states belong in Current State or Projects trackers — not as frozen fields in this T1 doc.

---

## Capability Maturity Model

### Purpose of CM levels

Holding Capability Maturity (CM) measures **Atlas OS readiness** as a whole. It is distinct from AI process maturity L0–L4 ([AI Strategy](00_ATLAS_BRAIN.md#ai-strategy)).

| Model | Scope | Levels |
|---|---|---|
| **CM-0–CM-5** | Holding OS capability | This section |
| **L0–L4** | Individual process AI maturity | Brain AI Strategy |
| **Org Stage 0–4** | Headcount/structure scaling | [Organization](03_ORGANIZATION.md#organizational-scaling) |
| **Company lifecycle stage** | Per-asset stage | [Company Lifecycle](00_ATLAS_BRAIN.md#company-lifecycle) |

### CM levels

| Level | Name | Description | Typical phase |
|---|---|---|---|
| **CM-0** | Implicit | Knowledge in heads; ad-hoc execution | Pre-Atlas |
| **CM-1** | Documented | Brain/org docs exist; execution still fragile | P0 |
| **CM-2** | Managed | Playbooks/SOPs/projects/finance cadence run | P1 |
| **CM-3** | Leveraged | Measured OS advantage on assets; reuse begins | P2 |
| **CM-4** | Industrialized | Repeatable integrate/build; high L2+ coverage | P3 |
| **CM-5** | Productized / Institutional | Platform + succession + intelligence | P4–P5 |

### CM dimensions

Score each dimension 0–5. Holding CM is the **minimum** of dimension scores for gate purposes (weakest link), with average used for diagnostics.

| Dimension | ID | What "5" looks like |
|---|---|---|
| Governance & judgment | CM-D1 | Principles applied; decisions logged; gates respected |
| Knowledge compounding | CM-D2 | Findable, fresh, applied knowledge; precedent used |
| AI & automation | CM-D3 | Eligible BAU at target L-levels with ROI |
| Financial truth | CM-D4 | Timely close; portfolio truth; capital discipline |
| Operational integration | CM-D5 | Scorecards; declining integrate cost; shared services |
| Portfolio stewardship | CM-D6 | Lifecycle discipline; exit honesty; autonomy spectrum |
| Delivery system | CM-D7 | Projects briefed, measured, handed off |
| Organizational clarity | CM-D8 | Single owners; interfaces; scale without bureaucracy |
| Platform / infrastructure | CM-D9 | Standards encoded in tooling operators actually use |
| Learning loop | CM-D10 | Retros → standards → better decisions demonstrably |

### Dimension rubrics (summary)

#### CM-D1 Governance & judgment

| Score | Evidence |
|---|---|
| 0 | No written principles or decisions |
| 1 | Docs exist; rarely used in live decisions |
| 2 | Material decisions use framework sometimes |
| 3 | Material decisions use framework by default; escalations work |
| 4 | Precedent search + reviews improve hit rate |
| 5 | New leaders decide consistently via corpus; exceptions rare and logged |

#### CM-D2 Knowledge compounding

| Score | Evidence |
|---|---|
| 0 | Oral culture |
| 1 | Docs exist; hard to find |
| 2 | Structure + ownership; onboarding path |
| 3 | Retrieval works; staleness managed |
| 4 | Knowledge changes behavior measurably |
| 5 | Cross-portfolio intelligence; knowledge as product |

#### CM-D3 AI & automation

| Score | Evidence |
|---|---|
| 0 | No AI in workflows |
| 1 | Ad-hoc assistant usage unmanaged |
| 2 | Spec'd agents; registry; some L2 |
| 3 | Default L2 on repeated processes; ROI tracked |
| 4 | Templates; L3 common; eval harness |
| 5 | L4 pilots; decision support; portfolio intelligence |

#### CM-D4 Financial truth

| Score | Evidence |
|---|---|
| 0 | Unreliable numbers |
| 1 | Manual close; delayed |
| 2 | Documented close; budgets |
| 3 | Portfolio package; hurdles applied |
| 4 | Automated reporting; unit economics standard |
| 5 | Capital allocation visibly improves from feedback loops |

#### CM-D5 Operational integration

| Score | Evidence |
|---|---|
| 0 | Each asset invents ops |
| 1 | Checklist aspirational |
| 2 | Scorecard v1 used once |
| 3 | Multiple integrates; playbook scarring |
| 4 | Declining marginal effort; shared services |
| 5 | Weeks-not-years as default; self-serve integrate |

#### CM-D6 Portfolio stewardship

| Score | Evidence |
|---|---|
| 0 | No lifecycle |
| 1 | Opportunistic deals only |
| 2 | Evaluate/acquire discipline |
| 3 | Integrate + operate cadence |
| 4 | Optimize + honest exits |
| 5 | Stewardship culture; autonomy spectrum healthy |

#### CM-D7 Delivery system

| Score | Evidence |
|---|---|
| 0 | Ad-hoc initiatives |
| 1 | List of projects; no briefs |
| 2 | Lifecycle partially followed |
| 3 | Briefs + metrics + retros default |
| 4 | Handoffs clean; portfolio visible |
| 5 | Delivery system strengthens OS each cycle |

#### CM-D8 Organizational clarity

| Score | Evidence |
|---|---|
| 0 | Unclear ownership |
| 1 | Org doc exists |
| 2 | Owners named; dual-hats labeled |
| 3 | Interfaces + escalation work |
| 4 | Scale stages navigated without principle break |
| 5 | Coordination tax controlled at large scale |

#### CM-D9 Platform / infrastructure

| Score | Evidence |
|---|---|
| 0 | Tool chaos |
| 1 | Inventory |
| 2 | Preferred stack + access baseline |
| 3 | Data policies; automations reliable |
| 4 | OS platform MVP used |
| 5 | Self-serve organism; standards encoded |

#### CM-D10 Learning loop

| Score | Evidence |
|---|---|
| 0 | No retros |
| 1 | Retros filed; unread |
| 2 | Some standards updated from learning |
| 3 | Closed loop on most projects |
| 4 | Decision quality trends improve |
| 5 | Organization learns faster than environment changes |

### CM assessment process

1. **Frequency:** Quarterly light score; annual deep score.
2. **Owners:** Each dimension has a dept owner; Brain owns aggregate.
3. **Evidence pack:** Links to artifacts, not opinions.
4. **Calibration:** Brain challenges score inflation.
5. **Publication:** Aggregate in [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md).
6. **Action:** Weakest dimensions become quarterly priorities.

### CM to phase mapping

| Phase exit | Minimum holding CM | Notes |
|---|---|---|
| P0 → P1 | CM-1 | Docs real |
| P1 → P2 | CM-2 | Managed execution |
| P2 → P3 | CM-3 | Leverage shown |
| P3 → P4 | CM-4 | Industrialized |
| P4 → P5 | CM-5 on D1–D3, D8–D10; ≥4 elsewhere | Platform + institutional signals |
| P5 → P6 | Sustained CM-5 + succession | Time + stress tests |

---

## Success Criteria

### Hierarchy of success

```
Vision success (decades)     ← 01_WHY + Vision Horizon
Phase success (gates)        ← Major Phases exit criteria
Annual success (theme KPIs)  ← Annual Planning Model
Quarterly success (deltas)   ← Quarterly Planning Model
Project success (briefs)     ← Project Lifecycle
```

Philosophical constellation: [What Success Looks Like](01_WHY_ATLAS_EXISTS.md#what-success-looks-like). This section makes success **auditable** for roadmap governance.

### Holding-level success criteria by horizon

#### H0 success criteria

| ID | Criterion | Metric / evidence |
|---|---|---|
| SC-H0-01 | Brain is operable | T1 set Active; used in decisions |
| SC-H0-02 | Ownership exists | Single owners on material outcomes |
| SC-H0-03 | Truth channel open | Current State + bad news examples |
| SC-H0-04 | First execution loop | ≥1 project full lifecycle |
| SC-H0-05 | First capital discipline | Buckets + hurdles written |

#### H1 success criteria

| ID | Criterion | Metric / evidence |
|---|---|---|
| SC-H1-01 | Integration speed | Weeks-scale integrate on ≥1 asset |
| SC-H1-02 | Automation depth | Majority repeated holding processes ≥ L2 |
| SC-H1-03 | Financial honesty | Actuals vs plan published; misses explained |
| SC-H1-04 | Knowledge findability | Operators find answers without tribal ask (target in Current State) |
| SC-H1-05 | Returns discipline | Portfolio vs hurdle reviewed quarterly |
| SC-H1-06 | OS attribution | Retros identify system contribution |

#### H2 success criteria

| ID | Criterion | Metric / evidence |
|---|---|---|
| SC-H2-01 | Repeatability | Marginal integrate effort declining across ≥3 assets |
| SC-H2-02 | Headcount leverage | Capability growth > headcount growth |
| SC-H2-03 | Platform pull | Operators use shared OS weekly |
| SC-H2-04 | L3 prevalence | Eligible BAU mostly L3 |
| SC-H2-05 | External signal | At least qualitative pull for Atlas infrastructure |

#### H3 success criteria

| ID | Criterion | Metric / evidence |
|---|---|---|
| SC-H3-01 | Succession | New leadership cohort effective via systems |
| SC-H3-02 | Precedent power | Decision quality aided by corpus |
| SC-H3-03 | Intelligence | Cross-portfolio patterns inform strategy |
| SC-H3-04 | Form integrity | No eighth shadow department; principles intact |

#### H4 success criteria

| ID | Criterion | Metric / evidence |
|---|---|---|
| SC-H4-01 | Permanence | Continuity across generations |
| SC-H4-02 | Stewardship | Assets left better; reputation intact |
| SC-H4-03 | Compounding | Knowledge/automation library still expanding usefully |

### Anti-success (explicit failures)

Atlas treats the following as roadmap failure modes even if revenue grows:

| Anti-success | Why it fails the thesis |
|---|---|
| Portfolio growth without integration | Holding illusion returns |
| Automation vanity metrics | L-levels without ROI or owners |
| Narrative over truth | Destroys learning loop |
| Heroic saves as culture | Systems atrophy |
| Principle exceptions normalized | Identity erosion |
| Headcount as progress | Coordination tax |
| Roadmap as wishlist | Non-executable strategy |

### Success criteria for roadmap process itself

| Criterion | Target |
|---|---|
| Quarterly roadmap review held | 4/4 years |
| Phase gates documented | 100% of transitions |
| Current State phase field accurate | Always |
| Milestone waiver rate | Low; each waived has DR |
| Department plans reference phase | 100% |

---

## Expansion Strategy

### Expansion thesis

Atlas expands when expansion **strengthens the holding OS** and clears capital/strategic tests — not when expansion merely increases logos under a brand.

Build vs acquire evaluation remains in [Build vs. acquire framework](00_ATLAS_BRAIN.md#build-vs-acquire-framework). This section sequences *when* expansion modes are appropriate by phase.

### Expansion modes

| Mode | Description | Earliest phase | Preferred when |
|---|---|---|---|
| **E-Build** | New venture from first principles | P1 | OS is the product; greenfield; learning strategic |
| **E-Acquire** | Purchase existing business | P2 (P1 only with caution) | Proven ops; Atlas leverage clear |
| **E-Integrate-deep** | Deeper OS penetration in existing assets | P2+ | Always preferred before new logos |
| **E-Shared-services** | Centralize a function across assets | P3 | Clear reuse; SLA feasible |
| **E-Platform** | Productize OS for operators | P4 | Demand + CM-4 |
| **E-Sector** | Enter new sector cluster | P3+ | Playbooks portable; talent available |
| **E-Geo** | Enter new geography | P3+ | Compliance + ops capacity |
| **E-External-knowledge** | Publish frameworks selectively | P5+ | Quality bar; no inappropriate leak |
| **E-Operator-network** | Community of portfolio leaders | P4+ | Multi-operator portfolio |

### Expansion sequencing rules

1. **Deepen before widen** — Prefer E-Integrate-deep over new acquire when CM-D5 < 3.
2. **OS before logos** — No multi-asset expansion while P0 incomplete.
3. **One integrate scar at a time** — Until playbook v2, limit concurrent integrates.
4. **Capital reserve preserved** — Expansion cannot starve Reserve bucket ([Capital buckets](00_ATLAS_BRAIN.md#capital-buckets)).
5. **Autonomy spectrum respected** — Expansion does not smother local brand/product ([Autonomy spectrum](00_ATLAS_BRAIN.md#portfolio-company-autonomy-spectrum)).
6. **Exit is expansion of quality** — Honest exits are strategic hygiene, not failure.

### Geographic expansion

| Stage | Condition | Work |
|---|---|---|
| G0 | None | Single operating geo |
| G1 | Compliance + banking ready | First foreign entity or remote ops |
| G2 | Regional ops pod | [Org Stage 3 pattern](03_ORGANIZATION.md#organizational-scaling) |
| G3 | Multi-region standards | Localized playbook extensions, not forks |

### Sector expansion

| Rule | Detail |
|---|---|
| Portability test | Can ≥50% of integrate playbook apply? |
| Talent test | Can we staff judgment in-sector? |
| Data test | Can we segment and still learn cross-portfolio? |
| Capital test | Clears hurdles with sector risk adjustment |
| Thesis test | Strengthens OS, not vanity diversification |

### Expansion kill criteria

Stop or reverse an expansion path when:

- Strategic fit fails Brain mission questions
- Integration scorecard red beyond recovery window
- OS contribution negative after optimize cycle
- Key-person dependency recreates oral culture
- Principle exceptions required to "make it work"

Log kill decisions in [`06_DECISIONS.md`](06_DECISIONS.md).

### Expansion and public narrative

Holding-level communications coordinated through Brain ([External communication](00_ATLAS_BRAIN.md#external-communication)). Expansion announcements never outrun phase reality.

---

## AI Evolution

### Anchor

Strategy and standards: [AI Strategy](00_ATLAS_BRAIN.md#ai-strategy), [Automation Standards](00_ATLAS_BRAIN.md#automation-standards), [AI Participation](03_ORGANIZATION.md#ai-participation-inside-departments).

This section defines **evolution targets by phase** — not a second strategy.

### AI evolution stages

| Stage | Phase | Target state |
|---|---|---|
| AI-0 | P0 | Humans use AI ad-hoc; no registry |
| AI-1 | P1 | Registry; specs; first production agents; L1–L2 |
| AI-2 | P2 | ROI tracked; L2 default on repeated holding processes |
| AI-3 | P3 | Template library; eval harness; reuse across assets |
| AI-4 | P4 | L3 majority eligible BAU; decision support assists scoring |
| AI-5 | P5+ | L4 selective; cross-portfolio intelligence; continuous eval culture |

### Department AI embedding roadmap

| Department | P1 focus | P2–P3 focus | P4+ focus |
|---|---|---|---|
| Brain | Draft assistance; decision packaging | Precedent retrieval | Decision support agents |
| Knowledge | Summarization; tagging | Staleness detection; retrieval | Knowledge product UX |
| AI | Platform + registry | Templates + eval | L4 pilots; model ops |
| Finance | Close assist; variance drafts | Automated reporting L2+ | Forecasting agents supervised |
| Operations | KPI anomaly flags | Integrate checklist agents | Self-serve ops agents |
| Assets | DD research assist | Memo drafting + checklists | Portfolio pattern alerts |
| Projects | Status synthesis | Risk prediction assist | Portfolio balancing assist |

### AI evolution principles (planning)

1. **SOP before agent** — No production agent without documented process.
2. **Owner before autonomy** — Named human owner always.
3. **Eval before L-increment** — Promote maturity only with evidence.
4. **Segment before cross-learning** — Data segmentation by default.
5. **Model-agnostic** — No vendor loyalty roadmap commitments.
6. **Human on one-way doors** — Non-negotiable.

### AI milestone dependency notes

- M-A-003 (L2 default) depends on M-O-001 KPI dictionary and M-K-003 playbooks.
- M-A-009 (decision support) depends on M-G-003 decision corpus depth.
- M-A-010 (cross-portfolio intel) depends on M-I-003 data segmentation policy.

### AI risk evolution

| Phase | Dominant AI risk | Control |
|---|---|---|
| P1 | Shadow AI / unmanaged tools | Registry + standards |
| P2 | Silent failures | Fail loudly; monitoring |
| P3 | Template misuse | Eval benchmarks; owners |
| P4 | Over-autonomy | Guardrails; L3 boundaries |
| P5 | Distributional shift | Continuous eval; human audits |

### AI ROI model (roadmap expectation)

Every production automation reports:

| Metric | Purpose |
|---|---|
| Hours saved / period | Labor leverage |
| Error rate vs baseline | Quality |
| Cost (model + maintenance) | Economic truth |
| Exception rate | Autonomy readiness |
| Reuse count | Compounding |

Targets by phase are set numerically in Current State; qualitatively: **positive ROI before L3 promotion**.

---

## Infrastructure Evolution

### Definition

Infrastructure means the **technical and operational substrate** of the holding OS: identity, data, tooling, environments, platform software, and reliability — distinct from portfolio product infrastructure.

### Infrastructure layers

| Layer | Contents | Primary owners |
|---|---|---|
| L-Doc | Docs, templates, versioning | Knowledge + Brain |
| L-Access | Identity, permissions, secrets | Operations + AI |
| L-Data | Storage, segmentation, pipelines | AI + Finance + Ops |
| L-Automation | Agents, workflows, registry | AI |
| L-Observe | Logging, metrics, alerts | AI + Operations |
| L-Platform | Atlas OS software + portal | AI + Projects |
| L-Edge | Portfolio connectors | Operations + Assets |

### Evolution by phase

| Phase | Infrastructure focus | Done when |
|---|---|---|
| P0 | Doc substrate in repo/knowledge base | T1 readable + versioned |
| P1 | Access baseline; tooling inventory; logging for automations | M-I-001/002 |
| P2 | Data segmentation; portfolio connectors; dashboards | Multi-asset safe |
| P3 | Reliability targets; shared services systems | SLAs met |
| P4 | Platform MVP + portal | Weekly operator use |
| P5+ | Hardening; intelligence layer; succession of infra owners | Runbooks + deputies |

### Reliability posture

| Class | Examples | Target posture |
|---|---|---|
| Critical | Financial truth, access, decision log integrity | High; tested restores |
| Important | Automations, dashboards | Monitored; fallback manual |
| Best-effort | Experimental agents | Clear labels; easy disable |

### Build vs buy for infrastructure

Follow founding principles on build/buy without restating them. Roadmap bias:

| Layer | Default |
|---|---|
| Commodity cloud/identity | Buy |
| Atlas-specific workflows/standards encoding | Build |
| Model providers | Buy; abstract |
| Integration playbooks | Build (knowledge) |
| Portal UX | Build when P4 demand real |

### Infrastructure anti-goals

- Building a platform before P3 repeatability
- Custom everything when standards are not stable
- Infra for its own sake without operator pull
- Centralization that breaks portfolio autonomy spectrum

---

## Knowledge Evolution

### Anchor

Architecture and lifecycle: [Knowledge Management](00_ATLAS_BRAIN.md#knowledge-management), [Documentation Standards](00_ATLAS_BRAIN.md#documentation-standards). Philosophy: [Why Documentation Is Infrastructure](01_WHY_ATLAS_EXISTS.md#why-documentation-is-infrastructure), [Why Compounding Knowledge Is the Greatest Competitive Advantage](01_WHY_ATLAS_EXISTS.md#why-compounding-knowledge-is-the-greatest-competitive-advantage).

### Knowledge evolution stages

| Stage | Phase | State |
|---|---|---|
| K-0 | Pre/P0 | Fragments; founder memory |
| K-1 | P0–P1 | T1 governance corpus; glossary started |
| K-2 | P1 | Playbooks/SOPs; onboarding path; decision log used |
| K-3 | P2 | Retrieval usable; staleness process; DD research support |
| K-4 | P3 | Precedent search; cross-asset briefs; quality bar enforced |
| K-5 | P4+ | Knowledge-as-product; powers portal; selective externalization later |

### Knowledge corpus growth model

| Corpus type | Growth driver | Quality control |
|---|---|---|
| Governance (T1) | Brain reviews | Versioning policy |
| Standards (T2) | Process change | Knowledge + Brain |
| Playbooks (T3) | Dept ownership | Review cadence |
| SOPs (T4) | Ops change | Process owner |
| Decisions (T5) | Every material decision | Decision owner → Knowledge |
| Retrospectives | Project/incident close | Projects/Ops |
| Research | Opportunities + markets | Knowledge |

### Knowledge evolution KPIs (targets in Current State)

| KPI | Intent |
|---|---|
| % docs with owner + review date | Hygiene |
| Stale doc rate | Entropy resistance |
| Time-to-find for standard queries | Findability |
| % projects with retro filed | Learning loop |
| % material decisions in log | Judgment capture |
| Reuse rate of playbooks across assets | Compounding |

### Knowledge → AI coupling

| Knowledge maturity | Enables AI capability |
|---|---|
| Structured SOPs | L2 automations |
| Tagged corpus | Retrieval agents |
| Decision corpus | Precedent + scoring assist |
| Cross-asset structured data | Portfolio intelligence |

### Knowledge anti-patterns

- Wiki sprawl without owners
- Duplicating Brain content into department docs
- Capturing only successes
- Treating Knowledge as "write later"
- Measuring page count instead of application

---

## Organization Evolution

### Anchor

Structure and scaling stages: [`03_ORGANIZATION.md`](03_ORGANIZATION.md) — especially [Organizational Scaling](03_ORGANIZATION.md#organizational-scaling) and [Scaling Without Changing Principles](03_ORGANIZATION.md#scaling-without-changing-principles).

This section maps **org evolution to roadmap phases** without redefining departments.

### Phase ↔ org stage coupling

| Roadmap phase | Typical org stage | Notes |
|---|---|---|
| P0 | Stage 0 | One operator; label hats |
| P1 | Stage 0–1 | Name dept heads; first charters |
| P2 | Stage 1 | Dual-hat discipline; AI registry owners |
| P3 | Stage 2 | Sub-teams; portfolio operators |
| P4 | Stage 2–3 | Platform staffing; avoid manager middleware |
| P5 | Stage 3–4 | Deputies; succession; coordination tax audits |
| P6 | Stage 4 | Institutional minimal Brain headcount via systems |

**Rule:** Org stage may lag phase maturity (lean is good). Org stage must not leapfrog CM maturity (headcount without systems is bad).

### Hiring roadmap posture

Hiring philosophy remains in Organization. Roadmap posture:

| Phase | Hire for | Delay hiring for |
|---|---|---|
| P0–P1 | System builders who write | Task volume roles |
| P2 | Operators who integrate + measure | Pure coordinators |
| P3 | Portfolio operators; specialists with charters | Generic managers |
| P4+ | Platform + domain depth | Relay layers |

### Organization evolution milestones

| ID | Milestone | Phase |
|---|---|---|
| M-ORG-001 | Dual-hat labeling convention live | P0–P1 |
| M-ORG-002 | Role charters for active seats | P1 |
| M-ORG-003 | Interface SLAs acknowledged | P1–P2 |
| M-ORG-004 | First portfolio operator charter | P3 |
| M-ORG-005 | First sub-team charters | P3 |
| M-ORG-006 | Coordination tax audit v1 | P4 |
| M-ORG-007 | Deputy coverage for critical depts | P5 |
| M-ORG-008 | Succession packet complete | P5 |

### Organization risks on the roadmap

| Risk | Phase most likely | Mitigation |
|---|---|---|
| Shadow eighth department | P3+ | Governance Boundaries |
| Manager middleware creep | P3–P4 | Charter must own systems |
| Dual-hat confusion | P1–P2 | Label hats in writing |
| Portfolio silo relapse | P2+ | Interface reviews; shared KPIs |

---

## Product Evolution

### Two product surfaces

Atlas has two product meanings:

| Surface | Definition | Owner |
|---|---|---|
| **Holding OS product** | Reusable infrastructure making all assets better | Brain + AI + Ops + Knowledge |
| **Portfolio products** | Goods/services each asset sells to customers | Portfolio operators + Assets |

See [The holding as product](00_ATLAS_BRAIN.md#the-holding-as-product).

### Holding OS product evolution

| Stage | Phase | Product increment |
|---|---|---|
| HOS-1 | P0–P1 | Docs, templates, decision framework as product |
| HOS-2 | P2 | Integration playbook + reporting package + agents |
| HOS-3 | P3 | Shared services catalog + template library |
| HOS-4 | P4 | Software platform + portal |
| HOS-5 | P5+ | Intelligence layer + operator network |

### Portfolio product evolution (holding constraints)

The roadmap does **not** prescribe specific portfolio product roadmaps. It constrains them:

1. Portfolio product bets must clear Decision Framework when material.
2. Local product speed must not break financial reporting / KPI standards.
3. Shared OS capabilities preferred over per-asset reinvented stacks.
4. Brand/customer experience remains local per autonomy spectrum.

### Product evolution success tests

| Test | Applies to |
|---|---|
| Does this ship strengthen the HOS? | Holding OS increments |
| Does this create durable customer value? | Portfolio products |
| Does this create reusable pattern? | Both |
| Does this increase coordination tax? | Reject or redesign |

### Product anti-goals

- Holding trying to brand all portfolio customer products as one consumer brand by default
- Building HOS features nobody in portfolio uses
- Portfolio products that require permanent principle exceptions

---

## Automation Evolution

### Anchor

[Automation Standards](00_ATLAS_BRAIN.md#automation-standards); eligibility, specs, registry reviews.

### Automation maturity wave plan

| Wave | Phase | Scope | Target |
|---|---|---|---|
| W0 | P0 | None systematic | Manual OK |
| W1 | P1 | Holding BAU candidates | Registry + first L2 |
| W2 | P2 | Finance/ops/knowledge high-frequency | L2 default |
| W3 | P3 | Cross-asset templates | Reuse ≥2 contexts |
| W4 | P4 | Eligible BAU → L3 | Guardrailed autonomy |
| W5 | P5+ | Selective L4 | Self-improving within bounds |

### Automation domain priority order (default)

Unless Current State overrides:

1. Financial reporting & reconciliation assists
2. Knowledge capture, tagging, staleness
3. Project status synthesis
4. Integration checklist execution assists
5. KPI anomaly detection
6. DD research drafting
7. Vendor/ops routine workflows
8. Decision packaging / precedent retrieval

### Automation evolution metrics

| Metric | Wave relevance |
|---|---|
| Candidates above frequency threshold not yet automated | W1+ |
| % production automations with specs + owners | All |
| Flaky automation rate | W2+ |
| Reuse ratio (deployments / templates) | W3+ |
| Exception rate trend | W4+ |

### Automation retirement

Automations are retired when:

- ROI negative after improvement attempts
- Process obsolete
- Risk exceeds value
- Replaced by superior template

Retirement is a success of hygiene, not a failure — log in registry.

---

## Finance and Capital Evolution

### Anchor

[Capital Allocation Philosophy](00_ATLAS_BRAIN.md#capital-allocation-philosophy); Finance department in Organization.

### Finance evolution stages

| Stage | Phase | State |
|---|---|---|
| F-1 | P1 | Close SOP; buckets; hurdles written |
| F-2 | P2 | Portfolio reporting; unit economics; investment memos standard |
| F-3 | P3 | Automated reporting L2+; consolidated views |
| F-4 | P4+ | Predictive assists; capital process institutionalized |

### Capital evolution by era

| Era | Deploy posture | Measurement emphasis |
|---|---|---|
| E0 | Infra + small experiments | Learning + runway |
| E1 | Prove leverage on assets | OS-attributed returns |
| E2 | Scale winners; cut losers | Holding ROIC; MOIC/IRR as fit |
| E3+ | Institutional discipline | Multi-year compounding under stewardship |

### Finance roadmap milestones (pointer)

See M-F-001…M-F-008 in Strategic Milestones. Numeric thresholds only in Current State.

### Finance risks

| Risk | Mitigation |
|---|---|
| Optimistic projections without reviews | Decision review cadences |
| Starving infrastructure bucket | Annual theme protects infra % |
| Fully deployed = fully exposed | Reserve policy |
| Local books incompatible | Chart mapping in integrate SLA |

---

## Portfolio and Assets Evolution

### Anchor

[Company Lifecycle](00_ATLAS_BRAIN.md#company-lifecycle); Assets department in Organization.

### Portfolio shape by phase

| Phase | Indicative shape | Constraint |
|---|---|---|
| P0 | Zero or prospecting only | Do not close before substrate |
| P1 | 0–1 asset path active | Kernel must keep pace |
| P2 | 1–2 assets; prove integrate | Measure leverage |
| P3 | 3–8 assets | Repeatability |
| P4 | Clusters | Platform absorbs complexity |
| P5+ | Multi-sector/geo as thesis allows | Institutional controls |

Indicative counts are **not quotas**. Quality and CM gates dominate.

### Assets evolution work

| Phase | Assets focus |
|---|---|
| P1 | Opportunity pipeline hygiene; memo standard |
| P2 | First integrate excellence; board cadence |
| P3 | Operator model; playbook scarring; exits honesty |
| P4 | Clusters; self-serve OS adoption |
| P5 | Pattern library across portfolio |

### Portfolio health signals (roadmap-relevant)

| Signal | Good | Bad |
|---|---|---|
| Integrate SLA adherence | On-time green | Chronic red |
| OS reuse | Rising | Per-asset forks |
| Reporting lag | Low | Chronic delay |
| Principle exceptions | Rare | Normalized |
| Exit honesty | Timely | Sunk-cost retention |

---

## Operations Evolution

### Anchor

Operations department; [Operating Philosophy](00_ATLAS_BRAIN.md#operating-philosophy); integration standards in Company Lifecycle.

### Operations evolution stages

| Stage | Phase | State |
|---|---|---|
| O-1 | P1 | KPI dictionary; process maps for holding BAU |
| O-2 | P2 | Integration execution; incident drills; vendor baseline |
| O-3 | P3 | Shared services; playbook v2+; dashboard live |
| O-4 | P4+ | Self-serve ops; coordination tax control |

### Continuous improvement cadence (roadmap enforcement)

Brain already defines weekly/monthly/quarterly/annual loops ([Continuous improvement as a system](00_ATLAS_BRAIN.md#continuous-improvement-as-a-system)). Roadmap requires these loops to **feed milestone and CM updates** — not exist as theater.

| Cadence | Roadmap output |
|---|---|
| Weekly | Blockers affecting milestones escalated |
| Monthly | Automation candidates + KPI deltas |
| Quarterly | CM light score + roadmap review inputs |
| Annually | Deep CM + annual plan |

---

## Projects Evolution

### Anchor

[Project Lifecycle](00_ATLAS_BRAIN.md#project-lifecycle); Projects department.

### Projects system evolution

| Stage | Phase | State |
|---|---|---|
| PR-1 | P1 | Intake/triage/brief discipline |
| PR-2 | P2 | Metrics + retros + handoff gates |
| PR-3 | P3 | Visible infrastructure portfolio vs asset projects |
| PR-4 | P4+ | Platform delivery factory; high parallelism with clear DRIs |

### Project portfolio mix targets (directional)

| Phase | Infra / OS projects | Asset projects | Experimental |
|---|---|---|---|
| P1 | High | Low–med | Capped |
| P2 | Med-high | Med | Capped |
| P3 | Med | High | Capped |
| P4 | High (platform) | Med | Capped |
| P5+ | Med (intelligence) | Med-high | Capped |

Exact mix in annual plan / Current State.

### Projects anti-patterns

- Initiatives without briefs
- Eternal projects that never hand off
- Priority thrash weekly without Brain change
- Measuring success by launches not outcomes

---

## Scaling Plan

### Scaling thesis

Atlas scales **capability first, surface area second, headcount third**.

```
Capability (CM, L-levels, playbooks)
        ↓ enables
Surface area (assets, geos, sectors)
        ↓ may require
Headcount (org stages)
```

Inverting this order recreates traditional holding failure modes described in [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md).

### Scaling dimensions

| Dimension | Scales via | Invariant |
|---|---|---|
| Assets | Playbooks + operators | Lifecycle + standards |
| People | Charters + sub-teams | Seven departments; single owner |
| Automations | Templates | Owners + eval |
| Knowledge | Corpus + retrieval | Single source of truth |
| Capital | Buckets + hurdles | Reserve + honesty |
| Geos/sectors | Extensions not forks | Brain standards |

### Scaling gates

| Scale action | Prerequisite gate |
|---|---|
| Second concurrent integrate | Integration playbook ≥ v1 + capacity |
| Third+ asset | P2 exit or explicit waiver DR |
| Org Stage 2 staffing | CM ≥ 2; interface SLAs |
| Org Stage 3 staffing | CM ≥ 3; coordination tax plan |
| New sector | Sector expansion tests pass |
| Platform build (major capital) | P3 exit |

### Scaling plan by horizon

#### H0 scaling plan

- Scale documentation completeness and decision hygiene
- Do not scale asset count for its own sake
- AI scales personal leverage of few operators

#### H1 scaling plan

- Scale integrate quality and L2 coverage
- Add second asset only with scorecard capacity
- Hire system builders ahead of coordinators

#### H2 scaling plan

- Scale template reuse and shared services
- Grow portfolio operators with charters
- Begin platform only with pull

#### H3+ scaling plan

- Scale institutional mechanisms (deputies, succession, intel)
- Audit coordination tax annually
- Prefer automation and knowledge over layers

### Scaling metrics

| Metric | Healthy pattern |
|---|---|
| CM vs headcount | CM leads or matches |
| Assets vs integrate capacity | Capacity ≥ in-flight integrates |
| Automations vs exceptions | Exceptions stable/down |
| Managers vs owners | Owners dominate |

---

## Milestone Dependencies

### Dependency types

| Type | Meaning | Example |
|---|---|---|
| **Hard** | Cannot start/finish B without A | Platform MVP needs P3 exit |
| **Soft** | B degraded without A | Decision support without deep corpus |
| **Policy** | Governance forbids B before A | Multi-asset scale before P0 complete |
| **Capacity** | People/capital constraint | Two integrates need ops capacity |

### Critical dependency chains

#### Chain 1 — Substrate → Kernel → Leverage

```
M-G-001 Brain set
   → M-G-002 Current State
   → M-G-004 Thresholds
   → M-K-003 Playbooks
   → M-A-001 Registry
   → M-A-002 First agents
   → M-O-002 Scorecard
   → M-S-002 First asset
   → M-S-003 First integrate
   → M-G-008 P1→P2 gate (via P2 exits)
```

#### Chain 2 — Repeatability → Platform

```
M-S-003 + M-S-004 integrates
   → M-O-005 Playbook v2
   → M-A-004 Templates
   → M-O-006 Shared services
   → M-G-009 P2→P3 / P3 exits
   → M-I-004 Platform MVP
   → M-I-005 Portal
```

#### Chain 3 — Knowledge → Intelligence

```
M-G-003 Decision log
   → corpus depth
   → M-K-007 Precedent search
   → M-A-009 Decision support
   → M-I-003 Data segmentation
   → M-A-010 Cross-portfolio intelligence
```

#### Chain 4 — Org clarity → Scale

```
M-ORG-001 Dual-hat labels
   → M-ORG-002 Charters
   → M-ORG-003 Interface SLAs
   → M-ORG-004 Portfolio operators
   → M-ORG-006 Coordination tax audit
   → M-G-012 Succession exercise
```

### Dependency matrix (selected hard deps)

| Milestone | Hard dependencies |
|---|---|
| M-G-007 P0→P1 | P0.1–P0.9 exit criteria |
| M-A-003 L2 default | M-A-001, M-K-003, process baselines |
| M-S-003 First integrate | M-S-002, M-O-002, M-F-001 |
| M-F-004 Reporting package | M-S-002, M-F-001 |
| M-A-007 L3 majority | M-A-003, M-A-005, guardrail policy |
| M-I-004 Platform MVP | P3 exit, M-A-004, operator demand evidence |
| M-A-010 Portfolio intel | M-I-003, multi-asset data, M-K-008 |
| M-G-012 Succession | M-G-011, CM-D1/D2 high, Org deputies |

### Parallelizable work

These may proceed in parallel if owners and capacity exist:

- Glossary (M-K-001) parallel with Current State (M-G-002)
- KPI dictionary (M-O-001) parallel with Finance close SOP (M-F-001)
- Project intake (M-P-001) parallel with automation registry (M-A-001)
- Vendor framework (M-O-003) parallel with second integrate (M-S-004) after first integrate

### Dependency break protocol

When a dependency will miss:

1. Owner flags yellow/red in weekly status.
2. Projects proposes resequence or scope cut.
3. If phase gate impacted → Brain roadmap review item.
4. Waiver only via Decision Record with expiry.
5. Update annual/quarterly plan artifacts — not silent slip.

---

## Long-Term Risks

### Anchor

Risk categories and matrices: [Risk Management](00_ATLAS_BRAIN.md#risk-management). This section catalogs **roadmap-horizon risks** — threats to multi-year evolution — not day-to-day incident lists.

### Strategic roadmap risks

| ID | Risk | Horizon | Likelihood posture | Impact | Mitigation |
|---|---|---|---|---|---|
| R-S-01 | Thesis failure: OS adds no leverage | H1 | Medium | Existential | P2 exit metrics; kill criteria |
| R-S-02 | Premature scale (logos before CM) | H0–H2 | High early | High | Phase gates; deepen-before-widen |
| R-S-03 | Mission drift to financial engineering only | H2–H4 | Medium | High | Mission questions; stewardship |
| R-S-04 | Principle erosion under pressure | All | Medium | Existential | Exception logging; Brain review |
| R-S-05 | Platform built too early | H1–H2 | Medium | High | P3 prerequisite |
| R-S-06 | Platform built too late | H2–H3 | Medium | Medium | Operator pull signals; annual theme |
| R-S-07 | Sector vanity diversification | H2+ | Medium | Medium | Sector tests |
| R-S-08 | External narrative outruns reality | All | Medium | Medium | Comms via Brain; truth first |

### Organizational roadmap risks

| ID | Risk | Mitigation |
|---|---|---|
| R-O-01 | Bureaucracy regression | Coordination tax audits; charter rules |
| R-O-02 | Key-person dependency | Documentation; deputies; automation |
| R-O-03 | Shadow governance | Quarterly org review |
| R-O-04 | Hiring coordinators not builders | Hiring philosophy enforcement |
| R-O-05 | Portfolio silos | Interfaces; shared KPIs; Knowledge |
| R-O-06 | Founder bottleneck past Stage 1 | Explicit escalation filters; ownership |

### AI and technical roadmap risks

| ID | Risk | Mitigation |
|---|---|---|
| R-A-01 | Silent automation failures | Fail loudly; monitoring |
| R-A-02 | Over-autonomy on one-way doors | Human accountability principle |
| R-A-03 | Vendor/model lock-in | Model-agnostic eval |
| R-A-04 | Data leakage across portfolio | Segmentation policy |
| R-A-05 | Eval theater | ROI + quality metrics required |
| R-A-06 | Capability cliff if models regress/change | Fallbacks; multi-vendor |

### Knowledge roadmap risks

| ID | Risk | Mitigation |
|---|---|---|
| R-K-01 | Corpus rot | Staleness flags; owners |
| R-K-02 | Unfindable knowledge | Retrieval milestones |
| R-K-03 | Documentation theater | Tie docs to gates and onboarding |
| R-K-04 | Loss on turnover | Offboarding + single source of truth |

### Financial roadmap risks

| ID | Risk | Mitigation |
|---|---|---|
| R-F-01 | Liquidity crunch from over-deploy | Reserve bucket |
| R-F-02 | Concentration in one asset | Diversification targets in Current State |
| R-F-03 | Sunk-cost retention | Exit criteria; honest reviews |
| R-F-04 | Starving infrastructure investment | Annual capital theme |

### External / environmental risks

| ID | Risk | Roadmap response |
|---|---|---|
| R-E-01 | Regulatory shifts on AI/data | Compliance track in Finance/Assets; reversible designs |
| R-E-02 | Macro capital scarcity | Preserve optionality; extend runway milestones |
| R-E-03 | Incumbent holdings copy form | Speed of compounding knowledge as moat |
| R-E-04 | Talent market shifts | Systems reduce hero dependency |

### Risk → roadmap interaction rules

1. High×High roadmap risks require explicit mitigation owners in annual plan.
2. Materialized risks that change phase feasibility trigger out-of-cycle roadmap review.
3. Risk acceptance is a Decision Record, not a vibe.
4. Do not confuse risk avoidance with refusing all expansion — calculated risk is required for compounding.

---

## What Is NOT on the Roadmap

### Purpose of exclusion

A roadmap without exclusions becomes a wishlist. The following are **explicitly out of scope** for this canonical roadmap unless a future Decision Record amends this section.

### Excluded categories

#### Not a product catalog

- Specific consumer/SaaS product feature lists for unnamed future portfolio companies
- Brand marketing campaign calendars
- Pricing experiments for local portfolio products (local autonomy)

#### Not a financial model

- Valuation targets, IPO timelines, or guaranteed IRRs
- Year-by-year revenue hockey sticks
- Exact capital dollar amounts (live in Current State / Finance plans)

#### Not an org chart of names

- Named individuals as permanent roadmap fixtures
- Headcount requisitions by quarter (planning artifacts elsewhere)
- Compensation bands

#### Not a technology bet list

- Commitment to a single model vendor
- Commitment to a single cloud forever
- Speculative AGI timelines as planning assumptions

#### Not activism or unrelated ventures

- Political campaigns
- Ventures that fail all three mission questions
- Acquisitions purely for prestige

#### Not a rewrite of Brain doctrine

- New founding principles
- Eighth department proposals without DR (and default no)
- Replacing human accountability with autonomous agents

### Explicitly deferred (maybe later, not now)

| Item | Earliest reconsideration |
|---|---|
| External knowledge products | P5 |
| Licensing Atlas OS externally | P4+ with Brain DR |
| Public company conversion | Not on roadmap; would be new strategic DR |
| Non-controlling financial-only portfolio (pure PE mode) | Discouraged; contradicts OS thesis |
| Heavy physical industrial ops without OS leverage thesis | Case-by-case; default no |

### Soft exclusions (allowed only with waiver)

| Item | Waiver requirements |
|---|---|
| Acquire before P1 exit | Brain DR + heightened reserve + integration capacity proof |
| Skip integration scorecard items | Time-boxed waiver; risk owner |
| L3 without ROI evidence | Forbidden (hard exclusion) |
| New geo before compliance ready | Forbidden until G1 conditions |

### How to propose adding something excluded

1. Write brief: why thesis-aligned, why now, what dependency chain.
2. Score via Decision Framework.
3. Brain Decision Record.
4. If approved, amend this section and relevant milestones.
5. Version bump this document.

---

## Quarterly Planning Model

### Purpose

The quarter is Atlas's **primary execution planning unit**. Annual themes constrain quarters; quarters do not invent new strategy.

### Quarterly cycle (90 days)

```
Week -2..0  : Prepare (inputs)
Week 1      : Set priorities (Brain)
Week 2–11   : Execute (Projects + depts)
Week 10–12  : Review + score (Brain + depts)
Week 12     : Lock next quarter draft
```

### Inputs to quarterly planning

| Input | Source |
|---|---|
| Current phase + CM scores | Current State |
| Annual theme + constraints | Annual plan memo |
| Open milestones | This roadmap + trackers |
| Capacity | Org + Finance |
| Risks & incidents | Ops/Finance risk reviews |
| Decision reviews due | Decision log |
| Portfolio needs | Assets |

### Quarterly outputs (required artifacts)

| Artifact | Owner |
|---|---|
| Quarterly Priorities memo (≤2 pages) | Brain |
| Top 3–7 company-level outcomes | Brain |
| Project portfolio for quarter | Projects |
| Department focus statements | Each dept head |
| CM light score update | Brain + depts |
| Current State refresh | Brain |
| Risk top-10 refresh | Finance + Ops + Brain |

### Priority-setting rules

1. **Phase first** — Priorities must advance current phase exit criteria or critical risk mitigations.
2. **Weakest CM dimension next** — Raise the minimum.
3. **Hard dependencies before nice-to-haves.**
4. **Cap WIP** — Prefer finishing milestones to starting many.
5. **Infra vs asset balance** — Respect directional mix for phase.
6. **No stealth priorities** — If it matters, it is written.

### Quarterly priority template

```markdown
## QQ YYYY Priorities

**Phase:** P#
**Annual theme:** …
**CM minimum (last):** #

### Outcomes (3–7)
1. … — Owner — Milestone IDs — Success metric

### Explicit non-goals this quarter
- …

### Capacity notes
- …

### Risks to watch
- …

### Review date
YYYY-MM-DD
```

### Mid-quarter correction

Allowed when:

- Hard external shock
- Red project health on a gate-critical milestone
- Principle conflict discovered

Not allowed for:

- Boredom
- Opportunistic shiny objects that fail mission questions
- Rebranding failure as "agility" without DR

Corrections producing strategy change → Decision Record + priorities amend.

### Quarterly review agenda (standard)

1. Truth: what we said vs what happened
2. Metrics: CM light, milestone states, AI ROI, finance actuals
3. Portfolio: integrate/operate health
4. Learning: retros → standards changes
5. Risks: new/changed roadmap risks
6. Next quarter draft priorities
7. Decisions needed (list)

### Quarterly anti-patterns

- 27 priorities
- Priorities without owners or metrics
- Review as celebration without misses
- Updating roadmap text instead of Current State for live status

---

## Annual Planning Model

### Purpose

The year sets **theme, capital posture, and phase ambition**. It is not a second roadmap and not a substitute for principles.

### Annual cycle

```
Month 10–11 : Discovery & evidence pack
Month 11    : Draft theme + capital buckets
Month 12    : Brain challenge & lock
Month 1     : Publish annual memo; Q1 priorities
Month 6     : Mid-year review (optional hard reset)
Month 9–10  : Pre-work next year
```

### Annual plan memo contents

| Section | Content |
|---|---|
| Theme | One sentence + one paragraph |
| Phase ambition | Target phase position by year-end |
| CM targets | Dimension floors |
| Capital buckets | % ranges (also mirrored to Current State) |
| Portfolio posture | Build/acquire/integrate/exit emphasis |
| Infra investment thesis | What OS capability must exist by year-end |
| Org posture | Hiring bands by capability, not vanity |
| Top annual milestones | Subset of register |
| Risk register annual | Top mitigations funded |
| Explicit non-goals | Year-level exclusions |

### Theme design rules

A good annual theme:

- Fits current phase
- Is falsifiable at year-end
- Constrains quarterly priorities
- Does not require principle exceptions
- Can be said in one sentence without jargon fog

Examples (illustrative, not commitments):

| Phase | Example theme |
|---|---|
| P0–P1 | "Make Atlas executable" |
| P2 | "Prove leverage on asset one" |
| P3 | "Second and third integrate cheaper than the first" |
| P4 | "Operators self-serve the OS weekly" |

### Mid-year review

Triggers for hard reset:

- Phase gate unexpectedly passed early
- Thesis evidence fails
- Macro/liquidity shock
- Major acquisition/divestiture

Otherwise: stay course; adjust quarters only.

### Annual planning roles

| Role | Responsibility |
|---|---|
| Brain | Owns theme, locks plan, challenges sandbagging |
| Finance | Capital buckets, constraints, return frames |
| Assets | Portfolio posture proposal |
| AI/Ops/Knowledge | Infra and capability proposals |
| Projects | Feasibility / WIP reality |
| All depts | Focus statements aligned to theme |

---

## Roadmap Review Process

### Review types

| Type | Cadence | Purpose |
|---|---|---|
| **Light review** | Quarterly | Status vs phase; CM light; priority alignment |
| **Deep review** | Semi-annual | Milestone register health; track evolution; amend roadmap |
| **Gate review** | On demand | Phase transition go/no-go |
| **Emergency review** | On trigger | Shock response; strategy fork |
| **Annual alignment** | Annual | Theme lock + roadmap coherence |

### Light review checklist

- [ ] Current phase field accurate in Current State
- [ ] Top milestones state updated in tracker
- [ ] CM light scores recorded
- [ ] Quarterly priorities graded
- [ ] New risks identified
- [ ] Waivers expiring soon reviewed
- [ ] No silent scope adds

### Deep review checklist

- [ ] Re-read Vision Horizon + phase intents
- [ ] Validate milestone register (add/retire/resequence)
- [ ] Audit dependency chains
- [ ] Compare expansion activity vs sequencing rules
- [ ] AI/automation maturity vs targets
- [ ] Knowledge hygiene metrics
- [ ] Org stage vs CM mismatch check
- [ ] What-is-not list still correct?
- [ ] Propose version bump if substantive edits

### Gate review checklist

- [ ] Exit criteria evidence pack complete
- [ ] Weakest CM dimension acceptable
- [ ] Finance confirms capital posture compatible
- [ ] Major risks have owners
- [ ] Decision Record drafted
- [ ] Communication plan for one-voice announcement
- [ ] Next phase entry workstreams named

### Emergency review triggers

- Liquidity crisis
- Material principle breach
- Catastrophic integration failure
- Legal/regulatory shock
- Loss of key systems without backup
- Strategic fork proposal with irreversible elements

### Review outputs

| Output | Required for |
|---|---|
| Written review notes | All |
| Actions with owners/dates | All |
| Current State updates | All |
| Decision Record | Gates, emergencies, material amendments |
| Roadmap PR/version bump | Deep reviews with edits |

### Review facilitation

- Default async evidence pack 72 hours before sync discussion.
- Sync time for decisions, not status reading.
- Knowledge archives pack.
- Brain owns facilitation; may delegate logistics to chief-of-staff role when org stage supports it.

---

## Roadmap Ownership

### Single owner

**Brain owns this document** — content, versioning, gate decisions, and coherence with principles.

Per [Single Owner Principle](03_ORGANIZATION.md#single-owner-principle): contributors many; owner one.

### RACI (roadmap governance)

| Activity | Brain | Dept heads | Projects | Finance | Knowledge | AI | Assets | Ops |
|---|---|---|---|---|---|---|---|---|
| Roadmap text changes | A/R | C | C | C | C | C | C | C |
| Phase gate decision | A/R | C | C | C | I | C | C | C |
| Quarterly priorities | A/R | C | C | C | I | C | C | C |
| Annual theme | A/R | C | C | C | I | C | C | C |
| Milestone delivery | A | C/R* | R | C/R* | C/R* | C/R* | C/R* | C/R* |
| CM scoring | A | R | C | R | R | R | R | R |
| Current State phase field | A/R | C | I | C | C | I | C | C |
| Tracker hygiene | A | C | R | I | C | C | C | C |

\* R for milestones in that department's track.

Legend: R = Responsible, A = Accountable, C = Consulted, I = Informed.

### Owner responsibilities (Brain)

1. Keep roadmap coherent with Brain docs and principles.
2. Refuse duplicate doctrine.
3. Run reviews and gates.
4. Prevent wishlist sprawl.
5. Ensure exclusions stay honest.
6. Approve material amendments.
7. Ensure Current State does not contradict roadmap silently.

### Contributor responsibilities (departments)

1. Propose track milestones with evidence standards.
2. Deliver owned milestones.
3. Surface dependency breaks early.
4. Do not maintain shadow roadmaps that conflict.
5. Align department plans to phase and theme.

### Shadow roadmap prohibition

Department "roadmaps" are **appendices** that refine delivery inside this canonical sequencing. If conflict arises, this document + Brain decision wins. Shadow strategy is organizational debt ([Organization Executes the Brain](03_ORGANIZATION.md#organization-executes-the-brain)).

---

## Change Control

### What counts as a change

| Change class | Examples | Process |
|---|---|---|
| **Typo / clarity** | Wording, formatting | Owner edit; no version bump required |
| **Minor** | New example, checklist item, clarification | MINOR version; note in changelog |
| **Major** | New phase, changed gate, new exclusion, resequence chains | MAJOR version; Decision Record; dept consult |
| **Emergency patch** | Critical inconsistency with principles | Brain fix + DR within 7 days |

Versioning follows Brain [Versioning Policy](00_ATLAS_BRAIN.md#versioning-policy).

### Amendment workflow

1. Proposer drafts change brief (problem, proposed text, impact on milestones/phases).
2. Identify affected tracks/departments.
3. Consult via async comments (72h default).
4. Brain decides; DR if Major.
5. Merge text; bump version; update changelog.
6. Update Current State if phase/ambition fields affected.
7. Notify departments one-voice.

### Forbidden changes

- Inserting new founding principles into this doc
- Quietly removing exclusions to justify a pet project
- Changing exit criteria after failing them without DR
- Dating milestones into this T1 as if they were contracts without Current State

### Changelog

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-08-08 | Initial canonical roadmap — horizons, phases, maturity, tracks, planning, ownership |

---

## Measurement and Scorecards

### Scorecard stack

| Scorecard | Cadence | Owner |
|---|---|---|
| Holding CM dimensions | Quarterly light / annual deep | Brain |
| Phase exit evidence pack | At gates | Knowledge assembles |
| Milestone tracker | Weekly | Projects |
| AI ROI / maturity | Monthly/quarterly | AI |
| Integration scorecard | Per integrate | Operations + Assets |
| Portfolio financial pack | Monthly/quarterly | Finance |
| Coordination tax audit | Annual (P4+) | Brain + Org |

### North-star holding metrics (directional)

Exact targets live in Current State. Categories:

| Category | Examples |
|---|---|
| Leverage | Integrate time, reuse ratio, hours saved |
| Truth | Close timeliness, forecast error, miss disclosure latency |
| Compounding | Playbook versions, precedent citations, stale rate |
| Autonomy quality | Exception rates, human override appropriateness |
| Scale efficiency | Capability/headcount, chaos per new asset |
| Stewardship | Exit honesty, customer/partner trust proxies |

### Metric quality rules

1. Prefer rates and cycle times over vanity counts.
2. Every metric has an owner and a source system/doc.
3. If unmet, explain — do not redefine success after the fact.
4. AI metrics include quality, not only speed.
5. Portfolio metrics distinguish OS contribution where feasible.

### Sample milestone evidence table

| Milestone | Evidence type | Storage |
|---|---|---|
| M-G-001 | Document statuses | `02_Brain/` |
| M-A-002 | Agent specs + eval baselines | AI registry |
| M-S-003 | Integration scorecard | Ops/Assets archive |
| M-F-004 | Reporting package samples | Finance |
| M-K-007 | DRs citing precedents | Decision log |

---

## Horizon Checklists

### H0 checklist (Foundation)

#### Governance
- [ ] `00_ATLAS_BRAIN.md` Active and referenced in decisions
- [ ] `01_WHY_ATLAS_EXISTS.md` Active
- [ ] `02_FOUNDING_PRINCIPLES.md` Active
- [ ] `03_ORGANIZATION.md` Active
- [ ] `04_ROADMAP.md` Active (this document)
- [ ] `05_CURRENT_STATE.md` initialized with phase field
- [ ] `06_DECISIONS.md` initialized
- [ ] `07_GLOSSARY.md` started

#### Operating
- [ ] Work labeled by seven departments
- [ ] Single owners on material outcomes
- [ ] At least one project completed through lifecycle
- [ ] Escalation thresholds drafted

#### Capital / risk
- [ ] Capital buckets described
- [ ] Reserve principle acknowledged in Current State
- [ ] Top risks listed

### H1 checklist (Proof of leverage)

#### OS leverage
- [ ] ≥1 asset integrated to scorecard standards
- [ ] Integrate cycle time measured
- [ ] Automation ROI reported for production agents
- [ ] Shared automation reused in ≥2 contexts

#### Truth
- [ ] Portfolio reporting package used
- [ ] Actuals vs plan reviewed with misses explained
- [ ] Decision reviews executed on large decisions

#### Knowledge / org
- [ ] Onboarding path works without tribal lore
- [ ] Staleness process running
- [ ] Dual-hat labeling consistent

### H2 checklist (Scaled organism)

- [ ] ≥3 assets through integrate with declining marginal effort
- [ ] Template library + eval harness
- [ ] Majority eligible holding BAU at L3 or justified exceptions
- [ ] Operators use shared OS weekly
- [ ] Coordination tax audit performed
- [ ] External pull signal documented (qualitative OK)

### H3 checklist (Institution)

- [ ] Succession exercise designed and passed
- [ ] Cross-portfolio intelligence used in ≥1 strategic decision
- [ ] Deputies for critical departments
- [ ] Principles stress-tested under adversity with records
- [ ] Knowledge-as-product adoption strong

### H4 checklist (Infrastructure)

- [ ] Continuity across leadership generations evidenced
- [ ] Stewardship outcomes evidenced on assets exited/held
- [ ] Roadmap still subordinated to principles
- [ ] Compounding library still useful (not museum)

---

## Scenario Planning

### Why scenarios

Roadmaps fail when they assume a single future. Atlas maintains a small set of scenarios to preserve optionality ([Optionality](02_FOUNDING_PRINCIPLES.md) as principle — applied here as planning).

### Base / Bull / Bear / Break

| Scenario | Character | Roadmap posture |
|---|---|---|
| **Base** | Steady capital; normal AI progress | Follow phases as written |
| **Bull** | Easy capital; fast AI gains | May accelerate tracks; **do not skip gates** |
| **Bear** | Scarce capital; slower growth | Extend calendars; protect Reserve; deepen OS on fewer assets |
| **Break** | Thesis evidence fails at P2 | Halt scale; redesign or wind down expansion; truth first |

### Scenario triggers

| Trigger | Move toward |
|---|---|
| Repeated integrate failures | Bear / Break evaluation |
| Strong reuse + pull + returns | Bull (accelerate platform prep) |
| Liquidity alarm | Bear immediately |
| Principle breach pattern | Break evaluation / governance crisis protocol |

### Scenario responses (playbooks)

#### Bull response

1. Keep phase gates.
2. Pull forward Soft-dependency work.
3. Increase Experimental bucket only within policy.
4. Hire builders, not celebration staff.
5. Document acceleration DR.

#### Bear response

1. Freeze vanity expansion.
2. Prioritize milestones that reduce burn via automation.
3. Deepen one asset rather than add many.
4. Protect Knowledge/AI core capacity.
5. Communicate honestly.

#### Break response

1. Stop claiming leverage.
2. Full evidence autopsy.
3. Options: reform OS, shrink to principles-only holding, or orderly exit paths.
4. Brain DR mandatory.
5. Do not narrate failure as success.

### Scenario review cadence

Revisit scenarios at deep roadmap reviews and when triggers fire. Do not maintain elaborate multi-variable Monte Carlos as a substitute for gates.

---

## Anti-Patterns

### Roadmap anti-patterns

| Anti-pattern | Looks like | Fix |
|---|---|---|
| Wishlist roadmap | Hundreds of undated hopes | Exclusions + WIP caps |
| Calendar tyranny | "It's Q3 so we must acquire" | Gates over calendars |
| Metric theater | Green dashboards, red reality | Truth over comfort |
| Shadow strategy | Dept plan contradicts Brain | Org executes Brain |
| Principle laundering | Renaming exception as innovation | DR + hierarchy |
| Premature platform | Building portal in P1 | P3 prerequisite |
| Logo collecting | Assets without integrate | Deepen-before-widen |
| Automation cosplay | Chatbots without SOP/owners | Eligibility criteria |
| Eternal P0 | Docs forever, no kernel | Time-box P0 with exit criteria |
| Horizon hopping | Citing H4 to skip H0 work | Read horizons in order |

### Planning anti-patterns

| Anti-pattern | Fix |
|---|---|
| 27 quarterly priorities | Cap 3–7 outcomes |
| Annual plan as fiction | Mid-year truth check; smaller promises |
| Review without decisions | End with DR list or explicit none |
| Status meetings as planning | Async status; sync for choices |

### Evolution-track anti-patterns

| Track | Anti-pattern |
|---|---|
| AI | L-level inflation |
| Knowledge | Page count KPI |
| Org | Manager layers without system ownership |
| Product | HOS features without users |
| Automation | No retirement path |
| Finance | Hockey-stick without reviews |
| Assets | Sunk-cost retention |
| Ops | Heroic firefighting celebrated over systems |
| Projects | No handoff |

---

## Practical Examples

### Example A — Solo founder in P0

**Context:** One operator; no portfolio yet.

**Correct roadmap behavior:**

- Complete Brain document set
- Label work by department in notes
- Log material decisions
- Initialize Current State phase = P0
- Resist acquiring "because opportunity" before substrate

**Incorrect:** Raising a large round to buy three companies in month two with no integrate scorecard.

### Example B — First acquisition during P1→P2

**Context:** Kernel mostly ready; first target appears.

**Correct:**

- Confirm P1 exit criteria nearly met
- Run build-vs-acquire checklist
- Pre-assign integrate DRI and scorecard
- Finance models with hurdles
- DR for acquire
- Treat integrate excellence as the milestone that matters more than press release

**Incorrect:** Close deal; postpone documentation; celebrate logo.

### Example C — Bull market temptation in P2

**Context:** Cheap capital; many brokers pitching.

**Correct:**

- Stay in deepen-before-widen until leverage metrics exist
- Maybe one additional asset if capacity proven
- Pull forward automation templates (soft deps) without skipping P2 exit
- Raise Experimental only within policy

**Incorrect:** Skip to P4 platform narrative to impress investors.

### Example D — Automation candidate

**Context:** Monthly close comments written manually 8 hours.

**Correct wave path:**

1. SOP exists (or write it)
2. Baseline time/error
3. Spec agent; owner = Finance lead
4. L1→L2 supervised
5. Eval 2–4 weeks
6. Registry + ROI
7. Consider template for portfolio companies later

**Incorrect:** Unowned GPT macro emailing banks.

### Example E — Phase gate refusal

**Context:** Calendar says "year 3"; integrate still red; CM-D5 = 2.

**Correct:** Brain refuses P2→P3; quarterly theme becomes "finish integrate machine"; update Current State; no shame in gate fail — shame in fake pass.

### Example F — Department shadow roadmap conflict

**Context:** AI dept wants platform now; Assets wants five acquires; Brain phase is P2.

**Correct:** Brain priorities memo states non-goals; AI focuses on templates/ROI; Assets focuses on second integrate quality; conflicts escalated with evidence not volume.

### Example G — Bear year

**Context:** Capital scarce; one healthy asset.

**Correct annual theme:** "Deepen OS on asset one; automate BAU; preserve reserve."
Milestones: M-A-003, M-O-005 scarring, M-F-007 — not M-S-008 clusters.

### Example H — Succession rehearsal (P5 prep)

**Context:** Deputy runs holding 90 days using only docs + systems.

**Success evidence:** Decisions logged; no oral tradition required for BAU; gaps become Knowledge tickets — not reasons to abandon succession.

---

### Counter-examples (compressed)

| # | Counter-example | Violates |
|---|---|---|
| CE-1 | "We'll document after we scale" | P0 gates; documentation principle |
| CE-2 | "L4 everywhere this year" | AI evolution stages; eval discipline |
| CE-3 | "Eighth department for synergy" | Org invariants |
| CE-4 | "Hide the miss until next quarter" | Truth; communication principles |
| CE-5 | "Roadmap is whatever the CEO said in Slack" | This document's authority |
| CE-6 | "Integration optional for talent deals" | Company lifecycle standards |
| CE-7 | "Metrics later; vibe now" | Success criteria |
| CE-8 | "Copy competitor holding org chart" | Organization executes Brain |

---

## Cross References

### Brain document map for roadmap users

| Need | Document | Section |
|---|---|---|
| Vision/mission | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) | Vision, Mission |
| Why / 50y philosophy | [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) | Long-Term Vision; Success |
| Principles | [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) | Core Principles; Hierarchy |
| Departments / scaling stages | [`03_ORGANIZATION.md`](03_ORGANIZATION.md) | Dept sections; Organizational Scaling |
| Live snapshot | [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) | (all) |
| Precedents | [`06_DECISIONS.md`](06_DECISIONS.md) | (all) |
| Terms | [`07_GLOSSARY.md`](07_GLOSSARY.md) | (all) |
| AI L0–L4 definitions | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) | AI Strategy |
| Automation eligibility | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) | Automation Standards |
| Project stages | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) | Project Lifecycle |
| Company stages | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) | Company Lifecycle |
| Capital buckets | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) | Capital Allocation Philosophy |
| Risk matrix | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) | Risk Management |

### Internal section map

| Topic | Section |
|---|---|
| Horizons | Vision Horizon |
| Eras / arcs | Multi-Year Evolution |
| Gates | Major Phases |
| Register | Strategic Milestones |
| CM model | Capability Maturity Model |
| Auditable success | Success Criteria |
| Build/acquire sequencing | Expansion Strategy |
| Track plans | AI…Projects Evolution sections |
| Scale order | Scaling Plan |
| Graph of deps | Milestone Dependencies |
| Horizon risks | Long-Term Risks |
| Scope discipline | What Is NOT on the Roadmap |
| 90-day model | Quarterly Planning Model |
| 12-month model | Annual Planning Model |
| Cadences | Roadmap Review Process |
| RACI | Roadmap Ownership |

---

## Document Maintenance

### Ownership

| Field | Value |
|---|---|
| Document | `04_ROADMAP.md` |
| Owner | Brain |
| Tier | T1 — Governance |
| Review cadence | Quarterly light alignment; semi-annual deep |
| Next review | 2026-11-08 |

### Maintenance checklist

- [ ] Links to Brain docs still valid
- [ ] No duplicated principles text crept in
- [ ] Milestone register coherent with phases
- [ ] Exclusions still intentional
- [ ] Changelog updated on substantive edit
- [ ] Version bumped appropriately
- [ ] Current State phase compatible
- [ ] Glossary terms updated if new roadmap terms added

### Deprecation

If superseded:

1. Status → Deprecated
2. Pointer to replacement at top
3. Do not delete history
4. DR explaining supersession

### Machine readability

Agents consuming this document should:

- Treat phase gates as authoritative constraints
- Resolve conflicts toward Principles > Brain OS > Organization > Roadmap sequencing > Current State numbers
- Never invent live metrics from this file
- Prefer linking milestone IDs in project briefs

---

## Appendix A — Phase Detail Cards

### Card P0 — Brain Substrate

| Field | Content |
|---|---|
| Intent | Encode judgment and structure |
| Primary owner | Brain |
| Supporting | All (as contributors) |
| Leading metrics | T1 completion; decision log hygiene |
| Lagging metrics | None required beyond substrate |
| Capital bias | Infrastructure + experimental small |
| Org stage bias | 0 |
| AI stage bias | AI-0→AI-1 start |
| Kill / stay signal | Stay until P0 exits met |

**Entry narrative:** Atlas chooses OS form over improvisation.

**Exit narrative:** A capable stranger can read Brain docs and understand how Atlas decides.

**Typical projects:** Doc completion, glossary, current state, first DR, tooling inventory start.

**Typical non-goals:** Multi-asset buys, public launch, platform engineering.

### Card P1 — Operating Kernel

| Field | Content |
|---|---|
| Intent | Make execution systematic |
| Primary owner | Brain + Ops + Projects |
| Leading metrics | Playbooks, registry, L2 count, close SOP |
| Capital bias | Infra heavy |
| Org stage bias | 0–1 |
| AI stage bias | AI-1 |

**Entry narrative:** Substrate exists; time to run the machine.

**Exit narrative:** Recurring work has owners, SOPs, and first supervised automations; finance closes on a cadence.

**Typical projects:** Playbook skeletons, automation registry, KPI dictionary, project intake, investment memo standard.

**Typical non-goals:** Platform MVP; multi-sector expansion.

### Card P2 — Leverage Demonstration

| Field | Content |
|---|---|
| Intent | Prove OS advantage on real assets |
| Primary owner | Assets + Operations + Finance |
| Leading metrics | Integrate time; AI ROI; reporting package use |
| Capital bias | Growth for proof; protect reserve |
| Org stage bias | 1 |
| AI stage bias | AI-2 |

**Entry narrative:** Kernel ready; asset in motion.

**Exit narrative:** Honest evidence that Atlas made an asset better faster than baseline.

**Typical projects:** First integrate, ROI dashboard, playbook scarring, decision reviews.

**Typical non-goals:** Logo collecting; L4 claims.

### Card P3 — Repeatable Machine

| Field | Content |
|---|---|
| Intent | Decline chaos per added asset |
| Primary owner | Operations + AI + Assets |
| Leading metrics | Marginal integrate effort; template reuse; L2 coverage |
| Capital bias | Scale winners; shared services |
| Org stage bias | 2 |
| AI stage bias | AI-3 |

**Exit narrative:** Third integrate is boring in the best way.

### Card P4 — Platform Organism

| Field | Content |
|---|---|
| Intent | Productize HOS |
| Primary owner | AI + Projects + Knowledge |
| Leading metrics | Weekly active operators on OS; L3 coverage |
| Capital bias | Infrastructure product investment |
| Org stage bias | 2–3 |
| AI stage bias | AI-4 |

**Exit narrative:** Operators complain when the portal is down — because they depend on it.

### Card P5 — Institutional Form

| Field | Content |
|---|---|
| Intent | Survive people |
| Primary owner | Brain |
| Leading metrics | Succession exercise; intel usage; deputy coverage |
| Org stage bias | 3–4 |
| AI stage bias | AI-5 |

**Exit narrative:** New leaders operate via systems; oral tradition optional.

### Card P6 — Infrastructure Era

| Field | Content |
|---|---|
| Intent | Durable economic infrastructure |
| Primary owner | Brain (stewardship) |
| Leading metrics | Generational continuity; stewardship outcomes |
| Exit | None — perpetual stewardship reviews |

---

## Appendix B — Evolution Track Scorecards

### How to use

Each quarter, track owners score 1–5 on the questions below. Attach evidence links. Brain uses results in CM light scoring.

### AI track scorecard questions

1. Is the registry complete for production automations?
2. Are L-levels accurate (no inflation)?
3. Is ROI reported for each production automation?
4. Are guardrails tested?
5. Is reuse rising?
6. Are failures loud and owned?
7. Is model evaluation current?
8. Any shadow AI requiring remediation?

### Knowledge track scorecard questions

1. % docs with owners/review dates
2. Stale rate trend
3. Findability spot-checks pass rate
4. Retro compliance
5. Decision log completeness for material decisions
6. Onboarding path currency
7. Duplication incidents fixed
8. Glossary coverage for new terms

### Infrastructure track scorecard questions

1. Access reviews current?
2. Critical systems restore tested?
3. Data segmentation incidents = 0?
4. Tooling inventory current?
5. Observability on production automations?
6. Platform adoption (if P4+)?
7. Vendor exit plans for critical vendors?
8. Security evals on model/vendor changes?

### Organization track scorecard questions

1. Single owners present on material outcomes?
2. Dual-hats labeled?
3. Interface SLAs honored?
4. Escalations following documented paths?
5. Charters exist for active seats?
6. Any shadow structures?
7. Hiring aligned to builders/judgment?
8. Org stage appropriate to CM?

### Product (HOS) track scorecard questions

1. Did HOS increments ship this quarter?
2. Do operators use them?
3. Did increments reduce local reinventing?
4. Any HOS feature without users to retire?
5. Autonomy spectrum respected?

### Automation track scorecard questions

1. Candidates above threshold queued?
2. Specs complete?
3. Flaky rate acceptable?
4. Retirements executed?
5. Wave plan on schedule vs phase?

### Finance track scorecard questions

1. Close on time?
2. Buckets respected?
3. Hurdles applied?
4. Reporting package used?
5. Reserve intact?
6. Misses explained promptly?

### Assets track scorecard questions

1. Pipeline hygiene?
2. Memos complete for material opps?
3. Integrate SLA status?
4. Lifecycle stages accurate?
5. Exit/hold honesty?
6. Operator charters current?

### Operations track scorecard questions

1. KPI dictionary currency?
2. Incident drills/reviews?
3. Vendor framework usage?
4. Shared services SLA health?
5. Continuous improvement actions closed?

### Projects track scorecard questions

1. Brief compliance?
2. WIP within capacity?
3. Red projects escalated?
4. Retro compliance?
5. Handoff confirmations?
6. Mix infra vs asset appropriate?

---

## Appendix C — Quarterly Calendar Patterns

### Standard quarter skeleton

| Week | Focus | Artifacts |
|---|---|---|
| 0 (pre) | Evidence pack assembly | CM inputs, milestone states |
| 1 | Priority lock | Quarterly Priorities memo |
| 2 | Project briefs confirmed | Briefs approved |
| 3 | Execution | Status green/yellow/red |
| 4 | Execution | Automation candidates review |
| 5 | Mid-check | WIP / dependency check |
| 6 | Execution | Portfolio integrate check |
| 7 | Execution | Finance flash vs plan |
| 8 | Execution | Knowledge hygiene sprint |
| 9 | Pre-review | Draft grades |
| 10 | Review prep | Async pack |
| 11 | Quarterly review | Notes + actions |
| 12 | Next quarter draft | Draft priorities |

### Quarter types

| Type | When | Emphasis |
|---|---|---|
| **Foundation quarter** | P0–P1 | Docs, kernel, hygiene |
| **Integrate quarter** | Around M-S-003/004/005 | Ops+Assets dominate WIP |
| **Automation quarter** | After SOP wave | AI+Ops |
| **Platform quarter** | P4 | Infra product |
| **Consolidation quarter** | After expansion spike | Debt paydown; deepen |
| **Truth quarter** | After misses | Retros; standard updates; no new logos |

### Mapping quarter types to phases

| Phase | Default quarter type mix (year) |
|---|---|
| P0 | 3–4 Foundation |
| P1 | 2 Foundation, 1–2 Automation, 0–1 Integrate prep |
| P2 | 1–2 Integrate, 1 Automation, 1 Truth/Consolidate |
| P3 | 2 Integrate/Repeat, 1 Shared services, 1 Automation |
| P4 | 2 Platform, 1 Consolidate, 1 Portfolio |
| P5+ | 1 Institutional, 1 Intelligence, 2 Operate/Optimize |

---

## Appendix D — Milestone Deep Notes

### M-G-001 — Brain OS document set

**Why it matters:** Without T1 substrate, later milestones optimize fog.

**Done means:** Active status on 00–04; referenced by at least one real decision each.

**Not done if:** Docs exist but unused; Current State empty.

**Common failure:** Polishing prose instead of initializing decisions/state.

### M-A-001 — Automation registry v1

**Why:** Invisible automations are unowned risks.

**Done means:** Registry lists candidates + production entries with owners, maturity, SOP links.

**Depends on:** Eligibility criteria understood from Brain Automation Standards.

### M-O-002 — Integration scorecard v1

**Why:** Integrate without scorecard is storytelling.

**Done means:** Areas/timelines from Company Lifecycle tracked on a living scorecard template.

**Used by:** M-S-003 and all later integrates.

### M-S-003 — First Integrate complete

**Why:** Thesis proof pivot.

**Done means:** Scorecard green or waived items explicitly DR'd with expiry; Knowledge base company overview done; reporting mapped.

**Failure mode:** "Mostly integrated" forever.

### M-A-003 — L2 default on repeated holding processes

**Why:** AI-native claim becomes real.

**Done means:** Coverage % meets Current State target; each counted process has SOP + owner + eval.

**Failure mode:** Counting ad-hoc chat usage as L2.

### M-I-004 — Atlas OS platform MVP

**Why:** Encodes standards into software operators use.

**Done means:** Weekly use by portfolio operators for ≥1 core workflow (playbooks, reporting, or automations).

**Hard gate:** P3 exit.

**Failure mode:** Beautiful empty app.

### M-G-012 — Succession exercise passed

**Why:** Institutional test.

**Done means:** Deputy/new lead operates 90 days; retrospective lists gaps converted to tickets; no catastrophic oral dependency.

### M-A-010 — Cross-portfolio intelligence

**Why:** Network effects of institutional memory become computational.

**Done means:** Pattern outputs used in at least one Assets/Brain decision with citation.

**Hard deps:** Segmentation policy + multi-asset data.

---

## Appendix E — Decision Templates for Roadmap Governance

### DR template — Phase gate

```markdown
## DR-YYYY-NNN: Phase gate P# → P#

**Date:**
**Owner:** Brain
**Type:** Strategic

### Context
Current phase, CM minimum, evidence pack link.

### Options considered
1. Approve transition
2. Conditional approve (list conditions + expiry)
3. Reject (remain in phase)

### Decision
…

### Success metrics
- Next phase entry workstreams started by …
- Current State updated same day

### Review date
…
```

### DR template — Milestone waiver

```markdown
## DR-YYYY-NNN: Waiver for milestone M-xxx

**Date:**
**Owner:**
**Type:** Strategic | Operational

### Context
Why waiver requested; what risk accepted.

### Options
1. Deny waiver
2. Time-boxed waiver (expiry)
3. Rescope milestone

### Decision
…

### Success metrics / expiry
…
```

### DR template — Roadmap major amendment

```markdown
## DR-YYYY-NNN: Amend 04_ROADMAP (major)

**Date:**
**Owner:** Brain
**Type:** Strategic

### Context
What is wrong with current sequencing.

### Options
1. Keep as-is
2. Amend (summary of text changes)
3. Defer

### Decision
…

### Success metrics
- Version bumped
- Departments notified
- Current State reconciled
```

---

## Appendix F — Capability Maturity Worked Example

### Illustrative scores (not live data)

| Dimension | Score | Note |
|---|---|---|
| CM-D1 Governance | 2 | Framework used sometimes |
| CM-D2 Knowledge | 2 | Structure exists; findability weak |
| CM-D3 AI | 1 | Ad-hoc |
| CM-D4 Finance | 2 | Close documented |
| CM-D5 Integration | 1 | Scorecard not yet used on live asset |
| CM-D6 Portfolio | 1 | Prospecting |
| CM-D7 Delivery | 2 | Briefs starting |
| CM-D8 Org | 2 | Dual-hats labeled |
| CM-D9 Platform | 1 | Inventory only |
| CM-D10 Learning | 1 | Few retros |

**Minimum = 1 → Holding CM-1.**

**Phase implication:** May exit P0 if P0 criteria met; not ready for P2.

**Quarterly implication:** Raise CM-D3 and CM-D5 (registry + scorecard) before asset scale.

### After a strong P2 (illustrative)

| Dimension | Score |
|---|---|
| CM-D1 | 3 |
| CM-D2 | 3 |
| CM-D3 | 3 |
| CM-D4 | 3 |
| CM-D5 | 3 |
| CM-D6 | 3 |
| CM-D7 | 3 |
| CM-D8 | 3 |
| CM-D9 | 2 |
| CM-D10 | 3 |

**Minimum = 2 → still watch D9; Holding CM-2 diagnostically average ~2.9; gate uses minimum → address platform only when P3 approach requires.**

Note: Live scores belong exclusively in Current State.

---

## Appendix G — Expansion Decision Trees

### Tree — Should we acquire now?

```
Start
 ├─ P0 incomplete? → NO
 ├─ CM-D5 < 2 and already have unintegrated asset? → NO (deepen)
 ├─ Reserve would breach policy? → NO
 ├─ Integrate capacity available? → if NO, NO
 ├─ Build-vs-acquire favors build? → prefer BUILD path
 ├─ Clears hurdles + strategic fit? → if NO, NO
 └─ Yes → DR + integrate plan before close marketing
```

### Tree — Should we build platform now?

```
Start
 ├─ P3 exit met? → if NO, NO
 ├─ Operator pull evidenced? → if NO, wait
 ├─ Templates/library exist? → if NO, build templates first
 ├─ Capital infra bucket available? → if NO, resequencing
 └─ Yes → M-I-004 project brief
```

### Tree — Should we enter a new sector?

```
Start
 ├─ Phase < P3? → default NO
 ├─ Portability test < 50%? → NO or explicit DR
 ├─ Talent/judgment available? → if NO, NO
 ├─ Data segmentation ready? → if NO, NO
 └─ Thesis strengthens OS? → if NO, NO else DR
```

---

## Appendix H — Planning Worked Examples

### Example annual memo (abridged, illustrative)

```markdown
# Atlas Annual Plan YYYY

**Theme:** Prove leverage on asset one.
**Phase ambition:** Exit P2 or conditional near-exit.
**CM floors:** No dimension < 2 by Q4; D5 ≥ 3.
**Capital buckets:** Operating / Growth / Infra / Reserve / Experimental
  (percentages in Current State)
**Portfolio posture:** One integrate excellence; pipeline hygiene; no cluster expansion.
**Infra thesis:** ROI dashboard + L2 default on holding BAU.
**Org posture:** Remain Stage 1; hire only if CM bottleneck.
**Top milestones:** M-S-003, M-A-003, M-A-005, M-F-004, M-O-005(start)
**Non-goals:** Platform MVP; third geo; public brand campaign.
```

### Example quarterly priorities (abridged, illustrative)

```markdown
## Q3 YYYY Priorities

**Phase:** P2
**Annual theme:** Prove leverage on asset one
**CM minimum (last):** 2

### Outcomes
1. Integration scorecard green for Asset A — Ops — M-S-003 — SLA dates met
2. AI ROI dashboard live — AI — M-A-005 — monthly report
3. L2 on top 10 holding processes — AI/Ops — M-A-003 — coverage table
4. Portfolio reporting package used twice — Finance — M-F-004 — two closes

### Non-goals
- Second acquisition
- Portal UX
- New sector research deep-dive
```

---

## Appendix I — Risk × Phase Heat Map

| Risk ID | P0 | P1 | P2 | P3 | P4 | P5+ |
|---|---|---|---|---|---|---|
| R-S-01 Thesis failure | L | L | H | M | L | L |
| R-S-02 Premature scale | H | H | H | M | L | L |
| R-S-03 Mission drift | L | L | M | M | H | H |
| R-S-04 Principle erosion | M | M | M | M | M | M |
| R-S-05 Platform too early | L | H | H | M | L | L |
| R-S-06 Platform too late | L | L | L | M | H | M |
| R-O-01 Bureaucracy | L | L | L | M | H | H |
| R-O-02 Key person | H | H | M | M | L | L |
| R-A-01 Silent failures | L | M | H | H | H | M |
| R-A-02 Over-autonomy | L | L | M | M | H | H |
| R-K-01 Corpus rot | L | M | M | H | H | H |
| R-F-01 Liquidity | M | M | M | M | M | M |
| R-F-03 Sunk cost | L | L | M | H | H | H |

H = heightened attention; M = monitor; L = lower relative focus. Not a substitute for full risk reviews.

---

## Appendix J — Glossary Pointers for Roadmap Terms

Until [`07_GLOSSARY.md`](07_GLOSSARY.md) is complete, treat these as roadmap-local definitions. When glossary entries exist, glossary wins; remove duplication here in a future minor edit.

| Term | Roadmap-local definition |
|---|---|
| Holding OS / HOS | Reusable infrastructure product of Atlas |
| Phase gate | Go/no-go review against exit criteria |
| CM-n | Holding capability maturity level n |
| Track | Parallel evolution stream |
| Waiver | Time-boxed DR exception to a milestone/gate element |
| Deepen-before-widen | Expansion rule prioritizing integrate depth |
| Shadow roadmap | Conflicting unofficial strategy |
| Evidence pack | Linked artifacts proving exit criteria |
| Operator pull | Demand signal from portfolio operators for OS features |
| Coordination tax audit | Review of relay roles vs owner roles |

---

## Appendix K — Onboarding Path Addition for Roadmap

Brain onboarding path lists this document after Current State context ([Onboarding knowledge path](00_ATLAS_BRAIN.md#onboarding-knowledge-path)). Recommended roadmap reading order for new operators:

1. Purpose + How to Read
2. Vision Horizon (skim)
3. Major Phases — current phase card in Appendix A
4. What Is NOT on the Roadmap
5. Quarterly Planning Model
6. Track section for your department
7. Milestone Dependencies involving your track

Do not require memorizing the full milestone register on day one.

---

## Appendix L — Long-Form Phase Exit Evidence Index

### P0 evidence index

| Criterion | Evidence artifact | Owner |
|---|---|---|
| P0.1 | `00_ATLAS_BRAIN.md` header Status | Brain |
| P0.2 | `01_WHY_ATLAS_EXISTS.md` header | Brain |
| P0.3 | `02_FOUNDING_PRINCIPLES.md` header | Brain |
| P0.4 | `03_ORGANIZATION.md` header | Brain |
| P0.5 | `04_ROADMAP.md` header | Brain |
| P0.6 | `05_CURRENT_STATE.md` snapshot | Brain |
| P0.7 | `06_DECISIONS.md` format | Brain |
| P0.8 | `07_GLOSSARY.md` started | Knowledge |
| P0.9 | Sample work logs tagged by dept | All |

### P1 evidence index

| Criterion | Evidence artifact | Owner |
|---|---|---|
| P1.1 | Seven playbook stubs or charters | Dept heads |
| P1.2 | ≥3 project briefs + retros | Projects |
| P1.3 | Registry doc | AI |
| P1.4 | Maturity report ≥3 × L2 | AI |
| P1.5 | Close SOP + close artifacts | Finance |
| P1.6 | Scorecard template | Ops/Assets |
| P1.7 | Thresholds table in Current State | Brain/Finance |
| P1.8 | Onboarding checklist completed | Knowledge |

### P2 evidence index

| Criterion | Evidence artifact | Owner |
|---|---|---|
| P2.1 | Scorecard complete | Ops/Assets |
| P2.2 | Time study / comparison | Ops |
| P2.3 | Registry reuse fields | AI |
| P2.4 | Reporting package samples | Finance |
| P2.5 | ROI report | AI |
| P2.6 | Decision review notes | Brain |
| P2.7 | Logged failed hypothesis | Decision owner |

### P3 evidence index

| Criterion | Evidence artifact | Owner |
|---|---|---|
| P3.1 | Three scorecards archived | Assets/Ops |
| P3.2 | Effort trend table | Ops |
| P3.3 | Template library index | AI |
| P3.4 | Coverage report | AI/Ops |
| P3.5 | Interface SLA review notes | Org/Brain |
| P3.6 | Org stage evidence | Brain |
| P3.7 | Staleness report samples | Knowledge |

### P4 evidence index

| Criterion | Evidence artifact | Owner |
|---|---|---|
| P4.1 | Platform usage metrics | AI/Projects |
| P4.2 | Portal adoption | Knowledge/AI |
| P4.3 | Decision support logs | AI/Brain |
| P4.4 | L3 maturity report | AI |
| P4.5 | Pull signal memos | Assets/Brain |
| P4.6 | Coordination tax audit | Brain |

### P5 evidence index

| Criterion | Evidence artifact | Owner |
|---|---|---|
| P5.1 | Succession retro | Brain |
| P5.2 | Intel → decision citations | AI/Assets |
| P5.3 | Governance charter check | Brain |
| P5.4 | Knowledge product adoption | Knowledge |
| P5.5 | Stress-test DR set | Brain |

---

## Appendix M — Alignment Statements (Non-Duplicative)

These statements bind the roadmap to sibling docs without restating doctrine.

1. **Principles bind the roadmap.** If a milestone requires violating [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md), the milestone is wrong.
2. **Organization executes the roadmap.** Structure changes follow [`03_ORGANIZATION.md`](03_ORGANIZATION.md) governance boundaries.
3. **Brain OS defines mechanisms.** Lifecycles, AI levels, automation eligibility, capital philosophy remain in [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md).
4. **Why supplies conviction.** Fifty-year philosophical eras remain in [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md); this doc operationalizes them.
5. **Current State supplies truth.** Numbers, names, live phase, and thresholds remain in [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md).
6. **Decisions supply precedent.** Gates, waivers, and amendments log in [`06_DECISIONS.md`](06_DECISIONS.md).
7. **Glossary supplies language.** Shared terms consolidate in [`07_GLOSSARY.md`](07_GLOSSARY.md).

---

## Closing

Atlas compounds by sequencing ambition behind evidence. This roadmap is the canonical sequencing contract: horizons to orient, phases to gate, milestones to verify, tracks to evolve in parallel, planning models to execute, and ownership to prevent drift.

It does not replace principles, organization, or the Brain operating system. It tells time for them.

Advance phases when exit criteria are true. Slip calendars before faking gates. Deepen before widening. Measure leverage before narrating it. Keep humans accountable as machines take on more of the work.

When uncertain whether something belongs on the roadmap, return to the Brain's three mission questions — and to [What Is NOT on the Roadmap](#what-is-not-on-the-roadmap).

---

*This is the canonical roadmap of the Atlas Brain. Strategy without sequencing is aspiration; sequencing without principles is drift. Hold both.*

