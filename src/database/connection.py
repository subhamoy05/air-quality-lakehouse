"""
connection.py
=====================================

DuckDB Connection Manager

Responsibilities
----------------
✓ Open DuckDB connection
✓ Apply database configuration
✓ Close connection

This module contains no schema or table creation logic.
"""

from __future__ import annotations

import os
from pathlib import Path

import duckdb

from .config import DATABASE_FILE, DUCKDB_CONFIG


class DatabaseConnection:
    """
    Manage the application's DuckDB connection.
    """

    def __init__(self) -> None:
        self._connection: duckdb.DuckDBPyConnection | None = None
        self._database_path: Path | None = None

    # ======================================================
    # Connection
    # ======================================================

    def connect(self) -> duckdb.DuckDBPyConnection:
        """
        Create or return an active DuckDB connection.
        """

        if self._connection is None:
            try:
                self._connection = duckdb.connect(str(DATABASE_FILE))
                self._database_path = DATABASE_FILE
            except duckdb.IOException:
                fallback_path = Path("lakehouse.duckdb")
                try:
                    self._connection = duckdb.connect(str(fallback_path))
                    self._database_path = fallback_path
                except duckdb.IOException as exc:
                    self._connection = duckdb.connect(":memory:")
                    self._database_path = None
                    self._configure()
                    return self._connection

            self._configure()

        return self._connection

    # ======================================================
    # Configuration
    # ======================================================

    def _configure(self) -> None:
        """
        Apply DuckDB runtime settings.
        """

        if self._connection is None:
            return

        for key, value in DUCKDB_CONFIG.items():
            self._connection.execute(f"SET {key}='{value}'")

    # ======================================================
    # Access
    # ======================================================

    @property
    def connection(self) -> duckdb.DuckDBPyConnection:
        """
        Return an active connection.
        """

        return self.connect()

    # ======================================================
    # Execute SQL
    # ======================================================

    def execute(self, sql: str, parameters=None):
        """
        Execute SQL using the shared connection.
        """

        connection = self.connect()

        if parameters is None:
            return connection.execute(sql)

        return connection.execute(sql, parameters)

    # ======================================================
    # Close
    # ======================================================

    def close(self) -> None:
        """
        Close the database connection.
        """

        if self._connection is not None:
            self._connection.close()
            self._connection = None
            self._database_path = None


# ==========================================================
# Singleton
# ==========================================================

database = DatabaseConnection()


def get_connection() -> duckdb.DuckDBPyConnection:
    """
    Return the shared DuckDB connection.
    """
    return database.connection


def execute(sql: str, parameters=None):
    """
    Execute SQL using the shared connection.
    """
    connection = database.connection

    if parameters is None:
        return connection.execute(sql)

    return connection.execute(sql, parameters)


def close_connection() -> None:
    """
    Close the shared connection.
    """
    database.close()


__all__ = [
    "DatabaseConnection",
    "database",
    "get_connection",
    "execute",
    "close_connection",
]
