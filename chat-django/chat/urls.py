from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from chat import views


app_name = 'chat'

urlpatterns = [
    # site
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

    # api
    path(
        'api/chat/',
        views.ChatListCreateAPIView.as_view(),
        name='api-list'
    ),
    path(
        'api/chat/<uuid:id>/',
        views.ChatDeleteUpdateAPIView.as_view(),
        name='api-update'
    ),
    path(
        'api/chat/<uuid:id>/add_participant/',
        views.ChatAddParticipantAPIView.as_view(),
        name='api-add-participant'
    ),
    path(
        'api/chat/<uuid:id>/add_message/',
        views.ChatAddMessageAPIView.as_view(),
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
