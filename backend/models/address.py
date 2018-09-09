from django.db import models
from django.utils.translation import gettext as _

from backend.models.mixin import GroupMixin

__all__ = ('Address', 'StreetType', )


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


class StreetType(GroupMixin):
    name = models.CharField(max_length=12)
    short_name = models.CharField(max_length=4)

    class Meta:
        verbose_name = _('Тип улицы')
        verbose_name_plural = _('Типы улиц')

    def __str__(self):
        return _('{self.short_name}:{self.name}'.format(self=self))
