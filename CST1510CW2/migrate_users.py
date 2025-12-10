import json
from database_manager import databaseManager

def migrate_users(json_file="users.json"):
    db = databaseManager()
    db.connect()

    try:
        with open(json_file, "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        print("users.json not found.")
        return
    
    for username, data in users.items():
        db.execute_query("""
            INSERT OR IGNORE INTO users (username, password_hash, role, created_at, last_login)
            VALUES (?, ?, ?, ?, ?)
        """, (
            username,
            data["password_hash"],
            data["role"],
            data["created_at"],
            data["last_login"]
        ))

    print("Migration complete!")
    db.disconnect()

if __name__ == "main":
    migrate_users()

from components.footer import render_footer
render_footer()
