import logging
from django.shortcuts import render
log = logging.getLogger('trt')


def index(request):
    log.debug(request.user + " requested the website.")
    return render(request, 'trt/index.html')
