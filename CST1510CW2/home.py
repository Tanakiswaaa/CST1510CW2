st.markdown("---")
st.markdown("Domain Navigation")

domains = [
    ("Cybersecurity", "cybersecurity", "Security incidents and threat analysis"),
    ("Data Science", "data_science", "Dataset management and analytics"),
    ("IT Operations", "it_operations", "Service desk and ticket management"),
    ("Admin Panel", "admin", "System administration and user management")
]

cols = st.columns(2)

for idx, (label, domain_name, description) in enumerate(domains):
    with cols[idx % 2]:
        if st.button(f"{label}", use_container_width=True):
            
            # CYBERSECURITY
            if domain_name == "cybersecurity":
                st.switch_page("pages/cybersecurity_dashboard.py")
            
            # DATA SCIENCE
            elif domain_name == "data_science":
                st.info("Data Science Dashboard coming tomorrow!")
            
            # IT OPERATIONS
            elif domain_name == "it_operations":
                st.info("IT Operations Dashboard coming soon!")
            
            # ADMIN PANEL
            elif domain_name == "admin":
                st.info("Admin Panel coming in Week 10!")

from components.footer import render_footer
render_footer()
