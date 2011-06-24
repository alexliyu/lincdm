"""Urls for the entry sitemap"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

urlpatterns = patterns('lincdm.views.sitemap',
                       url(r'^$', 'sitemap',
                           {'template': 'sitemap.html'},
                           name='entry_sitemap'),
                       )
