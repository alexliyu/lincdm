"""Urls for the blog tags"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

tag_conf = {'template_name': 'blog/tag_list.html'}

urlpatterns = patterns('blog.views.tags',
                       url(r'^$', 'tag_list',
                           tag_conf, name='blog_tag_list'),
                       url(r'^(?P<tag>[- \w]+)/$', 'tag_detail',
                           name='blog_tag_detail'),
                       url(r'^(?P<tag>[- \w]+)/page/(?P<page>\d+)/$',
                           'tag_detail', name='blog_tag_detail_paginated'),
                       )
