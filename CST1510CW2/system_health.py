import streamlit as st
import psutil
import platform
import time

st.set_page_config(page_title="System Health", layout="wide")

st.title("🩺 System Health Monitor")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("CPU Usage", f"{psutil.cpu_percent()}%")

with col2:
    st.metric("Memory Usage", f"{psutil.virtual_memory().percent}%")

with col3:
    st.metric("Disk Usage", f"{psutil.disk_usage('/').percent}%")

st.markdown("---")

st.subheader("🖥️ Host System Info")

st.code(f"""
OS: {platform.system()}
Release: {platform.release()}
Python: {platform.python_version()}
""")
