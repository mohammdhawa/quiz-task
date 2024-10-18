from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsTeacherOrReadOnly, IsTeacherOrReadOnlyOrIsStudentForSubmission  # Import the custom permission
from .models import Quiz, Question, Choice, StudentQuizSubmission, Answer
from .serializers import (
    QuizSerializer, QuestionSerializer, ChoiceSerializer,
    StudentQuizSubmissionSerializer, AnswerSerializer, UserRegistrationSerializer
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny


class UserRegistrationAPI(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]  # Allow anyone to register


class QuizListCreateAPI(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]  # Use the custom permission

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class QuizDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]  # Use the custom permission

class QuestionListCreateAPI(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]  # Use the custom permission

    def get_queryset(self):
        quiz_id = self.kwargs.get('quiz_id')
        if quiz_id:
            return Question.objects.filter(quiz_id=quiz_id)
        return Question.objects.all()

    def perform_create(self, serializer):
        quiz_id = self.kwargs.get('quiz_id')
        serializer.save(quiz_id=quiz_id)

class QuestionDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]  # Use the custom permission

class ChoiceListCreateAPI(generics.ListCreateAPIView):
    serializer_class = ChoiceSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]  # Use the custom permission

    def get_queryset(self):
        question_id = self.kwargs.get('question_id')
        if question_id:
            return Choice.objects.filter(question_id=question_id)
        return Choice.objects.all()

    def perform_create(self, serializer):
        question_id = self.kwargs.get('question_id')
        serializer.save(question_id=question_id)

class ChoiceDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]  # Use the custom permission

class AnswerListCreateAPI(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]  # Use the custom permission

    def get_queryset(self):
        submission_id = self.kwargs.get('submission_id')
        if submission_id:
            return Answer.objects.filter(submission_id=submission_id)
        return Answer.objects.all()

    def perform_create(self, serializer):
        submission_id = self.kwargs.get('submission_id')
        serializer.save(submission_id=submission_id)

class AnswerDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]  # Use the custom permission


class StudentQuizSubmissionListCreateAPI(generics.ListCreateAPIView):
    queryset = StudentQuizSubmission.objects.all()
    serializer_class = StudentQuizSubmissionSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnlyOrIsStudentForSubmission]

    def perform_create(self, serializer):
        # Automatically set the student to the current user
        serializer.save(student=self.request.user)

class StudentQuizSubmissionDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentQuizSubmission.objects.all()
    serializer_class = StudentQuizSubmissionSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnlyOrIsStudentForSubmission]
