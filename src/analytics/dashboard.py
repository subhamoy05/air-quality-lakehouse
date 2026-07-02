"""
dashboard.py
============

Computational Environmental Intelligence Framework (CEIF)

Analytics Dashboard

Responsibilities
----------------
1. Dataset Overview
2. AQI Dashboard
3. Weather Dashboard
4. Correlation Dashboard
5. Trend Dashboard
6. Station Dashboard
7. Generate Analytics Summary
"""

from __future__ import annotations

from .analytics import AnalyticsEngine
from .eda import ExploratoryDataAnalysis
from .correlation import CorrelationAnalysis
from .trends import TrendAnalysis


class AnalyticsDashboard:
    """
    Central Analytics Dashboard.

    Combines all analytics modules into a
    single interface.
    """

    def __init__(self):

        self.analytics = AnalyticsEngine()

        self.eda = ExploratoryDataAnalysis()

        self.correlation = CorrelationAnalysis()

        self.trends = TrendAnalysis()

    # =====================================================
    # Dataset Overview
    # =====================================================

    def dataset_overview(self):

        return {

            "dataset_info":

                self.analytics.dataset_info(),

            "stations":

                self.analytics.station_list(),

            "districts":

                self.analytics.district_list(),

            "date_range":

                self.analytics.date_range()

        }

    # =====================================================
    # AQI Dashboard
    # =====================================================

    def aqi_dashboard(self):

        return {

            "average":

                self.analytics.average_aqi(),

            "maximum":

                self.analytics.maximum_aqi(),

            "minimum":

                self.analytics.minimum_aqi(),

            "daily":

                self.analytics.daily_aqi(),

            "monthly":

                self.analytics.monthly_aqi(),

            "yearly":

                self.analytics.yearly_aqi()

        }

    # =====================================================
    # Weather Dashboard
    # =====================================================

    def weather_dashboard(self):

        return {

            "summary":

                self.analytics.weather_summary(),

            "temperature":

                self.analytics.temperature_trend(),

            "humidity":

                self.analytics.humidity_trend(),

            "pressure":

                self.analytics.pressure_trend(),

            "wind_speed":

                self.analytics.wind_speed_trend()

        }

    # =====================================================
    # Station Dashboard
    # =====================================================

    def station_dashboard(self):

        return {

            "ranking":

                self.analytics.station_ranking(),

            "top_polluted":

                self.analytics.top_polluted_stations(),

            "cleanest":

                self.analytics.cleanest_stations()

        }

    # =====================================================
    # Trend Dashboard
    # =====================================================

    def trend_dashboard(self):

        return self.trends.summary()

    # =====================================================
    # Correlation Dashboard
    # =====================================================

    def correlation_dashboard(self):

        return {

            "matrix":

                self.correlation.correlation_matrix(),

            "ranking":

                self.correlation.feature_ranking(),

            "summary":

                self.correlation.summary()

        }

    # =====================================================
    # EDA Dashboard
    # =====================================================

    def eda_dashboard(self):

        return {

            "shape":

                self.eda.shape(),

            "missing":

                self.eda.missing_values(),

            "duplicates":

                self.eda.duplicate_records(),

            "aqi":

                self.eda.aqi_statistics(),

            "weather":

                self.eda.weather_statistics()

        }

    # =====================================================
    # Complete Dashboard
    # =====================================================

    def dashboard(self):

        return {

            "overview":

                self.dataset_overview(),

            "aqi":

                self.aqi_dashboard(),

            "weather":

                self.weather_dashboard(),

            "stations":

                self.station_dashboard(),

            "correlation":

                self.correlation_dashboard(),

            "eda":

                self.eda_dashboard(),

            "trends":

                self.trend_dashboard()

        }

    # =====================================================
    # Utility
    # =====================================================

    def close(self):

        self.analytics.close()

        self.eda.close()

        self.correlation.close()

        self.trends.close()

    def __enter__(self):

        return self

    def __exit__(

        self,

        exc_type,

        exc_value,

        traceback

    ):

        self.close()


# ==========================================================
# Demo
# ==========================================================

if __name__ == "__main__":

    with AnalyticsDashboard() as dashboard:

        print("=" * 80)
        print("CEIF ANALYTICS DASHBOARD")
        print("=" * 80)

        overview = dashboard.dataset_overview()

        print("\nDataset Information")
        print(overview["dataset_info"])

        print("\nStations")
        print(overview["stations"].head())

        print("\nAQI Dashboard")
        print(
            dashboard.aqi_dashboard()["average"]
        )

        print("\nWeather Dashboard")
        print(
            dashboard.weather_dashboard()["summary"]
        )

        print("\nCorrelation Ranking")
        print(
            dashboard
            .correlation_dashboard()["ranking"]
            .head()
        )

        print("\nDashboard Ready")