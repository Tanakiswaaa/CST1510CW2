import json
from pathlib import Path
from database_manager import databaseManager

def migrate_users(json_file="users.json"):
    p = Path(json_file)
    if not p.exists():
        print("users.json not founf - skipping.")
        return
    db = databaseManager()
    db.connect()

    try:
        with open(json_file, "r") as f:
            users = json.load(f)
        db = databaseManager()
        db.create_tables_if_not_exist()
        for username, data in user.items():
            db.execute_query("""
            INSERT OR IGNORE INTO users (username, password_hash, role, created_at, last_login)
            VALUES (?, ?, ?, ?, ?)
            """, (username, data.get("password_hash"), data.get("role"), data.get("created_at"), data.get("last_login")))                
        print("Migration done.")

if __name__ == "main":
    migrate_users()

