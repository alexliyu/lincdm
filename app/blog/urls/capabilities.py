"""Urls for the blog capabilities"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns
from django.contrib.sites.models import Site

from lincdm.settings import PROTOCOL

extra_context = {'protocol': PROTOCOL,
                 'site': Site.objects.get_current()}

urlpatterns = patterns('django.views.generic.simple',
                       url(r'^rsd.xml$', 'direct_to_template',
                           {'template': 'blog/rsd.xml',
                            'mimetype': 'text/xml',
                            'extra_context': extra_context},
                           name='blog_rsd'),
                       url(r'^wlwmanifest.xml$', 'direct_to_template',
                           {'template': 'blog/wlwmanifest.xml',
                            'mimetype': 'text/xml',
                            'extra_context': extra_context},
                           name='blog_wlwmanifest'),
                       )
