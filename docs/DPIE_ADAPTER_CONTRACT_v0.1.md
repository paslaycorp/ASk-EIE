# DPIE Adapter Contract v0.1

## Objective

Allow a business domain to plug into DPIE without gaining authority over the epistemic/verification core.

## Contract

Every adapter implements six conceptual operations:

1. `ingest(source)` — accept domain input.
2. `normalize(data)` — map input into canonical evidence structures.
3. `validate(envelope)` — enforce domain/schema requirements without redefining epistemic semantics.
4. `verify(envelope, core)` — invoke core verification services.
5. `evaluate(result)` — consume core results; never override core authority.
6. `render(result)` — produce domain-readable output and report references.

## Authority rule

The adapter is an interpreter, not an epistemic authority.

It MUST NOT:

- promote UNKNOWN to known;
- downgrade a contradiction without a declared core rule;
- fabricate provenance;
- change integrity state;
- authorize a transition rejected by the Governor;
- replace the Verification Kernel's semantic rule set;
- silently discard unresolved evidence gaps.

## Canonical result

A compliant adapter returns a result envelope containing:

- decision
- reason codes
- provenance characterization
- integrity characterization
- confidence/capacity information when available
- unresolved uncertainty
- contradictions
- evidence references
- audit reference

## Security requirements

Adapters operate inside a tenant-scoped security boundary. External input is untrusted. Authentication, authorization, validation, size/type limits, hashing, logging redaction, rate limiting, and fail-closed behavior belong to the platform boundary, not to customer-provided adapter code.

## Demonstration requirement

A reference adapter must be capable of accepting a synthetic business evidence package and producing a result that is traceable back to its evidence references.

## Cross-domain invariant

A new sector adapter must be implementable without modifying epistemic semantics in ECR-p, ECR-i, the Governor, Decision Lattice, or Verification Kernel. Any violation is an architecture finding requiring explicit review.
