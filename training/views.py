from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from models import Event
from django.forms import ModelForm
from django.http import HttpResponse
from django.forms import widgets
from django.forms.widgets import Input
import logging
logger = logging.getLogger('trt')


class HTML5Input(Input):
    def __init__(self, type, attrs):
        self.input_type = type
        super(HTML5Input, self).__init__(attrs)


class TrainingForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'description', 'location', 'trainers']
        widgets = {
            'date': HTML5Input(type='date', attrs={}),
            'name': widgets.TextInput(
                attrs={"placeholder": "What topic?"}),
            'location': widgets.TextInput(
                attrs={"placeholder": "Where?"}),
            'description': widgets.Textarea(
                attrs={"rows": 3,
                       "cols": 20,
                       "placeholder": "Describe your training!"}),
        }


class TrainingCreate(CreateView):
    model = Event
    form_class = TrainingForm
    success_url = "/training/"


class TrainingList(ListView):
    model = Event

    def get(self, request, **kwargs):
        if request.is_ajax():
            return super(TrainingList, self).get(request, **kwargs)
        return render(request, 'trt/index.html', {"target": "training"})

# Handle AJAX properly
    def head(self, request, **kwargs):
        last = self.get_queryset().latest('date')
        result = HttpResponse()
        result['Last-Modified'] = last.date.strftime(
            "%a %B %d %H:%M:%S %Y %z")
        return result

