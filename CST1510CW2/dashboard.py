if st.button("Cybersecurity", use_container_width=True):
    st.switch_page("pages/cybersecurity_dashboard.py")

if st.button("Data Science", use_container_width=True):
    st.switch_page("pages/data_science_dashboard.py")

if st.button("IT Operations", use_container_width=True):
    st.switch_page("pages/it_operations_dashboard.py")

if st.session_state.get("role") != "admin":
    st.error("You do not have permission to view this page.")
    st.stop()

from components.footer import render_footer
render_footer()
