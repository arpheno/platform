from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns(
        url(r'^materials$', include('elfinder.urls', namespace="elfinder")),
        url(r'^elfinder/', include('elfinder.urls')),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^materials$', include('elfinder.urls', namespace="elfinder")),
        url(r'', include('trt.urls', namespace="trt")),
        )
