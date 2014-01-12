from django.http import HttpResponse
from training.models import Event
from news.models import Entry
from account.models import TrtUser as User
from django.core import serializers
from models import LastModified
from django.template.loader import render_to_string


def fdate(which):
    # This is required for firefox compability.
    return which.strftime("%a %B %d %H:%M:%S %Y %z")


def pool(request):
    trainers = User.objects.all()
    data = render_to_string('async/trtusers.js', {'object_list': trainers})
    la = LastModified.objects.get(name="Trainers")
    lm = fdate(la.date)
    result = HttpResponse(data, content_type="application/json")
    result['Last-Modified'] = lm
    return result


def history(request):
    events = Event.objects.order_by('date')
    data = serializers.serialize("json", events)
    la = LastModified.objects.get(name="Event")
    lm = fdate(la.date)
    result = HttpResponse(data, content_type="application/json")
    result['Last-Modified'] = lm
    return result


def news(request):
    entries = Entry.objects.order_by('pub_date') # Get from DATABSE
    data = serializers.serialize("json", entries) # USE ENCODER TO JSON
    la = LastModified.objects.get(name="News") # Information from DB
    lm = fdate(la.date) # Important for AJAX
    result = HttpResponse(data, content_type="application/json")
    result['Last-Modified'] = lm
    return result
