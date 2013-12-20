from django.conf.urls import patterns, include, url
from django.contrib import admin
from trt import views
admin.autodiscover()
urlpatterns = patterns('',
        url(r'^header$', views.header),
        url(r'^$', views.index ),
        )
