from django.urls import path, include
from django.contrib.auth.models import User
from temperature.models import modeloDataTemperature
from rest_framework import serializers

# Serializers define the API representation.
class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = modeloDataTemperature
        fields = '__all__'
        
