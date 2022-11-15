from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=30, editable=False)
    last_name = models.CharField(max_length=30, editable=False)
    name = models.CharField(max_length=100, verbose_name="name")
    phone = models.CharField(max_length=20, verbose_name="phone")

    def __str__(self):
        return self.username
