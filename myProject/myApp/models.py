from django.db import models
from django.utils import timezone


# name, page numbeer and published date
class Book(models.Model):
    name = models.CharField(max_length=500)
    pageNumber = models.IntegerField()
    gender = models.CharField(max_length=300)
    publishedDate = models.DateTimeField(default=timezone.now())

# make, model and year attribute
class Car(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    yearAttirbutes = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.make