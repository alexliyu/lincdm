'''
Created on 2011-3-10

@author: alex
'''

from django.contrib import admin
from models import PushList, PushSet, PushsList
from pusharticle import Pusharticle

admin.site.register(PushList)
admin.site.register(PushSet)
admin.site.register(PushsList)
admin.site.app_name = 'push blog'
admin.site.register(Pusharticle)

