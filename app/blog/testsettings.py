"""Settings for testing blog"""
import os
from app.blog.xmlrpc import blog_XMLRPC_METHODS

DATABASES = {'default': {'NAME': 'blog_tests.db',
                         'ENGINE': 'django.db.backends.sqlite3'}}

SITE_ID = 1

ROOT_URLCONF = 'blog.tests.urls'

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.core.context_processors.request',
    'blog.context_processors.media',
    'blog.context_processors.version']

TEMPLATE_DIRS = [os.path.join(os.path.dirname(__file__),
                              'tests', 'templates')]

INSTALLED_APPS = ['django.contrib.contenttypes',
                  'django.contrib.comments',
                  'django.contrib.sessions',
                  'django.contrib.sites',
                  'django.contrib.admin',
                  'django.contrib.auth',
                  'django_xmlrpc',
                  'mptt', 'tagging', 'blog']

blog_PAGINATION = 3

XMLRPC_METHODS = blog_XMLRPC_METHODS
