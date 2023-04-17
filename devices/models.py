from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class modeloCategory(models.Model):
    category = models.CharField(max_length=150, null=True)
    def __str__(self) -> str:
        return self.category
    
    
class modeloDevices(models.Model):
    category = models.ForeignKey(modeloCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length=150, null=True)
    urlcloud = models.CharField(max_length=300, null=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name

