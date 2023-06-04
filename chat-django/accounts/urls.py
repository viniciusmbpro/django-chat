from django.urls import path

from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path(
        '',
        accounts_list,
        name="home"
    ),
    path(
        'accounts/<int:pk>/',
        accounts_detail,
        name="accounts"
    ),
]
