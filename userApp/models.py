from django.db import models
from mainApp.models import *
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    Gender = (('M', 'Male'), ('F', 'Female'))
    phone_number = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10, choices=Gender)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username
