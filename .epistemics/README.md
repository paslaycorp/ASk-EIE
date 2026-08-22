# Epistemic Adversary Framework

**Private Research Environment for Epistemic System Testing**

This directory contains private adversarial reasoning research. Everything here is excluded from version control via `.gitignore`.

## Quick Start

```bash
# Activate environment
source .epistemics/venv/bin/activate

# Run adversarial testing
python .epistemics/epistemic_adversary.py

# Generate remediation strategies (safe to commit)
python .epistemics/remediation_strategist.py
```

## Components

- `epistemic_adversary.py` - Full adversarial testing framework
- `attack_scenarios.yaml` - Detailed attack vector documentation  
- `remediation_strategist.py` - Convert findings into public hardening strategies
- `findings/` - Generated test results (local only, not tracked)

## Workflow

1. **Research Phase** - Run adversarial tests locally
2. **Analysis Phase** - Generate synthesis and findings
3. **Remediation Phase** - Run remediation strategist
4. **Disclosure Phase** - Share only the remediation report

## The Four Adversaries

1. **ConfidenceCalibrationAdversary** - Tests confidence drift and inversion
2. **ConsensusCorruptionAdversary** - Tests distributed consensus breaking
3. **JustificationChainAdversary** - Tests circular reasoning detection
4. **UncertaintyBlindSpotAdversary** - Tests unknown unknown exploitation

## Privacy

✅ **All .epistemics/ contents excluded from git**
✅ **Raw adversarial code stays private**
✅ **Remediation strategies can be shared publicly**
❌ **Never commit adversarial reasoning directly**
❌ **Never push .epistemics/ to shared repos**

## For Advanced Users

```bash
# Use git stash for extra privacy
git stash save 'epistemic research - local testing'

# Work on experiments...

# Recover when ready
git stash pop
```
