# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt import serializers as jwt_serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class CreateUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        write_only=True, required=True, min_length=5, max_length=24
    )
 

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'confirm_password',
            'name',
            'address',
            'contact',
            
            
        )
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5, 'max_length': 24},
            
        }

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError({'password': _("Passwords not matching!")})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return User.objects.create_user(**validated_data)



class UserSerializer(serializers.ModelSerializer):
    """
    Serializer to view all Users
    """ 

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'address', 'contact',   'is_active')
        read_only_fields = ('email', 'is_active')
