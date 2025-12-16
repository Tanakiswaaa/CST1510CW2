from database_manager import databaseManager
from datetime import datetime

db = databaseManager()

def create_ticket(title, category, priority, created_date, assigned_to=None):
    created_date = datetime.now().isoformat()
    db.execute_query("""
        INSERT INTO it_tickets (title, description, category, priority, status, created_by, assigned_to, created_date)
        VALUES (?, ?, ?, ?, 'NEW', ?, ?, ?)
    """, (title, "", category, priority, created_by, assigned_to, created_date))

def read_tickets(limit=500):
    df = db.get_table_data('it_tickets', limit=limit)
    return df

def update_ticket_status(ticket_id, new status):
    db.execute_query("UPDATE it_tickets SET status = ? WHERE ticket_id = ?", (status, ticket_id))
    
def delete_ticket(ticket_id):
    db.execute_query("DELETE FROM it_tickets WHERE ticket_id = ?", (ticket_id,))

