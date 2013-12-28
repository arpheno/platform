from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.views.generic import TemplateView


def adjusted_index(which):
    tname = 'trt/index.html'
    if which:
        ctxt = {"target": which}
        view = TemplateView.as_view(template_name=tname)
        return url(r'^' + which + '/', view, ctxt, name=which)
    else:
        ctxt = {"target": "news"}
        view = TemplateView.as_view(template_name=tname)
        return url(r'^$', view, ctxt, name=which)

urlpatterns = patterns(
    '',
    adjusted_index(''),
    adjusted_index('news'),
    url(r'^account/', include('account.urls')),
    adjusted_index('training'),
    adjusted_index('operational'),
    adjusted_index('news'),
    adjusted_index('contact'),

    url(r'^admin/', include(admin.site.urls), name='admin'),

    url(r'^async/', include('async.urls')),
    url(r'^materials/', include('materials.urls'), name='materials'),
)
