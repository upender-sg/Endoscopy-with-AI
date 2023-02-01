from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from . import models


class hospitalSerializer(serializers.ModelSerializer):
     class Meta:
        model = models.HospitalModel
        fields = "__all__"

class DepertmentlSerializer(serializers.ModelSerializer):
     class Meta:
        model = models.DepertmentModel
        fields = "__all__"
class StaffSerializer(serializers.ModelSerializer):
     class Meta:
        model = models.StaffModel
        fields = "__all__"
