"""Settings of blog"""
import os
from django.conf import settings

PING_DIRECTORIES = getattr(settings, 'blog_PING_DIRECTORIES',
                           ('http://www.3344520.tk/xmlrpc/',))
SAVE_PING_DIRECTORIES = getattr(settings, 'blog_SAVE_PING_DIRECTORIES',
                                bool(PING_DIRECTORIES))
SAVE_PING_EXTERNAL_URLS = getattr(settings, 'blog_PING_EXTERNAL_URLS', True)

COPYRIGHT = getattr(settings, 'blog_COPYRIGHT', 'LinCDM')

PAGINATION = getattr(settings, 'blog_PAGINATION', 10)
ALLOW_EMPTY = getattr(settings, 'blog_ALLOW_EMPTY', True)
ALLOW_FUTURE = getattr(settings, 'blog_ALLOW_FUTURE', True)

ENTRY_TEMPLATES = getattr(settings, 'blog_ENTRY_TEMPLATES', [])
ENTRY_BASE_MODEL = getattr(settings, 'blog_ENTRY_BASE_MODEL', '')

WYSIWYG = getattr(settings, 'blog_WYSIWYG',
                  'tinymce' in settings.INSTALLED_APPS \
                  and 'tinymce' or 'wymeditor')

MAIL_COMMENT = getattr(settings, 'blog_MAIL_COMMENT', True)
MAIL_COMMENT_REPLY = getattr(settings, 'blog_MAIL_COMMENT_REPLY', False)
AKISMET_COMMENT = getattr(settings, 'blog_AKISMET_COMMENT', True)

UPLOAD_TO = getattr(settings, 'blog_UPLOAD_TO', 'uploads')

PROTOCOL = getattr(settings, 'blog_PROTOCOL', 'http')
MEDIA_URL = getattr(settings, 'blog_MEDIA_URL',
                    os.path.join(settings.MEDIA_URL, 'blog/'))

FEEDS_FORMAT = getattr(settings, 'blog_FEEDS_FORMAT', 'rss')
FEEDS_MAX_ITEMS = getattr(settings, 'blog_FEEDS_MAX_ITEMS', 15)

PINGBACK_CONTENT_LENGTH = getattr(settings,
                                  'blog_PINGBACK_CONTENT_LENGTH', 300)

F_MIN = getattr(settings, 'blog_F_MIN', 0.1)
F_MAX = getattr(settings, 'blog_F_MAX', 1.0)

USE_BITLY = getattr(settings, 'blog_USE_BITLY',
                    'django_bitly' in settings.INSTALLED_APPS)

try:
    import tweepy
    USE_TWITTER = getattr(settings, 'blog_USE_TWITTER', True)
except ImportError:
    USE_TWITTER = False

TWITTER_CONSUMER_KEY = getattr(settings, 'TWITTER_CONSUMER_KEY', '')
TWITTER_CONSUMER_SECRET = getattr(settings, 'TWITTER_CONSUMER_SECRET', '')
TWITTER_ACCESS_KEY = getattr(settings, 'TWITTER_ACCESS_KEY', '')
TWITTER_ACCESS_SECRET = getattr(settings, 'TWITTER_ACCESS_SECRET', '')
