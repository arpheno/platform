from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from django.shortcuts import render
def index(request):
    return render(request, 'testenv/index.html')
def header(request):
    return render(request, 'testenv/header.html')
