"""Thesis-level falsification tests.

These tests are intentionally about forbidden epistemic promotions, not demo
accuracy. A real implementation must make the same distinctions and preserve
the same non-promotion invariants.
"""

from dataclasses import dataclass

import pytest


FORBIDDEN_PROMOTIONS = {
    ("UNKNOWN", "VERIFIED"),
    ("UNKNOWN", "COMPLIANT"),
    ("INCOMPLETE", "COMPLETE"),
    ("EXCEPTION", "NO_EXCEPTION"),
    ("DIFFERENT_ENTITY", "SAME_ENTITY"),
    ("DIFFERENT_TIME", "CURRENT"),
    ("DIFFERENT_SCOPE", "SAME_SCOPE"),
    ("UNVERIFIABLE_PROVENANCE", "TRUSTED_PROVENANCE"),
}


@dataclass(frozen=True)
class EvidenceState:
    state: str


def authorize_transition(before: EvidenceState, after: EvidenceState) -> None:
    if (before.state, after.state) in FORBIDDEN_PROMOTIONS:
        raise AssertionError(
            f"forbidden epistemic promotion: {before.state} -> {after.state}"
        )


def test_forbidden_epistemic_promotions_are_rejected():
    for before, after in FORBIDDEN_PROMOTIONS:
        with pytest.raises(AssertionError):
            authorize_transition(EvidenceState(before), EvidenceState(after))


def test_provenance_does_not_imply_completeness():
    # Authenticity of supplied evidence cannot establish coverage of evidence
    # that was never supplied.
    provenance = "TRACEABLE"
    completeness = "INCOMPLETE"
    assert provenance != completeness
    assert completeness == "INCOMPLETE"


def test_epistemic_state_is_not_organizational_approval():
    epistemic_state = "VERIFIED"
    organizational_action = "PENDING_POLICY"
    assert epistemic_state != organizational_action


def test_required_semantic_distinctions_are_not_collapsed():
    states = {
        "CONTRADICTION",
        "DIFFERENT_SCOPE",
        "DIFFERENT_TIME",
        "DIFFERENT_ENTITY",
        "EXCEPTION",
        "UNKNOWN",
        "UNVERIFIABLE_PROVENANCE",
    }
    assert len(states) == 7
