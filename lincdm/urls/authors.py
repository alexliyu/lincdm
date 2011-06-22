"""Urls for the entry authors"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns


urlpatterns = patterns('entry.views.authors',
                       url(r'^$', 'author_list',
                           name='entry_author_list'),
                       url(r'^(?P<username>[.+-@\w]+)/$', 'author_detail',
                           name='entry_author_detail'),
                       url(r'^(?P<username>[.+-@\w]+)/page/(?P<page>\d+)/$',
                           'author_detail',
                           name='entry_author_detail_paginated'),
                       )
