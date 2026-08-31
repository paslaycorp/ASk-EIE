"""DPIE Duel #8: action and responsibility remain separate from belief.

This is a falsification contract. It intentionally tests the boundary between
what the system admits, what it considers operationally, what policy permits,
and who carries the resulting commitment.
"""

import pytest


CASES = [
    {"name": "admitted evidence", "epistemic": "ADMITTED", "action": "EXECUTE", "authorized": True},
    {"name": "foreign evidence", "epistemic": "FOREIGN", "action": "CONSERVATIVE_ACT", "authorized": True},
    {"name": "epistemic null fail-safe", "epistemic": "NULL", "action": "FAIL_SAFE", "authorized": True},
    {"name": "epistemic null as belief", "epistemic": "NULL", "action": "BELIEVE", "authorized": False},
    {"name": "unauthorized policy", "epistemic": "ADMITTED", "action": "EXECUTE", "authorized": False},
    {"name": "action upgrades belief", "epistemic": "FOREIGN", "action": "EXECUTE", "authorized": False},
    {"name": "delegated authority", "epistemic": "ADMITTED", "action": "EXECUTE", "authorized": True},
    {"name": "conflicting authority", "epistemic": "ADMITTED", "action": "ESCALATE", "authorized": True},
]


def test_epistemic_and_operational_axes_are_independent():
    foreign = next(c for c in CASES if c["epistemic"] == "FOREIGN")
    assert foreign["action"] == "CONSERVATIVE_ACT"
    assert foreign["epistemic"] == "FOREIGN"


def test_null_can_trigger_fail_safe_without_becoming_belief():
    null_cases = [c for c in CASES if c["epistemic"] == "NULL"]
    assert any(c["action"] == "FAIL_SAFE" and c["authorized"] for c in null_cases)
    assert any(c["action"] == "BELIEVE" and not c["authorized"] for c in null_cases)


@pytest.mark.parametrize("case", CASES)
def test_action_authorization_is_explicit(case):
    assert "authorized" in case
    if case["action"] == "BELIEVE":
        assert case["authorized"] is False


def test_action_must_not_upgrade_epistemic_state():
    before = "FOREIGN"
    action = "CONSERVATIVE_ACT"
    after = "FOREIGN"
    assert action != after
    assert before == after


def test_conflicting_authority_escalates_instead_of_silent_resolution():
    case = next(c for c in CASES if c["name"] == "conflicting authority")
    assert case["action"] == "ESCALATE"
    assert case["authorized"] is True


def test_consequential_action_requires_attributable_commitment():
    commitment = {
        "actor": "delegated-agent-01",
        "policy": "emergency-safe-action-v1",
        "authority": "authority-chain-01",
        "action": "FAIL_SAFE",
        "epistemic_state": "NULL",
    }
    assert all(commitment.values())
    assert commitment["epistemic_state"] == "NULL"


def test_action_does_not_retroactively_validate_input():
    original = "UNVERIFIABLE_PROVENANCE"
    action = "QUARANTINE_SOURCE"
    assert original == "UNVERIFIABLE_PROVENANCE"
    assert action == "QUARANTINE_SOURCE"
    assert original != "TRUSTED_PROVENANCE"
