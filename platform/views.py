import logging
from django.shortcuts import render
log = logging.getLogger(__name__)
def index(request):
    log.debug(request.user)
    return render(request, 'platform/index.html')
def contact(request):
    return render(request, 'platform/contact.html')
