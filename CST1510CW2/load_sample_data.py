import pandas as pd
from database_manager import databaseManager

db = databaseManager()
db.connect()

def load_it_tickets():
    df = pd.read_csv("sample_data/it_tickets.csv")

    for _, row in df.iterrows():
        db.execute_query("""
            INSERT INTO it_tickets (title, category, status, assigned_to, created_date, resolved_date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            row["title"],
            row["category"]
            row["status"]
            row["assigned_to"]
            row["created_date"]
            row["resolved_date"]
        ))

    print("IT tickets loaded.")

if __name__ == "__main__":
    load_it_tickets()

from components.footer import render_footer
render_footer()
