import logging
from django.shortcuts import render
log = logging.getLogger(__name__)
def index(request):
    log.debug(request.user)
    return render(request, 'trt/index.html')
def contact(request):
    return render(request, 'trt/contact.html')
