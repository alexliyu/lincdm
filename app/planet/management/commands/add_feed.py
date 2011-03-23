#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from app.planet.management.commands import process_feed


class Command(BaseCommand):
    """
    Command to add a complete blog feed to our db.

    Usage:

    ./manage.py add_feed <feed_url>
    """
    def handle(self, *args, **options):
        if not len(args):
            print "You must provide the feed url as parameter"
            exit(0)

        feed_url = args[0]
        # process feed in create-mode
        process_feed(feed_url, create=True)
                
