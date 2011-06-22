#-*- coding:utf-8 -*-
'''
Created on 2011-6-22

@author: alex
'''
from django.db.models.query import QuerySet

class PublisherQuerySet(QuerySet):
    """Added publisher specific filters to queryset.
    """
    def drafts(self):
        return self.filter(publisher_is_draft=True)
    
    def public(self):
        return self.filter(publisher_is_draft=False)
