from datetime import date

from django.contrib import admin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import path
from django.utils.translation import gettext as _

from backend import views
from backend.models import *


class BaseGroupAdmin(admin.ModelAdmin):
    exclude = ('group', )

    def get_queryset(self, request):
        queryset = super(BaseGroupAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            group = request.user.groups.first()
            queryset = queryset.filter(group=group)
        return queryset

    def save_model(self, request, obj, form, change):
        obj.group = request.user.groups.first()
        super().save_model(request, obj, form, change)


class CustomerAdmin(BaseGroupAdmin):
    pass


class ContractAdmin(BaseGroupAdmin):
    actions = ('get_invoice', )

    def get_urls(self):
        urls = super(ContractAdmin, self).get_urls()
        urls += [
            path('invoice/<int:year>/<int:month>/<int:contract_id>', views.InvoiceView.as_view(), name='invoice'),
        ]
        return urls

    def get_invoice(self, request, queryset):
        if len(queryset) == 1:
            contract = queryset.first()
            today = date.today()
            year, month = today.year, today.month
            return redirect('admin:invoice', contract_id=contract.pk, year=year, month=month)
        messages.error(request, _('Можно сфомировать счет только для одного договора.'))
    get_invoice.short_description = _('Сформировать счет')


class AddressAdmin(BaseGroupAdmin):
    pass


class StreetTypeAdmin(BaseGroupAdmin):
    pass


class ServiceAdmin(BaseGroupAdmin):
    pass


class ServiceTypeAdmin(BaseGroupAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Contract, ContractAdmin)

admin.site.register(Address, AddressAdmin)
admin.site.register(StreetType, StreetTypeAdmin)

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceType, ServiceTypeAdmin)
