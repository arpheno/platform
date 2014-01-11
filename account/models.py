from django.db import models
from django.contrib.auth.models import AbstractUser


class Language(models.Model):
    name = models.CharField(max_length=15)


class TrtUser(AbstractUser):
    #Platform
    registration = models.CharField(max_length=100, blank=True, null=True)

    #General
    profile_picture = models.ImageField(upload_to="users", blank=True)
    born_on = models.DateField(blank=True, null=True)
    languages = models.ManyToManyField(Language)
    adress = models.TextField(max_length=100, blank=True, null=True)

    #EESTEC
    joined_eestec_on = models.DateField(blank=True, null=True)
    lc = models.CharField(max_length=50, blank=True, null=True)

    #Trainer
    trainer_status = models.CharField(max_length=100, blank=True, null=True)
    preferred_topics = models.TextField(max_length=100, blank=True, null=True)
    trainings_delivered = models.IntegerField(blank=True, null=True)
    #Contact
    hangout = models.CharField(max_length=100, blank=True, null=True)
    skype = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
