from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=55)
    breed = models.CharField(max_length=55)
    age = models.IntegerField()
