import json
from pathlib import Path

from dpie_fasttrack.contracts import VendorDueDiligenceAdapter


FIXTURE = Path(__file__).parents[1] / "examples" / "dpie_hostile_vendor_package.json"


def load_fixture():
    return json.loads(FIXTURE.read_text())


def test_hostile_fixture_preserves_every_evidence_item():
    payload = load_fixture()
    envelope = VendorDueDiligenceAdapter().normalize(payload["records"], payload["subject_id"])
    assert len(envelope.items) == len(payload["records"])
    assert {x.evidence_id for x in envelope.items} == {x["evidence_id"] for x in payload["records"]}


def test_provenance_does_not_equal_truth():
    payload = load_fixture()
    envelope = VendorDueDiligenceAdapter().normalize(payload["records"], payload["subject_id"])
    unverifiable = next(x for x in envelope.items if x.evidence_id == "forged")
    assert unverifiable.metadata["provenance"] == "unverifiable"
    assert unverifiable.claim.startswith("Vendor has never")
    # The adapter must preserve the claim; it must not upgrade it to VERIFIED.


def test_scope_difference_is_preserved_for_semantic_layer():
    payload = load_fixture()
    envelope = VendorDueDiligenceAdapter().normalize(payload["records"], payload["subject_id"])
    production = next(x for x in envelope.items if x.evidence_id == "sec-current")
    legacy = next(x for x in envelope.items if x.evidence_id == "legacy-encryption")
    assert production.metadata["scope"] == "production"
    assert legacy.metadata["scope"] == "development"
    # A downstream semantic engine must not infer contradiction from text alone.


def test_temporal_and_entity_context_survive_normalization():
    payload = load_fixture()
    envelope = VendorDueDiligenceAdapter().normalize(payload["records"], payload["subject_id"])
    retention = {x.evidence_id: x for x in envelope.items}
    assert retention["retention-contract"].metadata["legal_entity"] == "VendorCo LLC"
    assert retention["retention-policy"].metadata["legal_entity"] == "VendorCo Inc"
    assert retention["iso-expired"].metadata["expires"] == "2025-03-01"


def test_adapter_cannot_promote_unknown_by_construction():
    adapter = VendorDueDiligenceAdapter()
    result = adapter.evaluate({"decision": "DEFER", "provenance": "UNKNOWN", "integrity": "UNKNOWN"})
    assert result.provenance == "UNKNOWN"
    assert result.integrity == "UNKNOWN"
