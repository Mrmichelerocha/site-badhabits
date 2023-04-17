from django.shortcuts import render
from watch.serializer import WatchSerializer
from watch.models import modeloDataWatch
from rest_framework import viewsets

# Create your views here.
class WatchViewSet(viewsets.ModelViewSet):
    queryset = modeloDataWatch.objects.all()
    serializer_class = WatchSerializer
    
def watchall(request):
    data = {}
    data['db'] = modeloDataWatch.objects.all()
    return render(request, 'watch.html', data)