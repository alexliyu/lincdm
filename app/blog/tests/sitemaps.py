"""Test cases for blog's sitemaps"""
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from tagging.models import Tag

from app.blog.models import Entry
from app.blog.models import Category
from app.blog.managers import PUBLISHED
from app.blog.sitemaps import EntrySitemap
from app.blog.sitemaps import CategorySitemap
from app.blog.sitemaps import AuthorSitemap
from app.blog.sitemaps import TagSitemap


class blogSitemapsTestCase(TestCase):
    """Test cases for Sitemaps classes provided"""
    urls = 'blog.tests.urls'

    def setUp(self):
        self.site = Site.objects.get_current()
        self.author = User.objects.create(username='admin',
                                          email='admin@example.com')
        self.category = Category.objects.create(title='Tests', slug='tests')
        params = {'title': 'My entry 1', 'content': 'My content 1',
                  'tags': 'blog, test', 'slug': 'my-entry-1',
                  'status': PUBLISHED}
        self.entry_1 = Entry.objects.create(**params)
        self.entry_1.authors.add(self.author)
        self.entry_1.categories.add(self.category)
        self.entry_1.sites.add(self.site)

        params = {'title': 'My entry 2', 'content': 'My content 2',
                  'tags': 'blog', 'slug': 'my-entry-2',
                  'status': PUBLISHED}
        self.entry_2 = Entry.objects.create(**params)
        self.entry_2.authors.add(self.author)
        self.entry_2.categories.add(self.category)
        self.entry_2.sites.add(self.site)

    def test_entry_sitemap(self):
        sitemap = EntrySitemap()
        self.assertEquals(len(sitemap.items()), 2)
        self.assertEquals(sitemap.lastmod(self.entry_1), self.entry_1.last_update)

    def test_category_sitemap(self):
        sitemap = CategorySitemap()
        self.assertEquals(len(sitemap.items()), 1)
        self.assertEquals(sitemap.lastmod(self.category), self.entry_2.creation_date)
        self.assertEquals(sitemap.lastmod(Category.objects.create(
            title='New', slug='new')), None)
        self.assertEquals(sitemap.priority(self.category), '1.0')

    def test_author_sitemap(self):
        sitemap = AuthorSitemap()
        self.assertEquals(len(sitemap.items()), 1)
        self.assertEquals(sitemap.lastmod(self.author), self.entry_2.creation_date)
        self.assertEquals(sitemap.lastmod(User.objects.create(
            username='New', email='new@example.com')), None)
        self.assertEquals(sitemap.location(self.author), '/authors/admin/')

    def test_tag_sitemap(self):
        sitemap = TagSitemap()
        blog_tag = Tag.objects.get(name='blog')
        self.assertEquals(len(sitemap.items()), 2)
        self.assertEquals(sitemap.lastmod(blog_tag), self.entry_2.creation_date)
        self.assertEquals(sitemap.priority(blog_tag), '1.0')
        self.assertEquals(sitemap.location(blog_tag), '/tags/blog/')
