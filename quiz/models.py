from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Add related_name to avoid conflict
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Add related_name to avoid conflict
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class Quiz(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=5000)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    time_limit = models.DurationField()
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='quiz_teacher', on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='quiz_students', blank=True)

    def __str__(self):
        return self.title


multiple_choices = (
    ('multiple_choices', 'multiple_choices'),
)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField(max_length=5000)
    question_type = models.CharField(max_length=20, choices=multiple_choices)


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return str(self.question)


class StudentQuizSubmission(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='quiz_submissions', on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='student_submissions', on_delete=models.CASCADE)
    submission_time = models.DateTimeField()
    score = models.FloatField()

    def __str__(self):
        return str(self.quiz)


class Answer(models.Model):
    submission = models.ForeignKey(StudentQuizSubmission, related_name='answer_submission', on_delete=models.CASCADE)
    submission_time = models.DateTimeField()
    score = models.FloatField()

    def __str__(self):
        return str(self.submission)
