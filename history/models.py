from django.db import models
from async.models import LastModified


class Event(models.Model):
    name = models.CharField(max_length=50)
    EVENT_TYPE_CHOICES = (
        ('training', 'Training'),
        ('operational', 'Operational'),
    )
    type = models.CharField(
        max_length=11,
        choices=EVENT_TYPE_CHOICES,
        default='training')
    date = models.DateTimeField()
    description = models.TextField()
    trainers = models.TextField()

    def save(self, *args, **kwargs):
        LastModified.objects.get(name="Event").save()
        super(Event, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
