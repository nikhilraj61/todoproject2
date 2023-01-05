from django.db import models
# Create your models here.
import datetime


class Task(models.Model):
    def __str__(self):
      return  self.name
    name=models.CharField(max_length=250)
    priority=models.IntegerField()
    date=models.DateField(default=datetime.date.today)
