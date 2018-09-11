from django.db import models
from django.utils.translation import gettext as _

from backend.models.mixin import GroupMixin

__all__ = ('Company', 'LegacyEntity', )


class LegacyEntity(GroupMixin):
    first_name = models.CharField(max_length=32, verbose_name=_('Имя'))
    last_name = models.CharField(max_length=32, verbose_name=_('Фамилия'))
    patronymic = models.CharField(max_length=32, verbose_name=_('Отчествео'))
    document = models.CharField(max_length=255, verbose_name=_('На основании какого документа'))

    class Meta:
        verbose_name = _('Юридическое лицо')
        verbose_name_plural = _('Юридические лица')

    def get_full_name(self):
        return '{self.last_name} {self.first_name} {self.patronymic}'.format(self=self)

    def get_short_name(self):
        return '{self.last_name} {self.first_name[0]}.{self.patronymic[0]}'.format(self=self)

    def __str__(self):
        return self.get_short_name()


class Company(GroupMixin):
    name = models.CharField(max_length=255, verbose_name=_('Наименование компании'))
    description = models.CharField(max_length=255, verbose_name=_('Деталировка компании'))
    client = models.BooleanField(default=True, verbose_name=_('Клиент'))
    legacy_entity = models.ForeignKey('backend.LegacyEntityInvoice', on_delete=models.CASCADE, related_name='entities', verbose_name=_('Юридическое лицо'))

    class Meta:
        verbose_name = _('Компания')
        verbose_name_plural = _('Компании')

    def __str__(self):
        return _('{self.name}'.format(self=self))
