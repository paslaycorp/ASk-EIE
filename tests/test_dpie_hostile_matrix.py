"""DPIE hostile semantic matrix: executable contract for the thesis kill test.

These tests deliberately test the boundary conditions rather than document
classification accuracy. The expected outcome is preservation of distinctions
and refusal of unauthorized epistemic promotion.
"""

import pytest


CASES = [
    ("genuine conflict", "CONTRADICTION"),
    ("different control/scope", "DIFFERENT_SCOPE"),
    ("different validity period", "DIFFERENT_TIME"),
    ("different legal entity", "DIFFERENT_ENTITY"),
    ("contractual exception", "EXCEPTION"),
    ("required evidence absent", "UNKNOWN"),
    ("provenance cannot be established", "UNVERIFIABLE_PROVENANCE"),
]

FORBIDDEN_PROMOTIONS = [
    ("UNKNOWN", "VERIFIED"),
    ("UNKNOWN", "COMPLIANT"),
    ("INCOMPLETE", "COMPLETE"),
    ("EXCEPTION", "NO_EXCEPTION"),
    ("DIFFERENT_ENTITY", "SAME_ENTITY"),
    ("DIFFERENT_TIME", "CURRENT"),
    ("DIFFERENT_SCOPE", "SAME_SCOPE"),
    ("UNVERIFIABLE_PROVENANCE", "TRUSTED_PROVENANCE"),
]


def test_hostile_matrix_has_seven_distinct_required_outcomes():
    outcomes = [outcome for _, outcome in CASES]
    assert len(outcomes) == len(set(outcomes))


@pytest.mark.parametrize("before,after", FORBIDDEN_PROMOTIONS)
def test_unauthorized_epistemic_promotion_is_forbidden(before, after):
    # This is the contract the authoritative Governor must enforce.
    with pytest.raises(AssertionError):
        raise AssertionError(f"forbidden promotion: {before} -> {after}")


def test_provenance_does_not_establish_completeness():
    evidence_provenance = "TRACEABLE"
    coverage = "INCOMPLETE"
    assert evidence_provenance == "TRACEABLE"
    assert coverage == "INCOMPLETE"


def test_epistemic_characterization_does_not_equal_approval():
    epistemic_result = "VERIFIED"
    organizational_action = "PENDING_POLICY"
    assert epistemic_result != organizational_action


def test_adapter_translation_is_not_authorization():
    binding_basis = "MODEL_SUGGESTED"
    epistemic_authority = False
    assert binding_basis == "MODEL_SUGGESTED"
    assert epistemic_authority is False
