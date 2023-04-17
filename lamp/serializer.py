from django.urls import path, include
from django.contrib.auth.models import User
from lamp.models import modeloDataLamp
from rest_framework import serializers

# Serializers define the API representation.
class LampSerializer(serializers.ModelSerializer):
    class Meta:
        model = modeloDataLamp
        fields = '__all__'
        
