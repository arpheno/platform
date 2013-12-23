from django.shortcuts import render, redirect
import logging
from models import Event
log = logging.getLogger(__name__)

def operational(request):
    operational_list = Event.objects.filter(type='operational').order_by('date')
    context = {'event_list': operational_list}
    if request.is_ajax():
        log.debug("Got an AJAX request for the history section");
        return render(request,'history/partial.html',context)
    log.debug("Got a request for the history section");
    return render(request,'history/index.html',context)
def trainings(request):
    trainings_list = Event.objects.filter(type='training').order_by('date')
    context = {'event_list': trainings_list}
    if request.is_ajax():
        log.debug("Got an AJAX request for the history section");
        return render(request,'history/partial.html',context)
    log.debug("Got a request for the history section");
    return render(request,'history/index.html',context)
