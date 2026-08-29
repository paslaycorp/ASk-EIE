import pytest

from dpie_fasttrack.api import TenantContext, verify_vendor_request


def payload(tenant_id="tenant-a"):
    return {
        "tenant_id": tenant_id,
        "subject_id": "vendor-001",
        "records": [
            {"evidence_id": "e1", "source": "security", "claim": "Independent assessment exists"}
        ],
    }


def test_authenticated_tenant_can_verify():
    result = verify_vendor_request(payload(), TenantContext("tenant-a"))
    assert result["domain"] == "vendor_due_diligence"
    assert result["evidence_ids"] == ["e1"]


def test_cross_tenant_request_is_denied():
    with pytest.raises(PermissionError):
        verify_vendor_request(payload("tenant-b"), TenantContext("tenant-a"))


def test_unauthenticated_request_is_denied():
    with pytest.raises(PermissionError):
        verify_vendor_request(payload(), TenantContext("tenant-a", authenticated=False))


def test_oversized_claim_is_rejected():
    body = payload()
    body["records"][0]["claim"] = "x" * 10_001
    with pytest.raises(ValueError):
        verify_vendor_request(body, TenantContext("tenant-a"))


def test_record_count_is_bounded():
    body = payload()
    body["records"] = [body["records"][0]] * 101
    with pytest.raises(ValueError):
        verify_vendor_request(body, TenantContext("tenant-a"))
