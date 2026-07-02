"""
analytics/__init__.py
=====================

Computational Environmental Intelligence Framework (CEIF)

Analytics Package

This package provides tools for:

- Dataset Loading
- DuckDB Analytics
- SQL Query Library
- Exploratory Data Analysis (EDA)
- Correlation Analysis
- Trend Analysis
- Visualization
- Report Generation
- Data Export
- Dashboard

Author
------
Computational Environmental Intelligence Framework (CEIF)

"""

# ==========================================================
# Dataset Loader
# ==========================================================

from .loader import DatasetLoader

# ==========================================================
# DuckDB Analytics Engine
# ==========================================================

from .analytics import AnalyticsEngine

# ==========================================================
# Exploratory Data Analysis
# ==========================================================

from .eda import ExploratoryDataAnalysis

# ==========================================================
# Correlation Analysis
# ==========================================================

from .correlation import CorrelationAnalysis

# ==========================================================
# Trend Analysis
# ==========================================================

from .trends import TrendAnalysis

# ==========================================================
# Visualization Utilities
# ==========================================================

from .plots import Visualization

# ==========================================================
# Report Generation
# ==========================================================

from .reports import AnalyticsReportGenerator

# ==========================================================
# Export Utilities
# ==========================================================

from .exporter import DataExporter

# ==========================================================
# Analytics Dashboard
# ==========================================================

from .dashboard import AnalyticsDashboard

# ==========================================================
# Version Information
# ==========================================================

__version__ = "1.0.0"

__author__ = "CEIF Project"

__license__ = "MIT"

# ==========================================================
# Public API
# ==========================================================

__all__ = [

    # Dataset Loader
    "DatasetLoader",

    # Analytics
    "AnalyticsEngine",

    # EDA
    "ExploratoryDataAnalysis",

    # Correlation
    "CorrelationAnalysis",

    # Trend Analysis
    "TrendAnalysis",

    # Visualization
    "Visualization",

    # Reports
    "AnalyticsReportGenerator",

    # Export
    "DataExporter",

    # Dashboard
    "AnalyticsDashboard",
]