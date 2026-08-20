import sqlite3
import os

# Connect to your existing database safely
db_path = os.path.join(os.path.dirname(__file__), "../tokens.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Safely add the new column without touching existing data
try:
    cursor.execute("ALTER TABLE favorites ADD COLUMN amount REAL DEFAULT 0.0")
    print("Success: The 'amount' column was added safely! Your old data is untouched.")
except sqlite3.OperationalError:
    print("Notice: The 'amount' column already exists. Nothing was changed.")

conn.commit()
conn.close()
