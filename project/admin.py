from django.contrib import admin


class InvoiceAdminSite(admin.AdminSite):
    site_header = 'Invoice panel'
    site_title = 'Invoice'
    site_url = None
    index_title = 'Invoice panel'


invoice_admin = InvoiceAdminSite()
