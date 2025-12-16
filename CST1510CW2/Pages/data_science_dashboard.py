import streamlit as st
from components.layout import render_header, render_sidebar
from components.footer import render_footer
from database.database_manager import DatabaseManager
from components.charts import ChartBuilder

def page():
    if not st.session_state.get('logged_in'):
        st.warning("Please log in.")
        return
    if st.session_state.get('role') not in ['data_science', 'admin']:
        st.error("Access denied.")
        return

    render_header()
    render_sidebar(username=st.session_state.get('username'), role=st.session_state.get('role'))
    db = DatabaseManager()
    df = db.get_table_data('datasets_metadata')
    st.markdown("Data Science Dashboard")
    if not df.empty:
        st.plotly_chart(ChartBuilder.create_pie_chart(df, 'file_size_mb', 'department', 'Storage by Dept'), use_container_width=True)
        st.dataframe(df)
    else:
        st.info("No datasets yet.")
    render_footer()

if __name__ == "__main__":
    page()
