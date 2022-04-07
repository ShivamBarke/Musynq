from django.db import models

# Create your models here.
class MusynqUser(models.Model):
    name = models.CharField(max_length = 60)
    age = models.IntegerField()
    GENDER = (('M', 'Male'),('F','Female'), ('O','Others'))
    gender = models.CharField(max_length=1 , choices= GENDER)
    def __str__(self) -> str:
        return self.name
    