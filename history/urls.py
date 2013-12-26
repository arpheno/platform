from django.conf.urls import patterns, url
from views import History

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', History.as_view()),
)
