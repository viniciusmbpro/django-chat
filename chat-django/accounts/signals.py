from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Account

User = get_user_model()


@receiver(post_save, sender=User)
def create_account(sender, instance, created, *args, **kwargs):
    if created:
        # account = Account.objects.create(author=instance)
        # account.save()
        pass
