from django.contrib import admin
from .models import Quiz, Question, Choice, StudentQuizSubmission, Answer, User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    search_fields = ('username', 'email')
    list_filter = ('role',)


# Inline for Choice Model
class ChoiceAdmin(admin.TabularInline):
    model = Choice
    fields = ('question', 'text', 'is_correct')
    extra = 1  # Defines how many extra empty slots to display


# Inline for Question Model
class QuestionAdmin(admin.TabularInline):
    model = Question
    fields = ('quiz', 'text', 'question_type')
    extra = 1
    inlines = [ChoiceAdmin]


# Register Quiz Model with inlines
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'start_time', 'end_time', 'time_limit')
    search_fields = ('title', 'description')
    list_filter = ('start_time', 'end_time')
    inlines = [QuestionAdmin]  # Add Question inline to QuizAdmin


# Register StudentQuizSubmission Model
class StudentQuizSubmissionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'student', 'submission_time', 'score')
    list_filter = ('quiz', 'student', 'submission_time')


# Register Answer Model
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'submission', 'score', 'submission_time')


# Registering the models in the admin
admin.site.register(Quiz, QuizAdmin)
admin.site.register(StudentQuizSubmission, StudentQuizSubmissionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(User, UserAdmin)
