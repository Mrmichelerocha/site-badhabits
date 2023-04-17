from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers



router = routers.DefaultRouter()
router.register('datawatch', WatchViewSet, basename='datawatch')

urlpatterns = [
    path('', include(router.urls)),
    path('watch', views.watchall, name="watch"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

