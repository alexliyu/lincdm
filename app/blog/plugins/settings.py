"""Settings of blog.plugins"""
from django.conf import settings

HIDE_ENTRY_MENU = getattr(settings, 'blog_HIDE_ENTRY_MENU', True)

PLUGINS_TEMPLATES = getattr(settings, 'blog_PLUGINS_TEMPLATES', [])
try:
    from app.blog.plugins.menu import EntryMenu
    from app.blog.plugins.menu import TagMenu
    from app.blog.plugins.menu import AuthorMenu
    from app.blog.plugins.menu import CategoryMenu

    APP_MENUS = getattr(settings, 'blog_APP_MENUS', [EntryMenu, CategoryMenu,
                                                       TagMenu, AuthorMenu])
except ImportError:
    APP_MENUS = []
