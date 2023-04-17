from django.urls import path, include
from django.contrib.auth.models import User
from quiz.models import modeloQuiz
from rest_framework import serializers

# Serializers define the API representation.
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = modeloQuiz
        fields = '__all__'
        
