from django.db import models
from django.utils.translation import gettext as _

from backend.models.mixin import GroupMixin

__all__ = ('Company', 'LegacyEntity')


class Company(GroupMixin):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    client = models.BooleanField(default=True)
    legacy_entity = models.ForeignKey('backend.LegacyEntity', on_delete=models.CASCADE, related_name='entities', verbose_name=_('Юридическое лицо'))

    class Meta:
        verbose_name = _('Клиент')
        verbose_name_plural = _('Клиенты')

    def __str__(self):
        return _('{self.name}'.format(self=self))


class LegacyEntity(GroupMixin):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    patronymic = models.CharField(max_length=32)
    document = models.CharField(max_length=255)

    def get_full_name(self):
        return '{self.last_name} {self.first_name} {self.patronymic}'.format(self=self)

    def get_short_name(self):
        return '{self.last_name} {self.first_name[0]}.{self.patronymic[0]}'.format(self=self)

    def __str__(self):
        return self.get_full_name()