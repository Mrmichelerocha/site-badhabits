from django.shortcuts import render
from quiz.models import modeloQuiz
from quiz.serializer import QuizSerializer
from rest_framework import viewsets

# Create your views here.
class QuizViewSet(viewsets.ModelViewSet):
    queryset = modeloQuiz.objects.all()
    serializer_class = QuizSerializer
    
def quiz(request):
    if request.method == 'POST':
        valor = modeloQuiz( question_status=request.POST['valor']) 
        valor.save()
        return render(request, 'quiz.html', {'valor': valor})
    else:
        return render(request, 'quiz.html')