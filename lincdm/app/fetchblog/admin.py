'''
Created on 2011-3-10

@author: alex
'''

from django.contrib import admin
from app.fetchblog.models import  FeedList, FeedSet, FeedsList

admin.site.register(FeedList)
admin.site.register(FeedSet)
admin.site.register(FeedsList)
