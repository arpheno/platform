from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from views import index, contact

urlpatterns = patterns(
    '',
    url(r'^$', index, name="index"),
    url(r'^contact/', contact, name='contact'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
    url(r'^materials/', include('materials.urls'), name='materials'),
    url(r'^news/', include('news.urls'), name='news'),
    url(r'^history/', include('history.urls'), name='history'),
)
