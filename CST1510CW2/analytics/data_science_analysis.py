import pandas as pd
from database.db_manager import DatabaseManager


def load_datasets_df():
    db = DatabaseManager()
    rows = db.execute(
        """
        SELECT
            name,
            rows,
            columns,
            uploaded_by
        FROM datasets_metadata
        """,
        fetchall=True
    )

    df = pd.DataFrame(
        rows,
        columns=["name", "rows", "columns", "uploaded_by"]
    )
    return df


def dataset_sizes(df):
    df["size_score"] = df["rows"] * df["columns"]
    return df.sort_values(by="size_score", ascending=False)


def source_distribution(df):
    return df["uploaded_by"].value_counts().reset_index(
        name="dataset_count"
    ).rename(columns={"index": "source"})
