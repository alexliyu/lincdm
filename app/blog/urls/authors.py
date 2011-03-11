"""Urls for the blog authors"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

from app.blog.models import Author

author_conf = {'queryset': Author.published.all()}

urlpatterns = patterns('app.blog.views.authors',
                       url(r'^$', 'author_list',
                           author_conf, 'blog_author_list'),
                       url(r'^(?P<username>[.+-@\w]+)/$', 'author_detail',
                           name='blog_author_detail'),
                       url(r'^(?P<username>[.+-@\w]+)/page/(?P<page>\d+)/$',
                           'author_detail',
                           name='blog_author_detail_paginated'),
                       )
