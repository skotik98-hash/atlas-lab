# Integration Scorecard v1

> The populated tracking template used the moment any Atlas asset enters the Acquire/Build → Integrate transition, per [Phase 1 exit criterion P1.6](04_ROADMAP.md#phase-1--operating-kernel) and [`00_ATLAS_BRAIN.md` § Company Lifecycle § Integration standards](00_ATLAS_BRAIN.md#company-lifecycle). This is the scorecard itself — a trackable instance of the canonical standards table — not a redefinition of those standards.

**Document ID:** `integration_scorecard.md`
**Location:** `02_Brain/departments/`
**Status:** Draft
**Version:** 1.0
**Owner:** Антон (Operations hat) — co-referenced to Assets (stage handoff) and AI (automation-audit row); see [Ownership note](#ownership-note) below for how this document reconciles two slightly different department pairings named across canonical sources
**Last updated:** 2026-08-09
**Review date:** 2027-02-09

---

## Purpose

This document satisfies [Phase 1 exit criterion P1.6](04_ROADMAP.md#phase-1--operating-kernel) ("Integration scorecard v1 — Assets + Operations") and Roadmap milestone **M-O-002** ("Integration scorecard v1," success test: "Scorecard"). It operationalizes [`00_ATLAS_BRAIN.md` § Company Lifecycle § Integration standards (Acquire / Build → Integrate)](00_ATLAS_BRAIN.md#company-lifecycle), which states: *"New assets must reach minimum integration thresholds within defined timelines,"* and *"Integration progress is tracked on a scorecard reviewed weekly during integration, then monthly."*

This is the **populated tracking template**, not a restatement of the standard. The six integration areas, their standards, and their timelines are defined once, canonically, in `00_ATLAS_BRAIN.md`; they are reproduced here only as column headers because a scorecard requires them as tracking fields, exactly as [`ai_playbook.md`](ai_playbook.md)'s Agent Design Standards fields were reproduced as column headers in [`automation_registry.md`](automation_registry.md). The authoritative definition and rationale for each area remains in `00_ATLAS_BRAIN.md`; this document does not reinterpret or expand it.

## Ownership note

Two canonical sources name the Integrate stage's owners slightly differently, and this document reconciles both rather than silently picking one:

- `04_ROADMAP.md`'s P1.6 evidence field reads **"Assets + Operations."**
- `00_ATLAS_BRAIN.md`'s Company Lifecycle table names the Integrate stage's primary owner as **"Operations + AI."**

This scorecard is authored by the Operations hat (the department whose own playbook already anticipated it — see `operations_playbook.md` § Execution guidance), with Assets retaining the stage-handoff role (an asset moves from Assets' Acquire/Build stage into this scorecard) and AI retaining ownership of the "AI / automation audit" row specifically. No department's authority is expanded or reduced by this document; it only records who evidences which row.

## Explicit trigger condition

Per [`00_ATLAS_BRAIN.md` § Company Lifecycle](00_ATLAS_BRAIN.md#company-lifecycle) and `operations_playbook.md` § Execution guidance ("Integration scorecard trigger conditions"): **this scorecard opens the moment a new asset enters the Acquire/Build → Integrate transition.** Before that moment, the scorecard has nothing to track — it exists as a ready template, not an active instance.

As of this document's creation, **zero portfolio assets exist at any Company Lifecycle stage** (per [`05_CURRENT_STATE.md` § Current Assets](05_CURRENT_STATE.md#current-assets), read here, not modified), so this scorecard has never triggered. Every row below is therefore explicitly unscored.

## Scorecard template v1

**Per-integration header fields** (filled in only once a real asset triggers this scorecard):

| Field | Entry |
|---|---|
| Asset name | *(none — not yet triggered)* |
| Integrate start date | *(none — not yet triggered)* |
| Scorecard reviewer | *(none — not yet triggered)* |
| Review cadence | Weekly during integration, then monthly, per [`00_ATLAS_BRAIN.md` § Integration standards](00_ATLAS_BRAIN.md#company-lifecycle) |

**Integration areas** (columns reproduce the canonical standard and timeline from `00_ATLAS_BRAIN.md` § Integration standards; Status/Evidence/Row owner are this scorecard's own tracking fields):

| Area | Standard | Timeline | Status | Evidence | Row owner |
|---|---|---|---|---|---|
| Financial reporting | Atlas chart of accounts mapping, monthly close | 30 days | ⬜ Not triggered — no asset in Integrate | — | Finance |
| Operational KPIs | Defined and tracked in central dashboard | 45 days | ⬜ Not triggered — no asset in Integrate | — | Operations |
| Documentation | Key processes documented as SOPs | 60 days | ⬜ Not triggered — no asset in Integrate | — | Operations + Knowledge |
| Knowledge base | Company overview, org chart, key contacts in Knowledge | 14 days | ⬜ Not triggered — no asset in Integrate | — | Knowledge |
| AI / automation audit | Top 5 automation candidates identified | 45 days | ⬜ Not triggered — no asset in Integrate | — | AI |
| Decision framework | Company decisions follow Atlas framework | Immediate | ⬜ Not triggered — no asset in Integrate | — | Brain |

**Status legend** (for use once triggered): ⬜ Not triggered · 🟢 On track · 🟡 At risk (past 75% of timeline, incomplete) · 🔴 Past timeline, incomplete · ✅ Complete, evidenced.

No status above is anything but ⬜, and none may be changed to 🟢/🟡/🔴/✅ without a named asset, a real Integrate start date, and real evidence per row — per [Truth over comfort](02_FOUNDING_PRINCIPLES.md#truth-over-comfort), matching the same discipline [`automation_registry.md`](automation_registry.md) applied to automation maturity labels.

## How to use this scorecard (once a real integration exists)

1. When an asset enters Integrate, copy this template's header fields and area table into a per-asset tracking instance (analogous to how `PROJECT_BRIEF_P-001_MARKET_SCREEN_001.md` instantiated the Project Lifecycle template for a real initiative) — filed in `03_Knowledge/` or alongside the asset's own project folder, not by editing this template in place.
2. Fill in Asset name and Integrate start date from the real Acquire/Build → Integrate transition event.
3. Update each row's Status and Evidence weekly during integration, then monthly once stable, per the canonical review cadence.
4. Any row still ⬜/🔴 past its timeline is a candidate for escalation per the relevant department's [escalation rules](03_ORGANIZATION.md#organizational-anti-patterns).

## Honest current status

**Template only — zero integrations have occurred.** Per [`05_CURRENT_STATE.md` § Current Assets](05_CURRENT_STATE.md#current-assets) and § Company lifecycle scorecard ("Not applicable. No asset exists to score..."), there is no live instance of this scorecard anywhere in the vault. This document supplies the missing *template* — the artifact P1.6 asks for — not a claim that any integration work has begun.

## Status of this document

This is a **Draft T2/T3 artifact**, created to satisfy [Phase 1 exit criterion P1.6](04_ROADMAP.md#phase-1--operating-kernel) (Milestone M-O-002, "Integration scorecard v1"). At [Org Stage 0](03_ORGANIZATION.md#organizational-scaling), zero portfolio assets exist — every field above is a ready template, not evidenced practice.

## Cross references

- [`00_ATLAS_BRAIN.md` § Company Lifecycle](00_ATLAS_BRAIN.md#company-lifecycle) — lifecycle stages, Integration standards table, review cadence
- [`03_ORGANIZATION.md` § Department: Operations](03_ORGANIZATION.md#department-operations) and [§ Department: Assets](03_ORGANIZATION.md#department-assets) — canonical scope, ownership, KPIs
- [`operations_playbook.md`](operations_playbook.md) — trigger-condition anticipation this document populates
- [`assets_playbook.md`](assets_playbook.md) — Acquire/Build-stage handoff into this scorecard
- [`automation_registry.md`](automation_registry.md) — sibling P1.3 artifact using the same "populated template, honestly unscored until real evidence exists" pattern
- [`04_ROADMAP.md` § Phase 1 — Operating Kernel](04_ROADMAP.md#phase-1--operating-kernel) — P1.6 exit criterion this document evidences
- [`05_CURRENT_STATE.md` § Current Assets](05_CURRENT_STATE.md#current-assets) — live confirmation that zero assets exist (read, not modified, by this document)
- [`07_GLOSSARY.md`](07_GLOSSARY.md) — canonical definitions (Integration scorecard, Company Lifecycle stages)

---

*This is a Draft T2/T3 template, not yet Active. It supplements — and does not duplicate — [`00_ATLAS_BRAIN.md`](00_ATLAS_BRAIN.md) or `operations_playbook.md`.*
