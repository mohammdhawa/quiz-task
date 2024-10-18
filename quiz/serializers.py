from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import (Quiz, Question, Choice, StudentQuizSubmission, Answer)


User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'role')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class QuizSerializer(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True)
    teacher = serializers.StringRelatedField()
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    quiz = serializers.StringRelatedField()
    class Meta:
        model = Question
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    class Meta:
        model = Choice
        fields = '__all__'


class StudentQuizSubmissionSerializer(serializers.ModelSerializer):
    quiz = serializers.StringRelatedField()
    student = serializers.StringRelatedField()
    class Meta:
        model = StudentQuizSubmission
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    submission = serializers.StringRelatedField()
    class Meta:
        model = Answer
        fields = '__all__'
