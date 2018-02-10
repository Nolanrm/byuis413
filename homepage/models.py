from django.db import models
from django.contrib.auth.models import AbstractUser


# class Address(models.Model):

#     age = models.IntegerField()
#     birthdate = models.DateTimeField()
#     salary = models.IntegerField()
#     address = models.TextField(null=True, blank=True)
#     city = models.CharField(max_length=150, blank=True)
#     state = models.CharField(max_length=2, blank=True)
#     zip = models.CharField(max_length=15, blank=True)



# Quiz 1 -IS 413 -------------- SCORE: 10/10

#1 Assessment.objects.get(title='Exam 1') ----- 3
#1(correct) assessment.objects.get(title='Exam 1')

#2 Assessment.objects.filter(limit > 1) ------- 3
#2(correct) assessment = Assessment.objects.filter(limit__gt=1)

#3 Assessment.objects.filter(title='Exam 1').filter(title='Exam 2') --- 3
#3(correct) assessment = Assessment.objects.filter(title__startswith='Exam')