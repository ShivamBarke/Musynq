from django.db import models

# Create your models here.
class Questionnaire(models.Model):
    OPTIONS = (('1','not likely'), ('2','less likely'), ('3','rather not say'),('4','likely '), ('5','definitely'))
    userid = models.IntegerField(default=0)
    question1 = models.CharField(max_length=1,choices=OPTIONS, default='3')
    question2 = models.CharField(max_length=1,choices=OPTIONS,default='3')
    question3 = models.CharField(max_length=1,choices=OPTIONS,default='3')
    question4 = models.CharField(max_length=1,choices=OPTIONS,default='3')
    question5 = models.CharField(max_length=1,choices=OPTIONS,default='3')
    question6 = models.CharField(max_length=1,choices=OPTIONS,default='3')
    question7 = models.CharField(max_length=1,choices=OPTIONS,default='3')
    question8 = models.CharField(max_length=1,choices=OPTIONS,default='3')
    question9 = models.CharField(max_length=1,choices=OPTIONS,default='3')
    question10 = models.CharField(max_length=1,choices=OPTIONS,default='3')
    
