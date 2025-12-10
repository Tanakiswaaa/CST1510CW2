import streamlit as st
import pandas as pd
from database.database_manager import DatabaseManager
from components.charts import ChartBuilder

def cybersecurity_dashboard():
    st.set_page_config(page_title="Cybersecurity Dashboard", layout="wide")

 # Session check
    if 'logged_in' not in st.session_state:
        st.switch_page("pages/login.py")

    db = DatabaseManager()

    # Header
    st.markdown("## 🔐 Cybersecurity Intelligence Dashboard")
    st.markdown("Monitor threats, incidents, and response metrics.")

    # KPIs
    stats = db.get_domain_stats("cybersecurity")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Incidents", stats.get("total_incidents", 0))
    with col2:
        st.metric("Open Incidents", stats.get("open_incidents", 0))
    with col3:
        st.metric("Avg Resolution Time", f"{stats.get('avg_resolution_time', 0):.1f} hrs")

    st.markdown("---")

    # Load data
    df = db.get_table_data("cyber_incidents")

    # Charts
    st.subheader("📊 Incident Visualizations")

    col1, col2 = st.columns(2)

    with col1:
        if not df.empty:
            pie = ChartBuilder.create_pie_chart(df, "status", "status", "Incident Status Distribution")
            st.plotly_chart(pie, use_container_width=True)

    with col2:
        if not df.empty:
            bar = ChartBuilder.create_bar_chart(df, "severity", "id", "Incidents by Severity")
            st.plotly_chart(bar, use_container_width=True)

    st.markdown("---")

    # Data table
    st.subheader("📋 Incident Table")
    st.dataframe(df)

     # CRUD - Add Incident
    st.markdown("---")
    st.subheader("Report New Incident")

    with st.form("add_incident"):
        title = st.text_input("Incident Title")
        severity = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
        status = st.selectbox("Status", ["Open", "Investigating", "Resolved"])
        assigned_to = st.text_input("Assigned Analyst")

        submitted = st.form_submit_button("Create Incident")

        if submitted:
            db.execute_query("""
                INSERT INTO cyber_incidents (title, severity, status, assigned_to)
                VALUES (?, ?, ?, ?)
            """, (title, severity, status, assigned_to))

            st.success("✅ Incident successfully created")
            st.rerun()

    # Back button
    st.markdown("---")
    if st.button("⬅️ Back to Main Dashboard"):
        st.switch_page("pages/dashboard.py")

if __name__ == "__main__":
    cybersecurity_dashboard()

if st.session_state.get("role") != "admin":
    st.error("You do not have permission to view this page.")
    st.stop()




