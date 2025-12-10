# pages/it_operations_dashboard.py
import streamlit as st
from database.db_manager import DatabaseManager
from components.charts import ChartBuilder

def it_operations_dashboard():
    st.set_page_config(page_title="IT Operations Dashboard", layout="wide")

    if 'logged_in' not in st.session_state:
        st.switch_page("pages/login.py")

    db = DatabaseManager()

    st.markdown("## 🛠️ IT Operations Dashboard")
    st.markdown("Track tickets, performance, and service delivery.")

    stats = db.get_domain_stats("it_operations")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Tickets", stats.get("total_tickets", 0))
    with col2:
        st.metric("Open Tickets", stats.get("open_tickets", 0))
    with col3:
        st.metric("Avg Resolution Time", f"{stats.get('avg_resolution_time', 0):.1f} hrs")

    df = db.get_table_data("it_tickets")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        pie = ChartBuilder.create_pie_chart(df, "status", "status", "Ticket Status")
        st.plotly_chart(pie, use_container_width=True)

    with col2:
        bar = ChartBuilder.create_bar_chart(df, "priority", "id", "Tickets by Priority")
        st.plotly_chart(bar, use_container_width=True)

    st.markdown("---")
    st.subheader("🎫 Ticket Table")
    st.dataframe(df)

    # Create new ticket
    st.markdown("---")
    st.subheader("➕ Create Ticket")

    with st.form("add_ticket"):
        title = st.text_input("Ticket Title")
        priority = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"])
        status = st.selectbox("Status", ["Open", "In Progress", "Closed"])
        assigned_to = st.text_input("Assigned Engineer")

        submitted = st.form_submit_button("Create Ticket")

        if submitted:
            db.execute_query("""
                INSERT INTO it_tickets (title, priority, status, assigned_to)
                VALUES (?, ?, ?, ?)
            """, (title, priority, status, assigned_to))
            st.success("✅ Ticket created")
            st.rerun()

    if st.button("⬅️ Back to Dashboard"):
        st.switch_page("pages/dashboard.py")

if __name__ == "__main__":
    it_operations_dashboard()

if st.session_state.get("role") != "admin":
    st.error("You do not have permission to view this page.")
    st.stop()
