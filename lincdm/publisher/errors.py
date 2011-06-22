#-*- coding:utf-8 -*-
'''
Created on 2011-6-22

@author: alex
'''
class PublisherCantPublish(Exception):
    """Publisher can not publish instance, because there is something wrong"""

class MpttPublisherCantPublish(PublisherCantPublish):
    """Node is under mptt and can't be published because node parent isn't
    published."""
