import streamlit as st
from components.layout import render_header, render_sidebar
from components.footer import render_footer
from database.database_manager import DatabaseManager

def page():
    if not st.session_state.get('logged_in'):
        st.warning("Please log in to continue.")
        return
    render_header()
    render_sidebar(username=st.session_state.get('username'), role=st.session_state.get('role'))
    db = DatabaseManager()
    stats_cyber = db.get_domain_stats('cybersecurity')
    stats_ds = db.get_domain_stats('data_science')
    stats_it = db.get_domain_stats('it_operations')

    st.markdown("Quick Overview")
    c1, c2, c3 = st.columns(3)
    c1.metric("Cyber Incidents", stats_cyber.get('total_incidents', 0))
    c2.metric("Datasets", stats_ds.get('total_datasets', 0))
    c3.metric("IT Tickets", stats_it.get('total_tickets', 0))

    render_footer()

if __name__ == "__main__":
    page()
