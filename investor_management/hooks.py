app_name = "investor_management"
app_title = "Investor Management"
app_publisher = "dopy"
app_description = "investor_management"
app_email = "natenaelnebiyu@gmail.com"
app_license = "mit"

import frappe

def on_update(doc, method):
    if doc.status == "Approved" and not doc.rental_space:
        # Find first available space matching the investment type
        available_space = frappe.get_all("Rental Space",
            filters={
                "status": "Available",
                "space_type": doc.investment_type
            },
            limit=1
        )
        
        if available_space:
            space = frappe.get_doc("Rental Space", available_space[0].name)
            space.status = "Occupied"
            space.save()
            
            doc.rental_space = space.name
            doc.save()
            
            frappe.msgprint(f"Assigned Rental Space: {space.name}")