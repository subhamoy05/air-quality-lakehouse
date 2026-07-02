"""
trends.py
=========

Computational Environmental Intelligence Framework (CEIF)

Trend Analysis

Responsibilities
----------------
1. Hourly AQI Trend
2. Daily AQI Trend
3. Weekly AQI Trend
4. Monthly AQI Trend
5. Yearly AQI Trend
6. Seasonal AQI Trend
7. Temperature Trend
8. Humidity Trend
9. Pressure Trend
10. Wind Speed Trend
11. Station Comparison
"""

from __future__ import annotations

import pandas as pd

from .loader import DatasetLoader
from . import queries


class TrendAnalysis:
    """
    Trend Analysis Module.
    """

    def __init__(self):

        self.loader = DatasetLoader()

    # =====================================================
    # Generic Query
    # =====================================================

    def query(self, sql: str) -> pd.DataFrame:

        return self.loader.query(sql)

    # =====================================================
    # AQI Trends
    # =====================================================

    def hourly(self):

        return self.query(
            queries.HOURLY_AQI
        )

    def daily(self):

        return self.query(
            queries.DAILY_AQI
        )

    def monthly(self):

        return self.query(
            queries.MONTHLY_AQI
        )

    def yearly(self):

        return self.query(
            queries.YEARLY_AQI
        )

    # =====================================================
    # Weekly Trend
    # =====================================================

    def weekly(self):

        sql = """
        SELECT

            YEAR(datetime) AS year,

            WEEK(datetime) AS week,

            ROUND(AVG(aqi),2) AS average_aqi

        FROM environmental_master

        GROUP BY

            year,

            week

        ORDER BY

            year,

            week;
        """

        return self.query(sql)

    # =====================================================
    # Seasonal Trend
    # =====================================================

    def seasonal(self):

        sql = """
        SELECT

            CASE

                WHEN MONTH(datetime) IN (12,1,2)
                    THEN 'Winter'

                WHEN MONTH(datetime) IN (3,4,5)
                    THEN 'Summer'

                WHEN MONTH(datetime) IN (6,7,8,9)
                    THEN 'Monsoon'

                ELSE 'Post-Monsoon'

            END AS season,

            ROUND(AVG(aqi),2) AS average_aqi,

            ROUND(AVG(pm25),2) AS average_pm25,

            ROUND(AVG(pm10),2) AS average_pm10

        FROM environmental_master

        GROUP BY season

        ORDER BY average_aqi DESC;
        """

        return self.query(sql)

    # =====================================================
    # Weather Trends
    # =====================================================

    def temperature(self):

        return self.query(
            queries.TEMPERATURE_TREND
        )

    def humidity(self):

        return self.query(
            queries.HUMIDITY_TREND
        )

    def pressure(self):

        return self.query(
            queries.PRESSURE_TREND
        )

    def wind_speed(self):

        return self.query(
            queries.WIND_SPEED_TREND
        )

    # =====================================================
    # PM Trends
    # =====================================================

    def pm25(self):

        return self.query(
            queries.PM25_DAILY
        )

    def pm10(self):

        return self.query(
            queries.PM10_DAILY
        )

    # =====================================================
    # Station Comparison
    # =====================================================

    def station_comparison(self):

        return self.query(
            queries.STATION_RANKING
        )

    # =====================================================
    # Trend Summary
    # =====================================================

    def summary(self):

        return {

            "Hourly AQI":
                self.hourly(),

            "Daily AQI":
                self.daily(),

            "Weekly AQI":
                self.weekly(),

            "Monthly AQI":
                self.monthly(),

            "Yearly AQI":
                self.yearly(),

            "Seasonal AQI":
                self.seasonal(),

            "Temperature":
                self.temperature(),

            "Humidity":
                self.humidity(),

            "Pressure":
                self.pressure(),

            "Wind Speed":
                self.wind_speed(),

            "PM2.5":
                self.pm25(),

            "PM10":
                self.pm10(),

            "Station Comparison":
                self.station_comparison()
        }

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

    with TrendAnalysis() as trends:

        print("=" * 80)
        print("TREND ANALYSIS")
        print("=" * 80)

        print("\nHourly AQI")
        print(trends.hourly().head())

        print("\nDaily AQI")
        print(trends.daily().head())

        print("\nWeekly AQI")
        print(trends.weekly().head())

        print("\nMonthly AQI")
        print(trends.monthly().head())

        print("\nYearly AQI")
        print(trends.yearly().head())

        print("\nSeasonal AQI")
        print(trends.seasonal())

        print("\nTemperature Trend")
        print(trends.temperature().head())

        print("\nHumidity Trend")
        print(trends.humidity().head())

        print("\nPressure Trend")
        print(trends.pressure().head())

        print("\nWind Speed Trend")
        print(trends.wind_speed().head())

        print("\nStation Comparison")
        print(trends.station_comparison().head())