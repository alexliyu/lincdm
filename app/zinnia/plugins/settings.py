"""Settings of Zinnia.plugins"""
from django.conf import settings

HIDE_ENTRY_MENU = getattr(settings, 'ZINNIA_HIDE_ENTRY_MENU', True)

PLUGINS_TEMPLATES = getattr(settings, 'ZINNIA_PLUGINS_TEMPLATES', [])
try:
    from app.zinnia.plugins.menu import EntryMenu
    from app.zinnia.plugins.menu import TagMenu
    from app.zinnia.plugins.menu import AuthorMenu
    from app.zinnia.plugins.menu import CategoryMenu

    APP_MENUS = getattr(settings, 'ZINNIA_APP_MENUS', [EntryMenu, CategoryMenu,
                                                       TagMenu, AuthorMenu])
except ImportError:
    APP_MENUS = []
