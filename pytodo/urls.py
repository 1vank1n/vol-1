from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('pytodo.main.views',
    url(r'^$', 'home', name='home'),
    url(r'^task/new/$', 'new_task', name='new_task'),
    url(r'^task/delete/(\d+)$', 'del_task', name='del_task'),
    url(r'^admin/', include(admin.site.urls)),
)
