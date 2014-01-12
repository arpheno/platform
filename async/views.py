from django.http import HttpResponse
from history.models import Event
from news.models import Entry
from django.core import serializers
from models import LastModified

def history(request):
    events = Event.objects.order_by('date')
    data = serializers.serialize("json", events)
    la = LastModified.objects.get(name="Event")
    lm = str(la.date)
    result = HttpResponse(data, content_type="application/json")
    result['Last-Modified'] = lm
    return result

def news(request):
    entries = Entry.objects.order_by('pub_date')
    data = serializers.serialize("json", entries)
    la = LastModified.objects.get(name="News")
    lm = str(la.date)
    result = HttpResponse(data, content_type="application/json")
    result['Last-Modified'] = lm
    return result

# Create your views here.
