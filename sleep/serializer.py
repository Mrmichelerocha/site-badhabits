from django.urls import path, include
from django.contrib.auth.models import User
from sleep.models import modeloDataSleep
from rest_framework import serializers

# Serializers define the API representation.
class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = modeloDataSleep
        fields = '__all__'
        
