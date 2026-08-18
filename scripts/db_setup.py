import os
import sqlite3
import sys

# Add the parent directory to the system path to allow imports from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.tokens import TOKENS

conn = sqlite3.connect("../tokens.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS favorites")
cursor.execute("""
    CREATE TABLE favorites (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symbol TEXT,
        name TEXT,
        coin_type TEXT,
        value TEXT,
        network TEXT
    )
""")

for symbol, data in TOKENS.items():
    name = data.get("name")
    coin_type = data.get("type")
    value = data.get("value")
    network = data.get("network", "")

    cursor.execute(
        """
        INSERT INTO favorites (symbol, name, coin_type, value, network)
        VALUES (?, ?, ?, ?, ?)
    """,
        (symbol, name, coin_type, value, network),
    )

    print("Inserted:", symbol, name, coin_type, value, network)

conn.commit()
conn.close()

print(
    "Database setup complete. All tokens have been inserted into the favorites"
    " table."
)
