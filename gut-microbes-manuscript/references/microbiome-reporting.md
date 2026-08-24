# Microbiome reporting checklist

Apply only relevant items and state when an item is not applicable.

## Study population or model

- Eligibility, recruitment, setting, dates, and exclusions.
- Group definitions and exact analyzed sample sizes.
- Age, sex, diet, medication, antibiotics, geography, housing, cage, litter, or relevant confounders.
- Randomization, allocation concealment, blinding, and sample-size rationale when applicable.
- Human consent/ethics or animal approval and welfare details.

## Specimen handling

- Specimen type and anatomical site.
- Collection procedure, timing, preservatives, transport, storage, duration, and freeze-thaw history.
- Negative controls, positive/mock controls, blanks, and contamination handling.

## Molecular assay

- Extraction kit/protocol and modifications.
- 16S target region and primers, shotgun/metatranscriptomic library preparation, metabolomics platform, or other assay details.
- Instrument, read configuration, depth, and batch information.
- Quality control, filtering, host-read removal, chimera handling, and retained sample/read counts.

## Bioinformatics

- Pipeline, software, version, parameters, and reproducible workflow.
- ASV/OTU or taxonomic profiling method.
- Reference database name, release, and taxonomy level.
- Functional profiling method and pathway database.
- Rarefaction, normalization, compositional transformation, or model offset with justification.

## Statistics

- Primary and secondary endpoints.
- Exact tests and model formulas.
- Covariates, interactions, repeated measures, random effects, and batch effects.
- Effect sizes and uncertainty, not only P values.
- Multiple-testing method and threshold.
- Alpha-diversity metric and test.
- Beta-diversity distance, ordination, group test, permutations, and dispersion check.
- Differential-abundance method appropriate for sparse compositional data.
- Missing-data handling, outliers, sensitivity analyses, and validation.

## Results reporting

- State the denominator for every analysis.
- Match each number to a table, figure, or source dataset.
- Report exact P values where practical and distinguish raw from adjusted values.
- Report direction and magnitude of effects.
- Distinguish exploratory, confirmatory, and validation analyses.
- Avoid calling relative abundance an absolute bacterial load.
- Avoid calling taxonomic association a demonstrated function without functional evidence.

## Reproducibility

- Sequence/raw-data repository and accession identifier.
- Metadata availability and privacy constraints.
- Analysis code repository and version/commit when available.
- Supplementary methods, parameter files, and sample metadata dictionary.

## Interpretation guardrails

- Cross-sectional association does not establish temporal order or causality.
- A microbiome shift is not automatically dysbiosis.
- Diversity is not universally beneficial or harmful.
- Prediction performance requires appropriate validation and leakage control.
- Correlation networks do not establish ecological interaction.
