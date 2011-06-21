"""Urls for the blog feeds"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

from lincdm.blog.feeds import LatestEntries
from lincdm.blog.feeds import EntryDiscussions
from lincdm.blog.feeds import EntryComments
from lincdm.blog.feeds import EntryTrackbacks
from lincdm.blog.feeds import EntryPingbacks
from lincdm.blog.feeds import SearchEntries
from lincdm.blog.feeds import TagEntries
from lincdm.blog.feeds import CategoryEntries
from lincdm.blog.feeds import AuthorEntries


urlpatterns = patterns('',
                       url(r'^latest/$',
                           LatestEntries(),
                           name='blog_entry_latest_feed'),
                       url(r'^search/$',
                           SearchEntries(),
                           name='blog_entry_search_feed'),
                       url(r'^tags/(?P<slug>[- \w]+)/$',
                           TagEntries(),
                           name='blog_tag_feed'),
                       url(r'^authors/(?P<username>[.+-@\w]+)/$',
                           AuthorEntries(),
                           name='blog_author_feed'),
                       url(r'^categories/(?P<path>[-\/\w]+)/$',
                           CategoryEntries(),
                           name='blog_category_feed'),
                       url(r'^discussions/(?P<slug>[-\w]+)/$',
                           EntryDiscussions(),
                           name='blog_entry_discussion_feed'),
                       url(r'^comments/(?P<slug>[-\w]+)/$',
                           EntryComments(),
                           name='blog_entry_comment_feed'),
                       url(r'^pingbacks/(?P<slug>[-\w]+)/$',
                           EntryPingbacks(),
                           name='blog_entry_pingback_feed'),
                       url(r'^trackbacks/(?P<slug>[-\w]+)/$',
                           EntryTrackbacks(),
                           name='blog_entry_trackback_feed'),
                       )
