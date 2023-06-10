from django.urls import path

from apps.account import views

app_name = 'accounts'

urlpatterns = [
    # site
    path('accounts/register/', views.register_view, name='register'),
    path('accounts/register/create/',
         views.register_create, name='register_create'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/login/create/', views.login_create, name='login_create'),
    path('accounts/logout/', views.logout_view, name='logout'),
]
