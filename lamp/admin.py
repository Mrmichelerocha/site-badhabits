from django.contrib import admin
from lamp.models import modeloDataLamp

# Register your models here.
class lamp(admin.ModelAdmin):
    pass
admin.site.register(modeloDataLamp, lamp)