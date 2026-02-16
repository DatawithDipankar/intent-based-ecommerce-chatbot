import sqlite3
import os

DB_PATH = "database/ecommerce.db"

def setup_database():
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open("database/schema.sql", "r") as f:
        cursor.executescript(f.read())

    with open("database/seed_data.sql", "r") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()
    print("Database created successfully.")

if __name__ == "__main__":
    setup_database()
