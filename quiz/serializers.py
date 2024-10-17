from rest_framework import serializers

from .models import (Quiz, Question, Choice, StudentQuizSubmission, Answer)


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
