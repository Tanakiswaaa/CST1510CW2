import streamlit as st

st.set_page_config(
    page_title="Multi-Domain Intelligence Platform",
    layout="wide"
)

st.markdown("""
<style>
footer {visibility: hidden;}

.stButton>button {
    border-radius: 8px;
    font-weight: 600;
}

[data-testid="metric-container"] {
    background-color: #161B22;
    border-radius: 10px;
    padding: 1rem;
}

thead tr th {
    background-color: #1f2933;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("Multi-Domain Intelligence Platform")

st.markdown(
    """
    Welcome to the Multi-Domain Intelligence Platform.

    Use the sidebar to navigate between:
    - Login
    - Cybersecurity Dashboard
    - Data Science Dashboard
    - IT Operations Dashboard
    """
)

st.info(
    "This platform provides domain-specific intelligence, analytics, and AI-assisted insights "
    "for cybersecurity, data governance, and IT operations."
)
