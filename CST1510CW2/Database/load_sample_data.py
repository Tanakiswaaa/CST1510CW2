import pandas as pd
import sqlite3
from pathlib import Path

DB_NAME = "intelligence_platform.db"
DATA_DIR = Path("data")

FILES = {
    "cyber_incidents": "cyber_incidents.csv",
    "datasets_metadata": "datasets_metadata.csv",
    "it_tickets": "it_tickets.csv"
}

def load_csv_to_db(table_name: str, csv_file: str):
    """Load CSV into database table (replace on first load)"""
    conn = sqlite3.connect(DB_NAME)

    df = pd.read_csv(csv_file)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",   
        index=False
    )

    conn.close()
    print(f"Loaded {len(df)} rows into '{table_name}'")

def main():
    print("Loading project datasets...\n")

    for table, file in FILES.items():
        if Path(file).exists():
            load_csv_to_db(table, file)
        else:
            print(f"Missing file: {file}")

    print("\All datasets loaded successfully!")

def validate_csv(df, required_columns: list, name: str):
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        st.error(f"{name} CSV missing columns: {missing}")
        return False
    return True

if validate_csv(cyber_df,
    ['title', 'severity', 'status', 'assigned_to'],
    'Cyber Incidents'):
    cyber_df.to_sql('cyber_incidents', conn, if_exists='append', index=False)


if __name__ == "__main__":
    main()


