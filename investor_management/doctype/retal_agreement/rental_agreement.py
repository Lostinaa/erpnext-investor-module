import frappe
from frappe.utils import nowdate, add_months

def create_rent_invoice(doc, event):
    if doc.status == "Active":
        invoice = frappe.new_doc("Sales Invoice")
        invoice.customer = doc.investor
        invoice.due_date = add_months(nowdate(), 1)
        invoice.append("items", {
            "item_code": "RENT-" + doc.space_type,
            "qty": 1,
            "rate": doc.monthly_rent
        })
        invoice.insert()
        invoice.submit()
        frappe.msgprint(f"Rent Invoice {invoice.name} created")