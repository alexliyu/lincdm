"""Views for blog authors"""
from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list

from app.blog.models import Author
from lincdm.settings import PAGINATION
from app.blog.views.decorators import update_queryset


author_list = update_queryset(object_list, Author.published.all)


def author_detail(request, username, page=None):
    """Display the entries of an author"""
    author = get_object_or_404(Author, username=username)
    return object_list(request, queryset=author.entries_published_set(),
                       paginate_by=PAGINATION, page=page,
                       extra_context={'author': author})
