from django.views.generic.list import ListView
from django.shortcuts import render
from models import Entry
from django.http import HttpResponse


class NewsList(ListView):
    model = Entry

    def get(self, request, **kwargs):
        if request.is_ajax():
            return super(NewsList, self).get(request, **kwargs)
        return render(request, 'trt/index.html', {"target": "news"})

    def head(self, request, **kwargs):
        last = self.get_queryset().latest('pub_date')
        result = HttpResponse()
        result['Last-Modified'] = last.pub_date.strftime(
            "%a %B %d %H:%M:%S %Y %z")
        return result
