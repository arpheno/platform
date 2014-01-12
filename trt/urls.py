from django.conf.urls import patterns, include, url
from django.contrib import admin
from account.models import TrtUser as User
admin.autodiscover()
from django.views.generic import TemplateView, ListView


view = TemplateView.as_view(template_name='trt/index.html')
urlpatterns = patterns(
    '',
    url(r'^$',view,{"target": "news"}),
    url(r'^news/$',view,{"target": "news"} ),
    url(r'^training/$',view,{"target": "training"} ),
    url(r'^contact/$', view, {"target": "contact"}),
    url(r'^operational/$', view,{"target": "operational"}),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^pool/', ListView.as_view(model=User)),
    url(r'^account/', include('account.urls')),
    url(r'^async/', include('async.urls')),
    url(r'^materials/', include('materials.urls'), name='materials'),
)
