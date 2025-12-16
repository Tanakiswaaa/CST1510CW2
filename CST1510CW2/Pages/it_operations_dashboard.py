import streamlit as st
from components.layout import render_header, render_sidebar
from components.footer import render_footer
from database.database_manager import DatabaseManager
from database.crud_it import create_ticket, read_tickets
from components.charts import ChartBuilder

def page():
    if not st.session_state.get('logged_in'):
        st.warning("Please log in.")
        return
    if st.session_state.get('role') not in ['it_operations', 'admin']:
        st.error("Access denied.")
        return

    render_header()
    render_sidebar(username=st.session_state.get('username'), role=st.session_state.get('role'))
    db = DatabaseManager()
    df = read_tickets()

    st.markdown("IT Operations Dashboard")
    if not df.empty:
        st.plotly_chart(ChartBuilder.create_pie_chart(df['status'].value_counts().reset_index().rename(columns={0:'status',1:'count'}), 'count', 'status', 'Status Distribution'), use_container_width=True)
        st.dataframe(df)
    else:
        st.info("No tickets yet.")

    st.markdown("Create Ticket")
    with st.form("create_ticket"):
        title = st.text_input("Title")
        category = st.selectbox("Category", ["Hardware","Software","Network","Other"])
        priority = st.selectbox("Priority", ["Low","Medium","High","Critical"])
        assigned_to = st.text_input("Assign to")
        submitted = st.form_submit_button("Create")
    if submitted:
        create_ticket(title, category, priority, st.session_state.get('username'), assigned_to)
        st.success("Ticket created")
        st.experimental_rerun()

    render_footer()

if __name__ == "__main__":
    page()
