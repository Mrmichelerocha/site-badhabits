from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers



router = routers.DefaultRouter()
router.register('datatemperature', TemperatureViewSet, basename='datatemperature')

urlpatterns = [
    path('', include(router.urls)),
    path('temperature', views.temperatureall, name="temperature"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

