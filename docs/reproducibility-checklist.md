# Reproducibility Checklist

This checklist defines the minimum reproducibility expectations for proxy benchmark work.

It is designed for research-stage, non-diagnostic, non-therapeutic benchmark support only.

---

## Session identity

Each session should have:

- session ID
- participant code or synthetic subject ID
- date
- operator code
- device list
- signal list
- event marker list
- task condition
- environment note
- deviation note

No direct personal identifiers should be included in public files.

---

## Signal capture

Each signal stream should record:

- stream name
- device name
- sampling rate
- start time
- end time
- timestamp source
- sync method
- dropout count
- missing data note
- quality flag

---

## Event markers

Each event marker should record:

- event ID
- event type
- timestamp
- session ID
- condition label
- source
- annotation note

---

## Leakage review

Before any model result is reported, confirm:

- labels are not embedded in filenames
- labels are not embedded in folder names
- labels are not recoverable from session order
- participant leakage has been checked
- day leakage has been checked
- device leakage has been checked
- preprocessing was fixed before final evaluation
- final holdout was not tuned on
- excluded sessions were logged
- failed or partial sessions were recorded

---

## Minimum reporting

Every benchmark result should report:

- split strategy
- model version
- preprocessing version
- evaluation script version
- metric definition
- excluded sessions
- missing data handling
- known limitations
- leakage risks checked
- whether the data is synthetic, sample, or private

---

## Public release boundary

Public repository materials may include:

- synthetic data
- schema-only examples
- sample code
- toy examples
- mock dashboards
- reproducibility templates

Public repository materials must not include:

- raw human biosignals
- raw human video
- raw human audio
- face data
- private session logs
- consent forms with personal information
- identifiable metadata
- clinical records
- internal lab packages

---

## Final rule

A result that cannot be replayed is not yet benchmark evidence.

A result that leaks labels is not evidence.

A result that requires hidden interpretation is not ready for public comparison.
