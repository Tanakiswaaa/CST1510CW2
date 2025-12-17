from database.db_manager import DatabaseManager

def create_tables():
    db = DatabaseManager()

    # Users table
    db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """, commit=True)

    # Cybersecurity incidents
    db.execute("""
        CREATE TABLE IF NOT EXISTS cyber_incidents (
            incident_id INTEGER PRIMARY KEY,
            timestamp TEXT,
            severity TEXT,
            category TEXT,
            status TEXT,
            description TEXT,
            resolution_time_hours REAL
        )
    """, commit=True)

    # Data science datasets
    db.execute("""
        CREATE TABLE IF NOT EXISTS datasets_metadata (
            dataset_id INTEGER PRIMARY KEY,
            name TEXT,
            rows INTEGER,
            columns INTEGER,
            uploaded_by TEXT,
            upload_date TEXT
        )
    """, commit=True)

    # IT tickets
    db.execute("""
        CREATE TABLE IF NOT EXISTS it_tickets (
            ticket_id INTEGER PRIMARY KEY,
            priority TEXT,
            description TEXT,
            status TEXT,
            assigned_to TEXT,
            created_at TEXT,
            resolution_time_hours REAL
        )
    """, commit=True)


if __name__ == "__main__":
    create_tables()
    print("Database tables created successfully.")
