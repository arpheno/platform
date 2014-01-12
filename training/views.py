from django.views.generic.list import ListView
from django.shortcuts import render
from models import Event
from django.http import HttpResponse
import logging
logger = logging.getLogger('trt')


class TrainingList(ListView):
    model = Event

    def get(self, request, **kwargs):
        if request.is_ajax():
            return super(TrainingList, self).get(request, **kwargs)
        return render(request, 'trt/index.html', {"target": "training"})

    def head(self, request, **kwargs):
        last = self.get_queryset().latest('date')
        result = HttpResponse()
        result['Last-Modified'] = last.date.strftime(
            "%a %B %d %H:%M:%S %Y %z")
        return result
