"""Template tags and filters for blog's admin"""
from django.template import Library
from django.contrib.comments.models import Comment
from django.contrib.contenttypes.models import ContentType

from app.blog.models import Entry
from app.blog.models import Author
from app.blog.models import Category
from app.blog.managers import DRAFT
from app.blog.managers import tags_published

register = Library()


@register.inclusion_tag('blog/tags/dummy.html')
def get_draft_entries(
    number=5, template='admin/blog/widgets/_draft_entries.html'):
    """Return the latest draft entries"""
    return {'template': template,
            'entries': Entry.objects.filter(status=DRAFT)[:number]}


@register.inclusion_tag('blog/tags/dummy.html')
def get_content_stats(
    template='admin/blog/widgets/_content_stats.html'):
    """Return statistics of the contents"""
    content_type = ContentType.objects.get_for_model(Entry)

    discussions = Comment.objects.filter(
        is_public=True, content_type=content_type)

    return {'template': template,
            'entries': Entry.published.count(),
            'categories': Category.objects.count(),
            'tags': tags_published().count(),
            'authors': Author.published.count(),
            'comments': discussions.filter(flags=None).count(),
            'pingbacks': discussions.filter(flags__flag='pingback').count(),
            'trackbacks': discussions.filter(flags__flag='trackback').count(),
            'rejects': Comment.objects.filter(
                is_public=False, content_type=content_type).count(),
            }
