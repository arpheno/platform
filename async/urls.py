from django.conf.urls import patterns, url
from views import history, news

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^events', history),
    url(r'^news', news),
)
