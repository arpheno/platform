from django.conf.urls import patterns, include, url
from account.models import TrtUser as User

from django.views.generic import ListView
urlpatterns = patterns('',
                       url(r'^$', ListView.as_view(model=User)),
                       )
