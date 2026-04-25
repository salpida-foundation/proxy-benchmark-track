# Metadata Schema v0.1

Minimum metadata fields for proxy benchmark sessions.

This is a working helper document, not a canonical standard.

## Session fields

- session_id
- session_date
- operator_initials
- location_type
- protocol_version
- software_version
- device_set
- notes_file
- timezone
- session_start_time
- session_end_time

## Participant fields

Use only non-identifying participant codes.

- participant_code
- consent_status
- inclusion_note
- exclusion_note
- session_group
- repeat_session_flag

Do not store legal name, phone number, email, address, resident number, medical record number, or any direct identifier in public materials.

## Signal fields

- signal_type
- device_name
- device_serial_or_public_code
- sampling_rate
- timestamp_source
- sync_method
- channel_names
- unit
- missing_data_note
- artifact_note

## Event fields

- event_id
- event_label
- event_start_time
- event_end_time
- marker_source
- operator_note
- condition_label
- state_window_label

## Quality fields

- sync_error_note
- sensor_drop_note
- artifact_severity
- deviation_note
- usable_flag
- exclusion_reason
- preprocessing_version
- reviewer_initials

## Data path fields

- raw_data_path_internal
- public_sample_available
- processed_data_path
- metadata_file_hash
- analysis_script_version

## Boundary rule

This schema is for proxy benchmark support only.

It does not define CAIS compliance, Sal-Meter validation, certification status, clinical interpretation, diagnostic capability, or therapeutic relevance.
