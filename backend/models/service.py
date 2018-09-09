from django.db import models
from django.utils.translation import gettext as _

from backend.models.mixin import GroupMixin
from backend.settings import DEFAULT_CURRENCY, DEFAULT_DECIMAL_DIGITS, DEFAULT_DECIMAL_PLACES
from backend.utils import *

__all__ = ('Service', 'ServiceType', )


class ServiceType(GroupMixin):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=DEFAULT_DECIMAL_DIGITS, decimal_places=DEFAULT_DECIMAL_PLACES,
                                verbose_name=_('Цена услуги'))

    class Meta:
        verbose_name = _('Тип сервисной услуги')
        verbose_name_plural = _('Типы сервисных услуг')

    def __str__(self):
        return _('{self.name}({self.price} {DEFAULT_CURRENCY})'.format(self=self, DEFAULT_CURRENCY=DEFAULT_CURRENCY))


class Service(GroupMixin):
    contract = models.ForeignKey('backend.Contract', on_delete=models.CASCADE, related_name='services',
                                 verbose_name=_('Договор'))
    address = models.ForeignKey('backend.Address', on_delete=models.PROTECT, related_name='addresses',
                                verbose_name=_('Адрес'))
    count = models.PositiveSmallIntegerField(verbose_name=_('Количество услуг'), blank=True, default=1)
    date_from = models.DateField(verbose_name=_('Дата начала предоставления услуги'), blank=True, null=True)
    date_to = models.DateField(verbose_name=_('Дата окончания предоставления услуги'), blank=True, null=True)
    comment = models.CharField(max_length=255, verbose_name=_('Комментарий'), null=True, blank=True)

    type_service = models.ForeignKey('backend.ServiceType', on_delete=models.PROTECT, related_name='services',
                                     verbose_name=_('Тип услуги'), null=True, blank=True)
    price = models.DecimalField(max_digits=DEFAULT_DECIMAL_DIGITS, decimal_places=DEFAULT_DECIMAL_PLACES,
                                verbose_name=_('Цена услуги'), null=True, blank=True)

    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')

    def save(self, *args, **kwargs):
        if not self.date_from:
            self.date_from = self.contract.date_from
        super(Service, self).save(*args, **kwargs)

    @property
    def price_full(self):
        return (self.price or self.type_service.price) * self.count

    @property
    def price_without_vat(self):
        return calculate_price_without_vat(self.price_full)

    @property
    def price_vat(self):
        return calculate_vat(self.price_full)

    def __str__(self):
        return _('{self._meta.verbose_name} №{self.pk}({self.address})'.format(self=self))
