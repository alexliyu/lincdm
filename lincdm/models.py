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
from managers import AuthorPublishedManager, entries_published
class siteSetting(models.Model):
        sitename = models.CharField(max_length=15)
        sitetitle = models.CharField(default='', max_length=50)
    

class Author(User):
    """Proxy Model around User"""

    objects = models.Manager()
    published = AuthorPublishedManager()

    def entries_published(self):
        """Return only the entries published"""
        return entries_published(self.entries)

    @models.permalink
    def get_absolute_url(self):
        """Return author's URL"""
        return ('zinnia_author_detail', (self.username,))

    class Meta:
        """Author's Meta"""
        proxy = True
        

