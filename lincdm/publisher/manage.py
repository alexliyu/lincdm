#-*- coding:utf-8 -*-
'''
Created on 2011-6-22

@author: alex
'''

from django.db import models
from lincdm.publisher.query import PublisherQuerySet

class PublisherManager(models.Manager):
    """Manager with some support handling publisher.
    """
    def get_query_set(self):
        """Change standard model queryset to our own.
        """
        return PublisherQuerySet(self.model)
    
    def drafts(self):
        return self.filter(publisher_is_draft=True)
    
    def public(self):
        return self.filter(publisher_is_draft=False)
    
    """
    def all(self):
        raise NotImplementedError, ("Calling all() on manager of publisher "
            "object is not allowed. Please use drafts() or public() method "
            "instead. If this isn't accident use get_query_set().all() for " 
            "all instances.")
    """
