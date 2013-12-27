from django.http import HttpResponse
from history.models import Event
from django.core import serializers
from models import LastModified
from email import utils
import time

def history(request):
    events = Event.objects.order_by('date')
    data = serializers.serialize("json", events)
    la = LastModified.objects.get(name="Event")
    lm = str(la.date)
    result = HttpResponse(data, content_type="application/json")
    result['Last-Modified'] = lm
    return result
# Create your views here.
