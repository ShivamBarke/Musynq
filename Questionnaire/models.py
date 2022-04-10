from django.db import models

# Create your models here.
class Questionnaire(models.Model):
    OPTIONS = (('SD','Strongly Disagree'), ('D','Disagree'), ("CS","Can't Say"),('A','Agree'), ('SA','Strongly Agree'))
    userid = models.IntegerField(default=0)
    question1 = models.CharField(max_length=15,choices=OPTIONS, default='3')
    question10 = models.CharField(max_length=15,choices=OPTIONS,default='3')
    question3 = models.CharField(max_length=15,choices=OPTIONS,default='3')
    question4 = models.CharField(max_length=15,choices=OPTIONS,default='3')
    question5 = models.CharField(max_length=15,choices=OPTIONS,default='3')
    question6 = models.CharField(max_length=15,choices=OPTIONS,default='3')
    question7 = models.CharField(max_length=15,choices=OPTIONS,default='3')
    question8 = models.CharField(max_length=15,choices=OPTIONS,default='3')
    question9 = models.CharField(max_length=15,choices=OPTIONS,default='3')
    question2 = models.CharField(max_length=15,choices=OPTIONS,default='3')
    
class XWeightage(models.Model):
    QuestionNumber = models.IntegerField()
    SA = models.FloatField()
    A = models.FloatField()
    D = models.FloatField()
    SD = models.FloatField()

class YWeightage(models.Model):
    QuestionNumber = models.IntegerField()
    SA = models.FloatField()
    A = models.FloatField()
    D = models.FloatField()
    SD = models.FloatField()
