from django.db import models
from django.utils.translation import gettext as _


class Client(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('Клиент')
        verbose_name_plural = _('Клиенты')


class Contract(models.Model):
    number = models.CharField(max_length=7)
    start = models.DateField(verbose_name=_('Дата начала договора'))
    finish = models.DateField(verbose_name=_('Дата окончания договора'))
    client = models.ForeignKey('backend.Client', on_delete=models.PROTECT, related_name='сontracts', verbose_name=_('Клиент'))

    class Meta:
        verbose_name = _('Договор')
        verbose_name_plural = _('Договора')


class Address(models.Model):
    country = models.CharField(max_length=255, verbose_name=_('Страна'))
    region = models.CharField(max_length=255, verbose_name=_('Область'))
    city = models.CharField(max_length=255, verbose_name=_('Город'))
    street_name = models.CharField(max_length=255, verbose_name=_('Улица'))
    house_number = models.CharField(max_length=255, verbose_name=_('Номер дома'))
    house_letter = models.CharField(max_length=255, verbose_name=_('Буква дома'), blank=True, default='')

    class Meta:
        verbose_name = _('Адрес')
        verbose_name_plural = _('Адреса')


class Service(models.Model):
    contract = models.ForeignKey('backend.Address', on_delete=models.CASCADE, related_name='services', verbose_name=_('Адрес'))
    name = models.CharField(max_length=255, verbose_name=_('Наименование'))
    address = models.ForeignKey('backend.Address', on_delete=models.PROTECT, related_name='addresses', verbose_name=_('Адрес'))
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name=_('Стоимость'))
    count = models.PositiveSmallIntegerField(verbose_name=_('Количество услуг'))

    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')

