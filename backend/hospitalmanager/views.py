from django.shortcuts import render
from .import serializer, models

from rest_framework import generics, parsers, permissions, status, viewsets






class HospitalViewsSet(viewsets.ModelViewSet):
    queryset = models.HospitalModel.objects.all()
    serializer_class = serializer.hospitalSerializer

class DepertmentViewsSet(viewsets.ModelViewSet):
    queryset = models.DepertmentModel.objects.all()
    serializer_class = serializer.DepertmentlSerializer

class StaffViewsSet(viewsets.ModelViewSet):
    queryset = models.StaffModel.objects.all()
    serializer_class = serializer.StaffSerializer


# Create your views here.
