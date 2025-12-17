import pandas as pd
from pathlib import Path
from .db_manager import DatabaseManager


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_csv(table_name: str, csv_filename: str):
    db = DatabaseManager()
    conn = db.connect()

    csv_path = DATA_DIR / csv_filename
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    df = pd.read_csv(csv_path)

    if table_name == "cyber_incidents" and "resolution_time_hours" not in df.columns:
        df["resolution_time_hours"] = (
            df.index.to_series().apply(lambda x: (x % 72) + 1)
        )

    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

    print(f"{table_name} loaded successfully.")


if __name__ == "__main__":
    load_csv("cyber_incidents", "cyber_incidents.csv")
    load_csv("datasets_metadata", "datasets_metadata.csv")
    load_csv("it_tickets", "it_tickets.csv")
