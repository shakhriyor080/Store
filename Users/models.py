from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(null=True, blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    old_password = models.CharField(max_length=100)
    new_password1 = models.CharField(max_length=100)
    new_password2 = models.CharField(max_length=100)


    def __str__(self):
        return self.first_name
