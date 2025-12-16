import re
import secrets
from typing import Dict
import sqlite3
from datetime import datetime

class AdminSecurity:
    @staticmethod
    def validate_password_strength(password: str) -> Dict[str, bool]:
        validations = {
            'length': len(password) >= 8,
            'uppercase': bool(re.search(r'[A-Z]', password)),
            'lowercase': bool(re.search(r'[a-z]', password)),
            'digit': bool(re.search(r'\d', password)),
            'special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
        }
        return validations

    @staticmethod
    def generate_api_key() -> str:
        return secrets.token_urlsafe(32)

    @staticmethod
    def audit_log(action: str, user: str, details: str = ""):
        """Append audit log to DB table (creates table if missing)."""
        try:
            conn = sqlite3.connect('intelligence_platform.db')
            c = conn.cursor()
            c.execute('''
            CREATE TABLE IF NOT EXISTS audit_logs (
                log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                action TEXT,
                user TEXT,
                details TEXT,
                ip_address TEXT
            )
            ''')
            c.execute("INSERT INTO audit_logs (timestamp, action, user, details) VALUES (?, ?, ?, ?)",
                      (datetime.now().isoformat(), action, user, details))
            conn.commit()
        except Exception:
            pass
        finally:
            try:
                conn.close()
            except:
                pass
