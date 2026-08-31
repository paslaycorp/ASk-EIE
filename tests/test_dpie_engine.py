from dpie_fasttrack.engine import run_vendor_demo


def test_vendor_demo_exposes_traceability_and_gaps():
    result = run_vendor_demo(
        {
            "subject_id": "vendor-001",
            "records": [
                {"evidence_id": "e1", "source": "security", "claim": "Independent assessment exists"},
                {"evidence_id": "e2", "source": "contract", "claim": "Data processing responsibilities are defined"},
            ],
        }
    )
    assert result["decision"] == "REVIEW_REQUIRED"
    assert result["provenance"] == "TRACEABLE"
    assert result["evidence_ids"] == ["e1", "e2"]


def test_empty_vendor_package_defers():
    result = run_vendor_demo({"subject_id": "vendor-empty", "records": []})
    assert result["decision"] == "DEFER"
    assert "NO_EVIDENCE" in result["gaps"]
    assert result["provenance"] == "UNKNOWN"


def test_ai_claim_without_corroboration_is_review_required():
    result = run_vendor_demo(
        {
            "subject_id": "vendor-ai",
            "records": [
                {"evidence_id": "ai1", "source": "questionnaire", "claim": "Customer data is not used to train models"}
            ],
        }
    )
    assert result["decision"] == "REVIEW_REQUIRED"
    assert "AI_CLAIM_NEEDS_CORROBORATION" in result["gaps"]
