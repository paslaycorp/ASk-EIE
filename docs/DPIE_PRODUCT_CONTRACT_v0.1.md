# DPIE Product Contract v0.1

## Product thesis

DPIE is a sector-neutral decision-verification layer. Businesses provide heterogeneous evidence through adapters; DPIE returns a qualified, traceable, auditable decision output.

## Product boundary

```text
Business Inputs
      |
      v
Domain Adapter
      |
      v
Canonical Evidence Envelope
      |
      v
AEIF / ECR-p / ECR-i
      |
      v
Verification Kernel
      |
      v
Transition Governor
      |
      v
Decision Record
      |
      v
Business Output Adapter
```

## Commercial output contract

Every successful evaluation SHOULD be capable of producing:

- `decision`
- `reason_codes`
- `provenance`
- `integrity`
- `evidence_ids`
- `contradictions`
- `gaps`
- `uncertainty`
- `audit_reference`

The output must distinguish an absence of evidence from evidence of absence.

## Security invariants

1. All external input is untrusted.
2. Tenant identity is established before accessing tenant-scoped evidence.
3. Adapters cannot mutate core policy or authority.
4. Evidence references remain traceable after normalization.
5. Hashes are used where content identity matters.
6. Authorization failures fail closed.
7. Material decisions produce audit events.
8. Sensitive fields are excluded or redacted from ordinary logs.

## Demo-to-pilot path

### Demo
Synthetic evidence only. No customer secrets required.

### Trial
Customer supplies a sanitized evidence package through an isolated tenant/workspace.

### Pilot
DPIE evaluates one real workflow and produces an auditable decision report. Pilot success is measured by time saved, errors/gaps discovered, decisions accelerated, or risk avoided.

### Production
Usage-based verification with domain adapter, tenant controls, audit retention, reporting, and API integration.

## Sector strategy

Insurance/FAP is retained as the engineering reference domain. Vendor/AI due diligence is the first commercial proving workflow. Additional sectors are added only when an adapter can consume the canonical contract without modifying epistemic semantics.

## Anti-feature rule

Do not add generic chatbot behavior, domain-specific epistemic overrides, or sector features that cannot be tied to a measurable customer decision or verification workflow.
