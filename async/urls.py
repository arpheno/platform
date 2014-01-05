from django.conf.urls import patterns, url
from views import history, news, pool
urlpatterns = patterns(
    '',
    url(r'^events', history, name='eventapi'),
    url(r'^news', news, name='newsapi'),
    url(r'^pool', pool, name='poolapi'),
)
