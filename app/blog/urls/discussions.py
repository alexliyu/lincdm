"""Urls for the blog discussions"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
                       url(r'^success/$', 'django.views.generic.simple.direct_to_template',
                           {'template': 'comments/blog/entry/posted.html'},
                           name='blog_discussion_success'),
                       )
