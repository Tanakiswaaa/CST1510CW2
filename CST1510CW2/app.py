import streamlit as st
from components.layout import render_header

st.set_page_config(page_title="Multi-Domain Intelligence Platform", layout="wide")

def main():
    render_header()
    st.markdown("Welcome! Use the menu to go to the login page.")
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("Go to Login"):
            st.experimental_set_query_params(page="login")
            st.switch_page("pages/2_Login.py")
    with col2:
        if st.button("README"):
            st.info("See README.md in the project root.")
    from components.footer import render_footer
    render_footer()

if __name__ == "__main__":
    main()

   



