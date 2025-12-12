import streamlit as st
import pandas as pd
import plotly.express as px

from authentication.auth_system import AuthenticationSystem 
from database.database_manager import DatabaseManager
from database.crud_it import create_ticket, read_tickets, update_ticket_status, delete_ticket

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "user" not in st.session_state:
    st.session_session.user = None



def login_page():
    st.title("Login to Multi-Domain Intelligence Platform")

    username = st.text_input("Username")
    password = st.text_input("Password," type+"password")

    if st.button("Login"):
        auth = AuthenticationSystem()
        success, user = auth.login_user(username, password)

        if success:
            st.session_state.authenticated = True
            st.session_state.user = user
            st.success(f"Welcome, {user['username']}!")
            st.rerun()
        else:
            st.error("Invalid username or password")

def it_dashboard():
    st.title("IT Operations Dashboard")

    st.write("Manage tickets, visualise system performance, and track operations.")

    rows = read_tickets()
    df = pd.DataFrame(rows, columns=[
      "ticket_id", "title", "category", "status", "assigned_to", "created_date", "resolved_date"  
    ])

    st.subheader("Create New Ticket")

    title = st.text_input("Title")
    category = st.selectbox("Category", ["Hardware", "Software", "Network", "Account", "Other"])
    status = st.selectbox("Status", ["New", "Assigned", "In Progress", "Waiting for User", "Resolved", "Closed"])
    assigned_to = st.text_input("Assigned To (IT Staff)")
    created_date = st.date_input("Created Date")
    resolved_date = st.date_input("Resolved Date")

    if st.button("Create Ticket"):
        create_ticket(title, category, status, assigned_to, created_date.isoformat(), resolved_date.isoformat())
        st.success("Ticket created successfully!")
        st.rerun()

    st.divider()

    st.subheader("Ticket Overview")
    st.dataframe(df, use_container_width=True)

    st.divider()

    st.subheader("Update Ticket Status")

    ticket_ids = df["ticket_id"].tolist()
    if ticket_ids:
        selected_ticket = st.selectbox("Select Ticket ID", ticket_ids)
        new_status = st.selectbox("New Status", ["New", "Assigned", "In Progress", "Waiting for User", "Resolved", "Closed"])

        if st.button("Update Status"):
            update_ticket_status(selected_ticket, new_status)
            st.success("Ticket status updated!")
            st.rerun()

    st.divider()

    st.subheader("Delete Ticket")

    del_ticket = st.selectbox("Select Ticket to Delete", ticket_ids)

    if st.button("Delete Ticket"):
        delete_ticket(del_ticket)
        st.warning("Ticket deleted.")
        st.rerun()

    st.divider()

    st.subheader("Visual Analytics")

    if len(df) > 0:
        col1, col2 = st.columns(2)

        with col1:
            fig1 = px.bar(df, x="category", title="Tickets by Category")
            st.plotly_chart(fig1, use_container_width=True)

        with col2:
            fig2 = px.pie(df, names="status", title="Ticket Status Distribution")
            st.plotly_chart(fig2, use_container_width=True)



def main():
    if not st.session_state.authenticated:
        login_page()
        return

    user_role = st.session_state.user["role"]

    st.sidebar.title("📌 Navigation")
    st.sidebar.write(f"Logged in as: **{st.session_state.user['username']}**")
    st.sidebar.write(f"Role: **{user_role}**")

    page = st.sidebar.selectbox("Menu", ["IT Dashboard", "Logout"])

    if page == "IT Dashboard":
        it_dashboard()
    elif page == "Logout":
        st.session_state.authenticated = False
        st.session_state.user = None
        st.rerun()


if __name__ == "__main__":
    main()

from components.footer import render_footer
render_footer()

{
  "admin_user": {
    "password_hash": "$2b$12$kQw0r2w0pC5Tg8y5r3uKCO9KqZJmE2cG4QpNqfR5JxQe0CwqT1y3a",
    "role": "admin",
    "created_at": "2024-10-10T10:00:00",
    "last_login": null
  },
  "alice_cyber": {
    "password_hash": "$2b$12$CxHqKZrPqYw9hTtWjRr9mO/4B.srV3G9kZPuF9KnJxM3QnQZrP1eE",
    "role": "cybersecurity",
    "created_at": "2024-10-11T10:00:00",
    "last_login": null
  },
  "bob_data": {
    "password_hash": "$2b$12$M4Pqz5kqSgqL4vWjR9PqTe4yYwZVnD8nN8xkZPqV5B0fRjM1QeWqK",
    "role": "data_science",
    "created_at": "2024-10-11T10:00:00",
    "last_login": null
  },
  "charlie_it": {
    "password_hash": "$2b$12$Rkq3Y9f9kH2Fv5WqZp1MEOqvXn5FJmV7JZQn8R3KpZXp3yZ1wQ2aS",
    "role": "it_operations",
    "created_at": "2024-10-11T10:00:00",
    "last_login": null
  }
}
