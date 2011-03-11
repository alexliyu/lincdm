"""Urls for the blog search"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

urlpatterns = patterns('app.blog.views.search',
                       url(r'^$', 'entry_search', name='blog_entry_search'),
                       )
