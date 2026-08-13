# P-002 — Atlas Build Factory

**Project ID:** P-002
**Status:** Active — Definition (truth-layer / architecture only; no product code in this phase)
**Owner:** Антон
**Project type:** Infrastructure / Product-production system
**Created:** 2026-08-13
**Governing decisions:** [DR-2026-011](../../02_Brain/06_DECISIONS.md#dr-2026-011-pre-fop-period-no-external-commercial-contact) · [DR-2026-012](../../02_Brain/06_DECISIONS.md#dr-2026-012-atlas-product-foundation-five-factories-and-p-002)

---

## 1. Mission

Build and test an **autonomous product-production foundation** inside Atlas Lab so Atlas can later deliver custom digital companies, departments, and automated business systems from one reusable stack — not from unrelated one-off products.

Atlas Lab is not merely a bot-development studio.

Atlas Lab should evolve into:

**A factory for custom digital companies, departments and automated business systems.**

P-002 exists to make that real as a production system. It does not exist to contact the market, collect payment, or ship to external clients during the Pre-FOP Period ([DR-2026-011](../../02_Brain/06_DECISIONS.md#dr-2026-011-pre-fop-period-no-external-commercial-contact)).

---

## 2. Scope

In scope for P-002:

- Design the shared **Atlas Product Foundation**
- Design and, after Founder approval of this brief, implement the **five product factories** as configurations of that foundation
- Run **synthetic / internal orders** based on real public-company problems
- Run autonomous analysis, build, QA, fix, and review **inside** the controlled Atlas Lab environment
- Prepare everything needed for later commercial launch — without performing the launch

The five confirmed factories:

| Factory | Produces | Notes |
|---|---|---|
| **1. Atlas Bot Factory** | Telegram / messenger bots and conversational operators | First implementation factory |
| **2. Atlas Web Factory** | Websites, portals, public/client-facing web surfaces | After Bot Factory is proven on a synthetic order |
| **3. Atlas Business App / Mini-CRM Factory** | Internal business apps, mini-CRMs, operational tools | Not five CRMs; one factory |
| **4. Atlas AI Office Factory** | Configurable AI offices (roles, workflows, tools, controls) | Sales, Recruiting, Support, Operations, Marketing are **packages of this factory**, not independent codebases |
| **5. Atlas Document & Workflow Factory** | Document intake, extraction, routing, approvals, generated artefacts | Shared by offices and apps |

Potential catalogue (offerings, not separate products):

Websites & Portals · Business Automation · Custom CRM · AI Agents · AI Offices · Telegram / Messenger Bots · Document Automation · Sales Automation · Support Automation · Internal Business Systems · Dashboards & Management Intelligence

---

## 3. Non-goals

P-002 will **not**:

- Contact the external world commercially before FOP (no email, LinkedIn, Telegram outreach, contact forms, real proposals, real OUT records intended for sending, payment collection)
- Treat Sales, Recruiting, Support, Operations, or Marketing as five independent codebases
- Build five unrelated products that later have to be “integrated”
- Contact **Daniel Cobb** or **Gosselin**
- Create **OUT-0002**
- Deploy to production, spend material capital, or collect payment
- Rewrite the holding OS (that remains **P-001**)
- Modify the live Atlas Telegram bot, `tasks.db`, or Sales Pipeline runtime as part of factory work unless a later Founder-approved execute step explicitly says so
- Claim paid demand, customers, or a completed commercial loop

---

## 4. Architectural principles

```
Atlas Product Foundation
        ↓
Reusable modules
        ↓
Product factories
        ↓
Client-specific 10–30% customization
```

1. **One production foundation.** Factories are product lines on a shared core, not sibling startups.
2. **Reuse before uniqueness.** New client work should mostly select and configure modules; only 10–30% should be client-specific.
3. **Packages, not products, for departments.** Sales / Recruiting / Support / Operations / Marketing = AI Office Factory solution packages.
4. **Internal autonomy, external gates.** High autonomy is allowed inside Atlas Lab. External communication, production deployment, spending, payments, and other high-impact actions remain Founder-gated.
5. **Synthetic orders are first-class.** Real public companies may be used as realistic benchmarks. They are not clients until FOP + Founder approval + actual outreach authorization.
6. **Earn complexity.** Do not stand up all five factories as empty shells. Prove Foundation + Bot Factory + one synthetic order before multiplying surface area. This refines [DR-2026-010](../../02_Brain/06_DECISIONS.md#dr-2026-010-atlas-capital-engine--atlas-foundry-direction) anti-overbuild: the two-week build is the foundation, not five speculative products.
7. **P-001 remains the holding OS.** P-002 consumes Brain/Projects/AI rules; it does not replace them.

Relationship to Atlas Foundry: DR-2026-010 established Foundry as a **capability**, not a department. P-002 is the first project that implements that capability as a concrete production architecture.

---

## 5. Target production workflow

```
ORDER
  → Product Manager
  → Requirements / business analysis
  → Solution Architect
  → Select foundation + reusable modules
  → Build
  → QA
  → Fix loop
  → Security / Reviewer
  → Founder Review
  → only after approval: deployment / delivery / external action
```

Until FOP, the last arrow is **forbidden**. The pipeline may run through Founder Review and stop at `READY_FOR_REVIEW`.

---

## 6. Night Build target

The Founder should eventually be able to approve an artificial order before sleep.

Atlas should autonomously analyze, build, test, fix, and review it overnight.

In the morning Atlas should present a **READY_FOR_REVIEW** result.

Night Build is a **target**, not a current capability. It is out of scope until Foundation + at least one factory + one synthetic order exist.

---

## 7. Founder approval boundaries

| May proceed autonomously (inside Atlas Lab) | Founder-gated |
|---|---|
| Public-information research | Outbound email / LinkedIn / Telegram / contact forms |
| Identifying operational problems | Real proposals sent externally |
| Synthetic / internal orders | Real OUT records intended for sending |
| Design, architecture, internal build | Payment collection |
| QA, security review, fix loops | Production deployment / delivery |
| Simulated client / project / finance workflows | Spending of consequence |
| Preparing launch artefacts that are not sent | Any other external commercial action |
| Presenting READY_FOR_REVIEW | Credentials / irreversible / legally consequential actions |

---

## 8. Synthetic-order testing approach

Use real companies as **benchmark cases**, then issue internal orders Atlas treats as if they were clients — without contacting them.

### TASK-0002 disposition (canonical)

TASK-0002 research is **closed as a commercial-outreach cycle**. It produced benchmark / synthetic-order candidates only.

| Company | Role | Contact? | OUT record? |
|---|---|---|---|
| **Daniel Cobb** (UK property / lettings / property management) | Realistic **small-company benchmark** and first synthetic-order candidate | **No** (before FOP) | **Do not create OUT-0002** |
| **Gosselin Group** | **Enterprise internal benchmark only** | **No** | **No** |
| Approach People / OUT-0001 | Separate prior cycle; not a P-002 synthetic order | No new contact under P-002 | Already exists; do not extend here |

**Candidate synthetic solution (internal only):** AI Property Management / Lettings Inbox Copilot — a realistic first order for Bot Factory, with later optional Document / AI Office modules. Not a sold product. Not a live prospect.

No TASK-0002 result may be used as permission to reach Daniel Cobb, Gosselin, or any other external party.

---

## 9. Success criteria — two-week pre-FOP period

The Founder-confirmed objective is to use approximately the next two weeks to build and test the autonomous product-production foundation.

P-002 is successful for this window if **all** of the following are true:

1. **Foundation specified.** Atlas Product Foundation has a written module/interface map that later factories can share.
2. **Bot Factory v0.1 exists** as a reusable factory (not a one-off bot), capable of producing a client-shaped bot from an order.
3. **One synthetic autonomous order** has been run end-to-end through analyze → build → QA → fix → review, stopping at Founder Review / `READY_FOR_REVIEW`.
4. **No external commercial action** occurred (DR-2026-011 held).
5. **No second independent codebase** was created for Sales/Recruiting/Support/Ops/Marketing.
6. **Night Build is designed** (order → overnight loop → morning review) even if not yet run cross-factory.
7. **P-001 / Phase 1 claims are not falsified.** This sprint does not pretend to complete P1.2 / P1.4 / P1.5, create revenue, or exit Phase 1.

Stretch (not required to call the two weeks a success): Web Factory v0 skeleton **or** a second factory started only after the first synthetic order is `READY_FOR_REVIEW`.

---

## 10. First implementation sequence

Inspecting the existing system (P-001 holding OS, DR-2026-010 Foundry direction, internal Telegram bot as **Atlas Lab tooling not a factory**, OP-022 still in Research, zero production L2 automations) yields this sequence:

| Step | Work | Why this order |
|---|---|---|
| **A** | Atlas Product Foundation architecture | Without a shared core, the five factories become five codebases — the failure mode this project exists to prevent |
| **B** | Atlas Bot Factory v0.1 | Fastest complete deliverable shape; closest to existing Atlas Lab messenger tooling, which must remain a **separate internal OS tool** and not be silently reused as the factory |
| **C** | First synthetic autonomous order (Daniel Cobb–shaped lettings inbox copilot, internal only) | Proves ORDER → build → QA → Founder Review before multiplying factories |
| **D** | Web Factory | Typical next SMB surface after a bot; still on the same foundation |
| **E** | Business App / Mini-CRM Factory | Internal systems / mini-CRM as modules, not a new stack |
| **F** | AI Office Factory | Department packages (Sales, Support, …) configure this factory; building it after 2–3 product types exist prevents it from becoming a grab-bag |
| **G** | Document & Workflow Factory | Shared by offices and apps; introduced once there is something to attach documents to |
| **H** | Cross-factory autonomous Night Build testing | Requires Foundation + ≥2 factories + a working order pipeline |

**Do not skip A→C.** D–H start only after C has produced a `READY_FOR_REVIEW` result, unless the Founder explicitly re-sequences.

The current Telegram bot, live `tasks.db`, and Sales Pipeline runtime are **out of scope** for A–C unless a later Founder-approved execute step says otherwise.

---

## 11. Relationship to P-001

| | P-001 | P-002 |
|---|---|---|
| Purpose | Atlas holding operating system | Product-production foundation and factories |
| Commercial contact | Customer-acquisition artefacts exist; **frozen until FOP** | Synthetic orders only until FOP |
| OP-022 | Research opportunity for AI automation services | Consumes OP-022-type problems as **internal** orders, not as outreach |

P-002 does not kill P-001 or OP-022. It changes what is allowed to happen next: **build the factory internally**, do not hunt the next OUT record.

---

## 12. Immediate next step (after Founder approval of this definition)

Execute **Step A** only: write the Atlas Product Foundation architecture (shared modules, order schema, factory interface, quality/security gates). No product code before that architecture is Founder-reviewed.

---

*This brief is the canonical P-002 definition. Instance status lives in [`05_CURRENT_STATE.md`](../../02_Brain/05_CURRENT_STATE.md). Approved substance lives in [`06_DECISIONS.md`](../../02_Brain/06_DECISIONS.md). Unapproved ideas live in [`IDEA_BACKLOG.md`](../../02_Brain/IDEA_BACKLOG.md).*
