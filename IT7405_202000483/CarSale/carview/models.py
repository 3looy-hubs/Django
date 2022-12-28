from django.db import models


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    kilometers = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=100)