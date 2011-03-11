"""Urls for the blog feeds"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

from app.blog.feeds import LatestEntries, AtomLatestEntries
from app.blog.feeds import EntryDiscussions, AtomEntryDiscussions
from app.blog.feeds import EntryComments, AtomEntryComments
from app.blog.feeds import EntryTrackbacks, AtomEntryTrackbacks
from app.blog.feeds import EntryPingbacks, AtomEntryPingbacks
from app.blog.feeds import SearchEntries, AtomSearchEntries
from app.blog.feeds import TagEntries, AtomTagEntries
from app.blog.feeds import CategoryEntries, AtomCategoryEntries
from app.blog.feeds import AuthorEntries, AtomAuthorEntries

from app.blog.settings import FEEDS_FORMAT

if FEEDS_FORMAT == 'atom':
    urlpatterns = patterns('',
                           url(r'^latest/$',
                               AtomLatestEntries(),
                               name='blog_entry_latest_feed'),
                           url(r'^tags/(?P<slug>[- \w]+)/$',
                               AtomTagEntries(),
                               name='blog_tag_feed'),
                           url(r'^authors/(?P<username>[.+-@\w]+)/$',
                               AtomAuthorEntries(),
                               name='blog_author_feed'),
                           url(r'^categories/(?P<path>[-\/\w]+)/$',
                               AtomCategoryEntries(),
                               name='blog_category_feed'),
                           url(r'^search/(?P<slug>.*)/$',
                               AtomSearchEntries(),
                               name='blog_entry_search_feed'),
                           url(r'^discussions/(?P<slug>[-\w]+)/$',
                               AtomEntryDiscussions(),
                               name='blog_entry_discussion_feed'),
                           url(r'^comments/(?P<slug>[-\w]+)/$',
                               AtomEntryComments(),
                               name='blog_entry_comment_feed'),
                           url(r'^pingbacks/(?P<slug>[-\w]+)/$',
                               AtomEntryPingbacks(),
                               name='blog_entry_pingback_feed'),
                           url(r'^trackbacks/(?P<slug>[-\w]+)/$',
                               AtomEntryTrackbacks(),
                               name='blog_entry_trackback_feed'),
                           )
else:
    urlpatterns = patterns('',
                           url(r'^latest/$',
                               LatestEntries(),
                               name='blog_entry_latest_feed'),
                           url(r'^tags/(?P<slug>[- \w]+)/$',
                               TagEntries(),
                               name='blog_tag_feed'),
                           url(r'^authors/(?P<username>[.+-@\w]+)/$',
                               AuthorEntries(),
                               name='blog_author_feed'),
                           url(r'^categories/(?P<path>[-\/\w]+)/$',
                               CategoryEntries(),
                               name='blog_category_feed'),
                           url(r'^search/(?P<slug>.*)/$',
                               SearchEntries(),
                               name='blog_entry_search_feed'),
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
