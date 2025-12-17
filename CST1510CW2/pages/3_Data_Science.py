import streamlit as st
import plotly.express as px

from analytics.data_science_analysis import (
    load_datasets_df,
    dataset_sizes,
    source_distribution
)

# Access control
if "user" not in st.session_state or st.session_state["user"] is None:
    st.warning("Please log in to access the Data Science dashboard.")
    st.stop()

st.title("Data Science Governance Dashboard")

df = load_datasets_df()

st.subheader("Largest Datasets by Resource Consumption")
size_df = dataset_sizes(df)
fig1 = px.bar(
    size_df,
    x="name",
    y="size_score",
    title="Dataset Resource Consumption"
)
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Dataset Source Distribution")
source_df = source_distribution(df)
fig2 = px.bar(
    source_df,
    x="source",
    y="dataset_count",
    title="Datasets by Source Department"
)
st.plotly_chart(fig2, use_container_width=True)

st.markdown(
    """
    ### Governance Insight
    Analysis shows that a small number of datasets consume a
    disproportionately large amount of resources. Governance
    policies should prioritise archiving or optimising these
    high-impact datasets.
    """
)
