import frappe
import json


@frappe.whitelist(allow_guest=True)
def read_quota(site_name=None):
    # site_name = 'local.tour'
    if not site_name:
        return "sitename missing"
    doc = frappe.get_doc('ERPNext Site', site_name)
    if doc:
        return json.loads(doc.quota)
    return "not found"
