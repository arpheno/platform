from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from views import index, contact
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(r'^$', index, name="index"),
    url(r'^contact/', contact, name='contact'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
    url(r'^materials/', include('materials.urls'), name='materials'),
    url(r'^news/', TemplateView.as_view(template_name='news/index.html') , name='news'),
    url(r'^history/', TemplateView.as_view(template_name='history/index.html'), name='history'),
    url(r'^async/', include('async.urls')),
)
