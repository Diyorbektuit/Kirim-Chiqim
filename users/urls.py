from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.TgUsersCreate.as_view(), name='register'),
    path('registered/users/', views.TgUserList.as_view(), name='registered_users'),


]