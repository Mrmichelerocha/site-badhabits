from django.contrib import admin
from temperature.models import modeloDataTemperature

# Register your models here.
class temperature(admin.ModelAdmin):
    pass
admin.site.register(modeloDataTemperature, temperature)