from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# class Person(AbstractUser):
#     username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
#     email = models.EmailField(('email address'), unique = True)
#     native_name = models.CharField(max_length = 5)
#     phone_no = models.CharField(max_length = 10)
#     USERNAME_FIELD = 'email'

#     def __str__(self):
#         return f"{self.first_name} {self.first_name}"

class Stores(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    image = models.CharField(max_length=64)
    rating = models.IntegerField(max_length=5)

    def __str__(self):
        return f'{self.name}, loacated at {self.location}'

class Items(models.Model):
    item = models.CharField(max_length=64)
    price = models.CharField(max_length=64)
    image = models.ImageField(upload_to ='compare/')
    rating = models.IntegerField()
    storeWinner = models.CharField(max_length=64, blank=True)
    description = models.CharField(max_length=400,blank=True)

    def __str__(self):
        return f'{self.item} is sold for E {self.price}'