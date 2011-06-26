#-*- coding:utf-8 -*-
'''
Created on 2011-1-30

@author: 李昱
'''
from django.db import models
from datetime import datetime
from lincdm.entry.models import Category
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
        name = models.CharField(u'名称', default=u'李昱的博客', max_length=20)
        feedurl = models.CharField(u'rss订阅地址', default='http://alexliyu.blog.163.com/rss', max_length=300)
        latest = models.CharField(default='first', max_length=300)
        last_retrieved = models.DateTimeField(default=datetime.today().fromtimestamp(0))
        remotecategory = models.CharField(u'远程栏目', default='douban', max_length=300)
        remoteconf = models.CharField(u'远程配置', default='0', max_length=30)
        start_target = models.CharField(u'起始位置', default='nohtml', max_length=300)
        stop_target = models.CharField(u'结束位置', default='nohtml', max_length=300)
        allow_target = models.CharField(u'允许的标签', default='p i strong b u a h1 h2 h3 br img div embed span', max_length=300)
        mid_target = models.CharField(u'禁止的属性', default='ad1 ad2 href text/javascript st-related-posts h4 tags meta crinfo style randompost subscribe-af', max_length=300)
        end_target = models.CharField(u'允许的属性', default='src allowscriptaccess allowNetworking pluginspage width allowScriptAccess type wmode height quality invokeurls allownetworking invokeURLs', max_length=300)       
        category = models.ForeignKey(Category)
        
        def __unicode__(self):
            return self.name
        
        class Meta:
            verbose_name = u"采集列表"
            verbose_name_plural = u"采集列表"
            
        def testme(self):
            print self.name

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



