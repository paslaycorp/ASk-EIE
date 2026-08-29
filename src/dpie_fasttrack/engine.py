"""Small deterministic DPIE demo engine.

This is intentionally a proving harness, not a replacement for the
Verification Kernel. It converts adapter evidence into explicit observations
and refuses to claim verification where the evidence is insufficient.
"""

from collections import defaultdict
from typing import Any

from .contracts import AdapterDecision, CanonicalEvidence


class DPIDemoEngine:
    """Exercise the adapter boundary with conservative decision rules."""

    def verify(self, envelope: CanonicalEvidence) -> AdapterDecision:
        claims: dict[str, list[str]] = defaultdict(list)
        for item in envelope.items:
            claims[item.claim.lower()].append(item.evidence_id)

        gaps: list[str] = []
        contradictions: list[str] = []
        reason_codes: list[str] = []

        if not envelope.items:
            gaps.append("NO_EVIDENCE")
            reason_codes.append("INSUFFICIENT_EVIDENCE")
            decision = "DEFER"
        else:
            # Demo-only contradiction heuristic. It is deliberately narrow;
            # production semantics belong to the Verification Kernel.
            sources = {item.source for item in envelope.items}
            if len(sources) == 1:
                gaps.append("SINGLE_SOURCE")
                reason_codes.append("LIMITED_CORROBORATION")

            has_ai_claim = any("train" in item.claim.lower() for item in envelope.items)
            if has_ai_claim and len(envelope.items) < 2:
                gaps.append("AI_CLAIM_NEEDS_CORROBORATION")

            if gaps:
                decision = "REVIEW_REQUIRED"
                reason_codes.append("EVIDENCE_GAPS")
            else:
                decision = "REVIEW_REQUIRED"
                reason_codes.append("DEMO_REQUIRES_CORE_VERIFICATION")

        return AdapterDecision(
            decision=decision,
            reason_codes=tuple(reason_codes),
            evidence_ids=tuple(item.evidence_id for item in envelope.items),
            contradictions=tuple(contradictions),
            gaps=tuple(gaps),
            provenance="TRACEABLE" if envelope.items else "UNKNOWN",
            integrity="DEGRADED" if gaps else "UNKNOWN",
        )


def run_vendor_demo(payload: dict[str, Any]) -> dict[str, Any]:
    from .contracts import VendorDueDiligenceAdapter

    adapter = VendorDueDiligenceAdapter()
    records = adapter.ingest(payload.get("records", []))
    envelope = adapter.normalize(records, payload["subject_id"])
    adapter.validate(envelope)
    result = DPIDemoEngine().verify(envelope)
    return adapter.render(result)
