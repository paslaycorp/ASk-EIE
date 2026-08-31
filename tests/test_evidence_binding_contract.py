import pytest

FORBIDDEN = {
    ("UNKNOWN", "VERIFIED"),
    ("UNKNOWN", "COMPLIANT"),
    ("INCOMPLETE", "COMPLETE"),
    ("EXCEPTION", "NO_EXCEPTION"),
    ("DIFFERENT_ENTITY", "SAME_ENTITY"),
    ("DIFFERENT_TIME", "CURRENT"),
    ("DIFFERENT_SCOPE", "SAME_SCOPE"),
    ("UNVERIFIABLE_PROVENANCE", "TRUSTED_PROVENANCE"),
}


def test_binding_basis_is_finite_and_explicit():
    assert {
        "EXPLICIT", "RULE_DERIVED", "EXTERNALLY_ATTESTED",
        "HUMAN_ASSERTED", "MODEL_SUGGESTED", "UNRESOLVED"
    }


def test_translation_cannot_authorize_promotion():
    for before, after in FORBIDDEN:
        with pytest.raises(AssertionError):
            if (before, after) in FORBIDDEN:
                raise AssertionError(f"unauthorized promotion: {before} -> {after}")


def test_provenance_is_not_coverage():
    assert ("TRACEABLE", "INCOMPLETE") != ("COMPLETE", "COMPLETE")


def test_unresolved_mapping_is_not_equivalence():
    mapping = "UNRESOLVED"
    assert mapping not in {"SAME_ENTITY", "SAME_SCOPE", "CURRENT"}
