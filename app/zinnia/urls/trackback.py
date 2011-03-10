"""Urls for the Zinnia trackback"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

urlpatterns = patterns('app.zinnia.views.trackback',
                       url(r'^(?P<slug>[-\w]+)/$', 'entry_trackback',
                           name='zinnia_entry_trackback'),
                       )
