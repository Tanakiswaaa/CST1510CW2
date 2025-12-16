import bcrypt
from database_manager import DatabaseManager
from datetime import datetime
from utils.logger import log_event

class AuthenticationSystem:
    """User Authentication System Class"""
    
    def __init__(self):
        self.db = DatabaseManager()
        self.db.create_tables_if_not_exist()

    def register_user(self, username: str, password: str, role = "it_operations"):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()
        q = "INSERT OR IGNORE INTO users (username, password_hash, role, created_at) VALUES (?, ?, ?, ?)"
        self.db.execute_query(q, (username, hashed, role, datetime.now().isoformat()))
        log_event(f"User registered: {username}")
        return True
        
    def verify_user(self, username: str, password: str):
        q = "SELECT password_hash, role FROM users WHERE username = ?"
        res = self.db.execute_query(q, (username,), fetch=True)
        if res and len(res) > 0:
            stored = res[0]['password_hash']
            role = res[0].get('role')
            if bcrypt.checkpw(password.encode('utf-8'), stored.encode('utf-8')):
                q2 = "UPDATE users SET last_login = ? WHERE username = ?"
                self.db.execute_query(q2, (datetime.now().isoformat(), username))
                log_event(f"User logged in: {username}")
                return True, role
        return False, None