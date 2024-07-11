from django.db import models

# Create your models here.

class Stores(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    image = models.CharField(max_length=64)
    Rating = models.IntegerField(max_length=5)

    def __str__(self):
        return f'{self.name}, loacated at {self.location}'

