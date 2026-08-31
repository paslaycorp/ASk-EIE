# DPIE Commercial Proving Plan v0.1

## Hypothesis

Businesses will pay to reduce the cost and risk of making decisions from heterogeneous, conflicting, or incomplete evidence.

## First workflow

Vendor / AI due diligence.

## Demo promise

> DPIE tests whether the evidence supporting a business decision actually supports the decision, identifies conflicts and gaps, and produces an auditable decision record.

## Demo flow

1. Upload a synthetic vendor evidence package.
2. Normalize evidence through the adapter.
3. Run provenance/integrity/verification checks.
4. Apply the Governor to admissible transitions.
5. Display decision, supporting evidence, conflicts, gaps, and reason codes.
6. Export an auditable report.

## Customer-discovery questions

- Walk through the last vendor you had to approve.
- What evidence did you receive?
- Who reviewed it?
- Where did the process consume the most time?
- What evidence is commonly missing or contradictory?
- What happens when a claim cannot be verified?
- Who owns the final decision?
- What is the cost of a bad approval or a delayed approval?
- Would an auditable verification report change the workflow?
- What would this have to save or prevent to justify a paid pilot?

## Success criteria

Technical:

- Insurance and vendor adapters use the same epistemic core.
- No adapter can alter core authority.
- All material decisions have evidence references and reason codes.
- Security failures fail closed.

Commercial:

- At least one prospective user supplies a realistic workflow or sanitized evidence package.
- At least one prospect requests a pilot, quote, or paid evaluation.

Failure criterion:

If repeated customer discovery produces no credible economic value, stop expanding features and reassess the workflow before adding sectors.
