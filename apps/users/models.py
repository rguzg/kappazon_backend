from django.db import models
from django.contrib.auth.models import AbstractUser
from .genders import GENDERS


class User(AbstractUser):
    GENDER_CHOICES = [
        (GENDERS['Female'], 'Female'),
        (GENDERS['Male'], 'Male'),
        (GENDERS['Non-Binary'], 'Non-Binary')
    ]

    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=2, choices=GENDER_CHOICES, blank=True, null=True)
    image_url = models.URLField(max_length=200, blank=True, null=True)
