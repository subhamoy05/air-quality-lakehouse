from src.database.connection import get_connection

con = get_connection()

print("=" * 80)
print("DATABASE CONNECTION")
print("=" * 80)

print(con.execute("SHOW TABLES").fetchdf())