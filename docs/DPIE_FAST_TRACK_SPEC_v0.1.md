# DPIE Fast-Track Specification v0.1

**Status:** Proposed implementation baseline
**Branch:** `feature/dpie-fast-track`

## Purpose

Re-establish DPIE as a sector-neutral commercial decision/verification layer around the hardened epistemic core. The first commercial proving workflow is vendor/AI due diligence. Existing FAP/Insurance work remains the reference adapter and test domain.

## Non-negotiable core boundary

Adapters SHALL NOT redefine epistemic semantics, provenance levels, integrity levels, verification rules, authority, or transition admissibility.

Adapters translate between domain-specific business inputs/outputs and the canonical DPIE evidence model.

Core remains responsible for:

- provenance characterization
- integrity characterization
- uncertainty/UNKNOWN handling
- semantic rule evaluation
- verification
- transition authorization
- decision reason codes
- auditability

## Canonical adapter lifecycle

`ingest -> normalize -> validate -> verify -> evaluate -> render`

### Adapter input

An adapter receives domain data and maps it into a canonical Evidence Envelope containing, at minimum:

- evidence identity
- source identity/type
- content or content hash
- acquisition timestamp
- claimed event time where applicable
- contextual metadata
- domain assertions
- provenance references

### Adapter output

The adapter renders a core result into domain language without changing its epistemic meaning. A result SHOULD expose:

- decision
- confidence/capacity characterization
- provenance state
- integrity state
- unresolved uncertainty
- contradictions
- evidence gaps
- reason codes
- audit/report reference

## Security boundary

The fast-track implementation SHALL include:

- authenticated API boundary
- tenant isolation
- strict schema validation
- bounded uploads and content-type checks
- content hashing
- secrets outside source control
- rate limiting
- structured/redacted audit logging
- fail-closed authorization and integrity failures
- adapter isolation from core authority

No adapter receives authority to mutate kernel rules or Governor policy.

## Reference adapter

`FAP/Insurance` is the engineering reference adapter because existing FAP-Core/FAP-Insurance work supplies a real evidence workflow.

It is NOT the initial commercial sales specialization.

## Commercial proving adapter

`Vendor/AI Due Diligence` is the first commercial experiment.

Demo input may include synthetic:

- vendor security documentation
- SOC reports
- privacy/data-processing documentation
- contracts
- subprocessors
- AI/model claims
- questionnaire responses

The demo should expose supported claims, conflicts, missing evidence, provenance/integrity characterization, and a defensible review recommendation.

## Acceptance test

The strongest architecture test is cross-domain compatibility:

1. Process an insurance evidence case.
2. Process a vendor/AI due-diligence case.
3. Keep the epistemic core unchanged.
4. Confirm that only adapter/domain mapping and presentation differ.

If the second domain requires changes to epistemic semantics, document the failure as an abstraction-boundary finding rather than silently changing the kernel.

## Commercial hypothesis

DPIE should be presented as decision-verification infrastructure, not generic AI.

Initial proposition:

> DPIE tests whether the evidence supporting a business decision actually supports the decision, identifies conflicts and gaps, and produces an auditable decision record.

The first paid-pilot hypothesis is vendor/AI due diligence. The sector remains an experiment until customer discovery demonstrates willingness to pay.

## Delivery sequence

1. Freeze epistemic core.
2. Define canonical Evidence Envelope.
3. Implement adapter contract.
4. Implement security boundary.
5. Build vendor/AI due-diligence demo.
6. Run insurance and vendor workflows through the same core.
7. Obtain real customer evidence/workflow feedback.
8. Measure willingness to pay before expanding sectors.
