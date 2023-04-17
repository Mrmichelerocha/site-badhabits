from django.urls import path, include
from django.contrib.auth.models import User
from devices.models import modeloDevices
from rest_framework import serializers

# Serializers define the API representation.
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = modeloDevices
        fields = '__all__'
        
