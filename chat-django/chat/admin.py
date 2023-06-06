from django.contrib import admin
from django.dispatch import receiver
from .models import Chat, ChatParticipant, Message
from django.db.models.signals import post_save


class ChatParticipantInline(admin.TabularInline):
    model = ChatParticipant
    extra = 0
    fields = ('user',)
    show_change_link = True


class ChatParticipantAdmin(admin.ModelAdmin):
    list_display = ('chat', 'user')
    search_fields = ('chat__name', 'user__email')


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    fields = ('text', 'chat', 'terms', 'video_paths')
    show_change_link = True


class MessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'chat', 'terms', 'video_paths')
    search_fields = ('text', 'chat__name', 'terms', 'video_paths')


class ChatAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [ChatParticipantInline, MessageInline]


@receiver(post_save, sender=Chat)
def add_chat_creator_as_participant(sender, instance, created, **kwargs):
    if created:
        ChatParticipant.objects.create(chat=instance, user=instance.created_by)


admin.site.register(Chat, ChatAdmin)
admin.site.register(ChatParticipant, ChatParticipantAdmin)
admin.site.register(Message, MessageAdmin)
