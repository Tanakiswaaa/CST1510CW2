import sqlite3

class databaseManager:
    def __init__(self, db_path="intelligence_platform.db"):
        self.db_path = db_path
        self.conn = none
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def execute_query(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return self.curcor
        except Exception as e:
            print("Query Error:", e)
            print(query)
            return None
        
    def fetch_all(self, query, params=()):
        cursor = self.execute_query(query, params)
        return cursor.fetchall() if cursor else []
    
    def fetch_one(self, query, params=()):
        cursor = self.execute_query(query, params)
        return cursor.fetchone() if cursor else None
    
    def create_tables(self):
        users = """
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        username TEXT UNIQUE,
        password_hash TEXT,
        role TEXT, 
        created_at TEXT,
        last_login TEXT
        );
        """

        it_tickets = """
        CREATE TABLE IF NOT EXISTS IT_TICKETS (
        ticket_id INTEGER PRIMARY KEY AUROINCREMENT,
        title TEXT,
        category TEXT,
        status TEXT,
        assigned_to TEXT,
        created_date TEXT,
        resolved_date TEXT
        );
        """

        cyber = """
        CREATE TABLE IF NOT EXISTS cyber_incidents(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        severity TEXT,
        created_date TEXT,
        resolved_date TEXT
        );
        """

        datasets = """
        CREATE TABLE IF NOT EXISTS datasets_metadata (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dataset_name TEXT,
        rows INTEGER,
        size_mb REAL,
        department TEXT
        );
        """

        for table in [users, it_tickets, cyber, datasets]:
            self.execute_query(table)

from components.footer import render_footer
render_footer()
