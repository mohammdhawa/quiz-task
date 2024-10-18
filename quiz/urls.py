from django.urls import path
from .api import (
    QuizListCreateAPI, QuizDetailAPI,
    QuestionListCreateAPI, QuestionDetailAPI,
    ChoiceListCreateAPI, ChoiceDetailAPI,
    StudentQuizSubmissionListCreateAPI, StudentQuizSubmissionDetailAPI,
    AnswerListCreateAPI, AnswerDetailAPI
)

urlpatterns = [
    # Quiz URLs
    path('quizzes/', QuizListCreateAPI.as_view(), name='quiz-list-create'),
    path('quizzes/<int:pk>/', QuizDetailAPI.as_view(), name='quiz-detail'),

    # Question URLs
    path('quizzes/<int:quiz_id>/questions/', QuestionListCreateAPI.as_view(), name='question-list-create'),
    path('questions/<int:pk>/', QuestionDetailAPI.as_view(), name='question-detail'),

    # Choice URLs
    path('questions/<int:question_id>/choices/', ChoiceListCreateAPI.as_view(), name='choice-list-create'),
    path('choices/<int:pk>/', ChoiceDetailAPI.as_view(), name='choice-detail'),

    # Student Quiz Submission URLs
    path('submissions/', StudentQuizSubmissionListCreateAPI.as_view(), name='submission-list-create'),
    path('submissions/<int:pk>/', StudentQuizSubmissionDetailAPI.as_view(), name='submission-detail'),

    # Answer URLs
    path('submissions/<int:submission_id>/answers/', AnswerListCreateAPI.as_view(), name='answer-list-create'),
    path('answers/<int:pk>/', AnswerDetailAPI.as_view(), name='answer-detail'),
]
