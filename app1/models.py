from django.db import models
from datetime import datetime
import datetime

class ClassModel(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.CharField(max_length=20)
    date = models.DateField()
    time = models.CharField(max_length=10)
    fee = models.IntegerField()
    duration = models.CharField(max_length=10)
