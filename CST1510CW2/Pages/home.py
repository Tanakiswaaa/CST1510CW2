import streamlit as st
from components.layout import render_header, render_sidebar
from components.footer import render_footer

def page():
    render_header()
    render_sidebar(username=st.session_state.get('username'), role=st.session_state.get('role'))
    st.markdown("Welcome to your Multi-Domain Intelligence Platform")
    st.write("Use the navigation buttons to move between dashboards.")
    render_footer()

if __name__ == "__main__":
    page()

