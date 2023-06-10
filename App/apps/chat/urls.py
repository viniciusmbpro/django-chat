from django.urls import path
from apps.chat import views


app_name = 'chat'

urlpatterns = [
    path(
        '',
        views.ChatListViewBase.as_view(),
        name='chat-list'
    ),
    path(
        'accounts/dashboard/',
        views.dashboard,
        name='dashboard'
    ),
    path(
        'chat/dashboard/new/',
        views.DashboardChat.as_view(),
        name='dashboard_chat_new'
    ),
    path(
        'chat/dashboard/delete/',
        views.DashboardChatDelete.as_view(),
        name='dashboard_chat_delete'
    ),
    path(
        'chat/dashboard/<uuid:id>/edit/',
        views.DashboardChat.as_view(),
        name='dashboard_chat_edit'
    ),
    path(
        'chat/get_in/<uuid:id>/',
        views.ChatGetInView.as_view(),
        name='get-in'
    ),
    path(
        'chat/<uuid:id>/',
        views.ChatDetail.as_view(),
        name='chat-view'
    ),
    path(
        'chat/search/',
        views.ChatListViewSearch.as_view(),
        name='search'
    ),
    path(
        'chat/add_message/<uuid:id>/',
        views.ChatAddMessageView.as_view(),
        name='add-message'
    ),
]
