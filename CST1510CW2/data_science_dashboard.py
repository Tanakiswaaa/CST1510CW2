# pages/data_science_dashboard.py
import streamlit as st
from database.db_manager import DatabaseManager
from components.charts import ChartBuilder

def data_science_dashboard():
    st.set_page_config(page_title="Data Science Dashboard", layout="wide")

    if 'logged_in' not in st.session_state:
        st.switch_page("pages/login.py")

    db = DatabaseManager()
    df = db.get_table_data("datasets_metadata")

    st.markdown("## 📊 Data Science Dashboard")
    st.markdown("Manage datasets, storage, and quality metrics.")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        pie = ChartBuilder.create_pie_chart(df, "department", "department", "Datasets by Department")
        st.plotly_chart(pie, use_container_width=True)

    with col2:
        bar = ChartBuilder.create_bar_chart(df, "dataset_name", "file_size_mb", "Storage Usage (MB)")
        st.plotly_chart(bar, use_container_width=True)

    st.markdown("---")
    st.subheader("📁 Dataset Table")
    st.dataframe(df)

    # Create dataset
    st.markdown("---")
    st.subheader("➕ Register Dataset")

    with st.form("add_dataset"):
        name = st.text_input("Dataset Name")
        dept = st.text_input("Department")
        size = st.number_input("Size (MB)", min_value=1)
        quality = st.slider("Quality Score", 0, 100)

        submitted = st.form_submit_button("Add Dataset")

        if submitted:
            db.execute_query("""
                INSERT INTO datasets_metadata (dataset_name, department, file_size_mb, quality_score)
                VALUES (?, ?, ?, ?)
            """, (name, dept, size, quality))

            st.success("✅ Dataset added")
            st.rerun()

    if st.button("⬅️ Back to Dashboard"):
        st.switch_page("pages/dashboard.py")

if __name__ == "__main__":
    data_science_dashboard()
