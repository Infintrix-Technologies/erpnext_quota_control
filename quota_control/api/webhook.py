import frappe
import json


@frappe.whitelist(allow_guest=True)
def read_quota(site_name=None):
    if not site_name:
        return "sitename missing"
    if not frappe.db.exists('Tenant Quota', site_name):
        frappe.throw("Site '{0}' not found in quota control".format(site_name))
    doc = frappe.get_doc('Tenant Quota', site_name)

    result = {
        'users': doc.users,
        'active_users': doc.active_users,
        'space': doc.space,
        'used_space': doc.used_space,
        'private_files_size': doc.private_files_size,
        'public_files_size': doc.public_files_size,
        'backup_files_size': doc.backup_files_size,
        'db_space': doc.db_space,
        'used_db_space': doc.used_db_space,
        'company': doc.max_companies,
        'used_company': doc.used_companies,
        'count_administrator_user': doc.count_administrator_user,
        'count_website_users': doc.count_website_users,
        'valid_till': str(doc.valid_till) if doc.valid_till else None,
        'document_limit': {}
    }

    for row in doc.document_limit:
        result['document_limit'][row.document_type] = {
            'limit': row.limit,
            'period': row.period
        }

    return result


@frappe.whitelist(allow_guest=True, methods=['POST'])
def update_quota(site_name=None, data=None):
    if not site_name:
        return "sitename missing"
    if not data:
        return "data is missing"
    if not frappe.db.exists('Tenant Quota', site_name):
        return "not found"

    data_dict = json.loads(data) if isinstance(data, str) else data

    doc = frappe.get_doc('Tenant Quota', site_name)

    doc.users = data_dict.get('users', 5)
    doc.active_users = data_dict.get('active_users', 0)
    doc.space = data_dict.get('space', 0)
    doc.used_space = data_dict.get('used_space', 0)
    doc.private_files_size = data_dict.get('private_files_size', 0)
    doc.public_files_size = data_dict.get('public_files_size', 0)
    doc.backup_files_size = data_dict.get('backup_files_size', 0)
    doc.db_space = data_dict.get('db_space', 0)
    doc.used_db_space = data_dict.get('used_db_space', 0)
    doc.max_companies = data_dict.get('company', 2)
    doc.used_companies = data_dict.get('used_company', 1)
    doc.count_administrator_user = data_dict.get('count_administrator_user', 0)
    doc.count_website_users = data_dict.get('count_website_users', 0)
    doc.valid_till = data_dict.get('valid_till')

    doc.set('document_limit', [])
    for doctype_name, limit_info in data_dict.get('document_limit', {}).items():
        doc.append('document_limit', {
            'document_type': doctype_name,
            'limit': limit_info.get('limit', 10),
            'period': limit_info.get('period', 'Daily')
        })

    doc.flags.skip_cache_invalidation = True
    doc.save()
    return "updated"
