# -*- coding: utf-8 -*-
"""
"""
from django.conf.urls.defaults import patterns, url

from app.planet.feeds import PostFeed, AuthorFeed, AuthorTagFeed, TagFeed

# HTML view's urls
urlpatterns = patterns('app.planet.views',
    url(r'^blogs/(?P<blog_id>\d+)/$', "blog_detail", name="planet_blog_detail"),
    url(r'^blogs/$', "blogs_list", name="planet_blog_list"),

    url(r'^feeds/(?P<feed_id>\d+)/tags/(?P<tag>.*)/$', "feed_detail", name="planet_by_tag_feed_detail"),
    url(r'^feeds/(?P<feed_id>\d+)/$', "feed_detail", name="planet_feed_detail"),
    url(r'^feeds/$', "feeds_list", name="planet_feed_list"),

    url(r'^authors/(?P<author_id>\d+)/tags/(?P<tag>.*)/$', "author_detail", name="planet_by_tag_author_detail"),
    url(r'^authors/(?P<author_id>\d+)/$', "author_detail", name="planet_author_detail"),
    url(r'^authors/$', "authors_list", name="planet_author_list"),
    
    url(r'^tags/(?P<tag>.*)/feeds/$', "tag_feeds_list", name="planet_tag_feed_list"),
    url(r'^tags/(?P<tag>.*)/authors/$', "tag_authors_list", name="planet_tag_author_list"),
    url(r'^tags/(?P<tag>.*)/$', "tag_detail", name="planet_tag_detail"),
    url(r'^tags/$', "tags_cloud", name="planet_tag_cloud"),
    
    url(r'^opml/$', "opml", name="planet_opml"),
    url(r'^foaf/$', "foaf", name="planet_foaf"),
    
    url(r'^posts/(?P<post_id>\d+)/$', "post_detail", name="planet_post_detail"),
    url(r'^posts/$', "posts_list", name="planet_post_list"),
    
    url(r'^search/$', "search", name="planet_search"),

    url(r'^$', "index", name="planet_index"),
)

# Feed's urls
urlpatterns += patterns('',
    url(r'^posts/feeds/rss/$', PostFeed(), name="planet_rss_feed"),
    url(r'^feeds/rss/tags/(?P<tag>.*)/$', TagFeed(), name="planet_tag_rss_feed"),
    url(r'^feeds/rss/authors/(?P<author_id>\d+)/$', AuthorFeed(), name="planet_author_rss_feed"),
    url(r'^feeds/rss/authors/(?P<author_id>\d+)/tags/(?P<tag>.*)/$', AuthorTagFeed(), name="planet_tag_author_rss_feed"),
)

