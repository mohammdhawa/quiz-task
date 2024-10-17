from django.urls import path
from .api import (QuizListAPI, QuestionListAPI, ChoiceListAPI, StudentQuizSubmissionListAPI,
                  AnswerListAPI)

urlpatterns = [
    path('quiz/list', QuizListAPI.as_view(), name='quiz-list'),
    path('question/list', QuestionListAPI.as_view(), name='question-list'),
    path('choice/list', ChoiceListAPI.as_view(), name='choice-list'),
    path('quiz-submission/list', StudentQuizSubmissionListAPI.as_view(), name='quiz-submission'),
    path('answer/list', AnswerListAPI.as_view(), name='answer-list'),
]
