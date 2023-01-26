from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from . import models



class hospitalSerializer(serializers.ModelSerializer):
     class Meta:
        model = models.HospitalModel
        fields = "__all__"
