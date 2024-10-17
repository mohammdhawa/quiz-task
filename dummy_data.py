import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from quiz.models import Quiz, Question, Choice, StudentQuizSubmission, Answer  # Replace 'myapp' with your app name

# User = get_user_model()
#
# # Create users
# teacher = User.objects.create_user(username='teacher1', password='password')
# teacher.role = 'teacher'  # Set role after creation
# teacher.save()
#
# student1 = User.objects.create_user(username='student1', password='password')
# student1.role = 'student'  # Set role after creation
# student1.save()
#
# student2 = User.objects.create_user(username='student2', password='password')
# student2.role = 'student'  # Set role after creation
# student2.save()
#
# # Create a quiz
# start_time = datetime.now() + timedelta(days=1)
# end_time = start_time + timedelta(hours=1)
# time_limit = timedelta(minutes=30)
# quiz = Quiz.objects.create(
#     title='Sample Quiz',
#     description='A sample quiz description',
#     start_time=start_time,
#     end_time=end_time,
#     time_limit=time_limit,
#     teacher=teacher
# )
#
# # Add students to the quiz
# quiz.students.set([student1, student2])
#
# # Create questions
# question1 = Question.objects.create(
#     quiz=quiz,
#     text='What is the capital of France?',
#     question_type='multiple_choices'
# )
# question2 = Question.objects.create(
#     quiz=quiz,
#     text='Which programming language is used for Django?',
#     question_type='multiple_choices'
# )
#
# # Create choices for question 1
# Choice.objects.create(question=question1, text='Paris', is_correct=True)
# Choice.objects.create(question=question1, text='London', is_correct=False)
# Choice.objects.create(question=question1, text='Berlin', is_correct=False)
#
# # Create choices for question 2
# Choice.objects.create(question=question2, text='Python', is_correct=True)
# Choice.objects.create(question=question2, text='Java', is_correct=False)
# Choice.objects.create(question=question2, text='C++', is_correct=False)
#
# # Create a quiz submission
# submission = StudentQuizSubmission.objects.create(
#     quiz=quiz,
#     student=student1,
#     submission_time=datetime.now(),
#     score=80.0
# )
#
# # Create an answer
# Answer.objects.create(
#     submission=submission,
#     submission_time=datetime.now(),
#     score=40.0
# )
#
# print("Dummy data created successfully!")

from datetime import datetime, timedelta
# Replace 'myapp' with your app name

User = get_user_model()

# Create additional users
teachers = [
    User.objects.create_user(username=f'teacher{i}', password='password')
    for i in range(1, 4)  # Creates teacher1, teacher2, teacher3
]
for teacher in teachers:
    teacher.role = 'teacher'
    teacher.save()

students = [
    User.objects.create_user(username=f'student{i}', password='password')
    for i in range(1, 6)  # Creates student1, student2, student3, student4, student5
]
for student in students:
    student.role = 'student'
    student.save()

# Create quizzes and add students to each quiz
quizzes = []
for i in range(1, 4):  # Creates 3 quizzes
    start_time = datetime.now() + timedelta(days=i)
    end_time = start_time + timedelta(hours=1)
    time_limit = timedelta(minutes=30)
    quiz = Quiz.objects.create(
        title=f'Sample Quiz {i}',
        description=f'A sample quiz description for quiz {i}',
        start_time=start_time,
        end_time=end_time,
        time_limit=time_limit,
        teacher=teachers[i - 1]  # Assign a different teacher to each quiz
    )
    # Associate all students with this quiz
    quiz.students.set(students)  # Add all students to the quiz
    quizzes.append(quiz)

# Create questions and choices for each quiz
for quiz in quizzes:
    for j in range(1, 4):  # Creates 3 questions per quiz
        question = Question.objects.create(
            quiz=quiz,
            text=f'Question {j} for {quiz.title}?',
            question_type='multiple_choices'
        )
        # Create multiple choices for each question
        Choice.objects.create(question=question, text='Option A', is_correct=(j == 1))
        Choice.objects.create(question=question, text='Option B', is_correct=(j == 2))
        Choice.objects.create(question=question, text='Option C', is_correct=(j == 3))

# Create quiz submissions and answers for students
for quiz in quizzes:
    for student in students:
        submission_time = datetime.now() + timedelta(minutes=student.id)  # Stagger submissions by student ID
        score = (quiz.id * 10) + (student.id * 2)  # Random score calculation
        submission = StudentQuizSubmission.objects.create(
            quiz=quiz,
            student=student,
            submission_time=submission_time,
            score=score
        )
        # Create an answer for each submission
        Answer.objects.create(
            submission=submission,
            submission_time=submission_time,
            score=score / 2  # Half the submission score for the answer
        )

print("Expanded dummy data with students added to quizzes created successfully!")



