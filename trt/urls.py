from django.conf.urls import patterns, include, url
from django.conf import settings
from trt.views import materials,connector,index,header
from trt.views import login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^login/', login, name="login"),
    url(r'^header/$', header),
    url(r'^materials/$', materials),
    url(r'^connector/$', connector, name="trtconnector"),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, }),
    )
