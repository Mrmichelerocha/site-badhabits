from django.contrib import admin
from watch.models import modeloDataWatch

# Register your models here.
class watch(admin.ModelAdmin):
    pass
admin.site.register(modeloDataWatch, watch)