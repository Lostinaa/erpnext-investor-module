import frappe

def execute(filters=None):
    columns = [
        {"label": "Status", "fieldname": "status", "width": 120},
        {"label": "Count", "fieldname": "count", "fieldtype": "Int"}
    ]
    
    data = frappe.db.sql("""
        SELECT status, COUNT(*) as count
        FROM `tabInvestor`
        GROUP BY status
    """, as_dict=1)
    
    return columns, data