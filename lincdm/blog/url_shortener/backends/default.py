"""Default url shortener backend for blog"""
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

from lincdm.blog.settings import PROTOCOL


def backend(entry):
    """Default url shortener backend for blog"""
    return '%s://%s%s' % (PROTOCOL, Site.objects.get_current().domain,
                       reverse('blog_entry_shortlink', args=[entry.pk]))
