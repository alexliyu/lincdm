"""Defaults urls for the blog project"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
                       url(r'^tags/', include('app.blog.urls.tags',)),
                       url(r'^feeds/', include('app.blog.urls.feeds')),
                       url(r'^authors/', include('app.blog.urls.authors')),
                       url(r'^categories/', include('app.blog.urls.categories')),
                       url(r'^search/', include('app.blog.urls.search')),
                       url(r'^sitemap/', include('app.blog.urls.sitemap')),
                       url(r'^trackback/', include('app.blog.urls.trackback')),
                       url(r'^discussions/', include('app.blog.urls.discussions')),
                       url(r'^', include('app.blog.urls.quick_entry')),
                       url(r'^', include('app.blog.urls.capabilities')),
                       url(r'^', include('app.blog.urls.entries')),
                       )
