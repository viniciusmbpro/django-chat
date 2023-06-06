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
    path('', ChatListViewBase.as_view(), name='chat-list'),
    path('chat/get_in/<uuid:id>/', ChatGetInView.as_view(), name='get-in'),
    path('chat/<uuid:pk>/', ChatDetail.as_view(), name='chat-view'),
    path('chat/search/', ChatListViewSearch.as_view(), name='search'),
    path('chat/add_message/<uuid:id>/',
         ChatAddMessageView.as_view(), name='add-message'),

    # api
    path('api/chat/', ChatOperationsAPIView.as_view(), name='api-list'),
    path('api/chat/create/', ChatOperationsAPIView.as_view(), name='api-create'),
    path('api/chat/update/<uuid:pk>/',
         ChatOperationsAPIView.as_view(), name='api-update'),
    path('api/chat/delete/<uuid:pk>/',
         ChatOperationsAPIView.as_view(), name='api-delete'),
    path('api/chat/<uuid:pk>/', ChatDetailAPIView.as_view(), name='api-detail'),
    path('api/chat/<uuid:pk>/add_participant/',
         ChatAddParticipantAPIView.as_view(), name='api-add-participant'),
    path('api/chat/<uuid:id>/add_message/',
         ChatAddMessageAPIView.as_view(), name='api-add-message'),

    # rotas de autenticação
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
