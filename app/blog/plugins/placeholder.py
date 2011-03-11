"""Placeholder model for blog"""
from cms.models.fields import PlaceholderField

from app.blog.models import EntryAbstractClass


class EntryPlaceholder(EntryAbstractClass):
    """Entry with a Placeholder to edit content"""

    content_placeholder = PlaceholderField('content')

    class Meta:
        """EntryPlaceholder's Meta"""
        abstract = True
