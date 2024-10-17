from django.contrib import admin
from .models import Quiz, Question, Choice, StudentQuizSubmission, Answer, User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    search_fields = ('username', 'email')
    list_filter = ('role',)

# Register Quiz Model
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'start_time', 'end_time', 'time_limit')
    search_fields = ('title', 'description')
    list_filter = ('start_time', 'end_time')

# Register Question Model
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'text', 'question_type')
    search_fields = ('text',)

# Register Choice Model
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'is_correct')
    list_filter = ('is_correct',)

# Register StudentQuizSubmission Model
class StudentQuizSubmissionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'student', 'submission_time', 'score')
    list_filter = ('quiz', 'student', 'submission_time')

# Register Answer Model
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('submission', 'score', 'submission_time')

# Registering the models in the admin
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(StudentQuizSubmission, StudentQuizSubmissionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(User, UserAdmin)