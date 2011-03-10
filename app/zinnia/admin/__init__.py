"""Admin of Zinnia"""
from django.contrib import admin

from app.zinnia.models import Entry
from app.zinnia.models import Category
from app.zinnia.admin.entry import EntryAdmin
from app.zinnia.admin.category import CategoryAdmin


admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
