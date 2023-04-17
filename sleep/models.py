from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class modeloDataSleep(models.Model):
    ROUTINE = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )
    time_sleep = models.TimeField()
    time_wake = models.TimeField()

    routine_style = models.CharField(max_length=1, choices=ROUTINE, blank=False, null=False,default='M')
    owner = models.OneToOneField(User, on_delete=models.PROTECT)
    