# components/layout.py
import streamlit as st

PRIMARY = "#7df9ff"
BG = "#0F1117"
CARD = "#121316"
TEXT = "#e6eef3"
MUTED = "#9fb6bd"

def inject_global_css():
    st.markdown(f"""
    <style>
    .reportview-container .main {{ background: linear-gradient(180deg, {BG} 0%, #09090b 100%) !important; }}
    .db-header {{ background: linear-gradient(135deg, rgba(10,10,15,0.9), rgba(8,8,10,0.9)); padding: 18px; border-radius: 10px; color: {TEXT}; box-shadow: 0 8px 24px rgba(0,0,0,0.6); }}
    .stButton>button {{ background: linear-gradient(90deg, {PRIMARY}, #6ee7e7) !important; color: #020304 !important; border-radius:8px; }}
    .card {{ background: {CARD}; padding:12px; border-radius:10px; color:{TEXT}; border:1px solid #222; }}
    .muted {{ color: {MUTED}; }}
    .stDataFrame thead th {{ color: {TEXT} !important; }}
    a {{ color: {PRIMARY} !important; }}
    </style>
    """, unsafe_allow_html=True)

def render_header(title="Multi-Domain Intelligence Platform", subtitle="Unified dashboards • Secure access"):
    inject_global_css()
    st.markdown(f"""
    <div class="db-header">
      <h1 style="margin:0;">{title}</h1>
      <div class="muted" style="margin-top:6px;">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)

def render_sidebar(username=None, role=None):
    st.sidebar.markdown("---")
    if username:
        st.sidebar.markdown(f"{username}**  ")
    if role:
        st.sidebar.markdown(f"Role:** {role.replace('_',' ').title()}  ")
    st.sidebar.markdown("---")
    st.sidebar.button("Home", key="sb_home")
    st.sidebar.button("Logout", key="sb_logout")
    st.sidebar.markdown("---")
