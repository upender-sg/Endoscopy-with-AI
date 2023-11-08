
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions



schema_view = get_swagger_view(title='AI ENDOSCOPY API')


 
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', schema_view),
    path('user/', include('account.urls')),
    path('hospital/', include('hospitalmanager.urls')),
    path('/verify','verification.urls')
 
]
