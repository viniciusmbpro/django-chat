from django.db.models.deletion import PROTECT
from django.db.models.fields.json import JSONField
from django.db.models.fields.related import ForeignKey
from django.db.models.fields import TextField

from core.base.models import BaseModel

from django.db import models
from accounts.models import Account

class Chat(models.Model):
    name = models.CharField(max_length=255)
    participants = models.ManyToManyField(Account, related_name='chats', blank=True)

    def __str__(self):
        return self.name

class Message(BaseModel):
    text = TextField(verbose_name="texto")
    chat = ForeignKey(to="chat.Chat", verbose_name="para", related_name="messages_to", on_delete=PROTECT)
    terms = JSONField(verbose_name="termos", null=True, blank=True)
    video_paths = JSONField(verbose_name="caminho de vídeos", null=True, blank=True)

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"
        ordering = ["-created_at"]