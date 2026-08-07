# Atlas Organization

> The canonical operating manual for how Atlas is organized — departments, ownership, authority, interfaces, escalation, and scaling. The organization exists to execute the Brain, not replace it.

**Document ID:** `03_ORGANIZATION.md`  
**Location:** `02_Brain/`  
**Status:** Active  
**Version:** 1.0  
**Owner:** Brain  
**Classification:** Governance — organizational architecture  
**Last updated:** 2026-08-08  
**Review date:** 2026-11-08  
**Supersedes:** —  
**Authority:** This document is the authoritative source for *how Atlas is structured*, *who owns what*, *how authority flows*, and *how departments interact*. Strategic and philosophical context lives in sibling Brain documents — link to them; do not duplicate.

---

## Table of Contents

1. [Purpose](#purpose)
2. [Organizational Philosophy](#organizational-philosophy)
3. [Organization Executes the Brain](#organization-executes-the-brain)
4. [Why Departments Instead of Management Layers](#why-departments-instead-of-management-layers)
5. [Organizational Design Principles](#organizational-design-principles)
6. [Department Architecture Overview](#department-architecture-overview)
7. [Department: Brain](#department-brain)
8. [Department: Knowledge](#department-knowledge)
9. [Department: AI](#department-ai)
10. [Department: Finance](#department-finance)
11. [Department: Operations](#department-operations)
12. [Department: Assets](#department-assets)
13. [Department: Projects](#department-projects)
14. [Why Each Department Exists](#why-each-department-exists)
15. [Reporting Relationships](#reporting-relationships)
16. [Ownership vs Execution](#ownership-vs-execution)
17. [Single Owner Principle](#single-owner-principle)
18. [Contributor Model](#contributor-model)
19. [Decision Authority](#decision-authority)
20. [Escalation Authority](#escalation-authority)
21. [Execution Flow](#execution-flow)
22. [Accountability Model](#accountability-model)
23. [Responsibility Matrix](#responsibility-matrix)
24. [Department Interfaces](#department-interfaces)
25. [Communication Architecture](#communication-architecture)
26. [Synchronous vs Asynchronous Work](#synchronous-vs-asynchronous-work)
27. [Governance Boundaries](#governance-boundaries)
28. [Management Philosophy](#management-philosophy)
29. [Leadership Expectations](#leadership-expectations)
30. [Hiring Philosophy](#hiring-philosophy)
31. [Role Lifecycle](#role-lifecycle)
32. [Onboarding](#onboarding)
33. [Offboarding](#offboarding)
34. [AI Participation Inside Departments](#ai-participation-inside-departments)
35. [Organizational Scaling](#organizational-scaling)
36. [Scaling Without Changing Principles](#scaling-without-changing-principles)
37. [Organizational Anti-Patterns](#organizational-anti-patterns)
38. [Failure Modes](#failure-modes)
39. [Practical Examples](#practical-examples)
40. [Counter-Examples](#counter-examples)
41. [Operational Checklists](#operational-checklists)
42. [Organization Review Checklist](#organization-review-checklist)
43. [Cross References](#cross-references)
44. [Document Maintenance](#document-maintenance)

**Related documents:** [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) · [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) · [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) · [`04_ROADMAP.md`](04_ROADMAP.md) · [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) · [`06_DECISIONS.md`](06_DECISIONS.md) · [`07_GLOSSARY.md`](07_GLOSSARY.md)

---

## Purpose

### What this document is

This document defines **how Atlas is organized as an operating system** — the structural layer that converts strategy into repeatable execution across decades, portfolio companies, and generations of operators.

It answers:

- **Who owns what** — outcomes, systems, documents, decisions, and escalations
- **Who reports to whom** — functional accountability, not political hierarchy
- **Who decides what** — authority boundaries, thresholds, and escalation triggers
- **How work flows** — from intent to execution to measurement to knowledge capture
- **How the organization scales** — from one operator to a thousand, without abandoning principles

### What this document is not

| This document | Lives elsewhere |
|---|---|
| Mission, vision, long-term purpose | [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) |
| Why Atlas exists; structural critique of traditional orgs | [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) |
| Immutable principles and judgment infrastructure | [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) |
| Decision scoring criteria, one-way doors, capital philosophy | [Decision Framework](00_ATLAS_BRAIN.md#decision-framework), [Capital Allocation](00_ATLAS_BRAIN.md#capital-allocation-philosophy) |
| High-level department summaries | [Organizational Architecture](00_ATLAS_BRAIN.md#organizational-architecture) |
| Current headcount, active roles, staffing gaps | [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) |
| Strategic priorities and timeline | [`04_ROADMAP.md`](04_ROADMAP.md) |
| Canonical term definitions | [`07_GLOSSARY.md`](07_GLOSSARY.md) |

### Primary audience

| Audience | How to use this document |
|---|---|
| **New operators** | Read after Brain and Principles; before department playbooks |
| **Department heads** | Reference for ownership boundaries, interfaces, escalation |
| **Portfolio leaders** | Understand holding standards vs local execution autonomy |
| **AI agents** | Resolve ownership, route escalations, enforce single-owner metadata |
| **Future leaders** | Structural invariant — how Atlas organizes regardless of who leads |

### Design intent

Atlas is an **AI-native holding company** designed to compound over decades. Organization is not an HR artifact. It is **executable infrastructure** — as durable as code, as auditable as financial statements, and as legible to machines as to humans.

The organization exists to **execute the Brain**, not replace it. When structure and strategy conflict, structure must change — principles and Brain documents do not.

---

## Organizational Philosophy

### The holding as operating system

Atlas is not a collection of companies with a shared logo. It is a **single operating organism** — a holding OS — where seven departments each own a distinct layer of capability. Portfolio companies plug into that OS; they do not rebuild it.

See [Organizational Architecture](00_ATLAS_BRAIN.md#organizational-architecture) for the Brain-level architecture diagram. This document specifies **roles, authority, interfaces, and scaling** beneath that diagram.

### Core organizational beliefs

These beliefs govern structure. They derive from [Founding Principles](02_FOUNDING_PRINCIPLES.md) and [Operating Philosophy](00_ATLAS_BRAIN.md#operating-philosophy); they are stated here only as organizational implications.

| Belief | Organizational implication |
|---|---|
| **Systems over heroes** | Departments own systems; individuals own outcomes within systems |
| **Ownership** | Every artifact has exactly one accountable human owner — see [Single Owner Principle](#single-owner-principle) |
| **Transparency** | Information flows to those who need it; secrecy requires justification |
| **Extreme documentation** | Undocumented structure is non-existent structure |
| **AI-first thinking** | AI is embedded in every department, not isolated in a lab |
| **Centralize intelligence, distribute execution** | Brain + Knowledge + AI + Finance centralize; portfolio operators execute locally |
| **Compounding over optimization** | Org design favors reusable patterns over local maxima |

### The Ray Dalio principle applied to Atlas

**Believability-weighted decision rights.** Authority follows demonstrated competence in a domain, documented in outcomes — not tenure, title, or proximity to power.

In practice:

- A portfolio operator with five years of domain expertise and strong track record has believability on product decisions for their asset.
- Finance has believability on capital structure; Brain has believability on holding-wide strategy.
- Disagreement is resolved with evidence and principles, not rank — see [Decision Authority](#decision-authority).

### The Stripe principle applied to Atlas

**Write the org chart in documents, not in meetings.** If a reporting line, ownership boundary, or escalation trigger exists only in someone's head, it does not exist for scaling, delegation, or AI assistance.

Every structural element in this document must be:

- Findable in the knowledge base
- Referenced in playbooks and SOPs
- Machine-readable where feasible (owner fields, escalation tags)

### The Amazon principle applied to Atlas

**Single-threaded ownership.** No outcome has two owners. No project has two DRIs. No system has "the team" as owner.

Contributors are many; owners are one. See [Ownership vs Execution](#ownership-vs-execution).

### The OpenAI principle applied to Atlas

**Humans accountable; AI executable.** Agents participate inside departments as contributors to execution. Humans retain accountability for outcomes, guardrails, and one-way doors — see [Human accountability](02_FOUNDING_PRINCIPLES.md#human-accountability) and [AI Participation](#ai-participation-inside-departments).

---

## Organization Executes the Brain

### The relationship

```
┌─────────────────────────────────────────────────────────────┐
│  BRAIN DOCUMENTS (00–07)                                    │
│  Strategy · Principles · Frameworks · Standards             │
│  WHAT Atlas optimizes for and HOW it decides                │
└──────────────────────────┬──────────────────────────────────┘
                           │ constrains & informs
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  ORGANIZATION (this document)                               │
│  Departments · Ownership · Authority · Interfaces           │
│  WHO does WHAT and HOW work flows                           │
└──────────────────────────┬──────────────────────────────────┘
                           │ enables
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  EXECUTION LAYER                                            │
│  Playbooks · SOPs · Projects · Automations · Portfolio ops  │
│  WHAT happens daily                                         │
└─────────────────────────────────────────────────────────────┘
```

### Rules of engagement

1. **Brain sets direction; organization delivers.** Strategic shifts originate in Brain documents and [`06_DECISIONS.md`](06_DECISIONS.md). Departments implement — they do not silently redefine strategy.
2. **Organization proposes; Brain approves structural change.** Adding an eighth department, changing escalation thresholds, or altering governance boundaries requires a Decision Record — see [Governance Boundaries](#governance-boundaries).
3. **No shadow governance.** Informal power structures that bypass documented authority are organizational debt. Surface and fix them in quarterly org reviews.
4. **Portfolio autonomy within standards.** Portfolio operators execute locally; they do not opt out of holding standards defined in Brain — see [Portfolio company autonomy spectrum](00_ATLAS_BRAIN.md#portfolio-company-autonomy-spectrum).

### When organization and Brain diverge

| Situation | Resolution |
|---|---|
| Department routinely bypasses a Brain standard | Fix the department process or escalate standard change to Brain |
| Brain standard is unworkable at scale | Propose amendment via Decision Record; do not create informal workaround |
| Two departments claim same ownership | Brain arbitrates; resolution logged in [`06_DECISIONS.md`](06_DECISIONS.md) |
| Undocumented role performs de facto governance | Document the role or eliminate the function |

---

## Why Departments Instead of Management Layers

### The problem with traditional hierarchy

Traditional organizations scale coordination through **management layers** — people whose job is to relay, filter, reconcile, and approve. Each layer adds latency, distorts information, and creates political surface area.

See [Why Software Is Replacing Management](01_WHY_ATLAS_EXISTS.md#why-software-is-replacing-management) for the full argument. Organizationally, Atlas rejects middleware management as a default.

### What Atlas uses instead

**Functional departments** — permanent ownership domains aligned to layers of the holding OS:

| Traditional layer | Atlas replacement |
|---|---|
| Executive committee | Brain department + Decision Framework |
| Middle management | Documented ownership + escalation triggers + AI-assisted routing |
| Shared services (ad hoc) | Operations + Finance + Knowledge (defined interfaces) |
| Program management (ad hoc) | Projects department |
| IT / automation (ad hoc) | AI department |
| Corporate development (ad hoc) | Assets department |

### Why departments beat generic management

| Property | Management layers | Departments |
|---|---|---|
| **Clarity of ownership** | Ambiguous ("reports to VP") | Explicit (Finance owns monthly close) |
| **Machine legibility** | Relational, informal | Documented interfaces and KPIs |
| **Compounding** | Knowledge trapped in managers | Knowledge captured in Knowledge department |
| **Scaling cost** | Linear with headcount | Sublinear with automation |
| **Accountability** | Diffused across chain | Single owner per outcome |
| **AI integration** | Bolt-on assistants | Embedded in department workflows |

### What departments are not

- **Not silos.** Departments have defined interfaces; cross-department work is normal — see [Department Interfaces](#department-interfaces).
- **Not fiefdoms.** Department heads own their domain; they do not own holding strategy — Brain does.
- **Not permanent headcount containers.** A department may be one person or fifty; the **domain** is stable, staffing scales — see [Organizational Scaling](#organizational-scaling).

### The seven-department invariant

Atlas maintains **exactly seven canonical departments** unless Brain explicitly approves structural change:

1. **Brain** — Strategy, governance, OS definition
2. **Knowledge** — Institutional memory
3. **AI** — Intelligent infrastructure
4. **Finance** — Economic truth and capital
5. **Operations** — Execution discipline
6. **Assets** — Portfolio ownership
7. **Projects** — Initiative delivery

Sub-teams, squads, and portfolio-local orgs exist **inside or adjacent to** these domains. They do not replace them.

---

## Organizational Design Principles

Structural decisions follow these principles. When principles conflict, defer to [Principle Hierarchy](02_FOUNDING_PRINCIPLES.md#principle-hierarchy).

### 1. Clarity over comfort

Clear ownership may create temporary discomfort ("that's not my job" → "yes, it is — you're the owner"). Ambiguity creates permanent damage.

### 2. Interfaces over meetings

Departments coordinate through **defined inputs, outputs, and SLAs** — not through standing sync meetings that substitute for documentation.

### 3. Ownership over consensus

Consensus is a input mechanism, not a decision mechanism. One owner decides; contributors advise — see [Decision Authority](#decision-authority).

### 4. Documented over tribal

If it is not written in this document, a playbook, or a Decision Record, it is not organizational truth.

### 5. Leverage over headcount

Prefer one excellent operator with AI and automation over three operators doing manual coordination — see [Staffing philosophy](00_ATLAS_BRAIN.md#staffing-philosophy).

### 6. Stable domains, flexible staffing

Department **missions** change rarely. Department **headcount** changes frequently. Do not rename or merge departments to match headcount fluctuations.

### 7. Escalation is a feature, not a failure

Escalation means the system worked — a trigger fired, information reached the right level. Punishing escalation trains silence — see [Escalation Authority](#escalation-authority).

---

## Department Architecture Overview

### Structural diagram

```
                    ┌─────────────────────────────────┐
                    │            BRAIN                │
                    │  Strategy · Governance · OS     │
                    │  Sets direction for all         │
                    └───────────────┬─────────────────┘
                                    │
          ┌─────────────┬───────────┼───────────┬─────────────┐
          │             │           │           │             │
     ┌────▼────┐   ┌────▼────┐ ┌────▼────┐ ┌────▼─────┐  ┌────▼────┐
     │KNOWLEDGE│   │   AI    │ │ FINANCE │ │OPERATIONS│  │PROJECTS │
     │ Memory  │   │Intellect│ │ Capital │ │ Execution│  │Delivery │
     └────┬────┘   └────┬────┘ └────┬────┘ └────┬─────┘  └────┬────┘
          │             │           │           │             │
          └─────────────┴───────────┼───────────┴─────────────┘
                                    │
                           ┌────────▼────────┐
                           │     ASSETS      │
                           │   Portfolio     │
                           │  (value layer)  │
                           └─────────────────┘
```

### Department summary table

| Department | One-line mission | Layer owned | Default department head title |
|---|---|---|---|
| **Brain** | Define and maintain the holding OS | Governance & strategy | Chief Operating Architect / Holding Lead |
| **Knowledge** | Capture and surface institutional memory | Information architecture | Head of Knowledge |
| **AI** | Build and maintain intelligent infrastructure | Automation & augmentation | Head of AI |
| **Finance** | Maintain economic truth and allocate capital | Financial systems | Head of Finance / CFO |
| **Operations** | Run execution with discipline and consistency | Operational systems | Head of Operations / COO |
| **Assets** | Own portfolio value creation and lifecycle | Portfolio entities | Head of Assets |
| **Projects** | Deliver time-bound initiatives with accountability | Initiative delivery | Head of Projects |

### Cross-department interaction matrix

Full matrix lives in [Organizational Architecture — Cross-department interaction matrix](00_ATLAS_BRAIN.md#cross-department-interaction-matrix). This document adds **ownership, SLAs, and escalation** per interface — see [Department Interfaces](#department-interfaces).

---

## Department: Brain

### Mission

Define Atlas's direction, maintain the decision and governance infrastructure, and ensure all departments execute against a coherent holding operating system.

### Scope

**In scope:**

- Mission, principles, and operating philosophy (Brain documents)
- Strategic planning and portfolio direction
- Decision frameworks, escalation thresholds, governance boundaries
- Cross-department priority setting and conflict resolution
- Holding-wide standard changes (T1 documents)
- Quarterly and annual strategic reviews

**Out of scope:**

- Day-to-day portfolio operations (Operations + Assets)
- Building automations (AI)
- Maintaining playbooks and SOPs (Knowledge + domain departments)
- Financial close and reporting (Finance)
- Project delivery (Projects)

### Responsibilities

| Responsibility | Owner role | Output |
|---|---|---|
| Maintain Brain documents (00–07) | Brain lead | Updated governance docs |
| Set holding priorities | Brain lead | Quarterly priority memo |
| Resolve cross-department ownership disputes | Brain lead | Decision Record |
| Approve principle exceptions | Brain lead | DR + Principles log |
| Review escalation above department thresholds | Brain lead | Escalation resolution |
| Coordinate board / investor communication | Brain lead | Board materials |

### Ownership

| Asset / outcome | Owner |
|---|---|
| `00_ATLAS_BRAIN.md` | Brain lead |
| `01_WHY_ATLAS_EXISTS.md` | Brain lead |
| `02_FOUNDING_PRINCIPLES.md` | Brain lead |
| `03_ORGANIZATION.md` | Brain lead |
| `04_ROADMAP.md` | Brain lead (input from all departments) |
| `05_CURRENT_STATE.md` | Brain lead (input from all departments) |
| `06_DECISIONS.md` | Brain lead (curation); decision owners submit records |
| `07_GLOSSARY.md` | Brain lead (curation); all departments propose terms |
| Holding strategy | Brain lead |
| Governance boundary changes | Brain lead |

### Inputs

- Department status and escalations from all departments
- Financial health reports from Finance
- Portfolio performance from Assets + Operations
- Knowledge gaps and doc staleness flags from Knowledge
- AI capability and automation ROI from AI
- Project portfolio health from Projects
- External market and regulatory context

### Outputs

- Strategic direction and priority stack
- Approved Decision Records for holding-level decisions
- Updated governance documents
- Escalation resolutions
- Quarterly holding review

### Internal customers

All departments; portfolio leadership; board / investors (via coordinated materials)

### External customers

Investors, board members, strategic partners (holding-level narrative)

### KPIs

| KPI | Target cadence | Notes |
|---|---|---|
| Brain document freshness (% on review schedule) | Quarterly | Knowledge flags stale docs |
| Decision Record completeness | Per decision | All large decisions logged |
| Escalation resolution time | Per escalation | Median < 5 business days |
| Cross-department dispute count | Quarterly | Trending down as interfaces mature |
| Strategic priority clarity score | Quarterly survey | Operators can name top 3 priorities |

### Decision authority

| Decision type | Authority | Escalation |
|---|---|---|
| T1 document changes | Brain lead | Board for material strategy shifts |
| Principle exceptions | Brain lead | Documented in DR; rare |
| Cross-department priority conflicts | Brain lead | — |
| New department creation | Brain lead + DR | Board notification |
| Portfolio entry/exit (strategic) | Brain + Assets + Finance | Full Decision Framework |
| Holding-wide policy | Brain lead | DR if affects 2+ departments |

See [Decision Framework — Decision types and default owners](00_ATLAS_BRAIN.md#decision-framework).

### Escalation rules

Brain **receives** escalations; it does not replace department ownership.

| Trigger | Source | Brain action |
|---|---|---|
| Capital > threshold | Finance | Review + approve/deny |
| New asset / venture | Assets | Strategic fit review |
| Holding-wide standard change | Any department | Governance review |
| Principle exception | Any department | Judgment call + DR |
| Cross-department deadlock | Any department | Arbitrate ownership |
| Red project status | Projects | Continue / re-scope / kill |
| High-impact incident | Operations / AI | Strategic communication if needed |

Default triggers: [Escalation](00_ATLAS_BRAIN.md#escalation).

### Interfaces with other departments

| Department | Interface | SLA |
|---|---|---|
| **Knowledge** | Brain sets doc standards; Knowledge enforces | Standards updated within 5 days of Brain approval |
| **AI** | Brain sets AI strategy; AI implements | Strategy doc reviewed quarterly |
| **Finance** | Brain sets capital policy; Finance executes | Policy reviewed quarterly |
| **Operations** | Brain sets ops standards; Operations implements | Standard changes communicated within 48 hours |
| **Assets** | Brain sets portfolio direction; Assets proposes deals | Priority stack updated quarterly |
| **Projects** | Brain sets priorities; Projects sequences delivery | Priority changes reflected in project queue within 1 week |

---

## Department: Knowledge

### Mission

Ensure nothing Atlas learns is lost — capture, organize, validate, and surface institutional knowledge so every operator and agent can act with full context.

### Scope

**In scope:**

- Documentation standards (T2) and knowledge architecture
- Playbook and SOP curation standards
- Research and market intelligence coordination
- Decision log maintenance and searchability
- Onboarding knowledge paths
- Glossary curation support
- Document freshness and staleness monitoring

**Out of scope:**

- Writing domain playbooks (domain department owners)
- Strategic direction (Brain)
- Building retrieval automations (AI implements; Knowledge specifies requirements)
- Financial analysis content (Finance owns models; Knowledge stores)

### Responsibilities

| Responsibility | Output |
|---|---|
| Maintain documentation standards | T2 standards docs |
| Operate knowledge base architecture | Index, taxonomy, search |
| Curate onboarding reading paths | Onboarding guides |
| Flag stale / orphaned documents | Staleness reports to owners |
| Support due diligence research | Research briefs (with Assets) |
| Maintain decision log structure | Searchable `06_DECISIONS.md` |
| Coordinate glossary updates | Proposals to Brain for `07_GLOSSARY.md` |

See [Knowledge Management](00_ATLAS_BRAIN.md#knowledge-management) for lifecycle; this department **operates** that lifecycle.

### Ownership

| Asset / outcome | Owner |
|---|---|
| Documentation standards (T2) | Knowledge head (Brain approves) |
| Knowledge base architecture | Knowledge head |
| Onboarding knowledge path | Knowledge head |
| Decision log format and index | Knowledge head |
| Research archive structure | Knowledge head |
| Individual playbooks | Domain department (Knowledge audits compliance) |
| Individual SOPs | Process owner in Operations or domain dept |

### Inputs

- Documentation from all departments
- Decision Records from decision owners
- Retrospectives from Projects and Operations
- Research requests from Assets, Brain, Finance
- Automation specs from AI (for indexing)
- Staleness signals from automated audits

### Outputs

- Updated standards and templates
- Onboarding materials
- Research briefs
- Staleness and coverage reports
- Search and retrieval quality metrics

### Internal customers

All departments; AI (for RAG corpus); new operators; portfolio leaders

### External customers

Due diligence counterparties (controlled research outputs); partners (onboarding materials where appropriate)

### KPIs

| KPI | Target |
|---|---|
| Document staleness rate (% past review date) | < 10% |
| Onboarding path completion time | < 5 business days for core path |
| Decision log search success rate | > 95% findable within 2 queries |
| Playbook compliance (% processes with SOP) | Per Operations targets |
| Knowledge reuse rate (cross-portfolio doc views) | Trending up quarter over quarter |

### Decision authority

| Decision type | Authority |
|---|---|
| T2 documentation standard changes | Knowledge head + Brain approval |
| Taxonomy / tagging changes | Knowledge head |
| Archive vs retain | Knowledge head + domain owner |
| Research prioritization | Knowledge head |
| Holding-wide knowledge tool selection | Knowledge + AI + Brain |

### Escalation rules

| Trigger | Escalate to |
|---|---|
| Conflicting authoritative documents | Brain |
| Domain owner refuses documentation compliance | Brain |
| Knowledge tool failure / data loss | Brain + AI (incident) |
| Sensitive information mishandling | Brain + Finance (compliance) |

### Interfaces with other departments

| Department | Interface |
|---|---|
| **Brain** | Receives standards direction; informs strategy with knowledge gaps |
| **AI** | Provides corpus requirements; receives retrieval/automation tooling |
| **Finance** | Stores financial templates and models |
| **Operations** | Audits SOP coverage; receives process documentation |
| **Assets** | Supports DD research; receives portfolio learnings |
| **Projects** | Captures retrospectives; provides project archive structure |

---

## Department: AI

### Mission

Build and maintain the intelligent infrastructure that makes Atlas AI-native — agents, automations, integrations, and evaluation systems that embed AI in every department's workflows.

### Scope

**In scope:**

- AI tooling, agents, workflow automation
- Model selection, prompt engineering, evaluation
- Automation standards enforcement
- AI security and access policy implementation
- Automation registry and maturity tracking
- Cross-portfolio agent templating

**Out of scope:**

- Defining business outcomes automations serve (domain owners)
- Financial judgment on automations (Finance approves ROI thresholds)
- Writing playbooks (Knowledge + domain owners)
- Portfolio product AI features (portfolio operators, with AI support)

See [AI Strategy](00_ATLAS_BRAIN.md#ai-strategy) and [Automation Standards](00_ATLAS_BRAIN.md#automation-standards).

### Responsibilities

| Responsibility | Output |
|---|---|
| Build and maintain agents | Production agents in registry |
| Enforce agent design standards | Specs with owner, guardrails, fallback |
| Operate automation registry | Quarterly portfolio review |
| Evaluate and adopt models | Model evaluation reports |
| Embed AI in Operations workflows | L2+ automations for repeated processes |
| Support Finance reporting automation | Automated pipelines |
| Support Assets analysis | DD automation tooling |

### Ownership

| Asset / outcome | Owner |
|---|---|
| Automation registry | AI head |
| Agent design standards (T2) | AI head (Brain approves) |
| Individual agents | Named human owner per agent |
| Model vendor relationships | AI head |
| AI security implementation | AI head + Operations |
| Portfolio product ML | Portfolio operator (AI advises) |

### Inputs

- Automation candidates from Operations and all departments
- Process SOPs from Operations / Knowledge
- Data access policies from Finance and Brain
- ROI thresholds from Finance
- Strategic AI direction from Brain
- Incident reports involving AI errors

### Outputs

- Deployed agents and automations
- Automation specs and evaluations
- AI playbooks
- Maturity level assessments
- Quarterly automation ROI report

### Internal customers

All departments; portfolio operators; Knowledge (retrieval systems)

### External customers

Vendors (model providers); portfolio customers (only via portfolio products — not direct)

### KPIs

| KPI | Target |
|---|---|
| Repeated processes at L2+ maturity | 90% within 90 days of stabilization |
| Automation ROI (time saved vs cost) | Positive for all production automations |
| Agent failure rate | Below defined threshold per agent |
| Mean time to deploy new automation | Trending down |
| Cross-portfolio agent reuse rate | Trending up |

### Decision authority

| Decision type | Authority | Escalation |
|---|---|---|
| New agent deployment (within guardrails) | Agent owner + AI head | — |
| Model vendor selection (< threshold spend) | AI head | — |
| Holding-wide AI standard change | AI head | Brain |
| Cross-portfolio data access for agents | AI head | Brain + Finance |
| Autonomous (L3+) promotion | Agent owner + AI head | Brain if customer-facing |

### Escalation rules

| Trigger | Escalate to |
|---|---|
| AI incident with customer/revenue impact | Brain + Operations (incident protocol) |
| Guardrail breach | Agent owner immediately; AI head within 4 hours |
| Spend above automation budget threshold | Finance + Brain |
| Holding-wide AI policy conflict | Brain |

### Interfaces with other departments

| Department | Interface |
|---|---|
| **Brain** | Receives AI strategy; advises on leverage scoring |
| **Knowledge** | Automates capture; consumes corpus for RAG |
| **Finance** | Automates reporting; requests data access |
| **Operations** | Primary embedding partner for workflows |
| **Assets** | DD and analysis tooling |
| **Projects** | Builds infrastructure projects |

---

## Department: Finance

### Mission

Maintain economic truth across the holding and portfolio — capital allocation, reporting, compliance, and the financial inputs that make decisions evidence-based.

### Scope

**In scope:**

- Budgeting, forecasting, cash management
- Portfolio P&L, balance sheet, unit economics
- Investment analysis and hurdle rate enforcement
- Compliance, tax, financial reporting
- Capital allocation modeling and threshold management
- Financial escalation triggers

**Out of scope:**

- Strategic portfolio direction (Brain + Assets)
- Operational process design (Operations)
- Deal sourcing (Assets)
- Building non-financial automations (AI)

See [Capital Allocation Philosophy](00_ATLAS_BRAIN.md#capital-allocation-philosophy).

### Responsibilities

| Responsibility | Output |
|---|---|
| Monthly / quarterly financial close | Financial statements |
| Portfolio KPI dashboards | Unit economics reports |
| Investment memos (financial section) | Models and scenarios |
| Capital bucket management | Allocation reports |
| Threshold definition for escalations | Updated threshold tables |
| Compliance and tax filing | Filed returns, audit readiness |

### Ownership

| Asset / outcome | Owner |
|---|---|
| Holding financial statements | Finance head |
| Capital allocation model | Finance head |
| Hurdle rates and thresholds | Finance head (Brain approves policy) |
| Portfolio financial reporting standards | Finance head |
| Individual asset budgets | Asset operator (Finance consolidates) |
| Financial automations | Finance owner + AI (maintains) |

### Inputs

- Actuals from portfolio companies and Operations
- Deal models from Assets
- Project budgets from Projects
- Capital policy from Brain
- Automation data from AI

### Outputs

- Financial reports (monthly, quarterly)
- Investment analysis
- Budget vs actual variance reports
- Escalation triggers (updated quarterly)
- Cash flow forecasts

### Internal customers

Brain, Assets, Operations, Projects, portfolio operators, board

### External customers

Investors, auditors, tax authorities, lenders, counterparties

### KPIs

| KPI | Target |
|---|---|
| Close timeline (days after period end) | ≤ 10 business days |
| Forecast accuracy (rolling 90-day) | Within defined band |
| Portfolio reporting compliance | 100% on-time |
| Unit economics coverage | 100% of operating assets |
| Escalation threshold freshness | Updated quarterly |

### Decision authority

| Decision type | Authority | Escalation |
|---|---|---|
| Expense approval (within policy) | Finance policy + delegated owners | — |
| Budget reallocation (within department) | Department head | — |
| Capital deployment (below threshold) | Finance head + Assets | — |
| Capital deployment (above threshold) | Brain + Finance | Full DR |
| Hurdle rate change | Finance head | Brain + DR |
| New financial system / vendor (material) | Finance head | Brain |

### Escalation rules

| Trigger | Escalate to |
|---|---|
| Liquidity below reserve policy | Brain immediately |
| Material misstatement / fraud signal | Brain + legal |
| Portfolio company miss > threshold | Assets + Brain |
| Compliance deadline risk | Brain |

### Interfaces with other departments

| Department | Interface |
|---|---|
| **Brain** | Reports health; receives capital policy |
| **Knowledge** | Documents models and templates |
| **AI** | Reporting automation |
| **Operations** | KPI definitions; actuals collection |
| **Assets** | Deal analysis; portfolio financial oversight |
| **Projects** | Budget tracking |

---

## Department: Operations

### Mission

Run the day-to-day execution layer of Atlas with discipline — process design, performance monitoring, vendor management, and portfolio operational integration.

### Scope

**In scope:**

- Process design, implementation, optimization
- Vendor and shared services management
- Operational KPI tracking
- Issue resolution and continuous improvement
- Post-acquisition operational integration
- Incident response (operational)

**Out of scope:**

- Portfolio strategy and board governance (Assets)
- Building AI agents (AI)
- Financial close (Finance)
- Strategic priorities (Brain)
- Time-bound transformation projects (Projects — Operations contributes)

See [Company Lifecycle — Integration standards](00_ATLAS_BRAIN.md#integration-standards-acquire--build--integrate).

### Responsibilities

| Responsibility | Output |
|---|---|
| Define and maintain core SOPs | T4 SOP library |
| Operate shared services | Service catalog |
| Monitor operational KPIs | Dashboards |
| Run integration playbooks | Integration scorecards |
| Incident response (ops) | Incident reports |
| Identify automation candidates | Automation intake queue |

### Ownership

| Asset / outcome | Owner |
|---|---|
| Core operational SOPs | Named process owner per SOP |
| Shared vendor relationships | Operations head |
| Integration scorecard process | Operations head |
| Operational KPI definitions | Operations head (Finance validates financial KPIs) |
| Incident response runbook | Operations head |
| Portfolio local ops | Portfolio operator (within Atlas standards) |

### Inputs

- Standards from Brain
- Automation from AI
- Financial KPI targets from Finance
- Integration plans from Assets
- Project handoffs from Projects
- Portfolio operational data

### Outputs

- Process maps and SOPs
- KPI dashboards
- Vendor contracts (operational)
- Integration scorecards
- Incident reports and RCA
- Automation candidate list

### Internal customers

Assets, portfolio operators, Projects, Finance (actuals), Brain (escalations)

### External customers

Vendors; portfolio customers (via portfolio companies)

### KPIs

| KPI | Target |
|---|---|
| SOP coverage for repeated processes | > 95% |
| Integration scorecard completion (on timeline) | 100% |
| Operational incident MTTR | Per severity SLA |
| KPI dashboard freshness | Daily for critical metrics |
| Automation candidate conversion rate | Trending up |

### Decision authority

| Decision type | Authority | Escalation |
|---|---|---|
| Process change (single portfolio) | Portfolio operator | — |
| Process change (cross-portfolio) | Operations head | Brain if standard change |
| Vendor selection (< threshold) | Operations head | — |
| Vendor selection (above threshold) | Operations + Finance | Brain if multi-year |
| Incident containment actions | Incident commander (assigned per runbook) | — |

### Escalation rules

| Trigger | Escalate to |
|---|---|
| Cross-portfolio operational failure | Brain |
| Integration behind schedule (> 2 weeks) | Assets + Projects |
| Vendor failure affecting multiple assets | Brain + Finance |
| Safety / legal operational incident | Brain immediately |

### Interfaces with other departments

| Department | Interface |
|---|---|
| **Brain** | Escalates; receives standards |
| **Knowledge** | Documents processes |
| **AI** | Requests and consumes automations |
| **Finance** | Reports actuals; receives KPI definitions |
| **Assets** | Integration execution |
| **Projects** | Receives handoffs; executes initiatives |

---

## Department: Assets

### Mission

Own the portfolio — build, acquire, hold, and exit businesses and intellectual property where Atlas infrastructure creates durable value.

### Scope

**In scope:**

- Portfolio company management and board-level oversight
- Due diligence and deal execution
- Asset valuation, lifecycle tracking, exit planning
- Integration initiation (with Operations)
- Build-vs-acquire analysis
- Portfolio operator relationship management

**Out of scope:**

- Holding-wide governance (Brain)
- Day-to-day integration execution (Operations)
- Financial close (Finance)
- Venture build project management (Projects — Assets sponsors)

See [Company Lifecycle](00_ATLAS_BRAIN.md#company-lifecycle).

### Responsibilities

| Responsibility | Output |
|---|---|
| Pipeline management | Opportunity briefs |
| Due diligence | DD reports |
| Deal closing / venture launch | Close checklists |
| Board materials and governance | Board packs |
| Exit analysis | Exit memos |
| Portfolio operator performance management | Performance reviews |

### Ownership

| Asset / outcome | Owner |
|---|---|
| Portfolio companies (holding level) | Assets head |
| Individual portfolio company outcomes | Portfolio operator (Assets oversees) |
| Deal pipeline | Named deal owner per opportunity |
| Integration initiation | Assets deal owner → Operations handoff |
| Investment memos (strategic section) | Deal owner |

### Inputs

- Strategic direction from Brain
- Financial models from Finance
- Market research from Knowledge
- Analysis tooling from AI
- Integration capacity from Operations
- Build delivery from Projects

### Outputs

- Investment memos
- Due diligence reports
- Integration plans (initiation)
- Board materials
- Exit analyses
- Portfolio performance summaries

### Internal customers

Brain, Finance, Operations, Projects, portfolio operators

### External customers

Sellers, brokers, co-investors, portfolio company boards, management teams

### KPIs

| KPI | Target |
|---|---|
| Pipeline quality (conversion to close) | Per strategy |
| Integration initiation within SLA | 100% |
| Portfolio company KPI vs plan | Monitored monthly |
| MOIC / IRR by asset | vs hurdle rate |
| Exit discipline (kill losers) | Per capital policy |

### Decision authority

| Decision type | Authority | Escalation |
|---|---|---|
| Pass on opportunity | Deal owner | — |
| Proceed to DD | Deal owner + Finance | — |
| Submit IOI / LOI (below threshold) | Assets head | — |
| Close acquisition / launch venture | Brain + Finance + DR | Required |
| Portfolio operator hire (local) | Portfolio operator + Assets | Brain if sets precedent |
| Exit recommendation | Assets head + Finance | Brain + DR |

### Escalation rules

| Trigger | Escalate to |
|---|---|
| Any new asset / venture | Brain (always) |
| Deal terms with irreversible clauses | Brain + Finance |
| Portfolio company crisis | Brain + Operations |
| Strategic fit question | Brain |

### Interfaces with other departments

| Department | Interface |
|---|---|
| **Brain** | Proposes investments; receives direction |
| **Knowledge** | DD research; captures learnings |
| **AI** | Analysis and monitoring tooling |
| **Finance** | Deal models and capital |
| **Operations** | Integration handoff |
| **Projects** | Build and integration projects |

---

## Department: Projects

### Mission

Deliver time-bound initiatives with clear accountability — transforming priorities into shipped outcomes, captured knowledge, and clean handoffs.

### Scope

**In scope:**

- Project intake, triage, prioritization
- Milestone tracking and delivery accountability
- Cross-functional coordination
- Post-project retrospectives
- Resource allocation across initiative portfolio

**Out of scope:**

- Steady-state operations (Operations)
- Strategic priority setting (Brain)
- Permanent team building (departments hire; Projects borrows)
- Portfolio board governance (Assets)

See [Project Lifecycle](00_ATLAS_BRAIN.md#project-lifecycle).

### Responsibilities

| Responsibility | Output |
|---|---|
| Operate intake and triage | Approved / deferred / rejected log |
| Maintain project portfolio view | Status dashboard |
| Assign DRIs and contributors | Project briefs |
| Run milestone reviews | Gate decisions |
| Conduct retrospectives | Retro docs → Knowledge |
| Confirm handoffs | Handoff checklists |

### Ownership

| Asset / outcome | Owner |
|---|---|
| Projects department process | Projects head |
| Individual projects | Project DRI (one per project) |
| Project brief | Project DRI |
| Portfolio prioritization queue | Projects head (priorities from Brain) |

### Inputs

- Priorities from Brain
- Project requests from all departments and portfolio
- Budget envelopes from Finance
- Resource availability from department heads
- Technical builds from AI
- Strategic context from Assets

### Outputs

- Project briefs and plans
- Weekly status reports
- Milestone gate decisions
- Retrospectives
- Handoff packages to owning departments

### Internal customers

All departments; Brain (delivery against priorities); portfolio (transformation initiatives)

### External customers

None directly — external impact via project outcomes

### KPIs

| KPI | Target |
|---|---|
| On-time milestone delivery | > 80% |
| Projects with approved brief before execution | 100% |
| Handoff completion before project close | 100% |
| Retrospective within 5 days of close | 100% |
| Red project escalation to Brain | Within 48 hours of red status |

### Decision authority

| Decision type | Authority | Escalation |
|---|---|---|
| Intake reject / defer | Projects head | — |
| Approve project (within budget envelope) | Projects head + sponsor | — |
| Scope change (material) | Sponsor + Projects head | Brain if strategic |
| Kill project | Sponsor + Projects head | Brain if red |
| Resource conflict across departments | Projects head | Brain |

### Escalation rules

| Trigger | Escalate to |
|---|---|
| Red status (material miss) | Brain within 48 hours |
| Resource conflict unresolvable | Brain |
| Budget overrun above threshold | Finance + Brain |
| Strategic misalignment discovered | Brain + sponsor |

### Interfaces with other departments

| Department | Interface |
|---|---|
| **Brain** | Receives priorities; escalates blockers |
| **Knowledge** | Transfers retrospectives and docs |
| **AI** | Infrastructure project delivery |
| **Finance** | Budget tracking |
| **Operations** | Handoff of stable processes |
| **Assets** | Build and integration projects |

---

## Why Each Department Exists

Each department owns a **non-substitutable layer** of the holding OS. Removing one damages the whole system — not merely reduces capacity.

### Brain — irreplaceable because

Without Brain, Atlas has no coherent **direction or governance**. Portfolio companies revert to independent silos. Decisions become political. Principles become slogans. The holding becomes a traditional financial aggregate.

**Damage if removed:** Strategic drift; inconsistent decisions; inability to enforce standards; AI agents without authoritative policy corpus.

### Knowledge — irreplaceable because

Without Knowledge, Atlas **forgets**. Documentation decays. Decisions are not searchable. Onboarding resets the clock. AI retrieval quality collapses. Due diligence repeats past mistakes.

**Damage if removed:** Institutional amnesia; automation without substrate; operator dependency on tribal lore.

### AI — irreplaceable because

Without AI, Atlas is not **AI-native** — it is a documented traditional holding with higher writing standards. Operational leverage thesis fails. Marginal cost of portfolio growth stays linear.

**Damage if removed:** Manual coordination returns; speed advantage erodes; "automation first" becomes aspirational fiction.

### Finance — irreplaceable because

Without Finance, there is no **economic truth**. Capital allocation becomes narrative. Hurdle rates are ignored. Liquidity surprises become existential. Compliance risk compounds.

**Damage if removed:** Investment discipline collapses; portfolio cannot be measured; escalations lack financial grounding.

### Operations — irreplaceable because

Without Operations, nothing **runs reliably**. Integration stays on slides. SOPs don't exist. Incidents repeat. Portfolio companies never connect to the OS.

**Damage if removed:** Execution variance explodes; integration failures; customer impact from operational chaos.

### Assets — irreplaceable because

Without Assets, Atlas has **nothing to hold**. No portfolio discipline. No deal pipeline. No operator oversight. No lifecycle management. Brain strategy has no asset layer to act on.

**Damage if removed:** Holding company without assets — pure overhead.

### Projects — irreplaceable because

Without Projects, transformation **never finishes**. Initiatives bleed into BAU. No handoffs. No retrospectives. Permanent temporary teams. Roadmap items stall in "ongoing."

**Damage if removed:** Chronic initiative debt; ops teams absorb project work; knowledge never captured at project end.

### The completeness test

Ask: *Can another department absorb this domain without violating ownership principles?*

| Domain | Can absorb? | Why not |
|---|---|---|
| Governance | No | Conflict of interest — executors cannot govern themselves |
| Memory | No | Operators cannot objectively curate their own staleness |
| Automation platform | No | Domain owners lack cross-cutting infra expertise |
| Economic truth | No | Conflicts with deal advocacy (Assets) and spend (Operations) |
| Execution discipline | No | Assets optimizes value; Operations optimizes reliability |
| Portfolio ownership | No | Central function — not divisible by project |
| Initiative delivery | No | BAU consumes transformation without temporary structure |

---

## Reporting Relationships

### Functional vs administrative reporting

Atlas uses **functional reporting** — accountability flows to the department that owns the outcome — not traditional administrative hierarchy.

| Relationship type | Meaning | Example |
|---|---|---|
| **Department membership** | Primary home; career, standards, escalation | Engineer in AI reports to Head of AI |
| **Project assignment** | Temporary; DRI owns delivery | Same engineer on Projects initiative reports to Project DRI for duration |
| **Portfolio assignment** | Assets oversight; local autonomy within standards | Operator embedded in portfolio company |
| **Dotted-line input** | Advisory; no authority over priorities | Finance dotted-line to Operations on KPI definitions |

### Canonical reporting structure

```
                    ┌──────────────────┐
                    │   Brain Lead     │
                    │ (Holding leader) │
                    └────────┬─────────┘
                             │
     ┌───────────┬───────────┼───────────┬───────────┐
     │           │           │           │           │
┌────▼────┐ ┌────▼────┐ ┌────▼────┐ ┌────▼────┐ ┌────▼────┐
│Knowledge│ │   AI    │ │ Finance │ │  Ops    │ │Projects │
│  Head   │ │  Head   │ │  Head   │ │  Head   │ │  Head   │
└─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘
                             │
                      ┌──────▼──────┐
                      │ Assets Head │
                      └──────┬──────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
        ┌─────▼─────┐  ┌─────▼─────┐  ┌─────▼─────┐
        │ Portfolio │  │ Portfolio │  │ Portfolio │
        │ Operator A│  │ Operator B│  │ Operator C│
        └───────────┘  └───────────┘  └───────────┘
```

### Reporting rules

1. **Every operator has one department head** — primary functional home.
2. **Project DRI authority supersedes department priority for project scope only** — not for career or department standards.
3. **Portfolio operators report to Assets for portfolio outcomes** — and to local management for day-to-day product/team leadership where applicable.
4. **Brain lead does not micromanage departments** — escalations and quarterly reviews, not daily task assignment.
5. **No matrix without documentation** — if someone has two bosses, the authority split is written in project brief or role charter.

### Portfolio company reporting

Portfolio operators are **Atlas operators first**, asset leaders second:

- Atlas standards (reporting, decisions, documentation) are non-negotiable — see [Portfolio company autonomy spectrum](00_ATLAS_BRAIN.md#portfolio-company-autonomy-spectrum).
- Local product, hiring execution, and customer relationships remain with portfolio leadership.
- Assets head maintains portfolio-level oversight; Brain sets holding direction.

---

## Ownership vs Execution

### Definitions

| Term | Definition |
|---|---|
| **Ownership** | Accountability for an outcome's quality, timeliness, and improvement over time |
| **Execution** | The work performed to produce the outcome |
| **Owner** | One person accountable — may not perform most execution |
| **Executor / Contributor** | Person or agent performing tasks under owner's direction |

See [Ownership](02_FOUNDING_PRINCIPLES.md#ownership) for philosophical foundation.

### The separation principle

**Owners own outcomes; contributors execute tasks.** Conflating them creates either bottlenecks (owner does everything) or accountability vacuums (everyone executes, nobody owns).

```
Owner (accountable)
  ├── delegates → Contributor A (executes workstream 1)
  ├── delegates → Contributor B (executes workstream 2)
  ├── delegates → Agent X (executes automated steps)
  └── retains → Escalation, quality bar, final decision rights
```

### Ownership without execution

Valid and encouraged when:

- Owner has believability and judgment but limited capacity
- Work is highly parallelizable
- AI agents execute routine steps
- Owner's comparative advantage is coordination and system improvement

**Requirement:** Owner must still understand the outcome well enough to detect failure, accept praise/blame, and improve the system.

### Execution without ownership

Valid as **contribution** — invalid as **assignment**.

| Valid | Invalid |
|---|---|
| "Maria executes the financial model; James owns the investment memo" | "The team owns the integration" |
| "Agent drafts SOP; Operations owner approves and owns compliance" | "AI owns customer support outcomes" |

### Authority must match ownership

See [Ownership counter-examples](02_FOUNDING_PRINCIPLES.md#ownership). If an owner lacks budget, headcount, or decision rights to deliver, ownership is **performative** — fix authority or change owner.

### Handoff of ownership

Ownership transfers require:

1. Written handoff document (outcome state, risks, open items)
2. Named incoming owner acceptance
3. Update to all registries (automation owner, doc metadata, project brief)
4. Knowledge capture of lessons from prior owner

Silent handoffs are organizational bugs.

---

## Single Owner Principle

### Rule

**Exactly one human owner per outcome, system, document, decision, agent, and open issue.**

Not zero. Not two. One.

### What "owner" means

The owner is the **Directly Responsible Individual (DRI)** — the person who:

- Defines success criteria (or accepts inherited criteria)
- Assigns and unblocks contributors
- Makes final calls within their authority band
- Escalates when blocked or over threshold
- Captures lessons when outcomes diverge from plan
- Appears by name in metadata, project briefs, and incident records

### Where single owner applies

| Artifact | Owner field location |
|---|---|
| Governance document | Metadata block |
| Playbook / SOP | Document header |
| Project | Project brief `DRI:` field |
| Decision | Decision Record `Owner:` field |
| Agent / automation | Automation registry |
| Open operational issue | Issue tracker `owner:` |
| Portfolio company (holding level) | Assets registry |
| Portfolio outcome | Named portfolio operator |
| Risk mitigation plan | Risk register |

### Committee anti-pattern

Committees **advise**; they do not **own**.

| Pattern | Fix |
|---|---|
| "Steering committee owns the project" | Name one DRI; committee becomes advisory |
| "Brain and Finance co-own capital policy" | Finance owns policy; Brain approves changes |
| "Shared ownership between departments" | Split into two outcomes with two owners, or elevate to one parent outcome with one owner |

### Deputy model

Owners may designate a **deputy** for coverage — but deputy is not co-owner.

- Deputy acts when owner unavailable
- Owner retains accountability
- Deputy named in writing; not implicit

---

## Contributor Model

### Definition

**Contributors** perform work toward an outcome owned by someone else. Contributors may be humans, AI agents, vendors, or portfolio teams.

### Contributor types

| Type | Role | Accountability |
|---|---|---|
| **Human contributor** | Executes assigned workstream | To owner for deliverable quality |
| **AI agent** | Executes defined automation steps | Owner accountable; AI head for platform |
| **Vendor** | Delivers contracted scope | Owner manages vendor; Operations may own vendor relationship |
| **Advisory contributor** | Provides input, no delivery obligation | None beyond honest advice |
| **Cross-department contributor** | Loaned expertise | Home department head aware; project DRI directs |

### Listing contributors

Every project brief and significant initiative lists:

```markdown
**DRI:** [One name]
**Contributors:**
- [Name / Agent ID] — [workstream]
- [Name / Agent ID] — [workstream]
**Advisors:**
- [Name] — [domain]
```

### Contributor rights

- Clarity on scope and deadline
- Access to context required for work — see [Transparency](02_FOUNDING_PRINCIPLES.md#transparency)
- Escalation path when blocked (to DRI, not around DRI)
- Credit in retrospectives and Decision Records where material

### Contributor obligations

- Deliver to defined standard and timeline
- Document work in real time — not at project end
- Flag blockers within 24 hours
- Do not expand scope without DRI approval
- Do not assume ownership without explicit transfer

### AI as contributor

Agents are contributors, never owners. Every agent has a human owner accountable for behavior — see [Agent design standards](00_ATLAS_BRAIN.md#agent-design-standards).

---

## Decision Authority

### Authority layers

Atlas decision authority flows through four layers — see [Principle Hierarchy](02_FOUNDING_PRINCIPLES.md#principle-hierarchy):

```
Principles → Decision Rules → Process Owners → Executors
```

Organization implements **who decides at each layer**.

### Authority bands

| Band | Scope | Typical holder | Documentation |
|---|---|---|---|
| **L0 — Operational** | Reversible, within SOP, below spend threshold | Process owner, operator | Light or SOP reference |
| **L1 — Departmental** | Affects one department, reversible | Department head | Decision note or DR if material |
| **L2 — Cross-department** | Affects 2+ departments or portfolio | Relevant heads + sponsor | Decision Record required |
| **L3 — Holding** | Strategic, capital, irreversible | Brain + Finance/Assets as needed | Full Decision Framework |
| **L4 — Governance** | Principles, structure, T1 docs | Brain (+ board if applicable) | DR + version bump |

### Default owners by decision type

From [Decision Framework](00_ATLAS_BRAIN.md#decision-framework) — organizational enforcement:

| Decision type | Default owner | Co-owner / input |
|---|---|---|
| Investment / M&A | Assets deal owner | Finance (financial), Brain (strategic approval) |
| New venture / build | Assets sponsor | Projects (delivery), Brain (approval) |
| Capital allocation | Finance head | Brain (policy), Assets (requests) |
| Operational process change | Operations process owner | Knowledge (docs), AI (automation) |
| AI tooling / automation | Agent owner + AI head | Domain owner |
| Documentation standard | Knowledge head | Brain (approval) |
| Project prioritization | Projects head | Brain (priorities) |
| Personnel (department) | Department head | Brain if precedent-setting |
| Principle exception | Brain lead | DR mandatory |

### Believability-weighted input

Disagreement before decision uses **believability** — track record in domain, evidence quality — not rank.

Process:

1. Owner frames decision and options
2. Contributors with relevant believability provide written input
3. Owner decides and documents dissent if any
4. Team aligns externally — [One voice on decisions](00_ATLAS_BRAIN.md#communication-principles)

### Two-way vs one-way doors

See [One-way vs two-way doors](00_ATLAS_BRAIN.md#one-way-vs-two-way-doors).

| Door type | Authority default | Process depth |
|---|---|---|
| Two-way | Delegate to L0–L1 | Minimal DR |
| One-way | L3 minimum | Full framework + Brain |

When uncertain, treat as one-way.

---

## Escalation Authority

### Purpose of escalation

Escalation moves a decision or blocker to the **lowest authority level capable of resolving it** — not to the highest available title.

See [Escalation](00_ATLAS_BRAIN.md#escalation) for Brain defaults; this section defines **organizational mechanics**.

### Escalation is not failure

Escalation triggers exist because **no owner can hold all authority**. Using them is correct behavior. Suppressing them is a [failure mode](#failure-modes).

### Escalation paths by trigger

| Trigger | First escalation | Second escalation | Timeline |
|---|---|---|---|
| Blocked > 48 hours on owned outcome | Department head | Brain if cross-dept | Owner initiates at 48h |
| Spend above department threshold | Finance head | Brain + DR | Before commitment |
| New portfolio asset | Assets head | Brain (always) | Before term sheet |
| Holding-wide standard change | Brain | Board if material | Before rollout |
| Principle exception | Brain | DR + Principles review | Before action |
| Red project status | Projects head + sponsor | Brain | Within 48 hours |
| Operational incident (severity 1) | Incident commander | Brain + comms | Immediate |
| AI guardrail breach | Agent owner | AI head → Brain if external impact | Immediate |
| Liquidity below policy | Finance head | Brain | Same day |
| Ownership dispute | Department heads involved | Brain arbitrates | Within 5 business days |

### Default Brain escalation thresholds

Customize quarterly in [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md); defaults from Brain:

| Trigger | Threshold | Escalate to |
|---|---|---|
| Capital commitment | > defined % of deployable capital | Brain + Finance |
| New portfolio asset | Any acquisition or venture launch | Brain + Assets |
| Holding-wide standard change | Affects 2+ departments | Brain |
| Irreversible commitment | Contract > 12 months, exclusivity, IP transfer | Brain |
| Principle exception | Any deviation from Core Principles | Brain |

### Escalation packet requirements

Escalations without context waste senior attention. Minimum packet:

1. **Problem statement** — one paragraph
2. **Owner** — who owns resolution after escalation
3. **Options** — at least two with trade-offs
4. **Recommendation** — owner's preference
5. **Evidence** — data, precedents from [`06_DECISIONS.md`](06_DECISIONS.md)
6. **Decision needed by** — date and consequence of delay
7. **Authority requested** — specific approval needed

### Escalation anti-patterns

| Anti-pattern | Fix |
|---|---|
| Escalating without recommendation | Owner must recommend |
| Skipping levels to gain speed | Escalate to next level only unless severity 1 |
| Escalating to avoid ownership | Return to owner with authority or reassign ownership |
| Chronic re-escalation of same issue | System fix required — Projects or Operations |

---

## Execution Flow

### End-to-end flow

How intent becomes outcome in Atlas:

```
Strategy (Brain)
    ↓
Priority stack (Brain → Projects)
    ↓
Intake (Projects / department)
    ↓
Decision (owner + framework if needed)
    ↓
Brief / plan (owner + contributors)
    ↓
Execute (contributors + agents)
    ↓
Measure (Finance / Operations KPIs)
    ↓
Review (owner + cadence)
    ↓
Knowledge capture (Knowledge)
    ↓
Handoff to BAU (Operations / Assets / AI)
```

### Flow by work type

#### Strategic initiative

1. Brain sets priority → [`04_ROADMAP.md`](04_ROADMAP.md)
2. Projects triages → brief → DRI assigned
3. Cross-department contributors allocated
4. Weekly status; milestone gates
5. Retrospective → Knowledge
6. Handoff per [Project Lifecycle — Handoff](00_ATLAS_BRAIN.md#handoff)

#### Operational process

1. Operations identifies need or exception pattern
2. Process owner drafts SOP → Knowledge review
3. AI assesses automation candidate
4. Deploy with L2 maturity target
5. KPI monitoring via Finance/Ops dashboards

#### Investment / acquisition

1. Assets identifies opportunity
2. Finance models; Knowledge supports DD
3. Decision Framework → DR → Brain approval
4. Projects may run integration project
5. Operations executes integration scorecard
6. Assets owns steady-state portfolio outcome

#### Incident

1. Operations or domain owner **contains**
2. Incident commander assigned per runbook
3. Communicate per [Incident communication](#incident-communication)
4. Resolve → RCA within 5 business days — [Incident response](00_ATLAS_BRAIN.md#incident-response)
5. Knowledge captures RCA; system fix owned

### Parallelism

Departments execute **in parallel** where interfaces allow. Serial bottlenecks at Brain are failures — Brain decides, not executes.

---

## Accountability Model

### Accountability chain

```
Principles (immutable)
    ↓ inform
Brain (strategy + governance)
    ↓ assigns ownership
Department heads (domain outcomes)
    ↓ delegate
Owners / DRIs (specific outcomes)
    ↓ coordinate
Contributors + agents (execution)
```

### What accountability includes

| Included | Not included |
|---|---|
| Delivering or explaining miss | Punishment for honest bad news |
| System improvement after failure | Personal blame theater |
| Escalating blockers early | Heroics to mask broken systems |
| Documenting decisions and lessons | Perfection on first attempt |
| Measuring against pre-defined metrics | Moving goalposts post-hoc |

See [Human accountability](02_FOUNDING_PRINCIPLES.md#human-accountability).

### Accountability vs blame

Atlas separates **accountability** (forward-looking ownership of improvement) from **blame** (backward-looking punishment).

- Bad news reported early → accountability fulfilled
- Surprises at quarter end → communication failure + accountability gap
- Repeat failures without system fix → owner failed to improve system

### AI and accountability

Humans accountable for all material outcomes — including those primarily executed by AI. "The agent did it" is not an acceptable RCA conclusion.

### Portfolio accountability

Portfolio operators accountable for **asset outcomes within Atlas standards**. Assets head accountable for **portfolio-level performance and lifecycle discipline**. Brain accountable for **whether the portfolio composition matches strategy**.

### Review cadences

From [Operating Philosophy — Continuous improvement](00_ATLAS_BRAIN.md#continuous-improvement-as-a-system):

| Cadence | Accountability review |
|---|---|
| Weekly | Operational metrics; blockers |
| Monthly | Department KPIs; automation ROI |
| Quarterly | Strategic alignment; org review checklist |
| Annually | Portfolio assessment; principle alignment |

---

## Responsibility Matrix

Complete RACI-style matrix. **A** = Accountable (one only), **R** = Responsible (executes), **C** = Consulted, **I** = Informed.

Legend: `●` = Accountable, `R` = Responsible, `C` = Consulted, `I` = Informed, `·` = not involved

### Holding governance

| Outcome | Brain | Knowledge | AI | Finance | Ops | Assets | Projects |
|---|---|---|---|---|---|---|---|
| Mission & principles | ● | C | I | I | I | I | I |
| Strategic priorities | ● | C | C | C | C | C | R |
| T1 document maintenance | ● | R | I | I | I | I | I |
| Decision Records (holding) | ● | R | I | C | C | C | C |
| Cross-dept dispute resolution | ● | C | I | C | C | C | C |
| Org structure changes | ● | C | I | C | C | C | C |

### Capital & finance

| Outcome | Brain | Knowledge | AI | Finance | Ops | Assets | Projects |
|---|---|---|---|---|---|---|---|
| Capital allocation policy | ● | I | I | R | I | C | I |
| Financial close | I | C | R | ● | C | I | I |
| Portfolio unit economics | I | I | C | ● | C | R | I |
| Investment memos | C | C | C | R | I | ● | I |
| Budget enforcement | I | I | I | ● | C | C | C |
| Hurdle rate setting | ● | I | I | R | I | C | I |

### Portfolio & assets

| Outcome | Brain | Knowledge | AI | Finance | Ops | Assets | Projects |
|---|---|---|---|---|---|---|---|
| Deal pipeline | I | C | C | C | I | ● | I |
| Due diligence | I | R | C | R | C | ● | I |
| Acquisition close | ● | I | I | R | I | R | I |
| Portfolio operator performance | C | I | I | C | C | ● | I |
| Integration scorecard | I | C | C | I | ● | R | C |
| Exit decisions | ● | I | I | R | I | R | I |

### Operations & execution

| Outcome | Brain | Knowledge | AI | Finance | Ops | Assets | Projects |
|---|---|---|---|---|---|---|---|
| Core SOP library | C | ● | I | I | R | I | I |
| Shared vendor management | I | C | I | C | ● | C | I |
| Operational KPIs | C | I | C | C | ● | R | I |
| Incident response (ops) | I | R | C | I | ● | C | I |
| Portfolio BAU execution | I | I | C | I | C | ● | I |
| Automation candidate intake | I | I | C | I | ● | I | I |

### Knowledge & documentation

| Outcome | Brain | Knowledge | AI | Finance | Ops | Assets | Projects |
|---|---|---|---|---|---|---|---|
| Documentation standards (T2) | ● | R | C | I | I | I | I |
| Playbook compliance audit | I | ● | I | I | C | C | C |
| Onboarding path | C | ● | I | I | I | I | I |
| Decision log curation | ● | R | I | I | I | I | I |
| Glossary maintenance | ● | R | I | I | I | I | I |
| Research archive | I | ● | C | C | I | C | C |

### AI & automation

| Outcome | Brain | Knowledge | AI | Finance | Ops | Assets | Projects |
|---|---|---|---|---|---|---|---|
| AI strategy | ● | I | R | I | I | I | I |
| Agent design standards | ● | C | R | I | I | I | I |
| Automation registry | I | I | ● | I | C | I | C |
| Individual agent behavior | I | I | C | I | C | C | C |
| Agent owner assignment | I | I | ● | I | R | R | R |
| Model vendor selection | C | I | ● | C | I | I | I |

### Projects & delivery

| Outcome | Brain | Knowledge | AI | Finance | Ops | Assets | Projects |
|---|---|---|---|---|---|---|---|
| Project intake & triage | C | I | I | C | C | C | ● |
| Project DRI assignment | I | I | I | I | I | C | ● |
| Cross-dept resource allocation | ● | I | I | C | C | C | R |
| Milestone gate reviews | C | I | I | C | C | C | ● |
| Retrospectives | I | R | I | I | C | C | ● |
| Handoff to BAU | I | C | C | C | ● | ● | R |

### Risk & compliance

| Outcome | Brain | Knowledge | AI | Finance | Ops | Assets | Projects |
|---|---|---|---|---|---|---|---|
| Strategic risk | ● | I | I | C | I | R | I |
| Financial / compliance risk | C | I | I | ● | I | C | I |
| Operational risk | I | I | C | I | ● | C | I |
| Technical / AI risk | C | I | ● | I | R | I | I |
| Reputational risk | ● | I | I | I | I | R | I |
| Incident RCA | I | R | C | I | ● | C | C |

### Per-department outcome ownership summary

| Department | Primary accountable outcomes |
|---|---|
| **Brain** | Strategy, governance, T1 docs, holding-level decisions, escalation resolution |
| **Knowledge** | Documentation standards, knowledge architecture, decision log structure, onboarding path |
| **AI** | Automation registry, agent platform, AI standards, model vendor relationships |
| **Finance** | Economic truth, capital allocation execution, financial compliance, hurdle rates |
| **Operations** | SOP execution layer, integration ops, vendor ops, operational incidents |
| **Assets** | Portfolio value, deal pipeline, portfolio operators, asset lifecycle |
| **Projects** | Initiative delivery, project portfolio health, handoffs, retrospectives |

---

## Department Interfaces

Formal interfaces between departments. When SLAs slip, escalate per [Escalation Authority](#escalation-authority).

### Brain ↔ all departments

| Direction | Content | Channel | SLA |
|---|---|---|---|
| Brain → dept | Priority changes, standard updates | Written memo + DR if material | 48h acknowledgment |
| Dept → Brain | Escalations | Escalation packet | Per trigger timeline |
| Brain → all | Quarterly review outcomes | Broadcast | Within 1 week of review |

### Knowledge ↔ AI

| Direction | Content | SLA |
|---|---|---|
| Knowledge → AI | Corpus requirements, taxonomy | Spec within 10 business days of request |
| AI → Knowledge | Indexed content, retrieval metrics | Monthly quality report |
| Joint | Staleness automation rules | Quarterly review |

### Finance ↔ Assets

| Direction | Content | SLA |
|---|---|---|
| Assets → Finance | Deal model inputs | 5 business days before IC |
| Finance → Assets | Hurdle analysis, capital availability | 3 business days from complete model |
| Joint | Portfolio performance review | Monthly |

### Operations ↔ AI

| Direction | Content | SLA |
|---|---|---|
| Ops → AI | Automation intake tickets | Response within 3 business days |
| AI → Ops | Deployed automation + runbook | Per project timeline in brief |
| Joint | Automation ROI review | Quarterly |

### Projects ↔ Operations (handoff)

| Direction | Content | SLA |
|---|---|---|
| Projects → Ops | Handoff package (SOP, owner, metrics) | Before project close |
| Ops → Projects | Acceptance or gap list | 5 business days |
| Rejection | Gaps returned to Projects DRI | Resolve before close |

### Assets ↔ Operations (integration)

| Direction | Content | SLA |
|---|---|---|
| Assets → Ops | Integration plan at close | Day 0 |
| Ops → Assets | Weekly scorecard during integration | Weekly for 90 days |
| Ops → Assets | Integration complete sign-off | Per [integration standards](00_ATLAS_BRAIN.md#integration-standards-acquire--build--integrate) |

### Interface failure escalation

If an interface SLA is missed twice consecutively, the receiving department head escalates to Brain for system fix — not interpersonal conflict resolution.

---

## Communication Architecture

Communication is **operational infrastructure** — not culture fluff. See [Communication Principles](00_ATLAS_BRAIN.md#communication-principles); this section defines **organizational channels and protocols**.

### Communication types

Atlas uses five canonical communication types. Each has defined direction, channel, and expectations.

---

### One-way communication

**Definition:** Information flows from sender to receivers without required response.

**Purpose:** Broadcast truth, decisions already made, standards updates, status snapshots.

| Use case | Sender | Channel | Cadence |
|---|---|---|---|
| Strategic priority update | Brain | Brain doc + broadcast | Quarterly |
| Standard / policy change | Brain or dept head | Written memo + changelog | On change |
| Financial dashboard publish | Finance | Dashboard + summary | Monthly |
| Project status report | Project DRI | Written status | Weekly |
| KPI snapshot | Operations | Dashboard | Daily/weekly |

**Rules:**

- One-way does not mean opaque — include **context and rationale** where decisions are involved
- Receivers read async; no meeting required for consumption
- Questions follow **two-way** protocol — not reply-all debates

**Example:** Brain publishes Q3 priority stack in [`04_ROADMAP.md`](04_ROADMAP.md) update. All department heads acknowledge within 48 hours. Questions routed to Brain office hours async thread — not emergency meetings.

**Counter-example:** Announcing a major reorg via one-way Slack message without written rationale, owner map, or Decision Record — creates rumor economy and alignment failure.

---

### Two-way communication

**Definition:** Structured exchange where both parties contribute information toward a decision or resolution.

**Purpose:** Problem-solving, design reviews, believability-weighted input, negotiation of interfaces.

| Use case | Participants | Channel | Output |
|---|---|---|---|
| Decision input | Owner + believable contributors | Written comments on decision doc | Recorded in DR |
| Interface negotiation | Two department heads | Shared doc + optional sync | Signed interface agreement |
| Project scope clarification | DRI + sponsor | Brief comment thread | Brief update |
| Escalation discussion | Owner + escalation target | Escalation packet + call if needed | Decision logged |

**Rules:**

- **Written first** — sync supplements, does not replace, written exchange
- Owner decides after input; contributors do not hold veto unless explicitly granted
- Debate happens **before** decision; see [One voice on decisions](00_ATLAS_BRAIN.md#communication-principles)

**Example:** Finance and Assets negotiate hurdle rate for a new sector via shared memo. Both comment async. Brain decides with DR reference.

**Counter-example:** Twelve-person meeting with no owner, no doc, no outcome — information session masquerading as two-way communication.

---

### Broadcast communication

**Definition:** One-to-many distribution of holding-wide or department-wide information.

**Purpose:** Alignment, transparency, incident awareness, cultural signals.

| Scope | Authority to broadcast | Channel |
|---|---|---|
| Holding-wide | Brain lead only | Official holding channel + Brain doc |
| Department-wide | Department head | Dept channel + dept doc index |
| Project-wide | Project DRI | Project status channel |
| Incident (severity 1–2) | Incident commander | Incident channel + template |

**Rules:**

- Broadcasts are **factual and actionable** — what happened, what changes, what receivers should do
- No broadcast for information that belongs in a dashboard
- Sensitive personnel matters — restricted broadcast per policy; never public Slack

**Example:** Brain broadcasts quarterly review summary: priorities, org changes, capital posture. Links to full doc.

**Counter-example:** Department head broadcasts holding-wide strategic pivot — bypasses Brain; creates conflicting narratives.

---

### Decision communication

**Definition:** Communication of a **decided** outcome with rationale, owners, and next actions.

**Purpose:** Convert decision into aligned execution; create precedent for [`06_DECISIONS.md`](06_DECISIONS.md).

**Protocol:**

1. Decision owner publishes Decision Record (or decision section in project brief)
2. Required fields per [Documentation Standards](00_ATLAS_BRAIN.md#documentation-standards)
3. Notify affected parties within 24 hours
4. **One voice** — dissent recorded in DR, not relitigated in channels
5. Success metrics and review date included

| Decision size | Communication depth |
|---|---|
| L0–L1 | Decision note to affected team |
| L2 | Decision Record + dept heads |
| L3–L4 | DR + Brain broadcast + [`06_DECISIONS.md`](06_DECISIONS.md) entry |

**Example:** DR-2026-014: Acquire Company X — published to Assets, Finance, Operations, Brain. Integration owner named. Review dates at 30/90/180 days.

**Counter-example:** Verbal "we decided yes" in hallway; three teams execute incompatible versions.

---

### Incident communication

**Definition:** Time-sensitive communication when risk materializes — operational, financial, technical, reputational.

**Purpose:** Contain damage, align response, satisfy [Bad news fast](00_ATLAS_BRAIN.md#communication-principles).

**Severity levels:**

| Level | Definition | Comms lead | Brain notify |
|---|---|---|---|
| **S1 — Critical** | Revenue, customer, legal, safety impact | Incident commander | Immediate |
| **S2 — Major** | Material internal impact, recoverable | Incident commander | Within 4 hours |
| **S3 — Minor** | Localized, contained | Process owner | Weekly summary |
| **S4 — Near miss** | No impact; learning opportunity | Process owner | Retro only |

**Protocol (S1–S2):**

1. **Contain** — immediate action; stop bleeding
2. **Notify** — incident channel + affected dept heads
3. **Status updates** — every 60 minutes until stable (S1) or every 4 hours (S2)
4. **Brain briefing** — S1 within 1 hour; S2 within 4 hours
5. **Resolution announcement** — what fixed, what remains
6. **RCA** — within 5 business days; Knowledge archives

See [Incident response](00_ATLAS_BRAIN.md#incident-response).

**Example:** Payment processor outage (S1). Operations incident commander owns comms. Customer-facing portfolio notified. Brain briefed at T+45 minutes. Hourly updates until resolved.

**Counter-example:** Engineer fixes production silently; Finance discovers revenue gap days later — communication and accountability failure.

---

### Communication channel map

| Purpose | Primary channel | Backup |
|---|---|---|
| Strategic direction | Brain documents | Quarterly review sync |
| Project status | Written status doc | — |
| Operational issues | Issue tracker + escalation | Incident channel if S1–S2 |
| Decision records | [`06_DECISIONS.md`](06_DECISIONS.md) | DR in project folder |
| Portfolio performance | Finance dashboard | Board materials |
| Knowledge sharing | Knowledge base | — |
| Urgent blocker | Direct message to owner → escalation | Sync call if unresolved 24h |

See [Communication channels by purpose](00_ATLAS_BRAIN.md#communication-channels-by-purpose).

---

## Synchronous vs Asynchronous Work

### Default: async first

Atlas defaults to **asynchronous work** — written artifacts consumable on any schedule, in any timezone, by humans and agents.

See [Async first](00_ATLAS_BRAIN.md#communication-principles) and [Why Documentation Is Infrastructure](01_WHY_ATLAS_EXISTS.md#why-documentation-is-infrastructure).

### When sync is appropriate

| Use case | Sync format | Requirements |
|---|---|---|
| Decision with high ambiguity | Video call ≤ 45 min | Pre-read doc mandatory |
| Relationship building | 1:1 | Regular cadence, not status |
| Incident response (S1) | War room / call | Incident commander runs |
| Creative brainstorm (early) | Whiteboard session | Output captured in doc within 24h |
| Believability-weighted debate (deadlocked) | Moderated discussion | Decision logged immediately after |

### When sync is inappropriate

| Anti-use | Async replacement |
|---|---|
| Status updates | Written weekly status |
| Information sharing | Document + broadcast |
| Approval routing | Decision Record workflow |
| Documentation | Write directly |
| "Quick question" that needs context | Thread with full context |

### Meeting standards

From [Meeting standards](00_ATLAS_BRAIN.md#meeting-standards):

- Agenda, owner, desired outcome — or cancel
- Pre-read sent 24 hours ahead for decision meetings
- Notes and decisions logged within 24 hours
- No meeting without explicit reason async failed

### Timezone fairness

- Record all decision meetings
- Rotate inconvenient times quarterly
- **No decision finalized only in sync** without written confirmation

### AI and async

AI agents operate natively async. Human owners review agent outputs on cadence — not necessarily real-time — except for customer-facing S1 paths.

---

## Governance Boundaries

### What Brain governs

| Domain | Brain authority |
|---|---|
| Principles and T1 documents | Exclusive |
| Holding strategy | Exclusive |
| Cross-department ownership disputes | Arbitrates |
| Principle exceptions | Approves (rare) |
| Org structure (7 departments) | Approves changes |
| Capital policy | Sets; Finance executes |
| External holding narrative | Coordinates |

### What departments govern

| Domain | Authority |
|---|---|
| Department playbooks (T3) | Department head |
| SOPs (T4) | Process owner |
| Department hiring (within standards) | Department head |
| Department budget (within envelope) | Department head |
| Agent behavior (within standards) | Agent owner + AI head |

### What portfolio operators govern

| Domain | Authority |
|---|---|
| Product roadmap (aligned) | Portfolio operator |
| Local hiring execution | Portfolio operator |
| Customer relationships | Portfolio operator |
| Local tooling (with rationale) | Portfolio operator |
| Pricing (within strategy) | Portfolio operator |

See [Portfolio company autonomy spectrum](00_ATLAS_BRAIN.md#portfolio-company-autonomy-spectrum).

### Boundary violations

| Violation | Response |
|---|---|
| Department creates shadow T1 policy | Brain invalidates; DR on how it happened |
| Portfolio opts out of financial reporting | Assets + Finance escalation; compliance fix |
| Agent acts outside guardrails | Disable agent; RCA; owner accountability |
| Projects becomes permanent team | Handoff or department hire — Projects closes project |

### Changing governance boundaries

Requires:

1. Written proposal with rationale
2. Impact analysis on all affected departments
3. Decision Record
4. Brain approval
5. Update to this document (version bump)
6. Notification per [Decision communication](#decision-communication)

---

## Management Philosophy

### Management is not the default coordination layer

Atlas manages through **ownership, systems, and documentation** — not through supervisors relaying information.

See [Why Software Is Replacing Management](01_WHY_ATLAS_EXISTS.md#why-software-is-replacing-management).

### Role of department heads

Department heads are **system owners**, not task assigners:

| Do | Don't |
|---|---|
| Own domain outcomes and KPIs | Micromanage contributor tasks |
| Hire and develop judgment | Hire for manual throughput |
| Define and improve department systems | Become bottleneck for all decisions |
| Escalate structural issues to Brain | Resolve chronic issues with heroics |
| Enforce documentation and ownership standards | Accept "the team owns it" |

### Role of portfolio operator

Portfolio operators are **asset CEOs within Atlas standards**:

- Full accountability for asset outcomes
- Access to holding OS (AI, Knowledge, Finance, Operations)
- Must comply with reporting, decision, and documentation standards
- Not micromanaged by Assets unless performance or compliance gap

### Management density by scale

Management **headcount does not scale linearly** with organization size — systems do. See [Organizational Scaling](#organizational-scaling).

### Performance management

Performance evaluates:

1. **Outcomes vs metrics** agreed in advance
2. **System improvement** — did the person make the org stronger?
3. **Principle alignment** — see [Founding Principles](02_FOUNDING_PRINCIPLES.md)
4. **Ownership behavior** — escalation, documentation, handoffs

Not evaluated: hours visible, meeting attendance, political alignment.

---

## Leadership Expectations

### All leaders (department heads, DRIs, portfolio operators)

| Expectation | Standard |
|---|---|
| **Own outcomes** | Name appears on metrics; no diffused blame |
| **Write** | Decisions and plans documented before major execution |
| **Escalate early** | Blockers raised within 48 hours |
| **Teach** | Knowledge captured for successors |
| **Automate** | Repeated work becomes system or agent |
| **Truth** | Bad news reported immediately — [Truth over comfort](02_FOUNDING_PRINCIPLES.md#truth-over-comfort) |
| **Principle model** | Behavior visible as example |

### Brain lead expectations

- Maintain coherence across Brain documents
- Make holding-level calls when departments deadlock
- Protect principles from short-term pressure
- Say no to strategic distractions
- Ensure [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) reflects reality

### Department head expectations

- Domain KPI ownership
- Interface SLAs with peer departments
- Hiring bar enforcement
- No silent standard deviations
- Quarterly department retrospective to Knowledge

### Project DRI expectations

- Brief approved before execution
- Weekly status without reminder
- Milestone gate discipline
- Clean handoff or project not closed
- Retro within 5 days of close

### Portfolio operator expectations

- Asset plan aligned with Brain direction
- Atlas reporting on time
- Integration standards met
- Local team developed; not key-person dependent
- Exit or hold rationale documented when asked

---

## Hiring Philosophy

### What Atlas hires for

From [Staffing philosophy](00_ATLAS_BRAIN.md#staffing-philosophy) and [The new scarce resource](01_WHY_ATLAS_EXISTS.md#the-new-scarce-resource):

| Hire for | Not for |
|---|---|
| Judgment and taste | Task volume capacity |
| Domain expertise with evidence | Generic "management" career |
| System-building and documentation instinct | Heroic firefighting as identity |
| AI fluency and automation mindset | Manual process comfort |
| Ownership temperament | Consensus-seeking without accountability |
| Long-term orientation | Quarterly optics optimization |

### Hiring bar principles

1. **Would this person raise the average?** — If uncertain, no hire.
2. **Believability in domain** — Demonstrated outcomes, not just credentials.
3. **Documentation test** — Can they write how they think? Writing reveals clarity.
4. **Ownership test** — Tell me about something you owned end-to-end, including failure.
5. **Principle fit** — Explicit evaluation against [Founding Principles](02_FOUNDING_PRINCIPLES.md).

### Hiring authority

| Role type | Authority | Escalation |
|---|---|---|
| Department IC | Department head | Brain if new role type |
| Department head | Brain + DR | Board if executive |
| Portfolio local hire | Portfolio operator | Assets informed |
| Contractor / vendor | Process owner + Operations | Finance threshold |

### AI in hiring loops

- AI may screen for structured criteria — not final judgment
- AI generates interview guides from role charter
- **Human owns hire/no-hire** — always
- Bias checks on automated screening quarterly (AI + Brain)

### No hire scenarios

- Hire to "fill seat" without outcome definition
- Hire manager when individual contributor with systems thinking suffices
- Hire duplicate owner for same outcome
- Hire before workflow documented (likely need is automation)

---

## Role Lifecycle

### Stages

```
Define → Charter → Hire → Onboard → Operate → Develop → Transition → Close
```

### 1. Define

- Outcome needed (not just "headcount")
- Single owner for the role's outcomes defined
- Success metrics at 30/90/180 days
- Authority band (L0–L4)
- Budget approval from Finance

### 2. Charter

Role charter (T3) minimum fields:

```markdown
**Role:** [Title]
**Department:** [Dept]
**Reports to:** [Name]
**Outcome owned:** [One sentence]
**Success metrics:** [Measurable]
**Authority band:** [L0–L4]
**Interfaces:** [Departments / roles]
**Review date:** [YYYY-MM-DD]
```

### 3. Hire

Per [Hiring Philosophy](#hiring-philosophy).

### 4. Onboard

Per [Onboarding](#onboarding).

### 5. Operate

- Quarterly role review against charter
- Owner updates charter if scope shifts (Brain approval if L2+ authority change)

### 6. Develop

- Expand believability, not just scope
- System-building contributions to Knowledge
- Cross-department project exposure via Projects

### 7. Transition

- Promotion: new charter, explicit ownership transfer
- Lateral: ownership map updated
- Departure: [Offboarding](#offboarding)

### 8. Close

- Role eliminated when outcome automated or no longer strategic
- Automation or handoff documented before role closes
- No zombie roles — if charter unjustifiable, close role

---

## Onboarding

### Purpose

Onboard operators into **Atlas the OS** — not just a job description.

### Standard path (all operators)

From [Onboarding knowledge path](00_ATLAS_BRAIN.md#onboarding-knowledge-path):

| Day | Activity | Owner |
|---|---|---|
| 0–1 | Access provisioning (systems, knowledge base, dashboards) | Operations + IT |
| 1–3 | Read `00_ATLAS_BRAIN.md`, `01_WHY_ATLAS_EXISTS.md`, `07_GLOSSARY.md` | New operator |
| 3–5 | Read `02_FOUNDING_PRINCIPLES.md` (skim + deep on relevant principles) | New operator |
| 5–7 | Read `03_ORGANIZATION.md` + department charter | New operator |
| 7–10 | Read [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md), [`04_ROADMAP.md`](04_ROADMAP.md) | New operator |
| 10–15 | Department playbooks + assigned buddy sessions | Department head |
| 15–30 | First owned task with documented outcome | Manager / DRI |

### Onboarding checklist (operator)

- [ ] All system access granted and logged
- [ ] Brain reading path complete — quiz or summary doc optional per dept
- [ ] Department charter understood; owner named for operator's outcomes
- [ ] Met interface partners from adjacent departments
- [ ] First week status doc published by operator
- [ ] 30-day success metrics agreed in writing
- [ ] Added to relevant dashboards and communication channels
- [ ] Agent / automation tools provisioned (AI department)

### Onboarding checklist (manager)

- [ ] Role charter published before day 0
- [ ] Buddy assigned
- [ ] First owned outcome defined (not "shadow only")
- [ ] 30/90-day metrics in writing
- [ ] Intro to cross-department interfaces scheduled async
- [ ] Knowledge base "start here" link set for role

### Portfolio operator onboarding

Additional requirements:

- [ ] Integration scorecard status reviewed
- [ ] Assets intro and reporting calendar
- [ ] Atlas financial reporting walkthrough (Finance)
- [ ] Portfolio-specific playbook in Knowledge
- [ ] Board / governance expectations documented

### AI-assisted onboarding

- AI tutor mode on Brain docs — Q&A with citations
- Personalized reading list based on role charter
- **Human buddy validates understanding** — AI does not certify completion alone

---

## Offboarding

### Purpose

Preserve knowledge; close access; transfer ownership cleanly.

### Triggers

- Voluntary departure
- Role elimination
- Performance transition
- Contractor end

### Offboarding checklist

**Knowledge (before last day):**

- [ ] Ownership registry updated — all outcomes have new owner
- [ ] Handoff doc for each owned outcome, system, agent, doc
- [ ] Open issues reassigned in tracker
- [ ] Decision Records updated if owner field affected
- [ ] Retro on systems only this person knew — fix single-point-of-failure

**Access (last day or before):**

- [ ] All system access revoked
- [ ] API keys and agent credentials rotated
- [ ] Portfolio and vendor contacts notified of new owner

**Legal / Finance:**

- [ ] HR/offboarding checklist complete
- [ ] Equipment return
- [ ] Final expenses

**Knowledge archive:**

- [ ] Exit interview notes to Knowledge (patterns, not gossip)
- [ ] Lessons added to playbooks if applicable

### Emergency offboarding

Immediate access revocation; Brain notified; interim owner named within 4 hours for critical outcomes.

---

## AI Participation Inside Departments

### Model

AI participates **inside** every department as:

- **Executor** — automates routine steps
- **Augmenter** — drafts, analyzes, summarizes
- **Monitor** — flags anomalies against criteria
- **Router** — directs work to correct owner

AI does **not**:

- Own outcomes
- Approve one-way doors without human
- Override principles
- Become silent decision-maker

See [AI Strategy](00_ATLAS_BRAIN.md#ai-strategy) and [Human accountability](02_FOUNDING_PRINCIPLES.md#human-accountability).

### Department-by-department AI roles

| Department | AI participation |
|---|---|
| **Brain** | Strategy research drafts; decision precedent retrieval; principle conflict flagging |
| **Knowledge** | Indexing, staleness detection, summarization, onboarding tutor |
| **AI** | Self-hosting platform; eval pipelines; meta-automation |
| **Finance** | Reconciliation, variance analysis, forecast drafts, anomaly detection |
| **Operations** | SOP execution assist; incident triage; vendor ticket routing |
| **Assets** | DD document analysis; portfolio monitoring; comp benchmarking |
| **Projects** | Status synthesis; risk flagging; resource conflict detection |

### Maturity expectations

Default target: **L2 supervised automation** within 90 days of process stabilization — [AI maturity model](00_ATLAS_BRAIN.md#ai-maturity-model).

### Guardrails

Every department agent follows [Agent design standards](00_ATLAS_BRAIN.md#agent-design-standards). Department heads audit agent roster quarterly.

### Human + AI team composition

Prefer **one human owner + N agents** over **N humans doing manual work** when:

- Task is repeated and specifiable
- Error cost is below human review threshold
- Data access is policy-compliant

Prefer **human execution** when:

- Novel judgment
- High-stakes irreversible
- Relationship-critical
- Ethical nuance

---

## Organizational Scaling

The **seven departments are invariant**. Staffing, sub-teams, and interface complexity scale — principles and structure do not.

See [How the organization changes without changing principles](#scaling-without-changing-principles).

---

### Stage 0: One operator

**Profile:** Founder / holding lead; possibly zero employees.

| Department | Reality at scale |
|---|---|
| All seven | One person wears all hats — but **still labels work by department** in docs |
| Brain | This document + Brain docs ARE the org |
| Execution | Heavily AI-augmented; contractors for specialized spikes |

**Structural rules even at one:**

- Still assign **single owner** on every outcome — even if owner is the same human
- Still write Decision Records for material calls
- Still separate **project** work from **BAU** in briefs
- Do not skip metadata blocks — future you is the next operator

**Primary risk:** Implicit knowledge in founder's head. **Mitigation:** Extreme documentation as forcing function.

**Example:** Solo operator launches first acquisition. Assets owner = self. Operations integration checklist still executed. DR-2026-001 logged.

---

### Stage 1: ~10 people

**Profile:** One human per core department (or dual-hatted); first portfolio asset live.

| Change | Implementation |
|---|---|
| Department heads named | Each dept has one head; may still be IC |
| Role charters published | T3 docs for each seat |
| Interface SLAs activate | Peer dept heads acknowledge |
| Projects formalized | First dedicated Project DRI likely part-time |
| AI registry | First production agents with named owners |

**Reporting:** Flat — all dept heads report to Brain lead.

**Primary risk:** Dual-hatting causes ownership confusion. **Mitigation:** When acting as Finance vs Assets, **label hat in writing**.

**Example:** Head of Finance closes books (Finance hat) then evaluates deal (input to Assets DRI — not implicit owner of both without documenting).

---

### Stage 2: ~50 people

**Profile:** Multiple ICs per department; 3–8 portfolio assets; integration playbook proven.

| Change | Implementation |
|---|---|
| Sub-teams emerge | e.g., AI Platform vs AI Embedded; Ops Integration vs Ops Shared Services |
| Portfolio operators | Dedicated per asset or cluster |
| Projects team | 2–4 DRIs running parallel initiatives |
| Knowledge function | Dedicated curation; staleness automation live |
| Escalation volume | Brain filters via dept heads — not individual IC escalations |

**Reporting:** Dept heads → Brain lead. Sub-team leads → dept head. Portfolio operators → Assets head.

**Primary risk:** Department silos forming. **Mitigation:** Quarterly cross-dept project mandatory; interface SLA reviews.

**Example:** AI sub-team builds cross-portfolio agent template; Operations owns embedding per asset with local SOP tweaks documented.

---

### Stage 3: ~200 people

**Profile:** Full department benches; international portfolio; holding OS mature.

| Change | Implementation |
|---|---|
| Deputy dept heads | Coverage and development path |
| Regional Operations pods | Assets-aligned; standards centralized |
| Finance controller layer | Consolidation; portfolio reporting automated |
| Brain chief of staff | Filters escalation; owns quarterly review process |
| Governance council | **Advisory only** — not ownership committee |

**Reporting:** Two layers under dept heads max before ICs. Third layer triggers reorg review.

**Primary risk:** Middle coordination layer creep. **Mitigation:** Any new "manager" role requires charter proving **system ownership**, not relay function.

**Example:** Regional Ops pod lead owns integration SLA for EU assets — not "manager of managers" without outcomes.

---

### Stage 4: 1000+ people

**Profile:** Multi-sector portfolio; Atlas OS licensed or replicated patterns; generational leadership transition.

| Change | Implementation |
|---|---|
| Holding + portfolio legal entities | Clarity on which standards apply where |
| Brain succession documented | Principles and Brain docs are the continuity plan |
| Automation majority | L3+ on most repeated holding workflows |
| Knowledge as product | Internal retrieval infrastructure powers all operators |
| Minimal Brain headcount | Governance scales via docs and decision precedents |

**Invariant at 1000+:**

- Still seven departments at holding level
- Still single owner per outcome
- Still Brain executes strategy via organization — not via empire of coordinators

**Primary risk:** Bureaucratic regression — layers recreating management middleware. **Mitigation:** Annual "coordination tax audit" — count relay roles vs owner roles.

**Example:** 1000-person Atlas acquires in new sector. Integration still follows scorecard; local playbooks extend T3 — no new department without Brain DR.

---

## Scaling Without Changing Principles

### What scales

| Element | How it scales |
|---|---|
| Headcount | Sub-teams within departments |
| Portfolio assets | More portfolio operators; Assets clusters |
| Projects | More parallel DRIs |
| Automations | Agent templates across portfolio |
| Knowledge | Corpus size; retrieval sophistication |
| Decision precedents | [`06_DECISIONS.md`](06_DECISIONS.md) depth |

### What does not scale (invariant)

| Element | Invariant |
|---|---|
| Seven departments | No eighth without Brain DR |
| Single owner principle | Never "co-own" |
| Brain as strategy source | No shadow strategy |
| Principles | [Founding Principles](02_FOUNDING_PRINCIPLES.md) immutable layer |
| Documentation before execution | More important at scale, not less |
| Human accountability for material outcomes | Always |

### Adaptation mechanism

When scale exposes friction:

1. **First:** Fix process, automation, or interface SLA
2. **Second:** Add sub-team or specialist role with charter
3. **Third:** Adjust decision threshold in [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md)
4. **Last:** Propose structural change to Brain — never informal reorg

---

## Organizational Anti-Patterns

| Anti-pattern | Symptom | Fix |
|---|---|---|
| **Management middleware** | Managers who only relay status | Eliminate role; replace with dashboards + ownership |
| **Committee ownership** | Slow decisions; nobody accountable | Name one DRI |
| **Hero culture** | Same person firesaves repeatedly | Document system; automate; rotate ownership |
| **Meeting as workflow** | Calendar full; docs empty | Async status; meetings for decisions only |
| **Shadow governance** | Real decisions happen outside Brain | Surface and document or stop |
| **Org chart in stealth** | "Ask Sarah, she knows" | Update this doc and role charters |
| **Project permanence** | Projects team becomes second Operations | Handoff discipline |
| **Knowledge in Slack** | Answers lost in threads | Capture to Knowledge base |
| **AI without owner** | Agent runs unsupervised | Disable until owner named |
| **Portfolio silo** | Asset ignores holding standards | Assets escalation; compliance fix |
| **Title as authority** | VP overrides domain believability | Return to evidence and principles |
| **Escalation punishment** | Bad news hidden until crisis | Celebrate early escalation |
| **Duplicate Brain** | Dept writes competing "strategy" | Redirect to Brain process |
| **Hiring ahead of workflow** | Three people, no SOP | Document; automate; then hire |
| **Reorg as performance fix** | Boxes shuffle; systems unchanged | Fix systems first |

---

## Failure Modes

Organizational failure modes — detect early via [Organization Review Checklist](#organization-review-checklist).

### FM-01: Ownership vacuum

**Signal:** Recurring misses; "not my job" disputes; stale issues with no owner field.

**Root cause:** Assignment without single owner; committee culture.

**Recovery:** Ownership audit; name DRIs; update registries.

---

### FM-02: Brain bypass

**Signal:** Departments execute conflicting strategies; operators cite different priorities.

**Root cause:** Shadow decisions; stale [`04_ROADMAP.md`](04_ROADMAP.md).

**Recovery:** Brain priority refresh; DR on conflicts; comms broadcast.

---

### FM-03: Integration debt

**Signal:** Acquired assets never reach integration scorecard thresholds.

**Root cause:** Operations capacity; no Projects handoff; Assets closes deal and moves on.

**Recovery:** Dedicated integration project; weekly Brain visibility until green.

---

### FM-04: Knowledge rot

**Signal:** Staleness > 20%; operators rebuild known solutions; AI retrieval quality drops.

**Root cause:** Knowledge understaffed; no owner review cadence.

**Recovery:** Staleness sprint; enforce metadata review dates; automate flags.

---

### FM-05: Automation orphanage

**Signal:** Broken agents; nobody fixes; manual workaround persists silently.

**Root cause:** No agent owner; AI built without Operations adoption.

**Recovery:** Registry audit; disable orphans; redeploy with owner + SOP.

---

### FM-06: Project swamp

**Signal:** Many "ongoing" projects; no handoffs; BAU team overloaded.

**Root cause:** Projects closes without handoff acceptance; weak milestone gates.

**Recovery:** Kill or close projects; enforce handoff SLA; Brain review of portfolio.

---

### FM-07: Capital narrative drift

**Signal:** Investments clear verbally but not hurdle rate; dry powder silently depleted.

**Root cause:** Finance escalation thresholds not enforced.

**Recovery:** Finance + Brain audit; retroactive DR if needed; threshold reset.

---

### FM-08: Coordination tax explosion

**Signal:** Headcount up; output flat; meeting hours per operator up > 20% YoY.

**Root cause:** Hiring managers instead of systems; interface SLAs missing.

**Recovery:** Coordination tax audit; cut relay roles; automate status.

---

### FM-09: Key person dependency

**Signal:** One departure threatens asset or system; undocumentable tribal knowledge.

**Root cause:** Ownership without documentation; hero rewards.

**Recovery:** Cross-train; document; split ownership with deputies; automate.

---

### FM-10: Principle exception creep

**Signal:** Frequent "just this once" deviations; precedents contradict principles.

**Root cause:** Brain not logging exceptions; short-term pressure.

**Recovery:** Principle audit; DR for each exception; public reset if needed.

---

## Practical Examples

### Example 1: Cross-department automation

**Situation:** Monthly portfolio KPI report takes Finance analyst 3 days.

**Flow:**

1. Finance owner files automation intake → Operations queue → AI
2. AI builds L2 pipeline; Finance owner accountable
3. Knowledge documents report spec
4. Operations embeds in monthly close SOP
5. ROI tracked in automation registry

**Outcome:** 3 days → 2 hours review; template reused for new assets.

---

### Example 2: Acquisition integration

**Situation:** Atlas acquires SaaS company; 45-day integration clock starts.

**Flow:**

1. Assets closes deal (DR approved by Brain)
2. Projects spins integration project; DRI named
3. Operations runs scorecard; AI audits top 5 automation candidates
4. Knowledge captures company overview day 14
5. Finance maps chart of accounts day 30
6. Handoff to Assets portfolio operator at day 90

---

### Example 3: Red project recovery

**Situation:** Infrastructure project 6 weeks late; budget +40%.

**Flow:**

1. Projects DRI marks red; escalates to Brain within 48h
2. Escalation packet: continue / re-scope / kill options
3. Brain decides re-scope; DR logged
4. Brief updated; Finance adjusts envelope
5. Retro captures planning failure modes → Knowledge

---

### Example 4: Solo operator first hire

**Situation:** Founder hires first Head of Finance at ~8 people equivalent workload.

**Flow:**

1. Role charter published — owns economic truth, not "help with spreadsheets"
2. Onboarding path through Brain docs
3. First owned outcome: clean monthly close + dashboard by day 60
4. Founder relinquishes Finance **hat** explicitly in writing

---

### Example 5: Incident with AI guardrail breach

**Situation:** Customer support agent sends incorrect refund offer.

**Flow:**

1. Operations incident commander (S2)
2. Agent disabled; owner notified
3. Customer comms from portfolio operator
4. RCA: prompt gap; Knowledge updates agent spec
5. AI promotes fix; owner validates before re-enable

---

## Counter-Examples

### Counter-example 1: The steering committee

**Wrong:** "Integration steering committee owns post-acquisition success" — six VPs meet weekly.

**Right:** Projects DRI owns integration outcome; committee members are **contributors** with weekly async input.

---

### Counter-example 2: Brain duplication

**Wrong:** Operations publishes "Atlas Operational Strategy 2026" defining portfolio priorities.

**Right:** Operations publishes **SOPs and KPI definitions**; priorities cite [`04_ROADMAP.md`](04_ROADMAP.md).

---

### Counter-example 3: Shared ownership

**Wrong:** "Finance and Assets co-own the deal."

**Right:** Assets owns deal outcome; Finance owns model accuracy and capital compliance input.

---

### Counter-example 4: Meeting-driven project

**Wrong:** Daily standups replace written status; no brief; no DRI.

**Right:** Weekly written status; brief with DRI; meetings only at milestone gates.

---

### Counter-example 5: Hire the hero

**Wrong:** Hire legendary firefighter who "just gets things done" without documentation.

**Right:** Hire operator who built systems that **eliminated** need for firefighting; verify with references.

---

### Counter-example 6: Permanent war room

**Wrong:** S1 incident resolved but war room continues for weeks as coordination habit.

**Right:** Incident closed; RCA within 5 days; ongoing work becomes owned project or BAU SOP.

---

## Operational Checklists

### New department interface checklist

When two departments establish a new recurring interface:

- [ ] Named owners on both sides
- [ ] Inputs, outputs, format documented
- [ ] SLA agreed and published
- [ ] Escalation path if SLA missed
- [ ] Linked from both department playbooks
- [ ] Review date set (quarterly)

---

### New project launch checklist

- [ ] Brain priority reference or sponsor approval
- [ ] Project brief approved (T3)
- [ ] Single DRI named
- [ ] Contributors listed
- [ ] Budget in Finance envelope
- [ ] Success metrics and review dates
- [ ] Handoff destination identified
- [ ] Milestone gates scheduled

---

### New agent deployment checklist

- [ ] Human owner named
- [ ] Agent spec complete per [Agent design standards](00_ATLAS_BRAIN.md#agent-design-standards)
- [ ] Guardrails and fallback defined
- [ ] SOP reference linked
- [ ] Registered in automation registry
- [ ] Maturity level set (default L1→L2)
- [ ] Evaluation metrics baselined

---

### Acquisition close checklist (organizational)

- [ ] DR approved by Brain
- [ ] Portfolio operator or plan named
- [ ] Integration project DRI named
- [ ] Operations scorecard instantiated
- [ ] Knowledge company overview template assigned (14-day SLA)
- [ ] Finance reporting mapping started (30-day SLA)
- [ ] Communication plan: internal and external

---

### Weekly department head checklist

- [ ] Review domain KPI dashboard
- [ ] Unowned issues > 24h — assign or escalate
- [ ] Interface SLA misses — peer head sync async
- [ ] Escalations to Brain — packet complete?
- [ ] Documentation staleness flags — triaged
- [ ] Automation candidates — submitted if any

---

### Quarterly org health checklist

See [Organization Review Checklist](#organization-review-checklist) for full version.

---

## Organization Review Checklist

Run **quarterly** — owner: Brain lead with input from all department heads. Results summarized in quarterly review doc and [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) if material.

### Structure & ownership

- [ ] All seven departments have named head (or explicit dual-hat doc)
- [ ] Every active project has single DRI
- [ ] Every production agent has human owner
- [ ] Every T1–T3 doc has metadata owner and review date current
- [ ] No outcomes owned by "team" or committee without named DRI
- [ ] Role charters current for all department heads

### Authority & escalation

- [ ] Escalation thresholds match [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md)
- [ ] No chronic re-escalations unresolved > 2 quarters
- [ ] Brain bypass incidents reviewed and fixed
- [ ] Principle exceptions logged in [`06_DECISIONS.md`](06_DECISIONS.md)

### Interfaces & communication

- [ ] Department interface SLAs reviewed; misses addressed
- [ ] Meeting load per operator — trending stable or down
- [ ] Decision Records published within 24h of L2+ decisions
- [ ] S1/S2 incidents had compliant comms timelines

### Execution & delivery

- [ ] Project portfolio health: red projects have Brain visibility
- [ ] Handoff SLA compliance from Projects to Operations
- [ ] Integration scorecards on track for active acquisitions
- [ ] Automation registry reviewed by AI (quarterly)

### Knowledge & systems

- [ ] Document staleness rate < 10%
- [ ] Onboarding path updated for org changes
- [ ] Orphan automations = 0
- [ ] Key person dependency risks documented with mitigation

### People & scaling

- [ ] Hiring aligned to role charters — no seat-filling
- [ ] Offboarding handoffs complete for all departures in quarter
- [ ] Coordination tax indicators (meetings/headcount) acceptable
- [ ] Scale stage playbook matches current headcount band

### Output

- [ ] Action items assigned with single owners and dates
- [ ] Structural changes (if any) proposed via DR
- [ ] Cross-references updated in this document if org changed

---

## Cross References

This document is the **structural layer** of Atlas. Sibling documents provide strategy, philosophy, state, and vocabulary — **link rather than duplicate**.

### Relationship to every Brain document

| Document | Relationship |
|---|---|
| [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) | **Parent OS reference.** Brain defines mission, principles summary, decision framework, department overview, AI strategy, knowledge standards, lifecycles, and communication principles. **This document operationalizes** [Organizational Architecture](00_ATLAS_BRAIN.md#organizational-architecture) with ownership, authority, interfaces, scaling, and people systems. Brain points here for "reporting lines, roles, and staffing plans." |
| [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md) | **Philosophical foundation.** Explains *why* departments replace management layers and *why* software absorbs coordination. Read for conviction; this doc reads for **structure**. See especially [Why Software Is Replacing Management](01_WHY_ATLAS_EXISTS.md#why-software-is-replacing-management) and [Why Atlas Is Built as an Operating System](01_WHY_ATLAS_EXISTS.md#why-atlas-is-built-as-an-operating-system-instead-of-a-company). |
| [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md) | **Judgment infrastructure.** Principles govern organizational behavior — especially [Ownership](02_FOUNDING_PRINCIPLES.md#ownership), [Transparency](02_FOUNDING_PRINCIPLES.md#transparency), [Human accountability](02_FOUNDING_PRINCIPLES.md#human-accountability), [Systems over heroes](02_FOUNDING_PRINCIPLES.md#systems-over-heroes). Organization **manifests** principles in roles and authority — does not restate rationale. |
| [`03_ORGANIZATION.md`](03_ORGANIZATION.md) | **This document.** Canonical source for organizational operating system. |
| [`04_ROADMAP.md`](04_ROADMAP.md) | **Strategic direction.** Roadmap sets priorities that Projects sequences and departments staff against. Organization executes roadmap — does not replace it. Priority changes trigger [Decision communication](#decision-communication). |
| [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) | **Present snapshot.** Current headcount band, named department heads, active threshold values, and temporary org emphases. **Updates quarterly**; this document defines invariant structure. |
| [`06_DECISIONS.md`](06_DECISIONS.md) | **Decision precedents.** Organizational changes, escalations resolved, and authority disputes leave traces here. DRIs and Brain cite precedents when applying [Decision Authority](#decision-authority). |
| [`07_GLOSSARY.md`](07_GLOSSARY.md) | **Shared vocabulary.** Terms used here (DRI, holding OS, one-way door, believability, etc.) defined canonically in Glossary. Propose new terms via Knowledge → Brain. |

### Relationship to Principles

| Principle | Organizational expression in this document |
|---|---|
| Long-term thinking | Role lifecycle; scaling stages; no structural churn for short-term fixes |
| Truth over comfort | Incident communication; escalation rewarded |
| Evidence over opinion | Believability-weighted input; decision packets |
| Systems over heroes | Management philosophy; anti-patterns |
| Compounding over optimization | Knowledge interfaces; automation ownership |
| Ownership | Single Owner Principle; Responsibility Matrix |
| Transparency | Communication architecture; async default |
| Extreme documentation | Onboarding path; role charters; handoffs |
| AI-first thinking | AI participation by department |
| Automation by default | Agent ownership; scaling via automation not headcount |
| Simple before complex | Seven departments invariant; sub-teams before new departments |
| Reversible decisions | Authority bands L0–L1 delegation |
| Human accountability | AI as contributor never owner |
| Capital efficiency | Finance interfaces; hiring philosophy |
| Integrity | Governance boundaries; no shadow Brain |
| Optionality | Scaling without principle changes |
| Continuous improvement | Quarterly org review checklist |
| Knowledge compounds | Knowledge department interfaces; offboarding capture |
| Build before buy | AI and Knowledge as internal capabilities |
| Acquire when leverage exists | Assets + Operations integration flow |
| Data before intuition | KPI ownership per department |
| Action over perfection | Project handoff with documented gaps allowed |
| One source of truth | This doc for org; Brain for strategy; no duplication |

See [Principle-to-document map](02_FOUNDING_PRINCIPLES.md#cross-references).

### Relationship to Decisions

- Organizational structure changes → Decision Record required
- Escalation resolutions that set precedent → log in [`06_DECISIONS.md`](06_DECISIONS.md)
- Ownership disputes arbitrated by Brain → DR with ownership table update
- Principle exceptions → DR + Brain approval per [Governance Boundaries](#governance-boundaries)

### Relationship to Roadmap

| Roadmap element | Organizational response |
|---|---|
| New portfolio sector | Assets capacity; portfolio operator charter |
| Holding OS capability build | Projects + AI/Knowledge staffing |
| Geographic expansion | Operations regional pod (Stage 3+) |
| Headcount plan | Scale stage playbook band |
| Deprioritized initiative | Projects kill / defer; reassign contributors |

Roadmap changes do not automatically change departments — they change **priorities and staffing** within invariant structure.

### Relationship to Current State

[`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) holds **instance values** for this document's **type definitions**:

| This document defines | Current State holds |
|---|---|
| Escalation threshold categories | Actual % thresholds this quarter |
| Scale stage playbooks | Current headcount band |
| Department head role | Named individual |
| Active project interfaces | Projects in flight |
| "Customize quarterly" items | Current customization |

When Current State contradicts this document's invariant rules, **this document wins** — fix Current State or amend this doc via DR.

### Relationship to Glossary

Canonical definitions for organizational terms live in [`07_GLOSSARY.md`](07_GLOSSARY.md). Key terms used here:

| Term | Glossary entry (when published) |
|---|---|
| DRI | Directly Responsible Individual |
| Holding OS | Atlas operating system |
| Department | One of seven canonical functions |
| Contributor | Executes; does not own |
| Escalation | Authority transfer at defined trigger |
| Believability | Decision weight from track record |
| One-way door | Irreversible decision |
| Integration scorecard | Post-acquisition standards tracker |

Propose additions during quarterly Glossary review.

---

## Document Maintenance

| Field | Value |
|---|---|
| **Canonical owner** | Brain department (Brain lead) |
| **Suggested readers** | All operators; department heads (deep); portfolio leaders; AI agents (retrieval for ownership routing) |
| **Change process** | Propose via Decision Record → Brain review → version bump per [Versioning Policy](00_ATLAS_BRAIN.md#versioning-policy) → notify department heads → update [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md) if instance values affected |
| **Review cadence** | Quarterly (aligned with T1 governance schedule) |
| **AI retrieval note** | Agents resolve ownership, escalation targets, and interface SLAs from this document; defer to [`06_DECISIONS.md`](06_DECISIONS.md) for precedents; defer to [`07_GLOSSARY.md`](07_GLOSSARY.md) for terms |

### Changelog

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-08-08 | Initial release — organizational operating system: departments, ownership, authority, interfaces, communication, scaling, hiring, lifecycle, checklists |

---

*The organization exists to execute the Brain — not replace it.*

*For strategy and frameworks, see [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md). For conviction, see [`01_WHY_ATLAS_EXISTS.md`](01_WHY_ATLAS_EXISTS.md). For judgment, see [`02_FOUNDING_PRINCIPLES.md`](02_FOUNDING_PRINCIPLES.md). For who is named today, see [`05_CURRENT_STATE.md`](05_CURRENT_STATE.md).*



