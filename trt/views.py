from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
def index(request):
    k=render(request, 'trt/index.html')
    return k
def header(request):
    k=render(request, 'trt/header.html')
    return k
