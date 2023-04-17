from django.contrib import admin
from quiz.models import modeloQuiz

# Register your models here.
class quiz(admin.ModelAdmin):
    pass
admin.site.register(modeloQuiz, quiz)