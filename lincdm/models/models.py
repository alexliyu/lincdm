#-*- coding:utf-8 -*-
'''
Created on 2011-1-30

@author: 李昱
博客内容管理
'''
from django.db import models
from datetime import datetime
# Create your models here.

from django.db import models
from django.db.models import Q
from django.utils.html import strip_tags
from django.utils.html import linebreaks
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db.models.signals import post_save
from django.utils.importlib import import_module
from django.contrib.comments.models import Comment
from django.contrib.comments.models import CommentFlag
from django.contrib.comments.moderation import moderator
from django.utils.translation import ugettext_lazy as _
from lincdm.managers import AuthorPublishedManager, entries_published
from django.contrib import admin


class UserProfile(models.Model):
    url = models.URLField()
    home_address = models.TextField()
    phone_numer = models.IntegerField()
    user = models.ForeignKey(User, unique=True)
    
class SiteSetting(Site):
        
        sitename = models.CharField(max_length=15)
        sitetitle = models.CharField(default='', max_length=50)
        



class Author(User):
    """Proxy Model around User"""

    objects = models.Manager()
    published = AuthorPublishedManager()

    def entries_published(self):
        """返回已发布的文章"""
        return entries_published(self.entries)
    
    def blog_entries_published(self):
        """返回已发布的日志"""
        return entries_published(self.blogs)

    @models.permalink
    def get_absolute_url(self):
        """Return author's URL"""
        return ('entry_author_detail', (self.username,))

    class Meta:
        """Author's Meta"""
        proxy = True
        

