"""blog to WordPress command module"""
from django.conf import settings
from django.utils.encoding import smart_str
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.core.management.base import NoArgsCommand

from tagging.models import Tag

from lincdm.blog import __version__
from lincdm.blog.settings import PROTOCOL
from lincdm.blog.models import Entry
from lincdm.blog.models import Category


class Command(NoArgsCommand):
    """Command object for exporting a blog blog
    into WordPress via a WordPress eXtended RSS (WXR) file."""
    help = 'Export blog to WXR file.'

    def handle_noargs(self, **options):
        site = Site.objects.get_current()
        blog_context = {'entries': Entry.objects.all(),
                        'categories': Category.objects.all(),
                        'tags': Tag.objects.usage_for_model(Entry),
                        'version': __version__,
                        'description': 'Blog exported for django-blog-blog',
                        'language': settings.LANGUAGE_CODE,
                        'site': site,
                        'site_url': '%s://%s' % (PROTOCOL, site.domain)}
        export = render_to_string('blog/wxr.xml', blog_context)
        print smart_str(export)
