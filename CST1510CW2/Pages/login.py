import streamlit as st
from database.auth import Authentication
from components.layout import render_header, render_sidebar
from components.footer import render_footer

auth = Authentication()

def page():
    render_header()
    render_sidebar()
    st.title("Login")
    with st.form("login"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
    if submitted:
        ok, role = auth.verify_user(username, password)
        if ok:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.session_state['role'] = role
            st.success("Login successful")
            st.experimental_rerun()
        else:
            st.error("Invalid credentials")
    render_footer()

if __name__ == "__main__":
    page()
