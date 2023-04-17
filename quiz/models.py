from django.db import models

# Create your models here.
class modeloQuiz(models.Model):
    question_status = models.IntegerField(max_length=300, null=True)
    data_time = models.TimeField(auto_now=True)

    def __str__(self) -> str:
        return self.question_status