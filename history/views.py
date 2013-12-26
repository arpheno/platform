from django.http import HttpResponse
from django.shortcuts import render
from models import Event
from django.core import serializers
from django.views.generic.base import View


class History(View):

    def get(self, request, **kwargs):
        if "which" in request.GET:
            return self.events(request, request.GET['which'])
        return render(request, 'history/index.html')

    def events(self, request, which):
        events = Event.objects.filter(type=which).order_by('date')
        data = serializers.serialize("json", events)
        return HttpResponse(data, content_type="application/json")
