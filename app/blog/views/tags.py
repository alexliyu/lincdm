"""Views for blog tags"""
from django.views.generic.list_detail import object_list

from tagging.views import tagged_object_list

from app.blog.models import Entry
from app.blog.managers import tags_published
from app.blog.views.decorators import update_queryset

tag_list = update_queryset(object_list, tags_published)

tag_detail = update_queryset(tagged_object_list, Entry.published.all,
                             'queryset_or_model')
