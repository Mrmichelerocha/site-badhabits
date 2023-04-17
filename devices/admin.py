from django.contrib import admin
from devices.models import modeloDevices, modeloCategory

class Devices(admin.ModelAdmin):
    list_display = ('id','owner')
    list_display_links = ('id', 'owner')
    search_fields = ('owner',)
    list_per_page = 20

admin.site.register(modeloDevices, Devices)

class Category(admin.ModelAdmin):
    list_display = ('id','category')
    list_display_links = ('id', 'category')
    search_fields = ('category',)
admin.site.register(modeloCategory, Category)
