from django.db import models


# Create your models here.
class Breed(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    coat_length = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=200)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
