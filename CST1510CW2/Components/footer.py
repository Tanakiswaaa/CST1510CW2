import streamlit as st
from datetime import datetime

def render_footer():
    st.markdown("---")
    st.markdown(f"<div style='text-align:center; color:#9fb6bd;'>Multi-Domain Intelligence Platform • v1.0 • © {datetime.now().year}</div>", unsafe_allow_html=True)
   