"""Views for entry tags"""
from django.views.generic.list_detail import object_list

from tagging.views import tagged_object_list

from lincdm.entry.models import Entry
from lincdm.settings import PAGINATION
from lincdm.managers import tags_published
from lincdm.views.decorators import update_queryset
from lincdm.views.decorators import template_name_for_entry_queryset_filtered


tag_list = update_queryset(object_list, tags_published)


def tag_detail(request, tag, page=None, **kwargs):
    """Display the entries of a tag"""
    if not kwargs.get('template_name'):
        kwargs['template_name'] = template_name_for_entry_queryset_filtered(
            'tag', tag)

    return tagged_object_list(request, tag=tag,
                              queryset_or_model=Entry.published.all(),
                              paginate_by=PAGINATION, page=page,
                              **kwargs)
