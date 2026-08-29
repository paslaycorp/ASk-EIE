"""Minimal, dependency-light DPIE adapter contract.

This module intentionally contains no epistemic policy. It only defines the
translation boundary between untrusted business input and the DPIE core.
"""

from dataclasses import dataclass, field
from hashlib import sha256
from typing import Any, Mapping


@dataclass(frozen=True)
class EvidenceItem:
    evidence_id: str
    source: str
    claim: str
    content_hash: str
    observed_at: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class CanonicalEvidence:
    domain: str
    subject_id: str
    items: tuple[EvidenceItem, ...]
    adapter_version: str = "0.1"


@dataclass(frozen=True)
class AdapterDecision:
    decision: str
    reason_codes: tuple[str, ...]
    evidence_ids: tuple[str, ...]
    contradictions: tuple[str, ...] = ()
    gaps: tuple[str, ...] = ()
    provenance: str = "UNKNOWN"
    integrity: str = "UNKNOWN"


class VendorDueDiligenceAdapter:
    """Translate vendor-review records into canonical DPIE evidence.

    The adapter deliberately does not assign epistemic truth. Its job is
    ingestion, normalization, and presentation only.
    """

    DOMAIN = "vendor_due_diligence"
    VERSION = "0.1"

    def ingest(self, records: list[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
        if not isinstance(records, list):
            raise TypeError("records must be a list")
        return records

    def normalize(
        self, records: list[Mapping[str, Any]], subject_id: str
    ) -> CanonicalEvidence:
        if not subject_id or not isinstance(subject_id, str):
            raise ValueError("subject_id must be a non-empty string")

        items: list[EvidenceItem] = []
        for index, record in enumerate(records):
            if not isinstance(record, Mapping):
                raise TypeError(f"record {index} must be a mapping")

            claim = str(record.get("claim", "")).strip()
            source = str(record.get("source", "")).strip()
            if not claim or not source:
                raise ValueError(f"record {index} requires claim and source")

            raw = f"{source}\n{claim}".encode("utf-8")
            digest = sha256(raw).hexdigest()
            items.append(
                EvidenceItem(
                    evidence_id=str(record.get("evidence_id", f"ev-{index + 1}")),
                    source=source,
                    claim=claim,
                    content_hash=digest,
                    observed_at=record.get("observed_at"),
                    metadata=dict(record.get("metadata", {})),
                )
            )

        return CanonicalEvidence(
            domain=self.DOMAIN,
            subject_id=subject_id,
            items=tuple(items),
            adapter_version=self.VERSION,
        )

    def validate(self, envelope: CanonicalEvidence) -> None:
        if envelope.domain != self.DOMAIN:
            raise ValueError("unexpected domain")
        ids = [item.evidence_id for item in envelope.items]
        if len(ids) != len(set(ids)):
            raise ValueError("evidence IDs must be unique")
        for item in envelope.items:
            if len(item.content_hash) != 64:
                raise ValueError(f"invalid content hash: {item.evidence_id}")

    def evaluate(self, core_result: Mapping[str, Any]) -> AdapterDecision:
        """Consume core output without changing its epistemic fields."""
        return AdapterDecision(
            decision=str(core_result.get("decision", "DEFER")),
            reason_codes=tuple(core_result.get("reason_codes", ())),
            evidence_ids=tuple(core_result.get("evidence_ids", ())),
            contradictions=tuple(core_result.get("contradictions", ())),
            gaps=tuple(core_result.get("gaps", ())),
            provenance=str(core_result.get("provenance", "UNKNOWN")),
            integrity=str(core_result.get("integrity", "UNKNOWN")),
        )

    def render(self, decision: AdapterDecision) -> dict[str, Any]:
        return {
            "domain": self.DOMAIN,
            "decision": decision.decision,
            "reason_codes": list(decision.reason_codes),
            "evidence_ids": list(decision.evidence_ids),
            "contradictions": list(decision.contradictions),
            "gaps": list(decision.gaps),
            "provenance": decision.provenance,
            "integrity": decision.integrity,
        }
