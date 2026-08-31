# DPIE Thesis Attack v0.1

## Objective

Attempt to falsify the commercial and architectural thesis before expanding the product.

## Thesis under attack

A sector-neutral evidence/epistemic core can make business due-diligence decisions more defensible by preserving provenance, distinguishing evidence from inference, exposing contradictions and gaps, and refusing unsupported certainty.

## Attack matrix

| Attack | Falsification question | Failure signal |
|---|---|---|
| Customer bottleneck | Is evidence reasoning actually the dominant delay? | Stakeholder coordination dominates cycle time |
| Unverifiable claims | Can customer-accessible evidence establish material claims? | Most material claims remain UNKNOWN with no useful next action |
| Evidence selection | Can authentic but selectively incomplete packages mislead DPIE? | System equates provenance integrity with completeness |
| Missing-evidence detection | Can DPIE know what evidence ought to exist? | Requires undocumented domain policy to detect important omissions |
| Semantic contradiction | Can scope/time/definition differences be distinguished from contradiction? | Textual disagreement becomes CONFLICT |
| Temporal reasoning | Can validity, supersession, exceptions and effective periods be represented? | Current answer incorrectly ignores temporal state |
| Decision policy | Does DPIE confuse epistemic result with organizational action? | System claims evidence alone determines APPROVE/REJECT |
| LLM substitution | Is DPIE operationally better than generic document analysis? | No material advantage in reproducibility, auditability, controls, or workflow |
| Auditor interoperability | Can output be consumed without learning DPIE ontology? | Customer must translate internal categories manually |
| Adapter gaming | Can a compromised adapter manufacture authority? | Adapter can promote UNKNOWN/EVIDENCED to VERIFIED |
| Garbage evidence | Can ugly heterogeneous packages be processed without invented structure? | Silent normalization, dropped evidence, or hallucinated relationships |
| Throughput | Does rigor accelerate legitimate decisions? | Review burden increases without measurable risk/time benefit |

## Nuclear test fixture

Construct a deliberately hostile synthetic vendor package containing:

- valid current security assessment
- expired certification
- contradictory questionnaire answers
- marketing claims without supporting evidence
- subcontractor disclosure
- missing AI-training evidence
- multiple legal-entity names
- acquired subsidiary reference
- stale assessment
- contractual exception
- conflicting retention periods
- ambiguous terminology
- documents from different years
- one forged/unverifiable provenance item
- one authoritative-looking document that does not actually establish the claim

## Required scoring dimensions

### Provenance
Every material claim has a traceable origin, and source identity is not confused with claim truth.

### Integrity
Tampering, malformed identity, replay, and invalid evidence are detected or explicitly qualified.

### Semantics
The system distinguishes contradiction from differences in scope, time, population, definition, and exception.

### Uncertainty
Unsupported certainty is refused. Unknown is not silently converted into negative or positive evidence.

### Decision usefulness
A security/procurement reviewer can act on the output without learning internal DPIE ontology.

## Critical conceptual boundary

`Evidence integrity != evidence completeness.`

Authentic evidence can be strategically incomplete. DPIE must represent this limitation explicitly and, where possible, bind completeness requirements to an external decision policy or domain ontology rather than pretending completeness follows from provenance.

## Decision boundary

DPIE SHOULD characterize what can defensibly be established. Organizational policy determines what action follows.

Conceptually:

`Evidence -> Epistemic State -> Risk Interpretation -> Organizational Policy -> Action`

DPIE must not claim that strong evidence automatically implies APPROVE.

## Commercial kill criterion

Do not sell the vendor-due-diligence workflow merely because the epistemic output is more rigorous than an LLM summary. Demonstrate an operational advantage that a buyer values: reproducibility, evidence lifecycle control, tenant/security boundaries, deterministic policy enforcement, auditability, reduced review time, fewer missed conflicts/gaps, or materially better decision traceability.

## Adapter kill criterion

No adapter may assign epistemic authority that it does not possess. Adapter versioning and mapping rules must be auditable. A domain adapter is a translator, not a truth authority.

## Interpretation

A failed attack is not automatically a product failure. It may reveal that a requirement belongs above the sector-neutral core: domain ontology, risk policy, completeness specification, or organizational decision policy.

The core should shrink to the smallest semantics that remain genuinely sector-neutral.
