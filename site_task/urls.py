from django.conf.urls import patterns, include, url
from django.contrib import admin

import task.views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'task.views.lst', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^task/',  include('task.urls',  namespace='task')),
    url(r'^admin/', include(admin.site.urls)),
)
