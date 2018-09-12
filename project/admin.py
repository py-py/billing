from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext as _


class InvoiceAdminSite(admin.AdminSite):
    site_title = _('Invoice Admin Site')
    site_header = _('Invoice administration')
    index_title = _('Invoice administration')
    site_url = '/'


invoice_admin = InvoiceAdminSite(name='invoice_admin')


class CustomUserAdmin(UserAdmin):
    def save_model(self, request, obj, form, change):
        if not getattr(obj, 'pk'):
            obj.create_user_group = True
        super(CustomUserAdmin, self).save_model(request, obj, form, change)


invoice_admin.register(User, CustomUserAdmin)
invoice_admin.register(Group, GroupAdmin)
