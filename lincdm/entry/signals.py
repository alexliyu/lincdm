"""Signal handlers of Zinnia"""
import inspect
from functools import wraps

from django.db.models.signals import post_save

import settings


def disable_for_loaddata(signal_handler):
    """Decorator for disabling signals sent
    by 'post_save' on loaddata command.
    http://code.djangoproject.com/ticket/8399"""

    @wraps(signal_handler)
    def wrapper(*args, **kwargs):
        for fr in inspect.stack():
            if inspect.getmodulename(fr[1]) == 'loaddata':
                return
        signal_handler(*args, **kwargs)

    return wrapper




def disconnect_zinnia_signals():
    """Disconnect all the signals provided by Zinnia"""
    from zinnia.models import Entry

    post_save.disconnect(
        sender=Entry, dispatch_uid='zinnia.entry.post_save.ping_directories')
    post_save.disconnect(
        sender=Entry, dispatch_uid='zinnia.entry.post_save.ping_external_urls')
