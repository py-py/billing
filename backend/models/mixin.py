from django.db import models
from django.utils.translation import gettext as _

__all__ = ('GroupMixin', )


class GroupMixin(models.Model):
    group = models.ForeignKey('auth.Group', null=True, related_name="%(class)s", on_delete=models.CASCADE,
                              verbose_name=_('Группа'))

    class Meta:
        abstract = True

