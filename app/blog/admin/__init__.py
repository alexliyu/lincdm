"""Admin of blog"""
from django.contrib import admin

from app.blog.models import Entry
from app.blog.models import Category
from app.blog.admin.entry import EntryAdmin
from app.blog.admin.category import CategoryAdmin


admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
