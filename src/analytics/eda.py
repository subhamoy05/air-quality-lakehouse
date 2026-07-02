"""
eda.py
======

Computational Environmental Intelligence Framework (CEIF)

Exploratory Data Analysis (EDA)

Responsibilities
----------------
1. Dataset Summary
2. Missing Value Analysis
3. Duplicate Analysis
4. Data Type Summary
5. Numerical Statistics
6. Categorical Statistics
7. Outlier Detection
8. Station Summary
"""

from __future__ import annotations

import pandas as pd

from .loader import DatasetLoader


class ExploratoryDataAnalysis:
    """
    Exploratory Data Analysis.
    """

    def __init__(self):

        self.loader = DatasetLoader()

        self.df = self.loader.environmental_master()

    # =====================================================
    # Dataset Information
    # =====================================================

    def shape(self):

        return self.df.shape

    def columns(self):

        return list(self.df.columns)

    def data_types(self):

        return self.df.dtypes

    # =====================================================
    # Missing Values
    # =====================================================

    def missing_values(self):

        missing = self.df.isnull().sum()

        percent = (missing / len(self.df) * 100).round(2)

        return pd.DataFrame({"Missing Values": missing, "Percentage": percent})

    # =====================================================
    # Duplicate Records
    # =====================================================

    def duplicate_records(self):

        return self.df.duplicated().sum()

    # =====================================================
    # Quality Report
    # =====================================================

    def quality_report(self):

        data_types = self.data_types()

        missing_values = self.missing_values()

        duplicate_records = self.duplicate_records()

        report = {
            "total_rows": len(self.df),
            "total_columns": len(self.df.columns),
            "duplicate_records": int(duplicate_records),
            "missing_value_columns": int((missing_values["Missing Values"] > 0).sum()),
            "missing_value_total": int(missing_values["Missing Values"].sum()),
            "missing_value_percent": float(missing_values["Percentage"].mean()),
            "numeric_columns": int(
                (data_types == "float64").sum() + (data_types == "int64").sum()
            ),
            "categorical_columns": int((data_types == "object").sum()),
        }

        return report

    # =====================================================
    # Numerical Statistics
    # =====================================================

    def numerical_summary(self):

        return self.df.describe()

    # =====================================================
    # Categorical Statistics
    # =====================================================

    def categorical_summary(self):

        return self.df.describe(include=["object"])

    # =====================================================
    # Station Summary
    # =====================================================

    def station_summary(self):

        return (
            self.df.groupby(["station_id", "station_name", "district"])
            .agg(
                Records=("aqi", "count"),
                Average_AQI=("aqi", "mean"),
                Average_PM25=("pm25", "mean"),
                Average_PM10=("pm10", "mean"),
                Average_Temperature=("temperature", "mean"),
                Average_Humidity=("humidity", "mean"),
            )
            .reset_index()
        )

    # =====================================================
    # District Summary
    # =====================================================

    def district_summary(self):

        return (
            self.df.groupby("district")
            .agg(
                Records=("aqi", "count"),
                Average_AQI=("aqi", "mean"),
                Average_PM25=("pm25", "mean"),
                Average_PM10=("pm10", "mean"),
            )
            .reset_index()
        )

    # =====================================================
    # AQI Statistics
    # =====================================================

    def aqi_statistics(self):

        return self.df["aqi"].describe()

    # =====================================================
    # PM Statistics
    # =====================================================

    def pm_statistics(self):

        return self.df[["pm25", "pm10"]].describe()

    # =====================================================
    # Weather Statistics
    # =====================================================

    def weather_statistics(self):

        return self.df[
            [
                "temperature",
                "humidity",
                "pressure",
                "wind_speed",
                "wind_gust",
                "dew_point",
                "cloud_cover",
                "precipitation",
            ]
        ].describe()

    # =====================================================
    # Outlier Detection (IQR)
    # =====================================================

    def outlier_summary(self):

        numeric = self.df.select_dtypes(include="number")

        results = []

        for column in numeric.columns:

            q1 = numeric[column].quantile(0.25)

            q3 = numeric[column].quantile(0.75)

            iqr = q3 - q1

            lower = q1 - 1.5 * iqr

            upper = q3 + 1.5 * iqr

            count = ((numeric[column] < lower) | (numeric[column] > upper)).sum()

            results.append({"Feature": column, "Outliers": int(count)})

        return pd.DataFrame(results)

    # =====================================================
    # Complete Summary
    # =====================================================

    def summary(self):

        return {
            "Shape": self.shape(),
            "Duplicate Records": self.duplicate_records(),
            "Missing Values": self.missing_values(),
            "AQI": self.aqi_statistics(),
            "PM": self.pm_statistics(),
            "Weather": self.weather_statistics(),
        }

    # =====================================================
    # Utility
    # =====================================================

    def close(self):

        self.loader.close()

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_value, traceback):

        self.close()


# ==========================================================
# Demo
# ==========================================================

if __name__ == "__main__":

    with ExploratoryDataAnalysis() as eda:

        print("=" * 80)
        print("EXPLORATORY DATA ANALYSIS")
        print("=" * 80)

        print("\nShape")
        print(eda.shape())

        print("\nColumns")
        print(eda.columns())

        print("\nMissing Values")
        print(eda.missing_values())

        print("\nDuplicate Records")
        print(eda.duplicate_records())

        print("\nAQI Statistics")
        print(eda.aqi_statistics())

        print("\nStation Summary")
        print(eda.station_summary().head())

        print("\nOutlier Summary")
        print(eda.outlier_summary())
