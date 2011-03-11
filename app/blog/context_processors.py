"""Context Processors for blog"""
from app.blog import __version__
from app.blog.settings import MEDIA_URL
from lincdm.settings import LINCDM_NAME, LINCDM_TITLE
def media(request):
    """Adds media-related context variables to the context"""
    return {'blog_MEDIA_URL': MEDIA_URL}


def version(request):
    """Adds version of blog to the context"""
    return {'LINCDM_VERSION': __version__}

def sitename(request):
    return {'LINCDM_NAME':LINCDM_NAME}

def sitetitle(request):
    return {'LINCDM_TITLE':LINCDM_TITLE}
