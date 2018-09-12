from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=User, dispatch_uid="create_user_group")
def create_user_group(sender, instance, **kwargs):
    instance.groups.create(name=f'{instance.username}_group')
