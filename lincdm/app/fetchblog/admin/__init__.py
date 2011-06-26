from django.contrib import admin
from lincdm.app.fetchblog.admin.entry import FeedAdmin
from lincdm.app.fetchblog.models import  FeedList, FeedSet, FeedsList

admin.site.register(FeedList, FeedAdmin)
admin.site.register(FeedSet)
admin.site.register(FeedsList)
