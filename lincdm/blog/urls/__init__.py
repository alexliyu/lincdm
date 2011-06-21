"""Defaults urls for the blog project"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns

urlpatterns = patterns(
    '',
    url(r'^tags/', include('blog.urls.tags',)),
    url(r'^feeds/', include('blog.urls.feeds')),
    url(r'^authors/', include('blog.urls.authors')),
    url(r'^categories/', include('blog.urls.categories')),
    url(r'^search/', include('blog.urls.search')),
    url(r'^sitemap/', include('blog.urls.sitemap')),
    url(r'^trackback/', include('blog.urls.trackback')),
    url(r'^discussions/', include('blog.urls.discussions')),
    url(r'^', include('blog.urls.quick_entry')),
    url(r'^', include('blog.urls.capabilities')),
    url(r'^', include('blog.urls.entries')),
    )
