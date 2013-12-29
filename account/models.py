from django.db import models
from django.contrib.auth.models import AbstractUser


class TrtUser(AbstractUser):
    registration = models.CharField(max_length=100)
