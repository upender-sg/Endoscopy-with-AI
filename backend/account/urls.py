# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

app_name = 'user'
urlpatterns = [
    #path('roles/', views.UserRoleListView.as_view(), name='user_roles'),
    path('create/', views.CreateUserView.as_view(), name='user_create'),
    path('list/', views.UserList.as_view(), name='user_list'),
]