from django.conf.urls import patterns, url

from task import views

urlpatterns = patterns('task.views',
    url(r'^$',                              views.lst,              name='index'),
    url(r'list/$',                          views.lst,              name='lst'),
    url(r'calendar/$',                      views.calendar,         name='calendar'),
    url(r'form_task_add/$',                 views.form_task_add,    name='form_task_add'),
    url(r'^(?P<task_id>\d+)/start_now/$',   views.start_now,        name='start_now'),
    url(r'^(?P<task_id>\d+)/end_now/$',     views.end_now,          name='end_now'),
    url(r'^(?P<task_id>\d+)/task_detail/$', views.task_detail,      name='task_detail'),
    )

