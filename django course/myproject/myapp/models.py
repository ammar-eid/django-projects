from django.db import models

# Create your models here.
class Feature(models.Model):
    name=models.CharField(max_length=200)
    age=models.CharField(max_length=2)

class Person(models.Model):
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    confirmation=models.CharField(max_length=200)
    mobile=models.CharField(max_length=200)
