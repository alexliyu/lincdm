"""Defaults urls for the entry project"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns

urlpatterns = patterns(
    '',
    url(r'^tags/', include('entry.urls.tags',)),
    url(r'^feeds/', include('entry.urls.feeds')),
    url(r'^authors/', include('entry.urls.authors')),
    url(r'^categories/', include('entry.urls.categories')),
    url(r'^search/', include('entry.urls.search')),
    url(r'^sitemap/', include('entry.urls.sitemap')),
    url(r'^trackback/', include('entry.urls.trackback')),
    url(r'^discussions/', include('entry.urls.discussions')),
    url(r'^', include('entry.urls.quick_entry')),
    url(r'^', include('entry.urls.capabilities')),
    url(r'^', include('entry.urls.entries')),
    )
