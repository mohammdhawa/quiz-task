from rest_framework import generics

from .models import (Quiz, Question, Choice, StudentQuizSubmission, Answer)
from .serializers import (QuizSerializer, QuestionSerializer, ChoiceSerializer,
                          StudentQuizSubmissionSerializer, AnswerSerializer)


class QuizListAPI(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionListAPI(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceListAPI(generics.ListAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class StudentQuizSubmissionListAPI(generics.ListAPIView):
    queryset = StudentQuizSubmission.objects.all()
    serializer_class = StudentQuizSubmissionSerializer


class AnswerListAPI(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
