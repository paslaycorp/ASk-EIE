# DPIE Evidence Binding Contract v0.1

## Purpose

Define the smallest boundary between sector-specific input adapters and the existing epistemic core.

## One new concept

**Evidence Binding** binds external evidence to typed semantic references without granting epistemic authority.

```text
raw artifact -> adapter -> evidence binding -> PATRICK²/AEIF -> Governor
```

## Binding fields

A binding MAY identify:

- claim
- entity
- scope
- temporal applicability
- source/provenance
- evidence status
- semantic relationships
- binding basis

A binding MUST preserve the origin of each material interpretation.

## Binding basis

Semantic relationships MUST identify their basis:

- `EXPLICIT` — directly stated or structurally explicit in the source
- `RULE_DERIVED` — produced by a versioned deterministic mapping rule
- `EXTERNALLY_ATTESTED` — supplied by an identified external authority
- `HUMAN_ASSERTED` — explicitly entered by an identified reviewer
- `MODEL_SUGGESTED` — proposed by a model and not authoritative
- `UNRESOLVED` — insufficient basis for binding

`MODEL_SUGGESTED` and `UNRESOLVED` MUST NOT independently establish an authoritative semantic relationship.

## Non-promotion invariant

Adapters and binding logic MUST NOT increase epistemic authority merely by translating evidence.

No adapter may directly convert an input into a stronger epistemic state such as `VERIFIED` or `COMPLIANT` unless an explicitly authorized downstream rule independently licenses that transition.

Formally:

> Translation is not authorization.

## Completeness boundary

Evidence authenticity/provenance MUST remain distinct from evidence coverage.

```text
traceable evidence + incomplete coverage != complete evidence
```

Completeness MUST be evaluated relative to an explicit requirement/claim model. The adapter MUST NOT infer package completeness merely because supplied artifacts are authentic.

## Decision boundary

Epistemic characterization MUST remain distinct from organizational approval.

```text
Evidence
  -> epistemic state
  -> risk interpretation
  -> organizational policy
  -> action
```

The binding layer has no authority to approve or reject a vendor.

## Ambiguity rule

If entity, scope, temporal applicability, comparability, or semantic meaning cannot be established, the binding MUST preserve the ambiguity rather than silently collapsing it into equivalence.

## Required adversarial invariants

The following promotions are prohibited unless independently licensed by the authoritative semantic/governance layer:

- `UNKNOWN -> VERIFIED`
- `UNKNOWN -> COMPLIANT`
- `INCOMPLETE -> COMPLETE`
- `EXCEPTION -> NO_EXCEPTION`
- `DIFFERENT_ENTITY -> SAME_ENTITY`
- `DIFFERENT_TIME -> CURRENT`
- `DIFFERENT_SCOPE -> SAME_SCOPE`
- `UNVERIFIABLE_PROVENANCE -> TRUSTED_PROVENANCE`

## Sector-neutrality criterion

A new sector adapter is conformant only if it can produce bindings satisfying this contract without modifying the epistemic semantics or authority rules of the common core.
