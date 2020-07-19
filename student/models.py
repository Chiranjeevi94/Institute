from django.db import models
from django.db import migrations


class StudentModel(models.Model):
    name = models.CharField(max_length=20)
    contactno = models.IntegerField(unique=True)
    email = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=15)

class CourseModel(models.Model):
    name = models.CharField(max_length=20)
    contactno = models.IntegerField()
    course = models.CharField(max_length=20,unique=True)