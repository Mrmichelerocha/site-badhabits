from django.shortcuts import render
from temperature.serializer import TemperatureSerializer
from temperature.models import modeloDataTemperature
from rest_framework import viewsets

# Create your views here.
class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = modeloDataTemperature.objects.all()
    serializer_class = TemperatureSerializer
    
def temperatureall(request):
    data = {}
    data['db'] = modeloDataTemperature.objects.all()
    return render(request, 'temperature.html', data)