import json
from database_manager import databaseManager

def migrate_users(json_file="users.json"):
    db = databaseManager()
    db.connect()

    try:
        with open(json_file, "r") as f:
            users = json.load(f)
        except