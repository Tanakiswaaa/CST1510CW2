import streamlit as st
import plotly.express as px
from ai.assistant import ask_ai

from analytics.cyber_analysis import (
    load_incidents_df,
    incidents_by_category,
    avg_resolution_by_category,
    phishing_trend_over_time
)

# Access control
if "user" not in st.session_state or st.session_state["user"] is None:
    st.warning("Please log in to access the Cybersecurity dashboard.")
    st.stop()

st.title("Cybersecurity Intelligence Dashboard")

df = load_incidents_df()

st.subheader("Incident Distribution by Category")
cat_df = incidents_by_category(df)
fig1 = px.bar(
    cat_df,
    x="category",
    y="incident_count",
    title="Incidents by Threat Category"
)
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Average Resolution Time by Category")
res_df = avg_resolution_by_category(df)
fig2 = px.bar(
    res_df,
    x="category",
    y="resolution_time_hours",
    title="Response Bottleneck Analysis (Hours)"
)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Phishing Incident Trend Over Time")
trend_df = phishing_trend_over_time(df)
fig3 = px.line(
    trend_df,
    x="timestamp",
    y="incident_count",
    title="Weekly Phishing Incident Trend"
)
st.plotly_chart(fig3, use_container_width=True)

st.markdown(
    """
    ### Key Insight
    The analysis reveals a sustained increase in phishing incidents over time.
    Additionally, phishing incidents exhibit higher average resolution times
    compared to other threat categories, indicating a response bottleneck
    within incident handling workflows.
    """
)

st.subheader("AI Cybersecurity Assistant")

user_prompt = st.text_area(
    "Ask a question about the cybersecurity data:",
    placeholder="Why are phishing incidents taking longer to resolve?"
)

if st.button("Ask AI") and user_prompt.strip():
    with st.spinner("Analyzing data..."):
        response = ask_ai(user_prompt)
        st.write(response)
