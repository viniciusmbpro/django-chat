from django.db.models.deletion import PROTECT
from django.db.models.fields.json import JSONField
from django.db.models.fields.related import ForeignKey
from django.db.models.fields import TextField

from core.base.models import BaseModel

from django.db import models
from accounts.models import Account

from django.db import models
from django.db.models import Count, Q

class ChatManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset().annotate(
            participants_count=Count('chat_participants', distinct=True),
            messages_count=Count('messages_to', distinct=True),
        )
        return qs

class Chat(BaseModel):
    name = models.CharField(max_length=255)

    objects = ChatManager()

    def __str__(self):
        return self.name


class ChatParticipant(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_participants')
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='chat_participants')

    def __str__(self):
        return f"{self.chat.name} - {self.user.email}"


class Message(BaseModel):
    text = TextField(verbose_name="texto")
    chat = ForeignKey(to="chat.Chat", verbose_name="para",
                      related_name="messages_to", on_delete=PROTECT)
    terms = JSONField(verbose_name="termos", null=True, blank=True)
    video_paths = JSONField(
        verbose_name="caminho de vídeos", null=True, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"
        ordering = ["-created_at"]
