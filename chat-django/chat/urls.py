from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from chat.views import *

app_name = 'chat'

urlpatterns = [
    # site
    path(
        '', 
        ChatListViewBase.as_view(), 
        name='chat-list'
    ),
    path(
        'accounts/dashboard/', 
        dashboard, 
        name='dashboard'),
    path(
        'chat/dashboard/new/',
        DashboardChat.as_view(),
        name='dashboard_chat_new'
    ),
    path(
        'chat/dashboard/delete/',
        DashboardChatDelete.as_view(),
        name='dashboard_chat_delete'
    ),
    path(
        'chat/dashboard/<uuid:id>/edit/',
        DashboardChat.as_view(),
        name='dashboard_chat_edit'
    ),
    path(
        'chat/get_in/<uuid:id>/',
        ChatGetInView.as_view(), 
        name='get-in'
     ),
    path(
        'chat/<uuid:id>/',
        ChatDetail.as_view(), 
        name='chat-view'
     ),
    path(
        'chat/search/',
        ChatListViewSearch.as_view(), 
        name='search'
     ),
    path(
        'chat/add_message/<uuid:id>/',
        ChatAddMessageView.as_view(), 
        name='add-message'
     ),

    # api
    path(
        'api/chat/',
        ChatListCreateAPIView.as_view(), 
        name='api-list'
     ),
    path(
        'api/chat/<uuid:id>/',
        ChatDeleteUpdateAPIView.as_view(), 
        name='api-update'
     ),
    path(
        'api/chat/<uuid:id>/add_participant/',
        ChatAddParticipantAPIView.as_view(), 
        name='api-add-participant'
     ),
    path(
        'api/chat/<uuid:id>/add_message/',
        ChatAddMessageAPIView.as_view(), 
        name='api-add-message'
     ),

    # rotas de autenticação
    path(
        'api/token/',
        TokenObtainPairView.as_view(), 
        name='token_obtain_pair'
     ),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(), 
        name='token_refresh'
     ),
    path(
        'api/token/verify/',
        TokenVerifyView.as_view(), 
        name='token_verify'
     ),
]
