#-*- coding:utf-8 -*-
'''
Created on 2011-6-23

@author: alex
'''
from django.contrib import admin
from lincdm.menus.models import MenusTitle


class MenusAdmin(admin.ModelAdmin):
    pass


admin.site.register(MenusTitle, MenusAdmin)



