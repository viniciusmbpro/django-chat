from django.urls import path

from chat.views import *

app_name = 'chat'

urlpatterns = [
    path('chats/', ChatList.as_view(), name='chat-list'),
    path('chats/<int:pk>/', ChatDetail.as_view(), name='chat-detail'),
    path('chats/<int:pk>/delete/', ChatDelete.as_view(), name='chat-delete'),
    path('chats/<int:pk>/update/', ChatUpdate.as_view(), name='chat-update'),
    path('chats/<int:pk>/archive/', ChatArchive.as_view(), name='chat-archive'),
    path('chats/<int:pk>/unarchive/', ChatUnarchive.as_view(), name='chat-unarchive'),
    path('chats/<int:pk>/trash/', ChatTrash.as_view(), name='chat-trash'),
    path('chats/<int:pk>/restore/', ChatRestore.as_view(), name='chat-restore'),
    path('chats/<int:pk>/messages/<int:message_pk>/', ChatMessagesDetail.as_view(), name='chat-messages-detail'),
    path('chats/<int:pk>/messages/<int:message_pk>/read/', ChatMessagesRead.as_view(), name='chat-messages-read'),
    path('chats/<int:pk>/messages/<int:message_pk>/unread/', ChatMessagesUnread.as_view(), name='chat-messages-unread'),
    path('chats/<int:pk>/messages/<int:message_pk>/delete/', ChatMessagesDelete.as_view(), name='chat-messages-delete'),
    path('chats/<int:pk>/messages/<int:message_pk>/update/', ChatMessagesUpdate.as_view(), name='chat-messages-update'),
    path('chats/<int:pk>/messages/<int:message_pk>/reply/', ChatMessagesReply.as_view(), name='chat-messages-reply'),
    path('chats/<int:pk>/messages/<int:message_pk>/forward/', ChatMessagesForward.as_view(), name='chat-messages-forward'),
    path('chats/<int:pk>/messages/<int:message_pk>/copy/', ChatMessagesCopy.as_view(), name='chat-messages-copy'),
    path('chats/<int:pk>/messages/<int:message_pk>/move/', ChatMessagesMove.as_view(), name='chat-messages-move'),
    path('chats/<int:pk>/messages/<int:message_pk>/restore/', ChatMessagesRestore.as_view(), name='chat-messages-restore'),
    path('chats/<int:pk>/messages/<int:message_pk>/archive/', ChatMessagesArchive.as_view(), name='chat-messages-archive'),
    path('chats/<int:pk>/messages/<int:message_pk>/unarchive/', ChatMessagesUnarchive.as_view(), name='chat-messages-unarchive'),
    path('chats/<int:pk>/messages/<int:message_pk>/trash/', ChatMessagesTrash.as_view(), name='chat-messages-trash'),
]
