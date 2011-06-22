#-*- coding:utf-8 -*-
'''
Created on 2011-1-30

@author: 李昱
博客管理注册
'''
from django.contrib import admin

from lincdm.blog.models import Entry
from lincdm.blog.models import Category
from lincdm.blog.admin.entry import EntryAdmin
from lincdm.blog.admin.category import CategoryAdmin


admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
