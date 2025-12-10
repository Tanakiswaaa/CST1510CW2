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