from django.forms import ModelForm
from sleep.models import modeloDataSleep
from django import forms

class SleepForm(ModelForm):
    class Meta:
        model = modeloDataSleep
        fields = ['time_sleep','time_wake','routine_style', 'owner']
        
