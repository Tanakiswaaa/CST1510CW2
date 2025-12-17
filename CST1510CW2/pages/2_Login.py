import streamlit as st
from database.security import authenticate_user

st.title("Login")

# Ensure session state exists
if "user" not in st.session_state:
    st.session_state["user"] = None

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = authenticate_user(username, password)

    if user:
        st.session_state["user"] = user
        st.success(f"Login successful. Role: {user['role']}")
        st.info("Use the sidebar to access the available dashboards.")
    else:
        st.error("Invalid username or password.")

