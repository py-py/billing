from django.db import models
from django.utils.translation import gettext as _

from backend.models.mixin import GroupMixin

__all__ = ('Address', 'StreetType', )


class Address(GroupMixin):
    country = models.CharField(max_length=255, verbose_name=_('Страна'), default=_('Україна'))
    region = models.CharField(max_length=255, verbose_name=_('Область'), default=_('Київська'))
    city = models.CharField(max_length=255, verbose_name=_('Город'), default=_('Київ'))
    street_name = models.CharField(max_length=255, verbose_name=_('Улица'))
    street_type = models.ForeignKey('backend.StreetType', on_delete=models.PROTECT, verbose_name=_('Тип улицы'))
    building_number = models.CharField(max_length=255, verbose_name=_('Номер дома'))
    building_letter = models.CharField(max_length=255, verbose_name=_('Буква дома'), blank=True, default='')

    class Meta:
        verbose_name = _('Адрес')
        verbose_name_plural = _('Адреса')

    def __str__(self):
        region_address = _('обл. {self.region}'.format(self=self))
        city_address = _('м. {self.city}'.format(self=self))
        street_address = _('{self.street_type.short_name}. {self.street_name}'.format(self=self))
        building_address = _('{self.building_number}{self.building_letter}'.format(self=self))
        return ', '.join((region_address, city_address, street_address, building_address))


class StreetType(GroupMixin):
    name = models.CharField(max_length=12)
    short_name = models.CharField(max_length=4)

    class Meta:
        verbose_name = _('Тип улицы')
        verbose_name_plural = _('Типы улиц')

    def __str__(self):
        return _('{self.short_name}:{self.name}'.format(self=self))
