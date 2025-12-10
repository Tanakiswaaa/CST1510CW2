from database_manager import databaseManager
db = databaseManager
db.connect()

def create_ticket(title, category, status, assigned_to, created_date, resolved_date):
    db.execute_query("""
        INSERT INTO it_tickets (title, category, status, assigned_to, created_date, resolved_date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (title, category, status, assigned_to, created_date, resolved_date))

def read_tickets():
    return db.fetch_all("SELECT * FROM it_tickets")

def update_ticket_status(ticket_id, new status):
    db.execute_query("""
        UPDATE it_tickets SET status = ? WHERE ticket_id = ?
    """, (new_status, ticket_id))

def delete_ticket(ticket_id):
    db.execute_query("DELETE FROM it_tickets WHERE ticket_id = ?", (ticket_id,))

from components.footer import render_footer
render_footer()
