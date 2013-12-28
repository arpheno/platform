from django.shortcuts import render
from elfinder.views import ElfinderConnectorView
import logging
log = logging.getLogger(__name__)


def index(request):
    if request.is_ajax():
        return render(request, 'materials/elfinder-partial.html')
    return render(request, 'trt/index.html', {"target": "materials"})


def connector(request):
    connector_view = ElfinderConnectorView.as_view()
    log.debug(request.user.is_superuser)
    if request.user.is_superuser:
        response = connector_view(request, optionset="admin", start_path="default")
    elif request.user.is_staff:
        response = connector_view(request, optionset="staff", start_path="default")
    elif "trainer" in user.groups:
        response = connector_view(request, optionset="trainer", start_path="default")
    elif request.user.is_authenticated():
        group = request.user.groups.all()[0].name
        response = connector_view(request, optionset=group, start_path="default")
    else:
        response = connector_view(request, optionset="anon", start_path="default")
    return response
