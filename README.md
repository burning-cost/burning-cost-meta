# burning-cost

[![PyPI](https://img.shields.io/pypi/v/burning-cost)](https://pypi.org/project/burning-cost/)
[![Python](https://img.shields.io/pypi/pyversions/burning-cost)](https://pypi.org/project/burning-cost/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**One install. The full Burning Cost toolkit.**

```bash
pip install burning-cost
```

That single command installs all 10 flagship libraries for insurance pricing with modern ML.

---

## The problem this solves

The Burning Cost ecosystem has 10 libraries. They are designed to work together — causal inference to estimate treatment effects, conformal to put intervals on predictions, monitoring to track whether those predictions are still valid in production. But you should not have to remember which libraries to include in a requirements file when setting up a new pricing project or Colab notebook.

`burning-cost` is a meta-package: it has no code of its own. It is a single dependency that pulls in everything.

---

## What you get

| Library | What it does |
|---|---|
| `insurance-causal` | Double Machine Learning for causal treatment effects on observational data |
| `insurance-fairness` | Fairness auditing under UK Equality Act 2010 |
| `insurance-monitoring` | PSI/CSI drift, A/E monitoring, Gini tests, anytime-valid A/B testing |
| `insurance-conformal` | Distribution-free prediction intervals with coverage guarantees |
| `insurance-whittaker` | Whittaker-Henderson graduation for triangles and rating factors |
| `insurance-telematics` | Trip-level feature engineering and behavioural risk scoring |
| `insurance-credibility` | Buhlmann-Straub and hierarchical Bayesian credibility models |
| `insurance-frequency-severity` | Two-part freq/sev modelling with proper exposure handling |
| `insurance-gam` | Generalised Additive Models for interpretable rating factor curves |
| `insurance-governance` | FCA/PRA-aligned model risk management documentation |

---

## Usage

You do not import from `burning_cost` directly. Each library has its own namespace:

```python
from insurance_causal import CausalPricingModel
from insurance_conformal import InsuranceConformalPredictor
from insurance_monitoring import MonitoringReport
from insurance_fairness import FairnessAudit
```

The meta-package just ensures they are all installed.

---

## For new pricing projects

Add to your `pyproject.toml`:

```toml
[project]
dependencies = [
    "burning-cost",
]
```

Or for a requirements file:

```
burning-cost
catboost
polars
```

---

## Resources

- Website: [burning-cost.github.io](https://burning-cost.github.io)
- Examples: [github.com/burning-cost/burning-cost-examples](https://github.com/burning-cost/burning-cost-examples)
- 30-minute demo: [Colab notebook](https://colab.research.google.com/github/burning-cost/burning-cost-examples/blob/main/notebooks/burning_cost_30_minutes.ipynb)

---

## License

MIT
