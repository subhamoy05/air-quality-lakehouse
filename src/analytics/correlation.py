"""
correlation.py
==============

Computational Environmental Intelligence Framework (CEIF)

Correlation Analysis

Responsibilities
----------------
1. Correlation Matrix
2. AQI Correlations
3. Feature Ranking
4. Strongest Positive Correlations
5. Strongest Negative Correlations
"""

from __future__ import annotations

import pandas as pd

from .loader import DatasetLoader


class CorrelationAnalysis:
    """
    Correlation Analysis Module.
    """

    def __init__(self):

        self.loader = DatasetLoader()

        self.df = self.loader.environmental_master()

    # =====================================================
    # Numeric Dataset
    # =====================================================

    def numeric_dataset(self) -> pd.DataFrame:

        columns = [

            "aqi",

            "pm25",

            "pm10",

            "temperature",

            "humidity",

            "dew_point",

            "precipitation",

            "pressure",

            "cloud_cover",

            "wind_speed",

            "wind_direction",

            "wind_gust"

        ]

        return self.df[columns]

    # =====================================================
    # Correlation Matrix
    # =====================================================

    def correlation_matrix(
        self,
        method: str = "pearson"
    ) -> pd.DataFrame:

        return self.numeric_dataset().corr(method=method)

    # =====================================================
    # AQI Correlations
    # =====================================================

    def aqi_correlations(self):

        corr = self.correlation_matrix()

        return (

            corr["aqi"]

            .sort_values(
                ascending=False
            )

            .to_frame(
                "Correlation"
            )

        )

    # =====================================================
    # Feature Ranking
    # =====================================================

    def feature_ranking(self):

        ranking = self.aqi_correlations()

        ranking["Absolute"] = (

            ranking["Correlation"]

            .abs()

        )

        ranking = (

            ranking

            .sort_values(

                "Absolute",

                ascending=False

            )

        )

        return ranking

    # =====================================================
    # Positive Correlations
    # =====================================================

    def strongest_positive(self, top: int = 5):

        ranking = self.feature_ranking()

        ranking = ranking.drop(index="aqi")

        return ranking.head(top)

    # =====================================================
    # Negative Correlations
    # =====================================================

    def strongest_negative(self, top: int = 5):

        corr = self.aqi_correlations()

        corr = corr.sort_values(

            "Correlation"

        )

        return corr.head(top)

    # =====================================================
    # Individual Correlations
    # =====================================================

    def aqi_vs_pm25(self):

        return self.df["aqi"].corr(

            self.df["pm25"]

        )

    def aqi_vs_pm10(self):

        return self.df["aqi"].corr(

            self.df["pm10"]

        )

    def aqi_vs_temperature(self):

        return self.df["aqi"].corr(

            self.df["temperature"]

        )

    def aqi_vs_humidity(self):

        return self.df["aqi"].corr(

            self.df["humidity"]

        )

    def aqi_vs_pressure(self):

        return self.df["aqi"].corr(

            self.df["pressure"]

        )

    def aqi_vs_wind_speed(self):

        return self.df["aqi"].corr(

            self.df["wind_speed"]

        )

    def aqi_vs_wind_direction(self):

        return self.df["aqi"].corr(

            self.df["wind_direction"]

        )

    def aqi_vs_wind_gust(self):

        return self.df["aqi"].corr(

            self.df["wind_gust"]

        )

    def aqi_vs_dew_point(self):

        return self.df["aqi"].corr(

            self.df["dew_point"]

        )

    def aqi_vs_precipitation(self):

        return self.df["aqi"].corr(

            self.df["precipitation"]

        )

    def aqi_vs_cloud_cover(self):

        return self.df["aqi"].corr(

            self.df["cloud_cover"]

        )

    # =====================================================
    # Summary
    # =====================================================

    def summary(self):

        return {

            "PM2.5":

                self.aqi_vs_pm25(),

            "PM10":

                self.aqi_vs_pm10(),

            "Temperature":

                self.aqi_vs_temperature(),

            "Humidity":

                self.aqi_vs_humidity(),

            "Pressure":

                self.aqi_vs_pressure(),

            "Wind Speed":

                self.aqi_vs_wind_speed(),

            "Wind Direction":

                self.aqi_vs_wind_direction(),

            "Wind Gust":

                self.aqi_vs_wind_gust(),

            "Dew Point":

                self.aqi_vs_dew_point(),

            "Precipitation":

                self.aqi_vs_precipitation(),

            "Cloud Cover":

                self.aqi_vs_cloud_cover()

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

    with CorrelationAnalysis() as correlation:

        print("=" * 80)
        print("CORRELATION ANALYSIS")
        print("=" * 80)

        print("\nCorrelation Matrix")
        print(correlation.correlation_matrix())

        print("\nAQI Correlations")
        print(correlation.aqi_correlations())

        print("\nFeature Ranking")
        print(correlation.feature_ranking())

        print("\nStrongest Positive")
        print(correlation.strongest_positive())

        print("\nStrongest Negative")
        print(correlation.strongest_negative())

        print("\nSummary")
        print(correlation.summary())