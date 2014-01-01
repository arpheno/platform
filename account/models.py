from django.db import models
from django.contrib.auth.models import AbstractUser


class TrtUser(AbstractUser):
    registration = models.CharField(max_length=100, blank=True, null=True)
    lc = models.CharField(max_length=50, blank=True, null=True)
    trainings_delivered = models.IntegerField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="users", blank=True, null=True)
    born_on = models.DateField(blank=True, null=True)
    join_date = models.DateField(blank=True, null=True)
    languages = models.TextField(max_length=100, blank=True, null=True)
    preferred_topics = models.TextField(max_length=100, blank=True, null=True)
    contact = models.TextField(max_length=100, blank=True, null=True)
