from django.db import models


class LastModified(models.Model):
    date = models.DateTimeField(auto_now=True, blank=True, null=True)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
