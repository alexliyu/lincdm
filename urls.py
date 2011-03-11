#-*- coding:utf-8 -*-
'''
Created on 2011-1-30

@author: 李昱
'''
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from app.blog.sitemaps import TagSitemap
from app.blog.sitemaps import EntrySitemap
from app.blog.sitemaps import CategorySitemap
from app.blog.sitemaps import AuthorSitemap
import os
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lincdm.views.home', name='home'),
    # url(r'^lincdm/', include('lincdm.foo.urls')),
    (r'^$', 'django.views.generic.simple.redirect_to',
                        {'url': '/blog/'}),
                       url(r'^blog/', include('app.blog.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^admin_tools/', include('admin_tools.urls')),
     
)
sitemaps = {'tags': TagSitemap,
            'blog': EntrySitemap,
            'authors': AuthorSitemap,
            'categories': CategorySitemap, }

urlpatterns += patterns('django.contrib.sitemaps.views',
                        (r'^sitemap.xml$', 'index',
                         {'sitemaps': sitemaps}),
                        (r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',
                         {'sitemaps': sitemaps}),
                        )

urlpatterns += patterns('django.views.static',
                        url(r'^blog/(?P<path>.*)$', 'serve',
                            {'document_root': os.path.join(os.path.dirname(__file__),
                                                           'app', 'blog', 'media', 'blog')}),
                        )
