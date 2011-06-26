#-*- coding:utf-8 -*-
'''
Created on 2011-1-30

@author: 李昱
'''



XMLRPC_PINGBACK = [
    ('lincdm.xmlrpc.pingback.pingback_ping',
     'pingback.ping'),
    ('lincdm.xmlrpc.pingback.pingback_extensions_get_pingbacks',
     'pingback.extensions.getPingbacks')]

XMLRPC_METAWEBLOG = [
    ('lincdm.xmlrpc.metawelincdm.get_users_entrys',
     'entryger.getUsersBlogs'),
    ('lincdm.xmlrpc.metawelincdm.get_user_info',
     'entryger.getUserInfo'),
    ('lincdm.xmlrpc.metawelincdm.delete_post',
     'entryger.deletePost'),
    ('lincdm.xmlrpc.metawelincdm.get_authors',
     'wp.getAuthors'),
    ('lincdm.xmlrpc.metawelincdm.get_categories',
     'metaWelincdm.getCategories'),
    ('lincdm.xmlrpc.metawelincdm.new_category',
     'wp.newCategory'),
    ('lincdm.xmlrpc.metawelincdm.get_recent_posts',
     'metaWelincdm.getRecentPosts'),
    ('lincdm.xmlrpc.metawelincdm.get_post',
     'metaWelincdm.getPost'),
    ('lincdm.xmlrpc.metawelincdm.new_post',
     'metaWelincdm.newPost'),
    ('lincdm.xmlrpc.metawelincdm.edit_post',
     'metaWelincdm.editPost'),
    ('lincdm.xmlrpc.metawelincdm.new_media_object',
     'metaWelincdm.newMediaObject')]

XMLRPC_METHODS = XMLRPC_PINGBACK + XMLRPC_METAWEBLOG
