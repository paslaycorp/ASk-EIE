#!/bin/bash
# Private Epistemic Adversary Research Environment Setup
# Run this to initialize the private testing framework

echo "=== Epistemic Adversary Framework Setup ==="
echo ""

# Create directory structure
mkdir -p .epistemics/findings
mkdir -p .epistemics/reasoning_logs
mkdir -p .epistemics/test_results

echo "✓ Created .epistemics/ directory structure"

# Create Python virtual environment
python3 -m venv .epistemics/venv
source .epistemics/venv/bin/activate

echo "✓ Created isolated Python environment"

# Install requirements
pip install -q pydantic pyyaml dataclasses-json

echo "✓ Installed dependencies"

echo ""
echo "=== Setup Complete ==="
echo ""
echo "To use the epistemic adversary framework:"
echo ""
echo "1. Activate the environment:"
echo "   source .epistemics/venv/bin/activate"
echo ""
echo "2. Run adversarial testing:"
echo "   python .epistemics/epistemic_adversary.py"
echo ""
echo "3. Generate remediation strategies:"
echo "   python .epistemics/remediation_strategist.py"
echo ""
echo "4. Review findings (local only, not tracked):"
echo "   ls -la .epistemics/findings/"
echo ""
echo "WARNING: .epistemics/ is excluded from git."
echo "Do not commit research findings directly."
echo ""
