from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Chat, ChatParticipant


@receiver(post_save, sender=Chat)
def add_chat_creator_as_participant(sender, instance, created, **kwargs):
    if created:
        ChatParticipant.objects.create(chat=instance, user=instance.created_by)
