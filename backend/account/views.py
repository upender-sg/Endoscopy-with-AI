# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from rest_framework import generics, parsers, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt import views as jwt_views
from account import models, serializers



class CreateUserView(generics.CreateAPIView):
    """
    Create User API
    Only Admins can access this API
    """

    serializer_class = serializers.CreateUserSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    #permission_classes = [permissions.IsAuthenticated, cust_perms.ISAdminOrSuperAdmin]

class UserList(generics.ListAPIView):
    """
    View all Users
    Only Admins can access this API
    """

    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    #permission_classes = [permissions.IsAuthenticated, cust_perms.ISAdminOrSuperAdmin]

