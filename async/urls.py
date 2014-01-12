from django.conf.urls import patterns, url
from views import history, news

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^events', history, name='eventapi'),
    url(r'^news', news, name='newsapi'),
)
