import pandas as pd
from database.db_manager import DatabaseManager


def load_tickets_df():
    db = DatabaseManager()
    rows = db.execute(
        """
        SELECT
            assigned_to,
            status,
            resolution_time_hours
        FROM it_tickets
        """,
        fetchall=True
    )

    df = pd.DataFrame(
        rows,
        columns=["assigned_to", "status", "resolution_time_hours"]
    )
    return df


def avg_resolution_by_staff(df):
    return (
        df.groupby("assigned_to")["resolution_time_hours"]
        .mean()
        .reset_index()
        .sort_values(by="resolution_time_hours", ascending=False)
    )


def delay_by_status(df):
    return (
        df.groupby("status")["resolution_time_hours"]
        .mean()
        .reset_index()
        .sort_values(by="resolution_time_hours", ascending=False)
    )
