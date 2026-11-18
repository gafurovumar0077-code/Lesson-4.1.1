from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('registration/', registration, name='registration'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout_user'),
    path('administrator/', admin_home, name='admin_home'),
    path('teacher/', teacher_home, name='teacher_home'),
    path('student/', student_home, name='student_home'),
    path('get_students/', get_students, name='get_students'),
    path('create_student/', create_student, name='create_student'),
    path('update_student/<int:pk>/', update_student, name='update_student'),
    path('delete_student/<int:pk>/', delete_student, name='delete_student'),
    path('get_teachers/', get_teachers, name='get_teachers'),
    path('create_teacher/', create_teacher, name='create_teacher'),
    path('update_teacher/<int:pk>/', update_teacher, name='update_teacher'),
    path('delete_teacher/<int:pk>/', delete_teacher, name='delete_teacher'),
    path('get_classrooms/', get_classrooms, name='get_classrooms'),
    path('create_classroom/', create_classroom, name='create_classroom'),
    path('update_classroom/<int:pk>/', update_classroom, name='update_classroom'),
    path('delete_classroom/<int:pk>/', delete_classroom, name='delete_classroom'),
    path('get_grades/', get_grades, name='get_grades'),
    path('create_grade/', create_grade, name='create_grade'),
    path('update_grade/<int:pk>/', update_grade, name='update_grade'),
    path('delete_grade/<int:pk>/', delete_grade, name='delete_grade'),
]