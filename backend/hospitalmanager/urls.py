# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'users', views.HospitalViewsSet,basename="HospitalViewsSet")
router.register(r'departments', views.DepertmentViewsSet,basename="DepertmentViewsSet")
router.register(r'Staffviewsset', views.StaffViewsSet,basename="StaffViewsSet")

urlpatterns = [
    #path('roles/', views.UserRoleListView.as_view(), name='user_roles'),
    path('hospital/', include(router.urls)),


    
]
