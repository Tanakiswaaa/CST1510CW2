import pandas as pd
from database.db_manager import DatabaseManager


def load_incidents_df():
    db = DatabaseManager()
    rows = db.execute(
        """
        SELECT
            timestamp,
            severity,
            category,
            status,
            resolution_time_hours
        FROM cyber_incidents
        """,
        fetchall=True
    )

    df = pd.DataFrame(
        rows,
        columns=[
            "timestamp",
            "severity",
            "category",
            "status",
            "resolution_time_hours"
        ]
    )

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    return df


def incidents_by_category(df):
    return df["category"].value_counts().reset_index(
        name="incident_count"
    ).rename(columns={"index": "category"})


def avg_resolution_by_category(df):
    return (
        df.groupby("category")["resolution_time_hours"]
        .mean()
        .reset_index()
        .sort_values(by="resolution_time_hours", ascending=False)
    )


def phishing_trend_over_time(df):
    phishing_df = df[df["category"].str.lower() == "phishing"]
    return (
        phishing_df
        .set_index("timestamp")
        .resample("W")
        .size()
        .reset_index(name="incident_count")
    )
