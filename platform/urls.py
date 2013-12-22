from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
from views import login, logout, manage_account

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^trt/', include('trt.urls')),
    url(r'^login/', login, name="login"),
    url(r'^logout/', logout, name="logout"),
    url(r'^account/', manage_account, name="account"),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, }),
    )
