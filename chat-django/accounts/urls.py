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

    # urls para api
    path('api/register/create/', ApiRegisterCreateView.as_view(), name='api-register-create'),
    path('api/dashboard/', ApiDashboardView.as_view(), name='api-dashboard'),
]
