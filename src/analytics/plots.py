"""
plots.py
========

Computational Environmental Intelligence Framework (CEIF)

Visualization Utilities

Responsibilities
----------------
1. Line Plots
2. Bar Plots
3. Scatter Plots
4. Histograms
5. Boxplots
6. Save Figures
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class Visualization:
    """
    Visualization Utility Class.
    """

    def __init__(
        self,
        output_directory: str = "reports/plots"
    ):

        self.output_directory = Path(output_directory)

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        sns.set_theme(
            style="whitegrid",
            palette="deep"
        )

    # =====================================================
    # Helper
    # =====================================================

    def _save(
        self,
        filename: str
    ):

        path = self.output_directory / filename

        plt.tight_layout()

        plt.savefig(
            path,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        print(f"Saved -> {path}")

    # =====================================================
    # Line Plot
    # =====================================================

    def line_plot(

        self,

        dataframe: pd.DataFrame,

        x: str,

        y: str,

        title: str,

        xlabel: str,

        ylabel: str,

        filename: str

    ):

        plt.figure(figsize=(12,6))

        sns.lineplot(

            data=dataframe,

            x=x,

            y=y,

            linewidth=2

        )

        plt.title(title)

        plt.xlabel(xlabel)

        plt.ylabel(ylabel)

        self._save(filename)

    # =====================================================
    # Bar Plot
    # =====================================================

    def bar_plot(

        self,

        dataframe: pd.DataFrame,

        x: str,

        y: str,

        title: str,

        xlabel: str,

        ylabel: str,

        filename: str

    ):

        plt.figure(figsize=(12,6))

        sns.barplot(

            data=dataframe,

            x=x,

            y=y

        )

        plt.xticks(rotation=45)

        plt.title(title)

        plt.xlabel(xlabel)

        plt.ylabel(ylabel)

        self._save(filename)

    # =====================================================
    # Scatter Plot
    # =====================================================

    def scatter_plot(

        self,

        dataframe: pd.DataFrame,

        x: str,

        y: str,

        title: str,

        xlabel: str,

        ylabel: str,

        filename: str

    ):

        plt.figure(figsize=(10,6))

        sns.scatterplot(

            data=dataframe,

            x=x,

            y=y,

            alpha=0.6

        )

        plt.title(title)

        plt.xlabel(xlabel)

        plt.ylabel(ylabel)

        self._save(filename)

    # =====================================================
    # Histogram
    # =====================================================

    def histogram(

        self,

        dataframe: pd.DataFrame,

        column: str,

        bins: int = 30,

        filename: str = "histogram.png"

    ):

        plt.figure(figsize=(10,6))

        sns.histplot(

            dataframe[column],

            bins=bins,

            kde=True

        )

        plt.title(

            f"{column} Distribution"

        )

        plt.xlabel(column)

        plt.ylabel("Frequency")

        self._save(filename)

    # =====================================================
    # Box Plot
    # =====================================================

    def box_plot(

        self,

        dataframe: pd.DataFrame,

        column: str,

        filename: str = "boxplot.png"

    ):

        plt.figure(figsize=(8,6))

        sns.boxplot(

            y=dataframe[column]

        )

        plt.title(

            f"{column} Box Plot"

        )

        self._save(filename)

    # =====================================================
    # Correlation Heatmap
    # =====================================================

    def correlation_heatmap(

        self,

        dataframe: pd.DataFrame,

        filename: str = "correlation_heatmap.png"

    ):

        plt.figure(figsize=(12,10))

        corr = dataframe.corr(
            numeric_only=True
        )

        sns.heatmap(

            corr,

            annot=True,

            fmt=".2f",

            cmap="coolwarm",

            square=True,

            linewidths=0.5

        )

        plt.title("Correlation Matrix")

        self._save(filename)

    # =====================================================
    # AQI Trend
    # =====================================================

    def aqi_trend(

        self,

        dataframe: pd.DataFrame,

        filename: str = "aqi_trend.png"

    ):

        self.line_plot(

            dataframe,

            x="date",

            y="average_aqi",

            title="Daily AQI Trend",

            xlabel="Date",

            ylabel="Average AQI",

            filename=filename

        )

    # =====================================================
    # PM2.5 Trend
    # =====================================================

    def pm25_trend(

        self,

        dataframe: pd.DataFrame,

        filename: str = "pm25_trend.png"

    ):

        self.line_plot(

            dataframe,

            x="date",

            y="average_pm25",

            title="Daily PM2.5 Trend",

            xlabel="Date",

            ylabel="Average PM2.5",

            filename=filename

        )

    # =====================================================
    # PM10 Trend
    # =====================================================

    def pm10_trend(

        self,

        dataframe: pd.DataFrame,

        filename: str = "pm10_trend.png"

    ):

        self.line_plot(

            dataframe,

            x="date",

            y="average_pm10",

            title="Daily PM10 Trend",

            xlabel="Date",

            ylabel="Average PM10",

            filename=filename

        )

    # =====================================================
    # Temperature Trend
    # =====================================================

    def temperature_trend(

        self,

        dataframe: pd.DataFrame,

        filename: str = "temperature_trend.png"

    ):

        self.line_plot(

            dataframe,

            x="date",

            y="average_temperature",

            title="Temperature Trend",

            xlabel="Date",

            ylabel="Temperature (°C)",

            filename=filename

        )

    # =====================================================
    # Humidity Trend
    # =====================================================

    def humidity_trend(

        self,

        dataframe: pd.DataFrame,

        filename: str = "humidity_trend.png"

    ):

        self.line_plot(

            dataframe,

            x="date",

            y="average_humidity",

            title="Humidity Trend",

            xlabel="Date",

            ylabel="Humidity (%)",

            filename=filename

        )

    # =====================================================
    # Pressure Trend
    # =====================================================

    def pressure_trend(

        self,

        dataframe: pd.DataFrame,

        filename: str = "pressure_trend.png"

    ):

        self.line_plot(

            dataframe,

            x="date",

            y="average_pressure",

            title="Pressure Trend",

            xlabel="Date",

            ylabel="Pressure (hPa)",

            filename=filename

        )

    # =====================================================
    # Wind Speed Trend
    # =====================================================

    def wind_speed_trend(

        self,

        dataframe: pd.DataFrame,

        filename: str = "wind_speed_trend.png"

    ):

        self.line_plot(

            dataframe,

            x="date",

            y="average_wind_speed",

            title="Wind Speed Trend",

            xlabel="Date",

            ylabel="Wind Speed (km/h)",

            filename=filename

        )

    # =====================================================
    # Station Comparison
    # =====================================================

    def station_comparison(

        self,

        dataframe: pd.DataFrame,

        value_column: str = "average_aqi",

        filename: str = "station_comparison.png"

    ):

        plt.figure(figsize=(14,7))

        sns.barplot(

            data=dataframe,

            x="station_name",

            y=value_column

        )

        plt.xticks(rotation=90)

        plt.title("Station Comparison")

        plt.xlabel("Station")

        plt.ylabel(value_column.replace("_", " ").title())

        self._save(filename)

    # =====================================================
    # AQI vs PM2.5
    # =====================================================

    def aqi_vs_pm25(

        self,

        dataframe: pd.DataFrame,

        filename: str = "aqi_vs_pm25.png"

    ):

        self.scatter_plot(

            dataframe,

            x="pm25",

            y="aqi",

            title="AQI vs PM2.5",

            xlabel="PM2.5",

            ylabel="AQI",

            filename=filename

        )

    # =====================================================
    # AQI vs PM10
    # =====================================================

    def aqi_vs_pm10(

        self,

        dataframe: pd.DataFrame,

        filename: str = "aqi_vs_pm10.png"

    ):

        self.scatter_plot(

            dataframe,

            x="pm10",

            y="aqi",

            title="AQI vs PM10",

            xlabel="PM10",

            ylabel="AQI",

            filename=filename

        )

    # =====================================================
    # AQI vs Temperature
    # =====================================================

    def aqi_vs_temperature(

        self,

        dataframe: pd.DataFrame,

        filename: str = "aqi_vs_temperature.png"

    ):

        self.scatter_plot(

            dataframe,

            x="temperature",

            y="aqi",

            title="AQI vs Temperature",

            xlabel="Temperature (°C)",

            ylabel="AQI",

            filename=filename

        )

    # =====================================================
    # AQI vs Humidity
    # =====================================================

    def aqi_vs_humidity(

        self,

        dataframe: pd.DataFrame,

        filename: str = "aqi_vs_humidity.png"

    ):

        self.scatter_plot(

            dataframe,

            x="humidity",

            y="aqi",

            title="AQI vs Humidity",

            xlabel="Humidity (%)",

            ylabel="AQI",

            filename=filename

        )

    # =====================================================
    # AQI vs Pressure
    # =====================================================

    def aqi_vs_pressure(

        self,

        dataframe: pd.DataFrame,

        filename: str = "aqi_vs_pressure.png"

    ):

        self.scatter_plot(

            dataframe,

            x="pressure",

            y="aqi",

            title="AQI vs Pressure",

            xlabel="Pressure",

            ylabel="AQI",

            filename=filename

        )

    # =====================================================
    # Multi-Line Plot
    # =====================================================

    def multi_line_plot(

        self,

        dataframe: pd.DataFrame,

        x: str,

        y_columns: list,

        title: str,

        filename: str

    ):

        plt.figure(figsize=(14,7))

        for column in y_columns:

            plt.plot(

                dataframe[x],

                dataframe[column],

                linewidth=2,

                label=column

            )

        plt.legend()

        plt.title(title)

        plt.xlabel(x)

        plt.ylabel("Value")

        self._save(filename)

    # =====================================================
    # Forecast Plot
    # =====================================================

    def forecast_plot(

        self,

        actual,

        predicted,

        filename: str = "forecast.png"

    ):

        plt.figure(figsize=(12,6))

        plt.plot(

            actual,

            label="Actual",

            linewidth=2

        )

        plt.plot(

            predicted,

            label="Predicted",

            linewidth=2

        )

        plt.legend()

        plt.title("Forecast vs Actual")

        self._save(filename)

    # =====================================================
    # Available Plot Directory
    # =====================================================

    def output_path(self):

        return self.output_directory