import streamlit as st
from datetime import datetime

def render_footer():
    st.markdown("---")
    st.caption(f"""
    Multi-Domain Intelligence Platform  
    Version 1.0 – Final Release  
    © {datetime.now().year}
    """)

from components.footer import render_footer
render_footer()
