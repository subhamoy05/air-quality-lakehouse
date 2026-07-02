"""
demo.py
=======

Computational Environmental Intelligence Framework (CEIF)

Analytics Engine Demonstration

Runs the complete Analytics Engine.

Usage
-----
python -m src.analytics.demo
"""

from __future__ import annotations

from .analytics import AnalyticsEngine
from .eda import ExploratoryDataAnalysis
from .correlation import CorrelationAnalysis
from .trends import TrendAnalysis
from .plots import Visualization
from .reports import AnalyticsReportGenerator


def main():

    print("=" * 80)
    print("COMPUTATIONAL ENVIRONMENTAL INTELLIGENCE FRAMEWORK")
    print("Analytics Engine Demo")
    print("=" * 80)

    # =====================================================
    # Analytics Engine
    # =====================================================

    analytics = AnalyticsEngine()

    print("\nDataset Information")
    print("-" * 80)
    print(analytics.dataset_info())

    print("\nStation List")
    print("-" * 80)
    print(analytics.station_list().head())

    print("\nAverage AQI")
    print("-" * 80)
    print(analytics.average_aqi())

    print("\nStation Ranking")
    print("-" * 80)
    print(analytics.station_ranking().head())

    print("\nWeather Summary")
    print("-" * 80)
    print(analytics.weather_summary())

    # =====================================================
    # EDA
    # =====================================================

    eda = ExploratoryDataAnalysis()

    print("\nEDA")
    print("-" * 80)

    print("Shape")
    print(eda.shape())

    print("\nMissing Values")
    print(eda.missing_values().head())

    print("\nDuplicate Records")
    print(eda.duplicate_records())

    # =====================================================
    # Correlation
    # =====================================================

    correlation = CorrelationAnalysis()

    print("\nCorrelation Matrix")
    print("-" * 80)

    print(correlation.correlation_matrix())

    print("\nAQI Feature Ranking")
    print(correlation.feature_ranking())

    # =====================================================
    # Trends
    # =====================================================

    trends = TrendAnalysis()

    print("\nDaily AQI")
    print("-" * 80)

    daily = trends.daily()

    print(daily.head())

    print("\nMonthly AQI")
    print("-" * 80)

    print(trends.monthly().head())

    # =====================================================
    # Visualization
    # =====================================================

    plots = Visualization()

    dataset = analytics.environmental_master()

    print("\nGenerating Visualizations...")
    print("-" * 80)

    plots.histogram(
        dataset,
        "aqi",
        filename="aqi_histogram.png"
    )

    plots.box_plot(
        dataset,
        "aqi",
        filename="aqi_boxplot.png"
    )

    plots.correlation_heatmap(
        dataset,
        filename="correlation_heatmap.png"
    )

    plots.aqi_vs_pm25(
        dataset,
        filename="aqi_vs_pm25.png"
    )

    plots.station_comparison(
        analytics.station_ranking(),
        filename="station_comparison.png"
    )

    plots.aqi_trend(
        analytics.daily_aqi(),
        filename="daily_aqi.png"
    )

    print("Visualization Complete")

    # =====================================================
    # Reports
    # =====================================================

    print("\nGenerating Reports...")
    print("-" * 80)

    reports = AnalyticsReportGenerator()

    reports.generate_all_reports()

    print("Reports Generated")

    # =====================================================
    # Close
    # =====================================================

    analytics.close()
    eda.close()
    correlation.close()
    trends.close()

    print("\n" + "=" * 80)
    print("Analytics Engine Completed Successfully")
    print("=" * 80)


if __name__ == "__main__":

    main()