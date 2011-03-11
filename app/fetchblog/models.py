from django.db import models
from datetime import datetime
# Create your models here.
class FeedsList(models.Model):
        author_name = models.CharField(max_length=15)
        title = models.CharField(default='', max_length=50)
        date = models.DateTimeField(auto_now_add=True)
        link = models.URLField()
        excerpt = models.TextField()
        feed_link = models.URLField()
        abconf = models.CharField(default='0', max_length=50)
        start_target = models.CharField(default='nohtml', max_length=300)
        mid_target = models.CharField(default='nohtml', max_length=300)
        end_target = models.CharField(default='nohtml', max_length=300)
        allow_target = models.CharField(default='nohtml', max_length=300)
        stop_target = models.CharField(default='nohtml', max_length=300)
        fetch_stat = models.IntegerField(default=0)
        content = models.TextField()

class FeedList(models.Model):
        name = models.CharField(default='alexliyu', max_length=20)
        feedurl = models.CharField(default='http://alexliyu.blog.163.com/rss', max_length=300)
        latest = models.CharField(default='first', max_length=300)
        last_retrieved = models.DateTimeField(default=datetime.today().fromtimestamp(0))
        acategory = models.CharField(default='douban', max_length=300)
        abconf = models.CharField(default='0', max_length=30)
        start_target = models.CharField(default='nohtml', max_length=300)
        allow_target = models.CharField(default='nohtml', max_length=300)
        mid_target = models.CharField(default='nohtml', max_length=300)
        end_target = models.CharField(default='nohtml', max_length=300)
        stop_target = models.CharField(default='nohtml', max_length=300)

class FeedSet(models.Model):
        defDate = models.IntegerField(default=3600)
        defStat = models.BooleanField(default=True)
        defDir = models.CharField(default='', max_length=300)
        last_checked = models.DateTimeField(default=datetime.today().fromtimestamp(0))
        stat = models.BooleanField(default=False)
        delitems = models.IntegerField(default=0)
        delitemi = models.IntegerField(default=0)
        chnitemi = models.IntegerField(default=0)
        entryerrs = models.IntegerField(default=0)
        entryerri = models.IntegerField(default=0)
        last_entry = models.DateTimeField()
        last_feedslist = models.IntegerField(default=0)
        check_db_num = models.IntegerField(default=50)
        fetch_db_num = models.IntegerField(default=50)
        imgchecked_num = models.IntegerField(default=0)
        last_imgchecked = models.DateTimeField()

class Tempimages(models.Model):
        oldurl = models.URLField()
        newurl = models.URLField()
        stat = models.IntegerField(default=0)
        greatdate = models.DateTimeField(auto_now_add=True)
        parsedate = models.DateTimeField()



