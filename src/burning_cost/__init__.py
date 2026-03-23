"""
burning-cost: the full Burning Cost insurance pricing toolkit.

This is a meta-package. Installing it gives you all 10 flagship libraries
from the Burning Cost ecosystem in one go:

    pip install burning-cost

Libraries included
------------------
insurance-causal
    Double Machine Learning for causal effect estimation. Isolates the causal
    effect of price changes, telematics, and other treatments from selection bias
    in observational insurance data.

insurance-fairness
    Fairness auditing for insurance pricing models. Tests for indirect
    discrimination on protected characteristics under UK Equality Act 2010.

insurance-monitoring
    Model drift detection and monitoring. PSI/CSI feature drift, A/E ratio
    monitoring, Gini discrimination tests, Murphy decomposition, anytime-valid
    A/B testing, and PIT-based sequential calibration monitoring.

insurance-conformal
    Distribution-free prediction intervals with coverage guarantees. Pearson-
    weighted nonconformity scores for Poisson/Tweedie count data, locally-weighted
    conformal, conformal risk control for premium sufficiency, and Solvency II
    SCR bounds.

insurance-whittaker
    Whittaker-Henderson graduation for claim development triangles and rating
    factor smoothing. The actuarial workhorse, properly implemented.

insurance-telematics
    Telematics trip-level feature engineering and behavioural risk scoring.
    Speed profiles, harsh event detection, and mileage-adjusted frequency models.

insurance-credibility
    Credibility weighting and hierarchical Bayesian models for thin-data
    rating factors. Buhlmann-Straub and hierarchical GLM approaches.

insurance-frequency-severity
    Two-part frequency/severity modelling. Poisson/Tweedie GLMs with proper
    exposure handling, offset terms, and model diagnostics.

insurance-gam
    Generalised Additive Models for insurance pricing. Interpretable smooth
    terms for continuous rating factors, with visualisation utilities.

insurance-governance
    Model governance documentation and audit trail generation. FCA/PRA-aligned
    model risk management outputs from fitted pricing models.

Usage
-----
You do not import from ``burning_cost`` directly — import from the individual
libraries as needed::

    from insurance_causal import CausalPricingModel
    from insurance_conformal import InsuranceConformalPredictor
    from insurance_monitoring import MonitoringReport

See https://burning-cost.github.io for full documentation and examples.
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("burning-cost")
except PackageNotFoundError:
    __version__ = "0.0.0"

__all__ = ["__version__"]
