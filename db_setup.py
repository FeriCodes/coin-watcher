import sqlite3

conn = sqlite3.connect("tokens.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS favorites (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        coin_name TEXT,
        coin_id TEXT
    )
""")

conn.commit()
conn.close()
