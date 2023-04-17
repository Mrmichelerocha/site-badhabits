from django.shortcuts import render, redirect
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import viewsets
from devices.serializer import DeviceSerializer
from devices.models import modeloDevices
from devices.forms import DevicesForm
# Create your views here.


class DevicesViewSet(viewsets.ModelViewSet):
    queryset = modeloDevices.objects.all()
    serializer_class = DeviceSerializer
    
def devices(request):
    data = {}
    data = DevicesForm(request.POST or None)
    data.fields['category'].widget.attrs['style'] = "background:#000000; height: calc(3.5rem + 2px); padding: 1rem 0.75rem; display: block; width: 100%; padding: 0.375rem 0.75rem; font-size: 1rem; font-weight: 400; line-height: 1.5; color: #6C7293; background-color: #000; background-clip: padding-box; border: 1px solid #000; appearance: none; border-radius: 5px; transition: border-color 0.15s ease-in-out,box-shadow 0.15s ease-in-out;"
    data.fields['name'].widget.attrs['style'] = "background:#000000; height: calc(3.5rem + 2px); padding: 1rem 0.75rem; display: block; width: 100%; padding: 0.375rem 0.75rem; font-size: 1rem; font-weight: 400; line-height: 1.5; color: #6C7293; background-color: #000; background-clip: padding-box; border: 1px solid #000; appearance: none; border-radius: 5px; transition: border-color 0.15s ease-in-out,box-shadow 0.15s ease-in-out;"
    data.fields['urlcloud'].widget.attrs['style'] = "background:#000000; height: calc(3.5rem + 2px); padding: 1rem 0.75rem; display: block; width: 100%; padding: 0.375rem 0.75rem; font-size: 1rem; font-weight: 400; line-height: 1.5; color: #6C7293; background-color: #000; background-clip: padding-box; border: 1px solid #000; appearance: none; border-radius: 5px; transition: border-color 0.15s ease-in-out,box-shadow 0.15s ease-in-out;"
    data.fields['owner'].widget.attrs['style'] = "background:#000000; height: calc(3.5rem + 2px); padding: 1rem 0.75rem; display: block; width: 100%; padding: 0.375rem 0.75rem; font-size: 1rem; font-weight: 400; line-height: 1.5; color: #6C7293; background-color: #000; background-clip: padding-box; border: 1px solid #000; appearance: none; border-radius: 5px; transition: border-color 0.15s ease-in-out,box-shadow 0.15s ease-in-out;"
    
    if data.is_valid():
        data.save()
        return redirect('index')
    
    return render(request, 'registerdevices.html', {'form': data})

def alldevices(request):
    data = {}
    data['db'] = modeloDevices.objects.all()
    return render(request, 'devicesall.html', data)


  