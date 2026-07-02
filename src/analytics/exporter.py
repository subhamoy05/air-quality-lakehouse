"""
exporter.py
===========

Computational Environmental Intelligence Framework (CEIF)

Analytics Export Utilities

Responsibilities
----------------
1. Export CSV
2. Export Excel
3. Export JSON
4. Export HTML
5. Export Parquet
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


class DataExporter:
    """
    Generic Data Export Utility.
    """

    def __init__(
        self,
        output_directory: str | Path = "reports/analytics"
    ):

        self.output_directory = Path(output_directory)

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

    # =====================================================
    # CSV
    # =====================================================

    def to_csv(

        self,

        dataframe: pd.DataFrame,

        filename: str,

        index: bool = False

    ) -> Path:

        path = self.output_directory / filename

        dataframe.to_csv(

            path,

            index=index

        )

        print(f"CSV Saved : {path}")

        return path

    # =====================================================
    # Excel
    # =====================================================

    def to_excel(

        self,

        dataframe: pd.DataFrame,

        filename: str,

        index: bool = False

    ) -> Path:

        path = self.output_directory / filename

        dataframe.to_excel(

            path,

            index=index

        )

        print(f"Excel Saved : {path}")

        return path

    # =====================================================
    # JSON
    # =====================================================

    def to_json(

        self,

        dataframe: pd.DataFrame,

        filename: str,

        orient: str = "records"

    ) -> Path:

        path = self.output_directory / filename

        dataframe.to_json(

            path,

            orient=orient,

            indent=4

        )

        print(f"JSON Saved : {path}")

        return path

    # =====================================================
    # HTML
    # =====================================================

    def to_html(

        self,

        dataframe: pd.DataFrame,

        filename: str,

        index: bool = False

    ) -> Path:

        path = self.output_directory / filename

        dataframe.to_html(

            path,

            index=index

        )

        print(f"HTML Saved : {path}")

        return path

    # =====================================================
    # Parquet
    # =====================================================

    def to_parquet(

        self,

        dataframe: pd.DataFrame,

        filename: str,

        index: bool = False

    ) -> Path:

        path = self.output_directory / filename

        dataframe.to_parquet(

            path,

            index=index

        )

        print(f"Parquet Saved : {path}")

        return path

    # =====================================================
    # Export All
    # =====================================================

    def export_all(

        self,

        dataframe: pd.DataFrame,

        filename: str

    ):

        stem = Path(filename).stem

        self.to_csv(

            dataframe,

            f"{stem}.csv"

        )

        self.to_excel(

            dataframe,

            f"{stem}.xlsx"

        )

        self.to_json(

            dataframe,

            f"{stem}.json"

        )

        self.to_html(

            dataframe,

            f"{stem}.html"

        )

        self.to_parquet(

            dataframe,

            f"{stem}.parquet"

        )

    # =====================================================
    # Utility
    # =====================================================

    def exists(

        self,

        filename: str

    ) -> bool:

        return (

            self.output_directory /

            filename

        ).exists()

    def delete(

        self,

        filename: str

    ):

        file = self.output_directory / filename

        if file.exists():

            file.unlink()

            print(f"Deleted : {file}")

    def list_exports(self):

        return sorted(

            self.output_directory.glob("*")

        )


# ==========================================================
# Demo
# ==========================================================

if __name__ == "__main__":

    df = pd.DataFrame({

        "Station": [

            "WB001",

            "WB002",

            "WB003"

        ],

        "AQI": [

            95,

            110,

            82

        ],

        "PM25": [

            42.5,

            58.4,

            31.2

        ]

    })

    exporter = DataExporter()

    exporter.export_all(

        df,

        "sample_report"

    )

    print()

    print("Available Exports")

    print(

        exporter.list_exports()

    )