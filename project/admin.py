from django.contrib import admin
from django.utils.translation import gettext as _


class InvoiceAdminSite(admin.AdminSite):
    site_title = _('Invoice Admin Site')
    site_header = _('Invoice administration')
    index_title = _('Invoice administration')
    site_url = '/'


invoice_admin = InvoiceAdminSite(name='invoice_admin')
