from django.contrib import admin
from lincdm.app.fetchblog.admin.feedadmin import FeedAdmin
from lincdm.app.fetchblog.models import  FeedList, FeedSet, FeedsResult

admin.site.register(FeedList, FeedAdmin)
admin.site.register(FeedSet)
admin.site.register(FeedsResult)
