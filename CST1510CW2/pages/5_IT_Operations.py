import streamlit as st
import plotly.express as px

from analytics.it_ops_analysis import (
    load_tickets_df,
    avg_resolution_by_staff,
    delay_by_status
)

# Access control
if "user" not in st.session_state or st.session_state["user"] is None:
    st.warning("Please log in to access the IT Operations dashboard.")
    st.stop()

st.title("IT Operations Performance Dashboard")

df = load_tickets_df()

st.subheader("Average Resolution Time by Staff Member")
staff_df = avg_resolution_by_staff(df)
fig1 = px.bar(
    staff_df,
    x="assigned_to",
    y="resolution_time_hours",
    title="Staff Performance Analysis"
)
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Average Resolution Time by Ticket Status")
status_df = delay_by_status(df)
fig2 = px.bar(
    status_df,
    x="status",
    y="resolution_time_hours",
    title="Process Bottleneck Analysis"
)
st.plotly_chart(fig2, use_container_width=True)

st.markdown(
    """
    ### Operational Insight
    Tickets in specific workflow states exhibit longer
    resolution times, indicating process-related delays
    rather than individual staff performance issues.
    """
)
