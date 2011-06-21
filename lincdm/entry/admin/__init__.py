"""Admin of lincdm.content"""
from django.contrib import admin
from lincdm.entry.models import Entry
from lincdm.entry.models import Category
from lincdm.entry.admin.entry import EntryAdmin
from lincdm.entry.admin.category import CategoryAdmin

admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
