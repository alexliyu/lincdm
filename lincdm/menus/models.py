# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from lincdm.managers import MenusTitleManager

from lincdm.entry.models import Category

class CacheKeyManager(models.Manager):
    def get_keys(self, site_id=None, language=None):
        ret = self.none()
        if not site_id and not language:
            # Both site and language are None - return everything  
            ret = self.all()
        elif not site_id:
            ret = self.filter(language=language)
        elif not language:
            ret = self.filter(site=site_id)
        else:
            # Filter by site_id *and* by language.
            ret = self.filter(site=site_id).filter(language=language)
        return ret

class CacheKey(models.Model):
    '''
    This is to store a "set" of cache keys in a fashion where it's accessible 
    by multiple processes / machines.
    Multiple Django instances will then share the keys.
    This allows for selective invalidation of the menu trees (per site, per 
    language), in the cache.
    '''
    language = models.CharField(max_length=255)
    site = models.PositiveIntegerField()
    key = models.CharField(max_length=255)
    objects = CacheKeyManager()



class MenusTitle(models.Model):
    title = models.CharField("title", max_length=255)
    menu_title = models.CharField("title", max_length=255, blank=True, null=True, help_text="overwrite the title in the menu")
    slug = models.SlugField("slug", max_length=255, db_index=True, unique=False)
    path = models.CharField("Path", max_length=255, db_index=True)
    has_url_overwrite = models.BooleanField("has url overwrite", default=False, db_index=True, editable=False)
    application_urls = models.CharField('application', max_length=200, blank=True, null=True, db_index=True)
    redirect = models.CharField("redirect", max_length=255, blank=True, null=True)
    meta_description = models.TextField("description", max_length=255, blank=True, null=True)
    meta_keywords = models.CharField("keywords", max_length=255, blank=True, null=True)
    page_title = models.CharField("title", max_length=255, blank=True, null=True, help_text="overwrite the title (html title tag)")
    page = models.ForeignKey(Category, verbose_name="page", related_name="title_set")
    creation_date = models.DateTimeField("creation date", editable=False, default=datetime.now)
    
    objects = MenusTitleManager()
    

    
    def __unicode__(self):
        return "%s (%s)" % (self.title, self.slug) 

    def save(self, *args, **kwargs):
        # Build path from parent page's path and slug
        current_path = self.path
        parent_page = self.page.parent
        
        slug = u'%s' % self.slug
        if not self.has_url_overwrite:
            self.path = u'%s' % slug
            if parent_page:
                parent_title = MenusTitle.objects.get_title(parent_page)
                if parent_title:
                    self.path = u'%s/%s' % (parent_title.path, slug)
        super(MenusTitle, self).save(*args, **kwargs)

    @property
    def overwrite_url(self):
        """Return overrwriten url, or None
        """
        if self.has_url_overwrite:
            return self.path
        return None
        

        
class EmptyMenusTitle(object):
    """Empty title object, can be returned from Page.get_title_obj() if required
    title object doesn't exists.
    """
    title = ""
    slug = ""
    path = ""
    meta_description = ""
    meta_keywords = ""
    redirect = ""
    has_url_overwite = False
    application_urls = ""
    menu_title = ""
    page_title = ""
    
    @property
    def overwrite_url(self):
        return None

