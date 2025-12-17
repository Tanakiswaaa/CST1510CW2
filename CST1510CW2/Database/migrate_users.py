import sqlite3
import hashlib

DB_NAME = "intelligence_platform.db"

DEFAULT_USERS = [
    ("admin", "admin123", "admin"),
    ("cyber_analyst", "cyber123", "cybersecurity"),
    ("data_scientist", "data123", "data_science"),
    ("it_support", "it123", "it_operations")
]

def hash_password(password: str) -> str:
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def migrate_users():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for username, password, role in DEFAULT_USERS:
        cursor.execute(
            """
            INSERT OR IGNORE INTO users (username, password_hash, role)
            VALUES (?, ?, ?)
            """,
            (username, hash_password(password), role)
        )

    conn.commit()
    conn.close()

    print("Default users migrated successfully")

if __name__ == "__main__":
    migrate_users()
