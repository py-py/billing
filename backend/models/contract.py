from django.db import models
from django.utils.translation import gettext as _

from backend.models.mixin import GroupMixin

__all__ = ('Contract', )


class Contract(GroupMixin):
    number = models.CharField(max_length=7)
    date_from = models.DateField(verbose_name=_('Дата начала договора'))
    date_to = models.DateField(verbose_name=_('Дата окончания договора'), blank=True, null=True)
    executor = models.ForeignKey('backend.CompanyInvoice', on_delete=models.PROTECT, related_name='executors', verbose_name=_('Исполнитель'))
    client = models.ForeignKey('backend.CompanyInvoice', on_delete=models.PROTECT, related_name='clients', verbose_name=_('Заказчик'))

    class Meta:
        verbose_name = _('Договор')
        verbose_name_plural = _('Договора')

    def get_service_values(self, month=None, year=None):
        if not(month and year):
            query = self.services.filter(date_from__month__lte=month,
                                         date_from__year__lte=year,
                                         date_to__month__gte=month,
                                         date_to__year__gte=year)
        else:
            query = self.services.all()
        return [{'name': s.address,
                 'count': s.count,
                 'price_without_vat': s.price_without_vat,
                 'price_vat': s.price_vat,
                 'price_full': s.price_full} for s in query]

    def get_service_sum(self):
        return sum(s.price for s in self.services.all())

    def __str__(self):
        return _('Договор №{self.number} от {self.date_from}'.format(self=self))


