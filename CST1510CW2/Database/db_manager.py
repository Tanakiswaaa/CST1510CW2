import sqlite3
from typing import Any, Optional, Tuple

class DatabaseManager:
    def __init__(self, db_path: str = "intel_platform.db"):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)

    def execute(
        self,
        query: str,
        params: Tuple = (),
        fetchone: bool = False,
        fetchall: bool = False,
        commit: bool = False
    ) -> Optional[Any]:
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(query, params)

        result = None
        if fetchone:
            result = cursor.fetchone()
        elif fetchall:
            result = cursor.fetchall()

        if commit:
            conn.commit()

        conn.close()
        return result
