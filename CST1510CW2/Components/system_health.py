import streamlit as st
import psutil
import sqlite3
import time
from datetime import datetime

DB_NAME = "intelligence_platform.db"

def system_health():
    st.markdown("System Health Monitor")

    col1, col2, col3 = st.columns(3)

    # CPU Usage
    with col1:
        cpu = psutil.cpu_percent(interval=1)
        st.metric("CPU Usage", f"{cpu}%", "OK" if cpu < 75 else "High")

    # Memory Usage
    with col2:
        memory = psutil.virtual_memory().percent
        st.metric("Memory Usage", f"{memory}%", "OK" if memory < 75 else "High")

    # Disk Usage
    with col3:
        disk = psutil.disk_usage("/").percent
        st.metric("Disk Usage", f"{disk}%", "OK" if disk < 80 else "High")

    st.markdown("---")

    # Database Health
    st.markdown("Database Status")

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM cyber_incidents")
        incidents = cursor.fetchone()[0]
        conn.close()

        st.success(f"Database connected successfully — {incidents} cyber incidents found")

    except Exception as e:
        st.error("Database connection failed")
        st.code(str(e))

    st.markdown("---")
    st.caption(f"Last checked: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

