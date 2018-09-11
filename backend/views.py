from django import views
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from django.utils.decorators import method_decorator

from backend.decorators import contract_permission_required
from backend.models import Contract
from backend.utils import calculate_vat, calculate_price_without_vat

__all__ = ('InvoiceView', )


@method_decorator(login_required, name='dispatch')
@method_decorator(contract_permission_required, name='dispatch')
class InvoiceView(views.View):
    def get(self, request, *args, **kwargs):
        context = {}
        try:
            month = kwargs['month']
            year = kwargs['year']
            contract = Contract.objects.get(pk=kwargs['contract_id'])
        except (KeyError, Contract.DoesNotExist) as e:
            raise Http404

        context['year'] = year
        context['month'] = month
        context['contract'] = contract
        context['invoice_number'] = '{contract.number}/{year}/{month}'\
            .format(contract=contract, year=year, month=month)
        context['services'] = contract.get_service_values(month=month, year=year)

        context['sum'] = contract.get_service_sum()
        context['vat'] = calculate_vat(context['sum'])
        context['price_without_vat'] = calculate_price_without_vat(context['sum'])

        return render(request, 'billing/invoice.html', context)
