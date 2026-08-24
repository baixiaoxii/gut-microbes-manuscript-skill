# Input contract

## Minimum useful input

Accept source material in Chinese or English. A workable draft normally needs:

- study question and intended contribution;
- study design, groups, sample sizes, and primary endpoints;
- methods sufficient to interpret each result;
- result tables or exact numeric statements;
- figures and figure legends, if available;
- a reference list or permission to verify literature;
- known ethics, funding, conflict-of-interest, contribution, and data-access information.

## Preferred evidence manifest

Normalize heterogeneous files to this JSON shape:

```json
{
  "manuscript": {
    "title_working": "",
    "mode": "draft",
    "study_type": "human_cohort",
    "research_question": ""
  },
  "study": {
    "groups": [{"name": "", "n": 0}],
    "ethics": {"required": true, "approval_id": ""},
    "data_accession": "",
    "code_repository": ""
  },
  "methods": {
    "sample_collection": "",
    "extraction": "",
    "assay_or_sequencing": "",
    "bioinformatics": "",
    "statistics": ""
  },
  "results": [
    {
      "id": "R1",
      "statement": "",
      "sample_size": "",
      "effect": "",
      "uncertainty": "",
      "p_value": "",
      "multiple_testing": "",
      "source": "Figure 1"
    }
  ],
  "claims": [
    {"id": "C1", "text": "", "supported_by": ["R1"], "strength": "association"}
  ],
  "references": []
}
```

## File handling

- Preserve original files.
- Extract tables from `.xlsx`, `.csv`, `.docx`, or PDF without changing values.
- Treat image-only plots as incomplete quantitative evidence unless values can be read reliably or the author supplies source data.
- Keep figure filenames and panel labels stable.
- Record contradictions rather than choosing whichever value looks more plausible.

## Missing information policy

Critical missing fields include sample sizes, group definitions, primary statistical tests, sequencing/assay identity, ethics where applicable, and evidence supporting central claims.

Use a precise placeholder in draft mode. Ask the author before submission-ready mode. Never infer a missing value from a neighboring figure, a similar paper, or a conventional protocol.
