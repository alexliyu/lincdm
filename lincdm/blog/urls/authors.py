"""Urls for the blog authors"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns


info_conf = {
                 'template_name': 'blog/authors_list.html',
                 
                 }

urlpatterns = patterns('blog.views.authors',
                       url(r'^$', 'author_list', info_conf,
                           name='blog_author_list'),
                       url(r'^(?P<username>[.+-@\w]+)/$', 'author_detail',
                           name='blog_author_detail'),
                       url(r'^(?P<username>[.+-@\w]+)/page/(?P<page>\d+)/$',
                           'author_detail',
                           name='blog_author_detail_paginated'),
                       )
