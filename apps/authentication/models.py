from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Profile(models.Model):
    FEMALE = 'F'
    MALE = 'M'
    NON_BINARY = 'NB'

    GENDER_CHOICES = [
        (FEMALE, 'Female'),
        (MALE, 'Male'),
        (NON_BINARY, 'NON_BINARY')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    image_url = models.URLField(max_length=200)