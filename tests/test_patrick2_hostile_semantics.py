"""Hostile semantic cases derived from the PATRICK² v0.5 rule boundary.

This is a semantic reference test until a Datalog runtime is available in CI.
It deliberately tests the distinctions required before a production adapter is
allowed to feed canonical facts into PATRICK².
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Case:
    contradiction: bool = False
    comparable: bool = False
    relevant: bool = True
    required: bool = False
    satisfied: bool = False
    same_time: bool = True
    same_entity: bool = True
    same_scope: bool = True
    provenance_verifiable: bool = True
    exception: bool = False


def characterize(c: Case) -> set[str]:
    result: set[str] = set()
    # Mirrors PATRICK² R2: contradiction requires a semantic frame.
    if c.contradiction and c.comparable and c.relevant:
        result.add("CONTRADICTION")
    elif c.contradiction and not c.comparable:
        result.add("NOT_CONTRADICTION")
    # Mirrors R3's missing-requirement boundary.
    if c.required and not c.satisfied:
        result.add("INCOMPLETE")
    if not c.same_time:
        result.add("DIFFERENT_TIME")
    if not c.same_entity:
        result.add("DIFFERENT_ENTITY")
    if not c.same_scope:
        result.add("DIFFERENT_SCOPE")
    if not c.provenance_verifiable:
        result.add("UNVERIFIABLE_PROVENANCE")
    if c.exception:
        result.add("EXCEPTION")
    return result


def test_hostile_semantic_distinctions():
    cases = [
        (Case(contradiction=True, comparable=True), {"CONTRADICTION"}),
        (Case(contradiction=True, same_scope=False), {"NOT_CONTRADICTION", "DIFFERENT_SCOPE"}),
        (Case(same_time=False), {"DIFFERENT_TIME"}),
        (Case(same_entity=False), {"DIFFERENT_ENTITY"}),
        (Case(exception=True), {"EXCEPTION"}),
        (Case(required=True), {"INCOMPLETE"}),
        (Case(provenance_verifiable=False), {"UNVERIFIABLE_PROVENANCE"}),
    ]
    for case, expected in cases:
        assert characterize(case) == expected


def test_forbidden_epistemic_promotions_never_appear():
    cases = [
        Case(required=True),
        Case(provenance_verifiable=False),
        Case(exception=True),
        Case(same_entity=False),
        Case(same_time=False),
        Case(same_scope=False),
    ]
    for case in cases:
        result = characterize(case)
        assert "VERIFIED" not in result
        assert "COMPLIANT" not in result
        assert "COMPLETE" not in result


def test_scope_qualification_is_not_contradiction():
    result = characterize(Case(contradiction=True, same_scope=False))
    assert "CONTRADICTION" not in result
    assert "DIFFERENT_SCOPE" in result


def test_provenance_does_not_establish_truth_or_completeness():
    result = characterize(Case(provenance_verifiable=True, required=True, satisfied=False))
    assert "INCOMPLETE" in result
    assert "VERIFIED" not in result
    assert "COMPLETE" not in result
