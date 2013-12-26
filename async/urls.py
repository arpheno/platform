from django.conf.urls import patterns, url
from views import history

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^history', history)
)
