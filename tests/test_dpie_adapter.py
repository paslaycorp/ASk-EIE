from dpie_fasttrack import VendorDueDiligenceAdapter


def test_normalize_is_traceable_and_hashed():
    adapter = VendorDueDiligenceAdapter()
    envelope = adapter.normalize(
        [
            {
                "evidence_id": "soc2-1",
                "source": "vendor-security-report",
                "claim": "SOC 2 report exists",
                "observed_at": "2026-08-29T00:00:00Z",
            }
        ],
        "vendor-001",
    )
    adapter.validate(envelope)
    assert envelope.domain == "vendor_due_diligence"
    assert envelope.subject_id == "vendor-001"
    assert envelope.items[0].evidence_id == "soc2-1"
    assert len(envelope.items[0].content_hash) == 64


def test_invalid_input_fails_closed():
    adapter = VendorDueDiligenceAdapter()
    try:
        adapter.normalize([{"source": "only-source"}], "vendor-001")
    except ValueError:
        return
    raise AssertionError("invalid evidence must be rejected")


def test_adapter_does_not_override_core_semantics():
    adapter = VendorDueDiligenceAdapter()
    result = adapter.evaluate(
        {
            "decision": "QUARANTINE",
            "provenance": "TRACEABLE",
            "integrity": "DEGRADED",
            "reason_codes": ["CONFLICT"],
            "evidence_ids": ["ev-1"],
        }
    )
    assert result.decision == "QUARANTINE"
    assert result.provenance == "TRACEABLE"
    assert result.integrity == "DEGRADED"
