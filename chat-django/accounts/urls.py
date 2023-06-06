from django.urls import path

from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    # site
    path('accounts/register/', register_view, name='register'),
    path('accounts/register/create/', register_create, name='register_create'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/login/create/', login_create, name='login_create'),
    path('accounts/logout/', logout_view, name='logout'),
    path('accounts/dashboard/', dashboard, name='dashboard'),
    path(
        'accounts/dashboard/chat/new/',
        DashboardChat.as_view(),
        name='dashboard_chat_new'
    ),
    path(
        'accounts/dashboard/chat/delete/',
        DashboardChatDelete.as_view(),
        name='dashboard_chat_delete'
    ),
    path(
        'accounts/dashboard/chat/<uuid:id>/edit/',
        DashboardChat.as_view(),
        name='dashboard_chat_edit'
    ),
    path(
        'account/<int:id>/',
        AccountView.as_view(),
        name='account'
    ),

    # urls para api
    path('api/register/create/', api_register_create, name='api-register-create'),
    path('api/login/create/', api_login_create, name='api-login-create'),
    path('api/logout/', api_logout_view, name='api-logout'),
    # path('api/account/<int:id>/', ApiAccountView.as_view(), name='api-account'),
]
