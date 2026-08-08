# AI Playbook

> How the AI hat intakes agent proposals, applies the Agent Design Standards, and tracks progress toward default L2 automation maturity — as a precursor to, not a substitute for, the automation registry itself.

**Document ID:** `ai_playbook.md`
**Location:** `02_Brain/departments/`
**Status:** Draft
**Version:** 1.0
**Owner:** Анатолий (AI hat)
**Last updated:** 2026-08-08
**Review date:** 2027-02-08

---

## Mission

Build and maintain the intelligent infrastructure that makes Atlas AI-native — agents, automations, integrations, and evaluation systems that embed AI in every department's workflows — per [`03_ORGANIZATION.md` § Department: AI](03_ORGANIZATION.md#department-ai).

## Relationship to canonical Organization sections

This playbook does **not** restate AI's scope, responsibilities, ownership table, inputs/outputs, KPIs, decision authority, or escalation rules — those are canonical in [`03_ORGANIZATION.md` § Department: AI](03_ORGANIZATION.md#department-ai). This document covers execution mechanics only, per [One source of truth](02_FOUNDING_PRINCIPLES.md#one-source-of-truth).

A scope note: this playbook and the automation registry (Phase 1 exit criterion P1.3) are closely coupled but are two separate deliverables. This stub explicitly does **not** invent a registry location or structure — that decision belongs to a dedicated P1.3 planning pass. Wherever the registry is referenced below, it is marked as **not yet created**.

## Execution guidance

- **Automation registry initiation steps** — Before any agent is deployed, its proposal should be logged using the [Agent design standards](00_ATLAS_BRAIN.md#agent-design-standards) fields (Purpose, Trigger, Inputs, Outputs, Guardrails, Owner, Evaluation, Fallback), reproduced below as an intake form. This playbook is a direct dependency of the automation registry work; the registry itself does not yet exist at any path in this repository.
- **Agent Design Standards intake checklist** — Every proposed agent records: Purpose · Trigger · Inputs · Outputs · Guardrails · Owner · Evaluation · Fallback, per [`00_ATLAS_BRAIN.md` § Agent design standards](00_ATLAS_BRAIN.md#agent-design-standards).
- **L2 default target tracking** — Phase 1 exit criteria include a target of processes reaching L2 (supervised automation) maturity. This playbook is where the AI hat's side of that measurement should be recorded once any process has repeated enough to be eligible — per the [AI maturity model](00_ATLAS_BRAIN.md#ai-maturity-model), no process has stabilized yet, so no L-level promotion has occurred.
- **AI participation to specify (self-referential)** — Per [AI Participation Inside Departments, AI row](03_ORGANIZATION.md#ai-participation-inside-departments): self-hosting the platform, eval pipelines, and meta-automation. None of these are live; they are the department's own backlog.

## Minimum executable step / checklist

- [ ] Every new agent proposal is logged against the Agent Design Standards fields below **before** deployment, using the registry location once it is established by the P1.3 planning pass (not yet created — see scope note above).
- [ ] Track, per process, whether it has repeated three or more times (the [Automation by default](02_FOUNDING_PRINCIPLES.md#automation-by-default) threshold) and is therefore an automation-review candidate.
- [ ] Record model/vendor evaluations against [AI Strategy § Data and security principles](00_ATLAS_BRAIN.md#data-and-security-principles) before adoption.

**Agent Design Standards intake form (template):**

| Field | Entry |
|---|---|
| Purpose | — |
| Trigger | — |
| Inputs | — |
| Outputs | — |
| Guardrails | — |
| Owner | — |
| Evaluation | — |
| Fallback | — |

This checklist is a **proposed procedure**; no agent has been formally registered, specified, or owned per these standards to date — see [`05_CURRENT_STATE.md` § Current AI Capabilities](05_CURRENT_STATE.md#current-ai-capabilities).

## Status of this playbook

This is a **Draft T3 stub**, created to satisfy [Phase 1 exit criterion P1.1](04_ROADMAP.md#phase-1--operating-kernel) (Milestone M-K-003). At [Org Stage 0](03_ORGANIZATION.md#organizational-scaling), AI assistance used to date has been informal and unregistered — content above is proposed procedure, not evidenced practice, per [Truth over comfort](02_FOUNDING_PRINCIPLES.md#truth-over-comfort).

## Cross references

- [`03_ORGANIZATION.md` § Department: AI](03_ORGANIZATION.md#department-ai) — canonical scope, ownership, KPIs, authority
- [`03_ORGANIZATION.md` § AI Participation Inside Departments](03_ORGANIZATION.md#ai-participation-inside-departments) — AI row
- [`00_ATLAS_BRAIN.md` § Agent design standards](00_ATLAS_BRAIN.md#agent-design-standards)
- [`07_GLOSSARY.md`](07_GLOSSARY.md) — canonical definitions
- [`04_ROADMAP.md` § Phase 1 — Operating Kernel](04_ROADMAP.md#phase-1--operating-kernel) — the milestone this stub satisfies

---

*This is a Draft T3 playbook stub, not yet Active. It supplements — and does not duplicate — [`03_ORGANIZATION.md`](03_ORGANIZATION.md).*
