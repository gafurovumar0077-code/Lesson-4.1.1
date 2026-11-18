from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import *


def registration(request):
    if request.method == 'POST':
        data = request.POST
        if data:
            User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
        else:
            return redirect('registration')
        return redirect("login")
    return render(request, 'registration.html')


def login_user(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return redirect("login")
    return render(request, 'login.html')


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect("login")
    return redirect("home")


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def admin_home(request):
    if not request.user.is_superuser:
        return redirect("home")
    return render(request, 'admin_home.html')


@login_required
def get_students(request):
    students = Student.objects.all()
    return render(request, 'show_students.html', {'students': students})


@login_required
def create_student(request):
    if request.method == 'POST':
        data = request.POST
        Student.objects.create(
            user=User.objects.get(pk=data['user_id']),
            fullname=data['fullname'],
            classroom=Classroom.objects.get(pk=data['classroom_id']),
            phone=data['phone']
        )
        return redirect("get_students")
    return render(request, 'add_student.html', {'users': User.objects.all(), 'classrooms': Classroom.objects.all()})


@login_required
def update_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        data = request.POST
        student.fullname = data['fullname']
        student.classroom = Classroom.objects.get(pk=data['classroom_id'])
        student.phone = data['phone']
        student.save()
        return redirect("get_students")
    return render(request, 'update_student.html', {'student': student, 'classrooms': Classroom.objects.all()})


@login_required
def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect("get_students")
    return render(request, 'delete_student.html', {'student': student})


@login_required
def get_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'show_teachers.html', {'teachers': teachers})


@login_required
def create_teacher(request):
    if request.method == 'POST':
        data = request.POST
        Teacher.objects.create(
            user=User.objects.get(pk=data['user_id']),
            fullname=data['fullname'],
            subject=data['subject'],
            phone=data['phone']
        )
        return redirect("get_teachers")
    return render(request, 'add_teacher.html', {'users': User.objects.all()})


@login_required
def update_teacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'POST':
        data = request.POST
        teacher.fullname = data['fullname']
        teacher.subject = data['subject']
        teacher.phone = data['phone']
        teacher.save()
        return redirect("get_teachers")
    return render(request, 'update_teacher.html', {'teacher': teacher})


@login_required
def delete_teacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect("get_teachers")
    return render(request, 'delete_teacher.html', {'teacher': teacher})


@login_required
def get_classrooms(request):
    classrooms = Classroom.objects.all()
    return render(request, 'show_classrooms.html', {'classrooms': classrooms})


@login_required
def create_classroom(request):
    if request.method == 'POST':
        data = request.POST
        Classroom.objects.create(
            title=data['title'],
            teacher=Teacher.objects.get(pk=data['teacher'])
        )
        return redirect("get_classrooms")
    return render(request, 'add_classroom.html', {'teachers': Teacher.objects.all()})


@login_required
def update_classroom(request, pk):
    classroom = Classroom.objects.get(pk=pk)
    if request.method == 'POST':
        data = request.POST
        classroom.title = data['title']
        classroom.teacher = Teacher.objects.get(pk=data['teacher'])
        classroom.save()
        return redirect("get_classrooms")
    return render(request, 'update_classroom.html', {'classroom': classroom, 'teachers': Teacher.objects.all()})


@login_required
def delete_classroom(request, pk):
    classroom = Classroom.objects.get(pk=pk)
    if request.method == 'POST':
        classroom.delete()
        return redirect("get_classrooms")
    return render(request, 'delete_classroom.html', {'classroom': classroom})


@login_required
def get_grades(request):
    grades = Grade.objects.all()
    return render(request, 'show_grades.html', {'grades': grades})


@login_required
def create_grade(request):
    teacher = Teacher.objects.get(user=request.user)
    if request.method == 'POST':
        data = request.POST
        Grade.objects.create(
            student=Student.objects.get(pk=data['student_id']),
            teacher=teacher,
            grade=data['grade'],
            status=data.get('status') == 'on',
            comment=data['comment'],
            data=data['data']
        )
        return redirect("get_grades")
    return render(request, 'add_grade.html', {'students': Student.objects.all(), 'teacher': teacher})


@login_required
def update_grade(request, pk):
    teacher = Teacher.objects.get(user=request.user)
    grade = Grade.objects.get(pk=pk, teacher=teacher)
    if request.method == 'POST':
        data = request.POST
        grade.grade = data['grade']
        grade.status = data.get('status') == 'on'
        grade.comment = data['comment']
        grade.data = data['data']
        grade.save()
        return redirect("get_grades")
    return render(request, 'update_grade.html', {'grade': grade})


@login_required
def delete_grade(request, pk):
    teacher = Teacher.objects.get(user=request.user)
    grade = Grade.objects.get(pk=pk, teacher=teacher)
    if request.method == 'POST':
        grade.delete()
        return redirect("get_grades")
    return render(request, 'delete_grade.html', {'grade': grade})


@login_required
def teacher_home(request):
    teacher = Teacher.objects.filter(user=request.user).first()
    if teacher is None:
        return redirect('home')
    grades = Grade.objects.filter(teacher=teacher)
    return render(request, 'teacher_home.html', {'teacher': teacher, 'grades': grades})


@login_required
def student_home(request):
    student = Student.objects.filter(user=request.user).first()
    if student is None:
        return redirect('home')
    grades = Grade.objects.filter(student=student)
    return render(request, 'student_home.html', {'student': student, 'grades': grades})
