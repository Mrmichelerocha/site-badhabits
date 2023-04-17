from django.shortcuts import render
from lamp.serializer import LampSerializer
from lamp.models import modeloDataLamp
from rest_framework import viewsets

# Create your views here.
class LampViewSet(viewsets.ModelViewSet):
    queryset = modeloDataLamp.objects.all()
    serializer_class = LampSerializer
    
def lampall(request):
    data = {}
    data['db'] = modeloDataLamp.objects.all()
    return render(request, 'lamp.html', data)