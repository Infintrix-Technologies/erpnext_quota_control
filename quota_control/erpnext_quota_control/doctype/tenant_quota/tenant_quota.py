# Copyright (c) 2025, Infintrix Technologies and contributors
# For license information, please see license.txt

import requests
import frappe
from frappe.model.document import Document


class TenantQuota(Document):
	def on_update(self):
		if self.flags.get("skip_cache_invalidation"):
			return
		if not self.site_url:
			return
		try:
			url = f"{self.site_url.rstrip('/')}/api/method/erpnext_quota.erpnext_quota.quota.invalidate_cache"
			resp = requests.get(url, timeout=5)
			resp.raise_for_status()
		except Exception as e:
			frappe.log_error(f"Failed to invalidate cache for {self.site_url}: {e}", "Tenant Quota")
