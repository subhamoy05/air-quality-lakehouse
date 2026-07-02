"""
analytics.py
============

Computational Environmental Intelligence Framework (CEIF)

Analytics Engine

Responsibilities
----------------
1. Execute DuckDB SQL Queries
2. Dataset Analytics
3. AQI Analytics
4. PM Analytics
5. Weather Analytics
6. Station Analytics
7. Correlation Dataset
8. Forecast Dataset
"""

from __future__ import annotations

import pandas as pd

from .loader import DatasetLoader
from . import queries


class AnalyticsEngine:
    """
    Main Analytics Engine.

    This class acts as the central interface
    for all analytics operations.
    """

    def __init__(self):

        self.loader = DatasetLoader()

    # =====================================================
    # Generic Query
    # =====================================================

    def query(
        self,
        sql: str
    ) -> pd.DataFrame:

        return self.loader.query(sql)

    # =====================================================
    # Master Dataset
    # =====================================================

    def environmental_master(self):

        return self.loader.environmental_master()

    # =====================================================
    # Metadata
    # =====================================================

    def dataset_info(self):

        return self.query(
            queries.DATASET_INFO
        )

    def station_list(self):

        return self.query(
            queries.STATION_LIST
        )

    def district_list(self):

        return self.query(
            queries.DISTRICT_LIST
        )

    def date_range(self):

        return self.query(
            queries.DATE_RANGE
        )

    # =====================================================
    # AQI Analytics
    # =====================================================

    def average_aqi(self):

        return self.query(
            queries.AVERAGE_AQI
        )

    def maximum_aqi(self):

        return self.query(
            queries.MAXIMUM_AQI
        )

    def minimum_aqi(self):

        return self.query(
            queries.MINIMUM_AQI
        )

    def aqi_by_station(self):

        return self.query(
            queries.AQI_BY_STATION
        )

    def aqi_by_district(self):

        return self.query(
            queries.AQI_BY_DISTRICT
        )

    def daily_aqi(self):

        return self.query(
            queries.DAILY_AQI
        )

    def monthly_aqi(self):

        return self.query(
            queries.MONTHLY_AQI
        )

    def yearly_aqi(self):

        return self.query(
            queries.YEARLY_AQI
        )

    def hourly_aqi(self):

        return self.query(
            queries.HOURLY_AQI
        )

    # =====================================================
    # PM Analytics
    # =====================================================

    def pm25_daily(self):

        return self.query(
            queries.PM25_DAILY
        )

    def pm10_daily(self):

        return self.query(
            queries.PM10_DAILY
        )

    def pm_summary(self):

        return self.query(
            queries.PM_SUMMARY
        )

    # =====================================================
    # Weather Analytics
    # =====================================================

    def weather_summary(self):

        return self.query(
            queries.WEATHER_SUMMARY
        )

    def temperature_trend(self):

        return self.query(
            queries.TEMPERATURE_TREND
        )

    def humidity_trend(self):

        return self.query(
            queries.HUMIDITY_TREND
        )

    def pressure_trend(self):

        return self.query(
            queries.PRESSURE_TREND
        )

    def wind_speed_trend(self):

        return self.query(
            queries.WIND_SPEED_TREND
        )

    # =====================================================
    # Station Analytics
    # =====================================================

    def station_ranking(self):

        return self.query(
            queries.STATION_RANKING
        )

    def top_polluted_stations(self):

        return self.query(
            queries.TOP_10_POLLUTED
        )

    def cleanest_stations(self):

        return self.query(
            queries.TOP_10_CLEANEST
        )

    # =====================================================
    # Correlation
    # =====================================================

    def correlation_dataset(self):

        return self.query(
            queries.CORRELATION_DATASET
        )

    # =====================================================
    # Forecasting
    # =====================================================

    def forecast_dataset(self):

        return self.query(
            queries.FORECAST_DATASET
        )

    def ml_dataset(self):

        return self.query(
            queries.ML_DATASET
        )

    # =====================================================
    # Utility
    # =====================================================

    def close(self):

        self.loader.close()

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

    with AnalyticsEngine() as analytics:

        print("=" * 80)
        print("CEIF Analytics Engine")
        print("=" * 80)

        print("\nDataset Information")
        print(analytics.dataset_info())

        print("\nStations")
        print(analytics.station_list())

        print("\nAverage AQI")
        print(analytics.average_aqi())

        print("\nAQI By Station")
        print(analytics.aqi_by_station().head())

        print("\nDaily AQI")
        print(analytics.daily_aqi().head())

        print("\nMonthly AQI")
        print(analytics.monthly_aqi().head())

        print("\nWeather Summary")
        print(analytics.weather_summary())

        print("\nTop Polluted Stations")
        print(analytics.top_polluted_stations())