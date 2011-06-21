"""Urls for the blog trackback"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

urlpatterns = patterns('blog.views.trackback',
                       url(r'^(?P<slug>[-\w]+)/$', 'entry_trackback',
                           name='blog_entry_trackback'),
                       )
