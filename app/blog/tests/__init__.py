"""Unit tests for blog"""
from unittest import TestSuite
from unittest import TestLoader
from django.conf import settings
from django.db.models.signals import post_save

from app.blog.models import Entry
from app.blog.tests.entry import EntryTestCase
from app.blog.tests.category import CategoryTestCase
from app.blog.tests.managers import ManagersTestCase
from app.blog.tests.feeds import blogFeedsTestCase
from app.blog.tests.views import blogViewsTestCase  # ~3.5s ouch...
from app.blog.tests.pingback import PingBackTestCase  # ~0.9s
from app.blog.tests.metaweblog import MetaWeblogTestCase  # ~0.6s
from app.blog.tests.comparison import ComparisonTestCase
from app.blog.tests.quick_entry import QuickEntryTestCase
from app.blog.tests.sitemaps import blogSitemapsTestCase
from app.blog.tests.ping import ExternalUrlsPingerTestCase
from app.blog.tests.templatetags import TemplateTagsTestCase
from app.blog.tests.moderator import EntryCommentModeratorTestCase


def suite():
    """Suite of TestCases for Django"""
    suite = TestSuite()
    loader = TestLoader()

    test_cases = (ManagersTestCase, EntryTestCase, CategoryTestCase,
                  blogViewsTestCase, blogFeedsTestCase,
                  blogSitemapsTestCase, ComparisonTestCase,
                  ExternalUrlsPingerTestCase, TemplateTagsTestCase,
                  QuickEntryTestCase, EntryCommentModeratorTestCase)

    if 'django_xmlrpc' in settings.INSTALLED_APPS:
        test_cases += (PingBackTestCase, MetaWeblogTestCase)

    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)

    return suite

# Disconnecting signals provided by blog
post_save.disconnect(sender=Entry,
                     dispatch_uid='blog.entry.post_save.ping_directories')
post_save.disconnect(sender=Entry,
                     dispatch_uid='blog.entry.post_save.ping_external_urls')
