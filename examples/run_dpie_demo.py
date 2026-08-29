"""Run the DPIE vendor demo without requiring a web framework."""

import json
from pathlib import Path

from dpie_fasttrack.api import TenantContext, verify_vendor_request


ROOT = Path(__file__).resolve().parents[1]
payload = json.loads((ROOT / "examples" / "dpie_vendor_demo.json").read_text())
payload["tenant_id"] = "demo-tenant"

result = verify_vendor_request(payload, TenantContext("demo-tenant"))
print(json.dumps(result, indent=2, sort_keys=True))
