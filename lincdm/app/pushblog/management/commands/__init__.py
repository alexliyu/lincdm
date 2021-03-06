 <<<<<<< HEAD
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
import time
import mimetypes

from urlparse import urlparse
from datetime import datetime

from django.conf import settings
from django.contrib.sites.models import Site

from tagging.models import Tag

from app.planet.models import (Blog, Generator, Feed, FeedLink, Post, PostLink,
        Author, PostAuthorData, Enclosure)
from app.planet.signals import post_created

class PostAlreadyExists(Exception):
    pass

def process_feed(feed_url, create=False):
    """
    Stores a feed, its related data, its entries and their related data.
    If create=True then it creates the feed, otherwise it only stores new
    entries  and their related data.
    """

    def normalize_tag(tag):
        """
        converts things like "-noise-" to "noise" and "- noise -" to "noise"
        """
        if tag.startswith("-"):
            tag = tag[1:]
        if tag.endswith("-"):
            tag = tag[:-1]
        tag = tag.strip()
        return tag

    try:
        USER_AGENT = settings.USER_AGENT
    except AttributeError:
        print "Please set the variable USER_AGENT = <string> in your settings.py"
        exit(0)

    feed_url = str(feed_url).strip()

    try:
        planet_feed = Feed.objects.get(url=feed_url)
    except Feed.DoesNotExist:
        planet_feed = None

    print "*" * 20
    print "Feed: %s" % feed_url

    if create and planet_feed:
        # can't create it due to it already exists
        print "This feed already exists!"
        exit(0)

    if not create and not planet_feed:
        # can't update it due to it does not exist
        print "This feed does not exist!"
        exit(0)

    # retrieve and parse feed using conditional GET method
    if not create:
        modified = datetime.timetuple(planet_feed.last_modified)
        etag = planet_feed.etag
        # update last checked datetime
        planet_feed.last_checked = datetime.now()
        planet_feed.save()
    else:
        modified = etag = None

    document = feedparser.parse(feed_url, agent=USER_AGENT,
                                modified=modified, etag=etag)

    current_site = Site.objects.get(pk=settings.SITE_ID)

    if create:
        # then create blog, feed, generator, feed links and feed tags

        title = document.feed.get("title", "--")
        subtitle = document.feed.get("subtitle")
        blog_url = document.feed.get("link")
        rights = document.feed.get("rights") or document.feed.get("license")
        info = document.feed.get("info")
        guid = document.feed.get("id")
        image_url = document.feed.get("image", {}).get("href")
        icon_url = document.feed.get("icon")
        language = document.feed.get("language")
        etag = document.get("etag", '')
        last_modified = document.get("updated_parsed", datetime.now())

        feed_links = document.feed.get("links", [])
        if not blog_url:
            link = filter(lambda item: item["rel"] == "alternate", feed_links)
            if link:
                blog_url = link[0]["href"]

        blog, created = Blog.objects.get_or_create(
            url=blog_url, defaults={"title": title})

        generator_dict = document.feed.get("generator_detail", {})

        if generator_dict:
            generator, created = Generator.objects.get_or_create(
                name=generator_dict.get("name", "--"),
                link=generator_dict.get("link"),
                version=generator_dict.get("version"))
        else:
            generator = None

        planet_feed = Feed(title=title, subtitle=subtitle, blog=blog,
            url=feed_url, rights=rights, info=info, guid=guid,
            image_url=image_url, icon_url=icon_url, language=language,
            etag=etag, last_modified=last_modified, generator=generator,
            is_active=True, last_checked=datetime.now(),
            site=current_site
        )
        planet_feed.save()

        for tag_dict in document.feed.get("tags", []):
            name = tag_dict.get("term")
            if name:
                print name

        for link_dict in feed_links:
            feed_link, created = FeedLink.objects.get_or_create(
                feed=planet_feed,
                rel=link_dict.get("rel", "--"),
                mime_type=link_dict.get("type"),
                link=link_dict.get("href", blog_url)
            )

    entries = []

    total_results = int(document.feed.get("opensearch_totalresults", len(document.entries)))
    items_per_page = int(document.feed.get("opensearch_itemsperpage", 25))
    new_posts_count = 0

    if total_results == 0:
        print "No entries to store. status: %s %s" % (document.get("status"), document.get("debug_message"))
    else:
        print "Entries total count: %d" % total_results
        stop_retrieving = False
        while (total_results > len(entries)) and not stop_retrieving:

            # retrieve and store feed posts
            entries.extend(document.entries)
            print "Processing %d entries" % len(document.entries)

            for entry in document.entries:
                title = entry.get("title", "")
                url = entry.get("link")
                guid = entry.get("link")
                content = entry.get('description') or entry.get("content", [{"value": ""}])[0]["value"]
                comments_url = entry.get("comments")
                date_modified = entry.get("updated_parsed") or\
                    entry.get("published_parsed")
                try:
                    date_modified = datetime.fromtimestamp(
                        time.mktime(date_modified))
                except Exception:
                    date_modified = None

                try:
                    if len(Post.objects.filter(url=url, guid=guid)):
                        raise PostAlreadyExists
                    post = Post(title=title, url=url, guid=guid, content=content,
                        comments_url=comments_url, date_modified=date_modified,
                        feed=planet_feed)
                    # To have the feed entry in the pre_save signal
                    post.entry = entry
                    post.save()
                except PostAlreadyExists:
                    print "Skipping post %s (%s) because already exists"\
                        % (guid, url)
                    if not create:
                        # if it is in update-mode then stop retrieving when
                        # it finds repeated posts
                        stop_retrieving = True
                else:
                    new_posts_count += 1
                    # create post tags...
                    for tag_dict in entry.get("tags", []):
                        tag_name = tag_dict.get("term") or tag_dict.get("label")
                        tag_name = tag_name[:255]
                        tag_name = normalize_tag(tag_name)
                        try:
                            if "/" in tag_name:
                                # For path based categories
                                for subtag in tag_name.split("/"):
                                    if subtag:
                                        # empty string if starts/ends with slash
                                        Tag.objects.add_tag(post, '"%s"' % subtag)
                            else:
                                Tag.objects.add_tag(post, '"%s"' % tag_name)
                        except AttributeError, e:
                            print "Ignoring tag error: %s" % e
                    # create post links...
                    for link_dict in entry.get("links", []):
                        post_link, created = PostLink.objects.get_or_create(
                            post=post,
                            rel=link_dict.get("rel", "--"),
                            mime_type=link_dict.get("type"),
                            link=link_dict.get("href", "--"),
                            title=link_dict.get("title", "--")
                        )

                    # create and store enclosures...
                    if entry.get('media_thumbnail', False):
                        mime_type, enc = mimetypes.guess_type(urlparse(entry.get('media_thumbnail').href).path)
                        post_enclosure, created = Enclosure.objects.get_or_create(
                            post=post,
                            length=0,
                            mime_type=mime_type,
                            link=entry.get('media_thumbnail').href
                        )
                    for enclosure_dict in entry.get("enclosures", []):
                        post_enclosure = Enclosure(
                            post=post,
                            length=enclosure_dict.get("length", 0),
                            mime_type=enclosure_dict.get("type", ""),
                            link=enclosure_dict.get("href")
                        )
                        post_enclosure.save()

                    # create and store author...
                    author_dict = entry.get("author_detail")

                    if author_dict:
                        author, created = Author.objects.get_or_create(
                            name=author_dict.get("name", ""),
                            email=author_dict.get("email", ""),
                            profile_url=author_dict.get("href")
                        )
                        try:
                            PostAuthorData.objects.get(author=author, post=post)
                        except PostAuthorData.DoesNotExist:
                            pad = PostAuthorData(author=author, post=post)
                            pad.save()

                    # create and store contributors...
                    for contributor_dict in entry.get("contributors", []):
                        contributor, created = Author.objects.get_or_create(
                            name=author_dict.get("name", ""),
                            email=author_dict.get("email", ""),
                            profile_url=contributor_dict.get("href")
                        )
                        try:
                            PostAuthorData.objects.get(author=contributor, post=post)
                        except PostAuthorData.DoesNotExist:
                            pad = PostAuthorData(author=contributor, post=post,
                                is_contributor=True)
                            pad.save()

                    # We send a post_created signal
                    print 'post_created.send(sender=post)', post
                    post_created.send(sender=post, instance=post)

            if not stop_retrieving:
                opensearch_url = "%s?start-index=%d&max-results=%d" % \
                    (feed_url, len(entries) + 1, items_per_page)

                print "retrieving %s..." % opensearch_url
                document = feedparser.parse(opensearch_url, agent=USER_AGENT)

        if new_posts_count:
            # update last modified datetime
            planet_feed.last_modified = datetime.now()
            planet_feed.save()
        print "%d posts were created. Done." % new_posts_count

    print
    return new_posts_count
== == == = 
"""Commands module of blog"""
>>>>>>> 39ddaac01ddba11024a2c514d4a2e06a654cc9b8
