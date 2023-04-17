from django.urls import path, include
from django.contrib.auth.models import User
from watch.models import modeloDataWatch
from rest_framework import serializers

# Serializers define the API representation.
class WatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = modeloDataWatch
        fields = '__all__'
        
