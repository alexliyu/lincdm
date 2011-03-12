"""Urls for the blog tags"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

from app.blog.models import Entry
from settings import PAGINATION
from app.blog.managers import tags_published

tag_conf = {'queryset': tags_published(),
            'template_name': 'blog/tag_list.html'}

tag_conf_entry = {'queryset_or_model': Entry.published.all(),
                  'paginate_by': PAGINATION}

urlpatterns = patterns('app.blog.views.tags',
                       url(r'^$', 'tag_list',
                           tag_conf, name='blog_tag_list'),
                       url(r'^(?P<tag>[- \w]+)/$', 'tag_detail',
                           tag_conf_entry, name='blog_tag_detail'),
                       url(r'^(?P<tag>[- \w]+)/page/(?P<page>\d+)/$',
                           'tag_detail', tag_conf_entry,
                           name='blog_tag_detail_paginated'),
                       )
