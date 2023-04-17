from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers



router = routers.DefaultRouter()
router.register('devices', DevicesViewSet, basename='devices')

urlpatterns = [
    path('', include(router.urls)),
    path('registerdevices', views.devices, name="devices"),
    path('alldevices', views.alldevices, name="alldevices"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

