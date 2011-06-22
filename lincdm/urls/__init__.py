#-*- coding:utf-8 -*-
'''
Created on 2011-1-30

@author: 李昱
'''
from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('lincdm.grappelli.urls')),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^article/', include('lincdm.entry.urls')),
    url(r'^blog/', include('lincdm.blog.urls')),
    url(r'^', include('lincdm.urls.index')),
)
urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
        url(r'^media/(?P<path>.*)$', 'serve'),
        )

if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),
    ) + urlpatterns

