from django.conf.urls import patterns, include, url
from django.conf import settings
from views import  auth, out, UserProfile

urlpatterns = patterns('',
        url(r'^$', UserProfile.as_view(), name="index"),
        url(r'^login/', auth, name='login'),
        url(r'^logout/', out, name='logout'),
        )

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, }),
            )
