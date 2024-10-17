from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Quiz, Question, Choice, StudentQuizSubmission, Answer
from .serializers import (
    QuizSerializer, QuestionSerializer, ChoiceSerializer,
    StudentQuizSubmissionSerializer, AnswerSerializer
)


class QuizListCreateAPI(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the teacher to the current user
        serializer.save(teacher=self.request.user)


class QuizDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]


class QuestionListCreateAPI(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter questions by a specific quiz if 'quiz_id' is provided in the URL
        quiz_id = self.kwargs.get('quiz_id')
        if quiz_id:
            return Question.objects.filter(quiz_id=quiz_id)
        return Question.objects.all()

    def perform_create(self, serializer):
        # Associate the question with a specific quiz
        quiz_id = self.kwargs.get('quiz_id')
        serializer.save(quiz_id=quiz_id)


class QuestionDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class ChoiceListCreateAPI(generics.ListCreateAPIView):
    serializer_class = ChoiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter choices by a specific question if 'question_id' is provided in the URL
        question_id = self.kwargs.get('question_id')
        if question_id:
            return Choice.objects.filter(question_id=question_id)
        return Choice.objects.all()

    def perform_create(self, serializer):
        # Associate the choice with a specific question
        question_id = self.kwargs.get('question_id')
        serializer.save(question_id=question_id)


class ChoiceDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [IsAuthenticated]


class StudentQuizSubmissionListCreateAPI(generics.ListCreateAPIView):
    queryset = StudentQuizSubmission.objects.all()
    serializer_class = StudentQuizSubmissionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the student to the current user
        serializer.save(student=self.request.user)


class StudentQuizSubmissionDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentQuizSubmission.objects.all()
    serializer_class = StudentQuizSubmissionSerializer
    permission_classes = [IsAuthenticated]


class AnswerListCreateAPI(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter answers by a specific submission if 'submission_id' is provided in the URL
        submission_id = self.kwargs.get('submission_id')
        if submission_id:
            return Answer.objects.filter(submission_id=submission_id)
        return Answer.objects.all()

    def perform_create(self, serializer):
        # Associate the answer with a specific submission
        submission_id = self.kwargs.get('submission_id')
        serializer.save(submission_id=submission_id)


class AnswerDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
