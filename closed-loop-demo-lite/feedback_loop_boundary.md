# Feedback Loop Boundary

This document defines the boundary for a local closed-loop demo-lite surface in the **SICS Human-State Proxy Benchmark Track**.

It is a public helper boundary document.

It is not the Sal-Meter core signal track.

It does not define CAIS.

It does not grant CAIS compliance.

It does not validate Sal-Meter.

It does not validate benchmark performance.

It does not introduce raw human data.

It does not create diagnostic, clinical, therapeutic, surveillance, employment, insurance, educational, legal, eligibility, certification, or human-ranking authority.

It does not deploy a live feedback loop.

It does not automate intervention on real people.

---

## Purpose

A feedback loop can become dangerous when it is misunderstood.

A review prompt can become a command.

A synthetic event can become false evidence.

A placeholder can be mistaken for a product.

This document prevents that drift.

The purpose of this file is to define what a closed-loop demo-lite may show and what it must never claim.

The loop may show structure.

The loop must not claim intervention.

The loop may show how synthetic/sample fields connect.

The loop must not claim that real people are being monitored, treated, diagnosed, scored, ranked, or controlled.

---

## Core rule

A closed-loop demo-lite may connect:

- synthetic/sample AI-output events;
- synthetic/sample proxy fields;
- dashboard review states;
- feedback event logs;
- placeholder review prompts;
- boundary notices;
- audit-friendly metadata.

A closed-loop demo-lite must not connect:

- real human monitoring;
- diagnosis;
- therapy;
- surveillance;
- certification;
- employee evaluation;
- insurance scoring;
- legal eligibility;
- education scoring;
- person ranking;
- Sal-Meter validation;
- CAIS compliance.

Correct sentence:

    This local demo-lite shows a structure-only feedback event flow using synthetic/sample fields.

Incorrect sentence:

    This system detects human harm and automatically intervenes.

---

## Current status

    Research-stage feedback-loop boundary document.
    Public helper documentation only.
    Local demo-lite boundary only.
    Synthetic/sample fields only.
    Non-production.
    No live intervention.
    No benchmark evidence.
    No Sal-Meter input.
    No CAIS compliance.
    No raw human data.
    No identifiable data.
    No clinical data.
    No diagnostic authority.
    No therapeutic authority.
    No surveillance authority.
    No certification authority.
    No human-ranking authority.

---

## Required visible boundary language

Every public closed-loop demo-lite file, output, or placeholder script should preserve this boundary:

    Research-stage proxy benchmark helper demo.
    Synthetic/sample data only.
    Local placeholder only.
    Non-production.
    Not diagnostic.
    Not clinical.
    Not therapeutic.
    Not surveillance.
    Not certification.
    Not Sal-Meter.
    Not CAIS compliance.
    Not human ranking.
    No live intervention.
    No real-person automation.

This boundary must be visible before any demo output is interpreted.

A hidden disclaimer is not enough.

---

## Allowed feedback-loop claims

Allowed:

    local closed-loop demo-lite
    synthetic/sample feedback event log
    structure-only feedback loop
    non-production placeholder
    bounded review state
    review prompt
    dashboard-to-log demonstration
    AI-output event marker example
    proxy-field review example
    helper event log
    audit-friendly event structure
    not diagnostic
    not clinical
    not therapeutic
    not surveillance
    not certification
    not Sal-Meter
    not CAIS compliance
    not human ranking

Allowed sentence examples:

    This demo-lite shows how synthetic/sample feedback events may be logged for structure review.

    This local placeholder does not perform live monitoring, diagnosis, therapy, or intervention.

    This event log is a public helper structure and does not validate benchmark performance.

---

## Prohibited feedback-loop claims

Do not use:

    validated feedback loop
    clinical feedback loop
    diagnostic feedback
    therapeutic feedback
    real-time intervention
    production monitoring
    AI harm diagnosis
    human safety score
    psychological safety score
    employee risk score
    patient score
    insurance score
    legal eligibility score
    education score
    CAIS-compliant loop
    Sal-Meter feedback loop
    certified closed-loop system
    deployed intervention system
    human truth loop
    consciousness feedback score

Prohibited sentence examples:

    This feedback loop detects unsafe people.

    This feedback loop diagnoses human stress.

    This feedback loop provides therapeutic intervention.

    This feedback loop validates Sal-Meter output.

    This feedback loop is CAIS-compliant.

    This feedback loop determines who is right in a conflict.

---

## Allowed loop stages

A demo-lite loop may include the following stages:

    synthetic_input_event
    synthetic_ai_output_event
    synthetic_proxy_field_snapshot
    dashboard_review_state
    boundary_check
    placeholder_feedback_policy
    feedback_event_log_entry
    human_review_required
    hold_interpretation

These stages are structural placeholders.

They are not proof of performance.

They are not intervention logic.

---

## Prohibited loop stages

A demo-lite loop must not include stages named:

    diagnose_user
    treat_user
    intervene_on_person
    monitor_employee
    rank_participant
    score_patient
    approve_insurance
    determine_legal_eligibility
    assign_blame
    determine_who_is_right
    determine_who_is_wrong
    certify_result
    approve_CAIS
    validate_Sal_Meter
    trigger_clinical_alert
    trigger_therapeutic_action
    deploy_live_monitoring

Names become architecture.

Bad names create bad systems.

---

## Feedback action boundary

Allowed feedback actions:

    review_metadata
    review_timestamp_alignment
    review_leakage_risk
    review_public_private_boundary
    review_dashboard_claim_boundary
    review_qc_structure
    hold_interpretation
    require_human_review
    mark_synthetic_sample_only
    log_boundary_notice

Not allowed feedback actions:

    diagnose
    treat
    intervene
    monitor_person
    escalate_person
    remove_person
    rank_person
    identify_unsafe_user
    assign_blame
    determine_right_wrong
    certify_result
    approve_CAIS
    validate_Sal_Meter
    trigger_medical_action
    trigger_therapeutic_action
    trigger_surveillance_action

The loop may ask for review.

It must not command judgment.

---

## Event-log boundary

A feedback event log may contain:

    event_id
    session_id
    synthetic_timestamp
    event_type
    source_module
    input_status
    output_status
    review_state
    boundary_status
    synthetic_proxy_field_reference
    placeholder_feedback_action
    operator_note
    audit_note
    public_private_boundary
    sal_meter_input_status
    cais_compliance_status

A feedback event log must not contain:

    participant_name
    real_face_data
    real_voice_data
    raw_biosignal_data
    raw_video_data
    raw_audio_data
    identifiable_metadata
    health_record
    diagnosis
    treatment_plan
    therapy_instruction
    clinical_alert
    surveillance_score
    person_score
    employee_score
    insurance_score
    legal_score
    education_score
    Sal-Meter_raw_input
    CAIS_compliance_output

Event logs are not neutral.

They become memory.

Memory can become false evidence.

Therefore, every event log must remain bounded.

---

## Review-state boundary

Allowed review states:

    not_started
    synthetic_sample_only
    boundary_review_required
    metadata_review_required
    timestamp_review_required
    leakage_review_required
    qc_review_required
    human_review_required
    interpretation_hold
    helper_structure_pass
    helper_structure_fail

Not allowed review states:

    user_diagnosed
    user_treated
    unsafe_user_detected
    employee_failed
    patient_improved
    therapy_success
    clinical_alert_triggered
    surveillance_ready
    certified_pass
    CAIS_compliant
    Sal-Meter_validated
    human_truth_confirmed
    consciousness_level_detected

Review states are not human judgments.

They are helper states.

---

## Human review boundary

The demo-lite may contain:

    human_review_required

This means:

    A human should review the helper structure, metadata, boundary language, leakage risk, and interpretation limits before any claim is made.

It does not mean:

    A human must intervene on another person.
    A clinician must diagnose.
    A therapist must treat.
    A manager must monitor.
    A legal authority must act.
    A system has detected harm.
    A person has failed.

Human review is a boundary safeguard.

It is not an escalation verdict.

---

## AI-output event boundary

AI-output events may be represented only as synthetic/sample events.

Allowed:

    synthetic_ai_output_event
    sample_ai_response_marker
    mock_interaction_event
    toy_ai_output_window
    placeholder_ai_feedback_event

Not allowed:

    harmful_ai_output_detected
    clinical_harm_confirmed
    psychological_damage_detected
    unsafe_ai_intervention_triggered
    therapeutic_ai_feedback
    legal_fault_assignment
    person_blame_event

An AI-output event may mark structure.

It must not declare harm.

---

## Human-State Cost boundary

Human-State Cost may appear only as a bounded synthetic/sample proxy construct.

Allowed:

    synthetic_human_state_cost_proxy
    Human-State Cost Proxy Field
    bounded proxy construct
    interaction-window comparison placeholder
    synthetic burden field
    review-only construct

Not allowed:

    Human-State Cost Score
    human safety score
    psychological safety score
    clinical score
    diagnostic score
    therapy response score
    surveillance score
    employee risk score
    patient score
    legal risk score
    Sal-Meter score
    CAIS score
    consciousness score
    human truth score

Human-State Cost must not become a person score.

Human-State Cost must not become diagnosis.

Human-State Cost must not become therapy.

Human-State Cost must not become surveillance.

Human-State Cost must not become Sal-Meter.

Human-State Cost must not become CAIS compliance.

---

## Dashboard-to-loop boundary

A dashboard may pass only bounded helper states into a demo-lite event log.

Allowed dashboard inputs:

    metadata_completeness_status
    timestamp_alignment_status
    leakage_review_status
    qc_status
    boundary_notice
    synthetic_proxy_field_reference
    future_sal_meter_input_placeholder
    future_dyadic_mediation_status

Not allowed dashboard inputs:

    clinical_status
    diagnostic_status
    therapeutic_status
    employee_status
    legal_status
    insurance_status
    person_risk_score
    human_truth_score
    consciousness_score
    CAIS_compliance_result
    Sal-Meter_validation_result

The dashboard may inform review.

It must not command action.

---

## Placeholder policy boundary

A placeholder feedback policy may be named:

    boundary_review_policy
    metadata_review_policy
    leakage_review_policy
    timestamp_review_policy
    qc_review_policy
    interpretation_hold_policy
    synthetic_sample_only_policy

A placeholder feedback policy must not be named:

    clinical_intervention_policy
    therapy_policy
    diagnostic_policy
    surveillance_policy
    employee_monitoring_policy
    insurance_scoring_policy
    legal_eligibility_policy
    human_ranking_policy
    CAIS_compliance_policy
    Sal-Meter_validation_policy

Policy names are sharp tools.

They must not cut beyond the evidence.

---

## Script boundary

A placeholder script may:

    print boundary notices
    load synthetic/sample event examples
    create sample event-log dictionaries
    validate required sample fields
    demonstrate structure-only review flow
    show where human review would be required
    avoid network calls
    avoid real sensors
    avoid real-time monitoring
    avoid production automation

A placeholder script must not:

    collect real human data
    connect to biosensors
    connect to cameras
    connect to microphones
    process face data
    process voice data
    process raw biosignals
    monitor real users
    diagnose
    treat
    intervene
    classify a person
    rank a person
    score a person
    call production APIs
    deploy a service
    trigger external actions
    claim benchmark validation
    claim Sal-Meter validation
    claim CAIS compliance

---

## Local-only boundary

The demo-lite must remain local.

Allowed:

    local execution
    local sample log
    local placeholder output
    no network call
    no production endpoint
    no background service
    no external action trigger

Not allowed:

    deployed service
    background monitoring
    live user tracking
    production API call
    webhook intervention
    notification to third parties
    automated escalation
    real-time surveillance
    clinical alerting

Local means the loop stays in the sandbox.

It must not reach into a person’s life.

---

## Synthetic/sample-only boundary

Allowed data status:

    synthetic
    sample
    mock
    toy
    placeholder
    sample-structure-only

Not allowed data status:

    real_participant
    raw_human
    identifiable
    clinical
    medical
    private_user
    production_user
    Sal-Meter_input
    CAIS_compliance_record

A synthetic demo can teach structure.

It cannot prove reality.

---

## Non-production boundary

The demo-lite is non-production.

It must not be described as:

    production-ready
    deployment-ready
    clinical-ready
    device-ready
    certification-ready
    CAIS-ready
    Sal-Meter-ready
    monitoring-ready
    intervention-ready

Acceptable wording:

    non-production
    local placeholder
    research-stage helper
    structure-only
    public helper demonstration
    synthetic/sample-only demo-lite

---

## Diagnostic boundary

Do not use diagnostic language.

Prohibited:

    anxiety detected
    depression detected
    stress disorder
    burnout diagnosis
    mental health risk
    psychiatric state
    diagnostic confidence
    diagnostic label
    diagnostic feedback
    clinical diagnosis

Allowed:

    synthetic condition label
    sample window label
    proxy field
    review state
    boundary status
    non-diagnostic helper field

---

## Clinical boundary

Do not use clinical language.

Prohibited:

    patient status
    clinical state
    clinical score
    clinical alert
    clinical response
    triage
    medical decision support
    health-risk classification

Allowed:

    non-clinical proxy benchmark helper
    synthetic/sample interaction-window event
    research-stage review state
    helper event log

---

## Therapeutic boundary

Do not use therapeutic language.

Prohibited:

    therapy response
    treatment effect
    healing score
    recovery confirmed
    symptom reduction
    therapeutic feedback
    therapeutic intervention
    intervention efficacy

Allowed:

    synthetic feedback-window event
    sample review prompt
    non-therapeutic interaction placeholder
    interpretation hold

---

## Surveillance boundary

Do not use surveillance language.

Prohibited:

    employee monitoring
    student monitoring
    citizen monitoring
    compliance monitoring
    risk scoring
    disciplinary signal
    threat score
    behavioral policing
    unsafe person detection

Allowed:

    non-surveillance benchmark helper
    synthetic interaction-condition comparison
    public helper event log
    local placeholder only

---

## Certification boundary

Do not use certification language.

Prohibited:

    certified feedback loop
    validated loop
    approved loop
    official compliance output
    certified AI safety score
    commercial device readiness
    CAIS-certified output
    Sal-Meter validated output

Allowed:

    release-readiness helper
    demo-lite boundary document
    research-stage feedback-loop helper
    structure-only local placeholder

---

## Dyadic / mediation boundary

Future dyadic or conflict mediation references must remain bounded.

Allowed:

    synthetic dyadic interaction event
    conflict mediation benchmark preview
    future dyadic proxy benchmark placeholder
    synthetic dyadic feedback event example
    bounded review state
    interaction-window comparison

Required boundary:

    Not legal mediation.
    Not therapy.
    Not counseling.
    Not relationship diagnosis.
    Not fault assignment.
    Not who-is-right determination.
    Not who-is-wrong determination.
    Not surveillance.
    Not human ranking.
    Not Sal-Meter.
    Not CAIS compliance.

Not allowed:

    This loop decides who is right.
    This loop identifies the unsafe partner.
    This loop diagnoses the relationship.
    This loop provides therapy.
    This loop assigns blame.
    This loop ranks people in conflict.
    This loop triggers intervention between people.

A dyadic demo-lite may compare synthetic interaction windows.

It must not judge humans.

---

## Future Sal-Meter A/B comparison boundary

Future Sal-Meter A/B comparison references must remain inactive placeholders.

Allowed:

    future_sal_meter_input_placeholder
    future_proxy_core_comparison_placeholder
    not_present
    not_public
    not_validated_here
    future_placeholder_only
    hold_until_separate_governance

Not allowed:

    validated_sal_meter_input
    CAIS_compliant_signal
    official_consciousness_signal
    ground_truth_signal
    diagnostic_sal_meter_result
    Sal-Meter feedback loop
    Sal-Meter intervention loop

No Sal-Meter input is present in this repository.

No CAIS compliance is granted.

No Sal-Meter validation is claimed.

---

## Relationship to other folders

This file should remain aligned with:

    dashboard-mockup/dashboard_claim_boundary.md
    dashboard-mockup/sample_dashboard_fields.json
    dashboard-mockup/mockup_wireframe.md
    protocol-helper/session_label_rule.md
    protocol-helper/timestamp_sync_rule.md
    protocol-helper/metadata_completeness_rule.md
    protocol-helper/human_state_cost_construct_note.md
    protocol-helper/future_sal_meter_ab_comparison_rule.md
    evaluation-baseline/README.md
    sample-data/README.md

If this file conflicts with a stricter boundary file, the stricter boundary should be used.

---

## Allowed public output example

A safe output may look like this:

    Boundary: research-stage local demo-lite.
    Dataset: synthetic/sample only.
    Event: synthetic_ai_output_event.
    Review state: metadata_review_required.
    Feedback action: require_human_review.
    Interpretation: structure-only. Not evidence.

This is acceptable because it does not claim diagnosis, therapy, surveillance, Sal-Meter validation, CAIS compliance, or human ranking.

---

## Prohibited public output example

Do not output:

    The AI response harmed the user.
    The user is unsafe.
    The system should intervene.
    Clinical alert triggered.
    Therapy response confirmed.
    Sal-Meter signal validated.
    CAIS-compliant feedback loop approved.
    Human truth score confirmed.

This is prohibited because it creates authority without evidence.

---

## Review checklist

Before publishing or modifying closed-loop demo-lite material, check:

    [ ] Is the loop clearly marked as research-stage?
    [ ] Is the loop clearly marked as local?
    [ ] Is the loop clearly marked as non-production?
    [ ] Is the loop clearly marked as synthetic/sample-only?
    [ ] Is it clear that this is not Sal-Meter?
    [ ] Is it clear that this does not define CAIS?
    [ ] Is it clear that this does not grant CAIS compliance?
    [ ] Is it clear that this does not validate benchmark performance?
    [ ] Is it clear that this does not deploy live feedback?
    [ ] Is it clear that this does not automate intervention?
    [ ] Are raw human data excluded?
    [ ] Are identifiable data excluded?
    [ ] Are clinical data excluded?
    [ ] Are private user data excluded?
    [ ] Are diagnostic claims absent?
    [ ] Are clinical claims absent?
    [ ] Are therapeutic claims absent?
    [ ] Are surveillance claims absent?
    [ ] Are certification claims absent?
    [ ] Are human-ranking claims absent?
    [ ] Are person scores absent?
    [ ] Are Human-State Cost fields labeled as proxy fields only?
    [ ] Are feedback actions review-oriented, not intervention-oriented?
    [ ] Are future Sal-Meter A/B references inactive and bounded?
    [ ] Are future dyadic or mediation references inactive and bounded?

If any item fails, hold the loop.

---

## P2-3 issue alignment

This file implements:

    [P2-3] Add closed-loop demo-lite boundary pack

It satisfies:

    Create closed-loop-demo-lite/feedback_loop_boundary.md

---

## Completion status

    Feedback loop boundary document.
    Research-stage.
    Public helper documentation only.
    Local demo-lite boundary only.
    Synthetic/sample fields only.
    Non-production.
    Not benchmark evidence.
    Not Sal-Meter.
    Not CAIS compliance.
    No raw human data.
    No identifiable data.
    No clinical authority.
    No diagnostic authority.
    No therapeutic authority.
    No surveillance authority.
    No certification authority.
    No human-ranking authority.
    No live intervention.
    No production automation.

---

## Final rule

A feedback loop may help a future system learn restraint.

It must not become a hidden hand.

A log may preserve structure.

It must not become judgment.

A review prompt may protect evidence.

It must not become intervention.
