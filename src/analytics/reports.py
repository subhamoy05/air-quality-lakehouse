"""
reports.py
==========

Computational Environmental Intelligence Framework (CEIF)

Analytics Report Generator

Responsibilities
----------------
1. Dataset Reports
2. EDA Reports
3. AQI Reports
4. Weather Reports
5. Export Reports
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from .analytics import AnalyticsEngine
from .eda import ExploratoryDataAnalysis
from .correlation import CorrelationAnalysis
from .trends import TrendAnalysis
from .exporter import DataExporter


class AnalyticsReportGenerator:
    """
    Analytics Report Generator.
    """

    def __init__(

        self,

        output_directory: str = "reports/analytics"

    ):

        self.output_directory = Path(
            output_directory
        )

        self.output_directory.mkdir(

            parents=True,

            exist_ok=True

        )

        self.analytics = AnalyticsEngine()

        self.eda = ExploratoryDataAnalysis()

        self.correlation = CorrelationAnalysis()

        self.trends = TrendAnalysis()

        self.exporter = DataExporter(
            self.output_directory
        )

    # =====================================================
    # Dataset Summary
    # =====================================================

    def dataset_summary(self):

        df = pd.DataFrame([

            self.eda.quality_report()

        ])

        self.exporter.to_csv(

            df,

            "dataset_summary.csv"

        )

        self.exporter.to_excel(

            df,

            "dataset_summary.xlsx"

        )

        return df

    # =====================================================
    # Missing Values
    # =====================================================

    def missing_values_report(self):

        df = self.eda.missing_values()

        self.exporter.to_csv(

            df,

            "missing_values.csv"

        )

        self.exporter.to_excel(

            df,

            "missing_values.xlsx"

        )

        return df

    # =====================================================
    # Duplicate Records
    # =====================================================

    def duplicate_report(self):

        duplicates = pd.DataFrame({

            "Duplicate Records": [

                self.eda.duplicate_records()

            ]

        })

        self.exporter.to_csv(

            duplicates,

            "duplicate_records.csv"

        )

        self.exporter.to_excel(

            duplicates,

            "duplicate_records.xlsx"

        )

        return duplicates

    # =====================================================
    # AQI Summary
    # =====================================================

    def average_aqi_report(self):

        df = self.analytics.average_aqi()

        self.exporter.to_csv(

            df,

            "average_aqi.csv"

        )

        self.exporter.to_excel(

            df,

            "average_aqi.xlsx"

        )

        return df

    # =====================================================
    # Maximum AQI
    # =====================================================

    def maximum_aqi_report(self):

        df = self.analytics.maximum_aqi()

        self.exporter.to_csv(

            df,

            "maximum_aqi.csv"

        )

        self.exporter.to_excel(

            df,

            "maximum_aqi.xlsx"

        )

        return df

    # =====================================================
    # Minimum AQI
    # =====================================================

    def minimum_aqi_report(self):

        df = self.analytics.minimum_aqi()

        self.exporter.to_csv(

            df,

            "minimum_aqi.csv"

        )

        self.exporter.to_excel(

            df,

            "minimum_aqi.xlsx"

        )

        return df

    # =====================================================
    # Daily AQI
    # =====================================================

    def daily_aqi_report(self):

        df = self.analytics.daily_aqi()

        self.exporter.to_csv(

            df,

            "daily_aqi.csv"

        )

        self.exporter.to_excel(

            df,

            "daily_aqi.xlsx"

        )

        return df

    # =====================================================
    # Monthly AQI
    # =====================================================

    def monthly_aqi_report(self):

        df = self.analytics.monthly_aqi()

        self.exporter.to_csv(

            df,

            "monthly_aqi.csv"

        )

        self.exporter.to_excel(

            df,

            "monthly_aqi.xlsx"

        )

        return df

    # =====================================================
    # Yearly AQI
    # =====================================================

    def yearly_aqi_report(self):

        df = self.analytics.yearly_aqi()

        self.exporter.to_csv(

            df,

            "yearly_aqi.csv"

        )

        self.exporter.to_excel(

            df,

            "yearly_aqi.xlsx"

        )

        return df

    # =====================================================
    # Weather Summary
    # =====================================================

    def weather_summary_report(self):

        df = self.analytics.weather_summary()

        self.exporter.to_csv(

            df,

            "weather_summary.csv"

        )

        self.exporter.to_excel(

            df,

            "weather_summary.xlsx"

        )

        return df

    # =====================================================
    # Temperature Trend
    # =====================================================

    def temperature_report(self):

        df = self.analytics.temperature_trend()

        self.exporter.to_csv(

            df,

            "temperature_trend.csv"

        )

        self.exporter.to_excel(

            df,

            "temperature_trend.xlsx"

        )

        return df

    # =====================================================
    # Humidity Trend
    # =====================================================

    def humidity_report(self):

        df = self.analytics.humidity_trend()

        self.exporter.to_csv(

            df,

            "humidity_trend.csv"

        )

        self.exporter.to_excel(

            df,

            "humidity_trend.xlsx"

        )

        return df
    
    # =====================================================
    # Pressure Trend
    # =====================================================

    def pressure_report(self):

        df = self.analytics.pressure_trend()

        self.exporter.to_csv(
            df,
            "pressure_trend.csv"
        )

        self.exporter.to_excel(
            df,
            "pressure_trend.xlsx"
        )

        return df

    # =====================================================
    # Wind Speed Trend
    # =====================================================

    def wind_speed_report(self):

        df = self.analytics.wind_speed_trend()

        self.exporter.to_csv(
            df,
            "wind_speed_trend.csv"
        )

        self.exporter.to_excel(
            df,
            "wind_speed_trend.xlsx"
        )

        return df

    # =====================================================
    # PM2.5 Trend
    # =====================================================

    def pm25_report(self):

        df = self.analytics.pm25_daily()

        self.exporter.to_csv(
            df,
            "pm25_trend.csv"
        )

        self.exporter.to_excel(
            df,
            "pm25_trend.xlsx"
        )

        return df

    # =====================================================
    # PM10 Trend
    # =====================================================

    def pm10_report(self):

        df = self.analytics.pm10_daily()

        self.exporter.to_csv(
            df,
            "pm10_trend.csv"
        )

        self.exporter.to_excel(
            df,
            "pm10_trend.xlsx"
        )

        return df

    # =====================================================
    # Station Ranking
    # =====================================================

    def station_ranking_report(self):

        df = self.analytics.station_ranking()

        self.exporter.to_csv(
            df,
            "station_ranking.csv"
        )

        self.exporter.to_excel(
            df,
            "station_ranking.xlsx"
        )

        return df

    # =====================================================
    # Correlation Matrix
    # =====================================================

    def correlation_report(self):

        df = self.correlation.correlation_matrix()

        self.exporter.to_csv(
            df,
            "correlation_matrix.csv"
        )

        self.exporter.to_excel(
            df,
            "correlation_matrix.xlsx"
        )

        return df

    # =====================================================
    # AQI Correlation Ranking
    # =====================================================

    def aqi_correlation_report(self):

        df = self.correlation.feature_ranking()

        self.exporter.to_csv(
            df,
            "aqi_correlation.csv"
        )

        self.exporter.to_excel(
            df,
            "aqi_correlation.xlsx"
        )

        return df

    # =====================================================
    # Trend Summary
    # =====================================================

    def trend_summary_report(self):

        summary = self.trends.summary()

        for name, dataframe in summary.items():

            if hasattr(dataframe, "to_csv"):

                filename = (

                    name.lower()

                    .replace(" ", "_")

                    + ".csv"

                )

                self.exporter.to_csv(
                    dataframe,
                    filename
                )

        return summary

    # =====================================================
    # Generate All Reports
    # =====================================================

    def generate_all_reports(self):

        print("=" * 80)
        print("Generating Analytics Reports")
        print("=" * 80)

        self.dataset_summary()

        self.missing_values_report()

        self.duplicate_report()

        self.average_aqi_report()

        self.maximum_aqi_report()

        self.minimum_aqi_report()

        self.daily_aqi_report()

        self.monthly_aqi_report()

        self.yearly_aqi_report()

        self.weather_summary_report()

        self.temperature_report()

        self.humidity_report()

        self.pressure_report()

        self.wind_speed_report()

        self.pm25_report()

        self.pm10_report()

        self.station_ranking_report()

        self.correlation_report()

        self.aqi_correlation_report()

        self.trend_summary_report()

        print("\nAll reports generated successfully.")

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

    with AnalyticsReportGenerator() as reports:

        reports.generate_all_reports()