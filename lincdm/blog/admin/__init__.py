"""Admin of blog"""
from django.contrib import admin

from lincdm.blog.models import Entry
from lincdm.blog.models import Category
from lincdm.blog.admin.entry import EntryAdmin
from lincdm.blog.admin.category import CategoryAdmin


admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
