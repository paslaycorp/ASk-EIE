"""Minimal secure HTTP-facing boundary for the DPIE demo.

Framework-neutral by design: a host application can bind these functions to
FastAPI, Flask, an ASGI adapter, or another gateway without moving security
policy into domain adapters.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from .engine import run_vendor_demo

MAX_RECORDS = 100
MAX_CLAIM_LENGTH = 10_000


@dataclass(frozen=True)
class TenantContext:
    tenant_id: str
    authenticated: bool = True


def authorize(context: TenantContext, requested_tenant: str) -> None:
    if not context.authenticated:
        raise PermissionError("authentication required")
    if not context.tenant_id or context.tenant_id != requested_tenant:
        raise PermissionError("tenant authorization failed")


def validate_request(payload: Mapping[str, Any]) -> None:
    if not isinstance(payload, Mapping):
        raise TypeError("request body must be an object")
    subject_id = payload.get("subject_id")
    if not isinstance(subject_id, str) or not subject_id.strip():
        raise ValueError("subject_id is required")
    records = payload.get("records")
    if not isinstance(records, list) or len(records) > MAX_RECORDS:
        raise ValueError("records must be a bounded list")
    for record in records:
        if not isinstance(record, Mapping):
            raise ValueError("each record must be an object")
        claim = record.get("claim", "")
        if not isinstance(claim, str) or len(claim) > MAX_CLAIM_LENGTH:
            raise ValueError("claim is invalid or too large")


def verify_vendor_request(
    payload: Mapping[str, Any],
    context: TenantContext,
) -> dict[str, Any]:
    """Authorize, validate, and execute one tenant-scoped demo request."""
    validate_request(payload)
    authorize(context, str(payload["tenant_id"]))
    return run_vendor_demo(dict(payload))
