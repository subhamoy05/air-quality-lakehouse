"""
loader.py
=========

Computational Environmental Intelligence Framework (CEIF)

Dataset Loader

Responsibilities
----------------
1. Connect to DuckDB
2. Execute SQL Queries
3. Load Master Datasets
4. Return Pandas DataFrames
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import duckdb
import pandas as pd

from src.database.connection import get_connection

from . import queries


class DatasetLoader:
    """
    Dataset Loader for the Analytics Engine.
    """

    def __init__(self):

        self.connection = get_connection()

    # =====================================================
    # Generic SQL Executor
    # =====================================================

    def query(self, sql: str, parameters: Optional[list] = None) -> pd.DataFrame:
        """
        Execute SQL query.
        """

        try:
            if parameters:

                return self.connection.execute(sql, parameters).fetchdf()

            return self.connection.execute(sql).fetchdf()

        except duckdb.CatalogException as exc:
            if "environmental_master" in sql.lower():
                self._register_environmental_master_from_parquet()
                return self.query(sql, parameters=parameters)
            raise exc

    def _register_environmental_master_from_parquet(self) -> None:
        parquet_path = Path("data/silver/environment_master.parquet")

        if not parquet_path.exists():
            raise FileNotFoundError(f"Expected parquet file not found: {parquet_path}")

        self.connection.execute(
            f"CREATE OR REPLACE TABLE environmental_master AS SELECT * FROM read_parquet('{parquet_path}')"
        )

    # =====================================================
    # Master Datasets
    # =====================================================

    def environmental_master(self):

        try:
            return self.query(queries.ENVIRONMENTAL_MASTER)

        except duckdb.CatalogException:
            parquet_path = Path("data/silver/environment_master.parquet")

            if parquet_path.exists():
                self.connection.execute(
                    f"CREATE OR REPLACE TABLE environmental_master AS SELECT * FROM read_parquet('{parquet_path}')"
                )

                return self.query(queries.ENVIRONMENTAL_MASTER)

            raise

    # =====================================================

    def weather_master(self):

        try:

            return self.query(queries.WEATHER_MASTER)

        except duckdb.Error:

            return pd.DataFrame()

    # =====================================================

    def wbpcb_master(self):

        try:

            return self.query(queries.WBPCB_MASTER)

        except duckdb.Error:

            return pd.DataFrame()

    # =====================================================

    def realtime_environmental_master(self):

        try:

            return self.query(queries.REALTIME_ENVIRONMENTAL_MASTER)

        except duckdb.Error:

            return pd.DataFrame()

    # =====================================================
    # Generic Table Loader
    # =====================================================

    def table(self, table_name: str) -> pd.DataFrame:

        sql = f"""
        SELECT *
        FROM {table_name}
        """

        return self.query(sql)

    # =====================================================
    # Metadata
    # =====================================================

    def tables(self):

        return self.query("SHOW TABLES")

    # =====================================================

    def schema(self, table_name: str):

        return self.query(f"DESCRIBE {table_name}")

    # =====================================================

    def row_count(self, table_name: str) -> int:

        sql = f"""
        SELECT COUNT(*) AS total_rows
        FROM {table_name}
        """

        return int(self.query(sql).iloc[0]["total_rows"])

    # =====================================================

    def columns(self, table_name: str):

        return list(self.schema(table_name)["column_name"])

    # =====================================================

    def exists(self, table_name: str) -> bool:

        tables = self.tables()

        return table_name in tables["name"].values

    # =====================================================
    # Sample Dataset
    # =====================================================

    def sample(self, table_name: str, rows: int = 5):

        sql = f"""
        SELECT *
        FROM {table_name}
        LIMIT {rows}
        """

        return self.query(sql)

    # =====================================================
    # Utility
    # =====================================================

    def close(self):

        self.connection.close()

    # =====================================================

    def __enter__(self):

        return self

    # =====================================================

    def __exit__(self, exc_type, exc_value, traceback):

        self.close()


# ==========================================================
# Demo
# ==========================================================

if __name__ == "__main__":

    with DatasetLoader() as loader:

        print("=" * 80)
        print("DATASET LOADER")
        print("=" * 80)

        print("\nAvailable Tables")
        print(loader.tables())

        print("\nEnvironmental Master")
        print(loader.environmental_master().head())

        print("\nDataset Information")
        print(loader.row_count("environmental_master"))

        print("\nColumns")
        print(loader.columns("environmental_master"))

        print("\nSchema")
        print(loader.schema("environmental_master"))
