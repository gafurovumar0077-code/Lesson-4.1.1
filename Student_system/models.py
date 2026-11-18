from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date



class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    subject = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    created_at = models.DateTimeField(default=datetime.now())


class Classroom(models.Model):
    title = models.CharField(max_length=140)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now())
    

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)
    created_at = models.DateTimeField(default=datetime.now())


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    grade = models.IntegerField()
    status = models.BooleanField(default=True)
    comment = models.TextField(max_length=200)
    data = models.DateField(default=date.today)