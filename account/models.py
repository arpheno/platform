from django.db import models
from django.contrib.auth.models import AbstractUser


class TrtUser(AbstractUser):
    registration = models.CharField(max_length=100)
    lc = models.CharField(max_length=50)
    trainings_delivered = models.IntegerField(blank=True,null=True)
    profile_picture = models.ImageField(upload_to="users")
    born_on = models.DateField(blank=True,null=True)
    join_date = models.DateField(blank=True,null=True)
    languages = models.TextField(max_length=100)
    preferred_topics = models.TextField(max_length=100)
    contact = models.TextField(max_length=100)
