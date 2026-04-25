# Leakage Control Checklist

The Proxy Benchmark Track must prevent models from learning shortcuts instead of meaningful signal structure.

This checklist is a helper document for research-stage benchmark design.

## Basic checks

- Separate train, validation, and test sessions.
- Avoid mixing the same participant across splits unless explicitly testing within-subject stability.
- Avoid using timestamp, filename, folder name, device ID, operator ID, or session order as hidden labels.
- Keep preprocessing rules fixed before evaluation.
- Document all exclusions.
- Record failed and partial sessions.
- Keep raw data separate from processed data.
- Keep public sample data synthetic or non-identifying.
- Do not tune models on the final holdout set.
- Do not remove failed runs without logging the reason.

## Preferred holdout options

Use one or more of the following:

- participant holdout
- day holdout
- device holdout
- session holdout
- condition holdout
- operator holdout

## Minimum reporting

Every benchmark result should report:

- split strategy
- leakage risks checked
- missing data handling
- excluded sessions
- model version
- preprocessing version
- evaluation script version
- metric definition
- known limitations

## Red flags

Treat the following as leakage risks:

- unusually high accuracy without physiological plausibility
- model performance driven by session order
- condition labels embedded in filenames
- preprocessing performed after viewing labels
- same participant appearing in both train and test splits without disclosure
- manual exclusion of inconvenient samples without logged reason

## Boundary rule

This checklist does not define CAIS compliance, Sal-Meter validation, certification status, diagnostic capability, clinical interpretation, or therapeutic relevance.

It exists only to protect benchmark integrity.
