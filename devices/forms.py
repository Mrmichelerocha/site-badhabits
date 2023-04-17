from django.forms import ModelForm
from devices.models import modeloDevices
from django import forms

class DevicesForm(ModelForm):
    class Meta:
        model = modeloDevices
        fields = '__all__'
        
