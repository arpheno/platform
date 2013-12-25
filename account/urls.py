from django.conf.urls import patterns, include, url
from django.conf import settings
from views import *

urlpatterns = patterns('',
        url(r'^$', UserProfile.as_view(), name="index"),
        url(r'^login/', auth, name='login'),
        url(r'^logout/', out, name='logout'),
        url(r'^new/', new, name='register'),
        )

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, }),
            )
