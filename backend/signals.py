from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User, dispatch_uid="create_user_group")
def create_user_group(sender, instance, **kwargs):
    if getattr(instance, 'create_user_group', False):
        delattr(instance, 'create_user_group')
        instance.groups.create(name='{name}_group'.format(name=instance.username))
