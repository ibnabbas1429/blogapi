from django.contrib import admin
from django.db import models

# Create your models here.

class employees(models.Model):
    firstname=models.CharField(max_length=10)
    lastname  = models.CharField(max_length=10)
    emp_id = models.IntegerField()

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class questions(models.Model):
    questions = models.CharField(max_length=250)
    OptionA = models.CharField(max_length=250)
    OptionB = models.CharField(max_length=250)
    OptionC = models.CharField(max_length=250)
    OptionD = models.CharField(max_length = 250)
    correctAnswer = models.CharField(max_length=250)

    def __str__(self):
        return self.questions




