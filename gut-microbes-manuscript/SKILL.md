---
name: gut-microbes-manuscript
description: Create, revise, and audit evidence-grounded English Research Article manuscripts targeted to the Taylor & Francis journal Gut Microbes, using a supplied study outline, experimental results, figures, tables, methods, and references. Use when preparing a Gut Microbes manuscript, converting Chinese or English research materials into a submission-style Word document, organizing microbiome results into a journal-appropriate narrative, checking microbiome reporting completeness, or assessing whether a draft is submission-ready. Produce a visually verified .docx and never invent data, methods, citations, ethics approvals, accession numbers, or causal evidence.
---

# Gut Microbes Manuscript

## Scope

Prepare an English `Research Article` for *Gut Microbes* from author-supplied evidence. Support draft and submission-ready modes. Treat Review Articles, Rapid Communications, Data Notes, and other article types as out of v1 scope unless the user explicitly accepts an adapted workflow.

Use the built-in `documents` skill for every `.docx` creation or edit. Follow its complete render-inspect-iterate workflow and deliver only the final Word document unless the user requests QA files.

## Load references

Read only the references needed for the request:

- Always read `references/input-contract.md`, `references/evidence-guardrails.md`, and `references/journal-requirements.md`.
- Read `references/writing-patterns.md` when structuring or rewriting the manuscript.
- Read `references/microbiome-reporting.md` when auditing or drafting Methods, Results, or data statements.
- Read `references/submission-checklist.md` before labeling any output submission-ready.

Official journal instructions override cached guidance. If web access is available, verify the official *Gut Microbes* Instructions for Authors before final compliance review. Record the verification date in the readiness note. Never silently convert a general Taylor & Francis recommendation into a journal-specific requirement.

## Workflow

### 1. Classify the request

Determine the mode (`draft` or `submission-ready`), study design, supplied artifacts, whether literature retrieval is authorized, and requested deliverables. Default to `draft` when critical fields are missing.

### 2. Inventory the evidence

Extract supplied facts into an evidence manifest compatible with `scripts/audit_evidence.py`. Track study design, groups, sample sizes, exclusions, endpoints, ethics, methods, statistics, every result and its source, every proposed claim and its supporting result identifiers, and references actually supplied or independently verified.

Run:

```bash
python scripts/audit_evidence.py evidence.json --mode draft
```

Use `--mode submission-ready` only for the final gate.

### 3. Resolve consequential gaps

Ask only questions whose answers materially change interpretation, structure, or compliance. Group minor gaps into author placeholders. Never guess sample sizes, statistical methods, ethical approvals, accession identifiers, or experimental conditions.

Use this exact placeholder in draft mode:

```text
[AUTHOR INPUT REQUIRED: describe the missing information precisely]
```

### 4. Build an evidence-to-story map

Create an internal map before prose:

```text
research question -> evidence sequence -> figures/tables -> supported claims -> limitations
```

Choose the closest study-type pattern from `references/writing-patterns.md`. Adapt it to available evidence; never invent an experiment to complete a preferred narrative.

### 5. Draft in evidence-first order

Draft Results, Materials and methods, Discussion, Introduction, Abstract, Title/keywords, then declarations, references, and legends. Keep Results factual and figure-linked. Put interpretation in Discussion. Use association language for observational evidence and causal language only when supported.

### 6. Handle citations safely

Use only references supplied by the author or verified against a reliable bibliographic source. Never fabricate bibliographic metadata. Mark unresolved citations as author input. Learn structure and evidence order from published exemplars, but do not copy distinctive wording.

### 7. Create the Word manuscript

Use the `documents` skill. If current journal instructions do not impose a different template, apply conservative Taylor & Francis formatting: readable 12-point serif type, double spacing, at least 2.5 cm margins, real heading styles, page numbers, continuous line numbers when practical, and stable captions.

Include applicable title/author details, abstract, keywords, main sections, acknowledgments, contributions, disclosure, funding, data availability, ethics, references, figure legends, and supplementary-material statement. Italicize valid genus/species names, not higher ranks or informal community labels.

### 8. Run three QA gates

#### Evidence gate

- Map every major claim to supplied results.
- Reconcile numbers across text, tables, and figures.
- Match causal language to design.
- Report material limitations.

#### Reporting and journal gate

- Apply `references/microbiome-reporting.md`.
- Apply `references/submission-checklist.md`.
- Recheck current official instructions when available.

#### Document gate

- Render the `.docx` to page PNGs.
- Inspect every page at 100% zoom.
- Fix clipping, broken tables, glyphs, captions, headings, pagination, and spacing.
- Re-render after every layout-sensitive change.

## Output contract

In draft mode, return a polished `.docx` with precise author-input placeholders and summarize critical unresolved items in chat.

In submission-ready mode, return a `.docx` only after all critical gates pass. Otherwise return a clearly labeled draft and state the blockers.

Do not submit to a journal portal unless the user separately and explicitly requests that external action.
