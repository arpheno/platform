from django.shortcuts import render, redirect
from models import Entry
import logging
log = logging.getLogger(__name__)
def index(request):
    news_list = Entry.objects.order_by('-pub_date')[:5]
    context = {'news_list': news_list}
    if request.is_ajax():
        log.debug("Got an AJAX request for the news section");
        return render(request,'news/partial.html',context)
    log.debug("Got a request for the news section");
    return render(request,'news/index.html',context)
