"""Urls for the entry categories"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

from lincdm.entry.models import Category

category_conf = {'queryset': Category.tree.all()}

urlpatterns = patterns('django.views.generic.list_detail',
                       url(r'^$', 'object_list',
                           category_conf, 'entry_category_list'),
                       )

urlpatterns += patterns('entry.views.categories',
                        url(r'^(?P<path>[-\/\w]+)/page/(?P<page>\d+)/$',
                            'category_detail',
                            name='entry_category_detail_paginated'),
                        url(r'^(?P<path>[-\/\w]+)/$', 'category_detail',
                            name='entry_category_detail'),
                        )
