"""Applications hooks for blog.plugins"""
from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from app.blog.plugins.settings import APP_MENUS


class blogApphook(CMSApp):
    """blog's Apphook"""
    name = _('blog App Hook')
    urls = ['blog.urls']
    menus = APP_MENUS

apphook_pool.register(blogApphook)
