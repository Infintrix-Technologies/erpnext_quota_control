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


@frappe.whitelist(allow_guest=True, methods=['POST'])
def update_quota(site_name=None, data=None):
    # site_name = 'local.tour'
    if not site_name:
        return "sitename missing"
    if not data:
        return "data is missing"
    doc = frappe.get_doc('ERPNext Site', site_name)
    doc.quota = data
    doc.save()

    return "updated"
