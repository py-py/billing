from datetime import date

from django.contrib import messages
from django.shortcuts import redirect
from django.urls import path
from django.utils.translation import gettext as _

from backend import views
from backend.admin.base_admin import BaseGroupAdmin

__all__ = ('ContractAdmin', )


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

