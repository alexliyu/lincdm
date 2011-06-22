"""Urls for the entry feeds"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

from lincdm.entry.feeds import LatestEntries
from lincdm.entry.feeds import EntryDiscussions
from lincdm.entry.feeds import EntryComments
from lincdm.entry.feeds import EntryTrackbacks
from lincdm.entry.feeds import EntryPingbacks
from lincdm.entry.feeds import SearchEntries
from lincdm.entry.feeds import TagEntries
from lincdm.entry.feeds import CategoryEntries
from lincdm.entry.feeds import AuthorEntries


urlpatterns = patterns('',
                       url(r'^latest/$',
                           LatestEntries(),
                           name='entry_entry_latest_feed'),
                       url(r'^search/$',
                           SearchEntries(),
                           name='entry_entry_search_feed'),
                       url(r'^tags/(?P<slug>[- \w]+)/$',
                           TagEntries(),
                           name='entry_tag_feed'),
                       url(r'^authors/(?P<username>[.+-@\w]+)/$',
                           AuthorEntries(),
                           name='entry_author_feed'),
                       url(r'^categories/(?P<path>[-\/\w]+)/$',
                           CategoryEntries(),
                           name='entry_category_feed'),
                       url(r'^discussions/(?P<slug>[-\w]+)/$',
                           EntryDiscussions(),
                           name='entry_entry_discussion_feed'),
                       url(r'^comments/(?P<slug>[-\w]+)/$',
                           EntryComments(),
                           name='entry_entry_comment_feed'),
                       url(r'^pingbacks/(?P<slug>[-\w]+)/$',
                           EntryPingbacks(),
                           name='entry_entry_pingback_feed'),
                       url(r'^trackbacks/(?P<slug>[-\w]+)/$',
                           EntryTrackbacks(),
                           name='entry_entry_trackback_feed'),
                       )
