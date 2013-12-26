import json
from django.http import HttpResponse
from django.shortcuts import render
from models import Event
from django.core import serializers

def operational(request):
    data = serializers.serialize("json", Event.objects.filter(type='operational').order_by('date'))
    return HttpResponse(data, content_type="application/json")
def trainings(request):
    data = serializers.serialize("json", Event.objects.filter(type='training').order_by('date'))
    return HttpResponse(data, content_type="application/json")
def index(request):
    return render(request,'history/index.html')
