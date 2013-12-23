import datetime
from django.db import models

class Entry(models.Model):
    headline = models.CharField(max_length=50)
    message = models.TextField()
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.message
# Create your models here.
