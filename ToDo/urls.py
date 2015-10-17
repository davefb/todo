from django.conf.urls import patterns, include, url

from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ToDo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^todo/(?P<ignore>add)?$',  'ToDo.views.create' ),
    url(r'^todo/(?P<id>\d+)?/$',  'ToDo.views.list'),


    url(r'^todo/add/(?P<json>json)',  'ToDo.views.create' ),
    url(r'^todo/(?P<id>\d+)/(?P<json>json)',  'ToDo.views.list'),
    url(r'^todo/(?P<id>\d+)/add',  'ToDo.views.add_item'),
    url(r'^todo/(?P<id>\d+)/remove/(?P<itemid>\d+)', 'ToDo.views.remove_item'),

    url(r'^admin/', include(admin.site.urls)),
)
