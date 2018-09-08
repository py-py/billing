from django.db import models
from django.utils.translation import gettext as _

from backend.settings import DEFAULT_CURRENCY, DEFAULT_DECIMAL_DIGITS, DEFAULT_DECIMAL_PLACES

__all__ = ('Customer', 'Contract',
           'Service', 'ServiceType',
           'Address', 'StreetType')


class GroupMixin(models.Model):
    group = models.ForeignKey('auth.Group', null=True, related_name="%(class)s", on_delete=models.CASCADE, verbose_name=_('Группа'))

    class Meta:
        abstract = True
    

class Customer(GroupMixin):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    client = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Клиент')
        verbose_name_plural = _('Клиенты')

    def __str__(self):
        return _('{self.name}'.format(self=self))


class Contract(GroupMixin):
    number = models.CharField(max_length=7)
    date_from = models.DateField(verbose_name=_('Дата начала договора'))
    date_to = models.DateField(verbose_name=_('Дата окончания договора'), blank=True, null=True)
    executor = models.ForeignKey('backend.Customer', on_delete=models.PROTECT, related_name='executors', verbose_name=_('Исполнитель'))
    client = models.ForeignKey('backend.Customer', on_delete=models.PROTECT, related_name='clients', verbose_name=_('Заказчик'))

    class Meta:
        verbose_name = _('Договор')
        verbose_name_plural = _('Договора')

    def __str__(self):
        return _('Договор №{self.number} от {self.date_from}'.format(self=self))


class StreetType(GroupMixin):
    name = models.CharField(max_length=12)
    short_name = models.CharField(max_length=4)

    class Meta:
        verbose_name = _('Тип улицы')
        verbose_name_plural = _('Типы улиц')

    def __str__(self):
        return _('{self.short_name}:{self.name}'.format(self=self))


class Address(GroupMixin):
    country = models.CharField(max_length=255, verbose_name=_('Страна'))
    region = models.CharField(max_length=255, verbose_name=_('Область'))
    city = models.CharField(max_length=255, verbose_name=_('Город'))
    street_name = models.CharField(max_length=255, verbose_name=_('Улица'))
    street_type = models.ForeignKey('backend.StreetType', on_delete=models.PROTECT, verbose_name=_('Тип улицы'))
    building_number = models.CharField(max_length=255, verbose_name=_('Номер дома'))
    building_letter = models.CharField(max_length=255, verbose_name=_('Буква дома'), blank=True, default='')

    class Meta:
        verbose_name = _('Адрес')
        verbose_name_plural = _('Адреса')

    def __str__(self):
        city_address = _('обл. {self.region}, м. {self.city}'.format(self=self))
        street_address = _('{self.street_type.short_name}. {self.street_name}'.format(self=self))
        building_address = _('{self.building_number}{self.building_letter}'.format(self=self))
        return ', '.join((city_address, street_address, building_address))


class ServiceType(GroupMixin):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=DEFAULT_DECIMAL_DIGITS, decimal_places=DEFAULT_DECIMAL_PLACES, verbose_name=_('Цена услуги'))

    class Meta:
        verbose_name = _('Тип сервисной услуги')
        verbose_name_plural = _('Типы сервисных услуг')

    def __str__(self):
        return _('{self.name}({self.price} {DEFAULT_CURRENCY})'.format(self=self, DEFAULT_CURRENCY=DEFAULT_CURRENCY))


class Service(GroupMixin):
    contract = models.ForeignKey('backend.Contract', on_delete=models.CASCADE, related_name='services', verbose_name=_('Договор'))
    address = models.ForeignKey('backend.Address', on_delete=models.PROTECT, related_name='addresses', verbose_name=_('Адрес'))
    count = models.PositiveSmallIntegerField(verbose_name=_('Количество услуг'), blank=True, default=1)
    date_from = models.DateField(verbose_name=_('Дата начала предоставления услуги'), blank=True, null=True)
    date_to = models.DateField(verbose_name=_('Дата окончания предоставления услуги'), blank=True, null=True)
    comment = models.CharField(max_length=255, verbose_name=_('Комментарий'), null=True, blank=True)

    type_service = models.ForeignKey('backend.ServiceType', on_delete=models.PROTECT, related_name='services', verbose_name=_('Тип услуги'), null=True, blank=True)
    price = models.DecimalField(max_digits=DEFAULT_DECIMAL_DIGITS, decimal_places=DEFAULT_DECIMAL_PLACES, verbose_name=_('Цена услуги'), null=True, blank=True)

    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')

    def save(self, *args, **kwargs):
        if not self.date_from:
            self.date_from = self.contract.date_from
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return _('{self._meta.verbose_name} №{self.pk}({self.address})'.format(self=self))
