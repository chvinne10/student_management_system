from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField( max_length=50)
    rollno=models.CharField(max_length=40, unique=True)
    student_branch=models.CharField( max_length=50)
    section=models.CharField(max_length=20)
    place=models.CharField(max_length=60)
    
class Admin(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=120)

    