"""Defaults urls for the Zinnia project"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
                       url(r'^tags/', include('app.zinnia.urls.tags',)),
                       url(r'^feeds/', include('app.zinnia.urls.feeds')),
                       url(r'^authors/', include('app.zinnia.urls.authors')),
                       url(r'^categories/', include('app.zinnia.urls.categories')),
                       url(r'^search/', include('app.zinnia.urls.search')),
                       url(r'^sitemap/', include('app.zinnia.urls.sitemap')),
                       url(r'^trackback/', include('app.zinnia.urls.trackback')),
                       url(r'^discussions/', include('app.zinnia.urls.discussions')),
                       url(r'^', include('app.zinnia.urls.quick_entry')),
                       url(r'^', include('app.zinnia.urls.capabilities')),
                       url(r'^', include('app.zinnia.urls.entries')),
                       )
