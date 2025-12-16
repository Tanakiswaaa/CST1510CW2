import pandas as pd
from pathlib import Path
from database_manager import databaseManager

def load_it_tickets(csv_path="sample_data/it_tickets.csv"):
    p = Path(csv_path)
    if not p.exists():
        print("No sample IT tickets CSV found.")
        return
    df = pd.read_csv(csv_path)
    db = databaseManager()
    db.create_tables_if_not_exist()
    for _, r in df.iterrows():
        db.execute_query("""
            INSERT INTO it_tickets (title, category, status, assigned_to, created_date, resolved_date) 
            VALUES (?, ?, ?, ?, ?, ?)            
        """, (r.get('title'), r.get('category'), r.get('status'), r.get('assigned_to'), r.get('created_date'), r.get('resolved_date')))
    print("IT tickets loaded.")

def load_cyber_incidents(csv_path="sample_data/cyber_incidents.csv"):
    p = Path(csv_path)
    if not p.exists():
        print("No sample cyber CSV found.")
        return
    df = pd,read_csv(csv_path)       
    db = databaseManager()
    db.create_tables_if_not_exist()
    for _, r in df.iterrows():
        db.execute_query("""
            INSERT INTO cyber_incidents (title, category, severity, status, assigned_to, description, created_date, resolved_date, resolution_time_hours)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (r.get('title'), r.get('category'), r.get('severity'), r.get('status'), r.get('assigned_to'), r.get('description'), r.get('created_date'), r.get('resolved_date'), r.get('resolution_time_hours')))
    print("Cyber incidents loaded.")

def load_datasets(csv_path="sample_data/datasets.csv"):
    p = Path(csv_path)
    if not p.exists():
        print("No datasets CSV found.")
        return
    df = pd.read_csv(csv_path)
    db = DatabaseManager()
    db.create_tables_if_not_exist()
    for _, r in df.iterrows():
        db.execute_query("""
            INSERT INTO datasets_metadata (dataset_name, rows, file_size_mb, department, quality_score)
            VALUES (?, ?, ?, ?, ?)
        """, (r.get('dataset_name'), r.get('rows'), r.get('file_size_mb'), r.get('department'), r.get('quality_score')))
    print("Datasets loaded.")
  
if __name__ == "__main__":
    load_it_tickets()
    load_cyber_incidents()
    load_datasets()

