from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    FEMALE = 'F'
    MALE = 'M'
    NON_BINARY = 'NB'

    GENDER_CHOICES = [
        (FEMALE, 'Female'),
        (MALE, 'Male'),
        (NON_BINARY, 'NON_BINARY')
    ]

    birthdate = models.DateField(blank=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True)
    image_url = models.URLField(max_length=200, blank=True)
