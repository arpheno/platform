from django.conf.urls import patterns, url
from views import trainings, operational, index

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index),
    url(r'^trainings/$', trainings, name="trainingsajax"),
    url(r'^operational/$', operational, name="operationalajax"),
)
