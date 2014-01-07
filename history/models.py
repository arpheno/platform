from django.db import models
from async.models import LastModified
from account.models import TrtUser as User


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
    location = models.TextField(null=True, blank=True)  # TODO
    description = models.TextField()
    trainers = models.ManyToManyField(User)
    report = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User,
                                          null=True,
                                          blank=True,
                                          related_name="pax")
    im = models.ImageField(null=True, blank=True, upload_to="events")

    def save(self, *args, **kwargs):
        LastModified.objects.get(name="Event").save()
        super(Event, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Feedback(models.Model):
    content = models.TextField()
    training = models.ForeignKey(Event)
