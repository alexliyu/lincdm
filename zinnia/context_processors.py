"""Context Processors for Zinnia"""
from lincdm import __version__
from zinnia.settings import MEDIA_URL, LINCDM_NAME, LINCDM_TITLE


def media(request):
    """Adds media-related context variables to the context"""
    return {'ZINNIA_MEDIA_URL': MEDIA_URL}


def version(request):
    """Adds version of blog to the context"""
    return {'LINCDM_VERSION': __version__}

def sitename(request):
    return {'LINCDM_NAME':LINCDM_NAME}

def sitetitle(request):
    return {'LINCDM_TITLE':LINCDM_TITLE}
