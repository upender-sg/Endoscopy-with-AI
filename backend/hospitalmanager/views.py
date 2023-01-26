from django.shortcuts import render
from .import serializer, models

from rest_framework import generics, parsers, permissions, status, viewsets






class HospitalViwsSet(viewsets.ModelViewSet):
    queryset = models.HospitalModel.objects.all()
    serializer_class = serializer.hospitalSerializer


# Create your views here.
