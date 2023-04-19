from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, primary_key=False)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

class Course(models.Model):
    department = models.CharField(max_length=60)
    number = models.CharField(max_length=3)
    students = models.ManyToManyField(Student, related_name='student_courses')

    def __str__(self) -> str:
        return self.department + "-" + self.number