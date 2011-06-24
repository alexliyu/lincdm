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
   
    url(r'^blog/', include('lincdm.blog.urls')),
    url(r'^tags/', include('lincdm.urls.tags',)),
    url(r'^feeds/', include('lincdm.urls.feeds')),
    url(r'^authors/', include('lincdm.urls.authors')),
    url(r'^categories/', include('lincdm.urls.categories')),
    url(r'^search/', include('lincdm.urls.search')),
    url(r'^sitemap/', include('lincdm.urls.sitemap')),
    url(r'^trackback/', include('lincdm.urls.trackback')),
    url(r'^discussions/', include('lincdm.urls.discussions')),
    
    url(r'^', include('lincdm.urls.quick_entry')),
    url(r'^', include('lincdm.urls.capabilities')),
    url(r'^', include('lincdm.urls.entries')),
    url(r'^', include('lincdm.urls.index')),
)
urlpatterns += patterns('',
      (r'^static/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root':  settings.MEDIA_ROOT}),
      (r'^media/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root':  settings.MEDIA_ROOT}),
    )

if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),
    ) + urlpatterns

