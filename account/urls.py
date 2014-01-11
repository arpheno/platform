from django.conf.urls import patterns, url
from views import auth, out, new, complete
from django.views.generic import TemplateView


view = TemplateView.as_view(template_name='trt/index.html')

urlpatterns = patterns('',
                       url(r'^$', view, {"target": "account"}),
                       url(r'^login/', auth, name='login'),
                       url(r'^logout/', out, name='logout'),
                       url(r'^register/', new, name='register'),
                       url(r'^complete/(.*)$', complete),
                       )
