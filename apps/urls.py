
from django.contrib import admin
from django.urls import path

from apps.views import RegisterPage, CreatedUser

urlpatterns = [
    path('', RegisterPage.as_view(), name='user_create'),
    path('created', CreatedUser.as_view(), name='created'),
]
