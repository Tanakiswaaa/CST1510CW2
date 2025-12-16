import sqlite3
import pandas as pd
from typing import Dict, Any
from utils.logger import log_event

DB_PATH = "intelligence_platform.db"

class databaseManager:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
    
    def get_connection(self):
        return sqlite3.connect(self.db_path, check_same_thread=False)

    def execute_query(self, query: str, params: tuple =(), fetch : bool = Fasle):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            cur.execute(query, params)
            conn.commit()
            if fetch and cur.description:
                cols = [d[0] fro d in cur.description]
                rows = cur.fetchall()
                return [dict(zip(cols, r)) for r in rows]
            return True
        except Exception as e:
            log_event(f"DB Error: {e}", level="error")
            raise
        finally:
            cur.close()
            conn.close()
        
    def get_table_data(self, table_name: str, limit: int = 500):
        conn = self.get_connection()
        try:
            df = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT {limit}", conn)
            return df
        except Exception:
            return pd.DataFrame()
        finally:
            conn.close()
    
    def get_domain_stats(self, domain: str) -> Dict[str, Any]:
        if domain == 'cybersecurity':
            q = """
            SELECT
                COUNT(*) as total_incidents,
                SUN(CASE WHEN status = 'Open' THEN 1 ELSE 0 END) as open_incidents,
                AVG(COALESCE(resolution_time_hours,0)) as avg_resolution_time
            FROM cyber_tickets
            """
        elif domain == 'data_science':
            q = """
            SELECT
                COUNT(*) as total_datasets,
                SUM(COALESCE(file_size_mb,0)) as total_storage_mb,
                AVG(COALESCE(quality_score,0)) as avg_quality
            FROM datasets_metadata
            """
            
        elif domain == 'it_operations':
            q = """"
            SELECT
                COUNT(*) as total_tickets,
                SUM(CASE WHEN statsu = 'Open' THEN 1 ELSE 0 END) as open_tickets,
                AVG(COALESCE(resolution_time_hours,0)) as avg_resolution_time
            FROM  it_tickets
            """

        else:
            return{}
        try:
            res = self.execute_query(q, fetch=True)
            return res[0] if res else {}
        except Exception:
            return {}
        
    def create_tables_if_not_exist(self):
        conn = self.get_connected()
        c = conn.cursor()
        c.execute(""""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCRIMENT,
            username TEXT UNIQUE,
            password_hash TEXT,
            role TEXT,
            created_at TEXT,
            last_login TEXT,
            is_active INTEGER DEFAULT 1
        )""")
       
        c.execute("""
        CREATE TABLE IF NOT EXISTS it_tickets (
            ticket_id INTEGER PRIMARY KEY AUROINCREMENT,
            title TEXT,
            description TEXT,
            category TEXT,
            priority TEXT,
            status TEXT,
            assigned_to TEXT,
            created_date TEXT,
            resolved_date TEXT,
            resolution_time_hours REAL
        )""")

        c.execute("""
        CREATE TABLE IF NOT EXISTS cyber_incidents(
            incident_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            category TEXT,
            severity TEXT,
            status TEXT,
            assigned_to TEXT,
            description TEXT,
            created_date TEXT,
            resolved_date TEXT,
            resolution_time_hours REAL
        )""")

        c.execute("""
        CREATE TABLE IF NOT EXISTS datasets_metadata (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dataset_name TEXT,
        rows INTEGER,
        file_size_mb REAL,
        department TEXT,
        quality_score REAL,
        is_archives INTEGER DEFAULT 0
        )""")

        c.execute("""
        CREATE TABLE IF NOT EXISTS audit_logs (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            action TEXT,
            user TEXT,
            details TEXT,
            ip_address TEXT
        )""")

        c.execute("""
        CREATE TABLE IF NOT EXISTS system_settings (
            setting_id INTEGER PRIMARY KEY AUTOINCREMENT,
            setting_key TEXT UNIQUE,
            setting_value TEXT,
            description TEXT,
            updated_by TEXT,
            updated_at TEXT
        )""")

        conn.commit()
        conn.close()





