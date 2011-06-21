"""Unit tests for Zinnia"""
from unittest import TestSuite
from unittest import TestLoader
from django.conf import settings

from lincdm.blog.tests.entry import EntryTestCase  # ~0.2s
from lincdm.blog.tests.entry import EntryHtmlContentTestCase  # ~0.5s
from lincdm.blog.tests.entry import EntryGetBaseModelTestCase
from lincdm.blog.tests.signals import SignalsTestCase
from lincdm.blog.tests.category import CategoryTestCase
from lincdm.blog.tests.admin import EntryAdminTestCase
from lincdm.blog.tests.admin import CategoryAdminTestCase
from lincdm.blog.tests.managers import ManagersTestCase  # ~1.2s
from lincdm.blog.tests.feeds import ZinniaFeedsTestCase  # ~0.4s
from lincdm.blog.tests.views import ZinniaViewsTestCase  # ~1.5s ouch...
from lincdm.blog.tests.views import ZinniaCustomDetailViews  # ~0.3s
from lincdm.blog.tests.pingback import PingBackTestCase  # ~0.3s
from lincdm.blog.tests.metaweblog import MetaWeblogTestCase  # ~0.6s
from lincdm.blog.tests.comparison import ComparisonTestCase
from lincdm.blog.tests.quick_entry import QuickEntryTestCase  # ~0.4s
from lincdm.blog.tests.sitemaps import ZinniaSitemapsTestCase  # ~0.3s
from lincdm.blog.tests.ping import DirectoryPingerTestCase
from lincdm.blog.tests.ping import ExternalUrlsPingerTestCase
from lincdm.blog.tests.templatetags import TemplateTagsTestCase  # ~0.4s
from lincdm.blog.tests.moderator import EntryCommentModeratorTestCase  # ~0.1s
from lincdm.blog.tests.spam_checker import SpamCheckerTestCase
from lincdm.blog.tests.url_shortener import URLShortenerTestCase
from lincdm.blog.signals import disconnect_zinnia_signals
# TOTAL ~ 6.6s


def suite():
    """Suite of TestCases for Django"""
    suite = TestSuite()
    loader = TestLoader()

    test_cases = (ManagersTestCase, EntryTestCase,
                  EntryGetBaseModelTestCase, SignalsTestCase,
                  EntryHtmlContentTestCase, CategoryTestCase,
                  ZinniaViewsTestCase, ZinniaFeedsTestCase,
                  ZinniaSitemapsTestCase, ComparisonTestCase,
                  DirectoryPingerTestCase, ExternalUrlsPingerTestCase,
                  TemplateTagsTestCase, QuickEntryTestCase,
                  URLShortenerTestCase, EntryCommentModeratorTestCase,
                  ZinniaCustomDetailViews, SpamCheckerTestCase,
                  EntryAdminTestCase, CategoryAdminTestCase)

    if 'django_xmlrpc' in settings.INSTALLED_APPS:
        test_cases += (PingBackTestCase, MetaWeblogTestCase)

    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)

    return suite

disconnect_zinnia_signals()
