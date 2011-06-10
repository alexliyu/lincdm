#-*- coding:utf-8 -*-
'''
Created on 2011-1-30

@author: 李昱
'''
import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG
gettext = lambda s: s
COPYRIGHT = '33445120.Tk'
LINCDM_NAME = 'LinCDM'
LINCDM_TITLE = u'基于Django的开源博客' 
GRAPPELLI_ADMIN_TITLE = LINCDM_NAME

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
LANGUAGES = [
    ('zh-cn', gettext('Chinese')),
]
DEFAULT_LANGUAGE = 0
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_DIR, 'mycms.db'), # Or path to database file if using sqlite3.
        'USER': '', # Not used with sqlite3.
        'PASSWORD': '', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%s8gaa9$7t_r*o!w_l57#no+pp0&y0t&y=(g+(3uq=wk+=kwc-'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'zinnia.context_processors.media',
    'zinnia.context_processors.version',
    'zinnia.context_processors.sitename',
    'zinnia.context_processors.sitetitle',
)

CMS_TEMPLATES = (
    ('example.html', 'Example Template'),
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    
)
INTERNAL_IPS = ('127.0.0.1',)
ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	os.path.join(PROJECT_DIR, 'templates'),
)

# Should pages be allowed to inherit their parent templates?
CMS_TEMPLATE_INHERITANCE = True
# This is just a STATIC GLOBAL VAR
CMS_TEMPLATE_INHERITANCE_MAGIC = 'INHERIT'

CMS_PLACEHOLDER_CONF = {}

# Whether to enable permissions.
CMS_PERMISSION = False

# Decides if pages without any view restrictions are public by default, or staff only
CMS_PUBLIC_FOR = 'all' # or 'staff'
MENU_CACHE_DURATION = 3600
CMS_CONTENT_CACHE_DURATION = 60
CMS_CACHE_DURATIONS = {
     # Menu cache duration
    'menus': MENU_CACHE_DURATION,
    # Defines how long page content should be cached
    'content': CMS_CONTENT_CACHE_DURATION,
    # Defines how long user permissions should be cached
    'permissions': 60 * 60,
}

# Show the publication date field in the admin, allows for future dating
# Changing this from True to False could cause some weirdness.  If that is required,
# you should update your database to correct any future dated pages
CMS_SHOW_START_DATE = False

# Show the publication end date field in the admin, allows for page expiration
# Changing this from True to False could cause some weirdness.  If that is required,
# you should update your database and null any pages with publication_end_date set.
CMS_SHOW_END_DATE = False

# Whether the user can overwrite the url of a page
CMS_URL_OVERWRITE = True

# Allow to overwrite the menu title
CMS_MENU_TITLE_OVERWRITE = False

# Are redirects activated?
CMS_REDIRECTS = False

# Allow the description, title and keywords meta tags to be edited from the
# admin
CMS_SEO_FIELDS = False 

# a tuple of python path to AppHook Classes. Overwrites the auto-discovered apphooks.
CMS_APPHOOKS = ()  

#Should the tree of the pages be also be displayed in the urls? or should a flat slug structure be used?
CMS_FLAT_URLS = False

# Wheter the cms has a softroot functionionality
CMS_SOFTROOT = False

#Hide untranslated Pages
CMS_HIDE_UNTRANSLATED = True

#Fall back to another language if the requested page isn't available in the preferred language
CMS_LANGUAGE_FALLBACK = True

#Configuration on how to order the fallbacks for languages.
# example: {'de': ['en', 'fr'],
#           'en': ['de'],
#          }
CMS_LANGUAGE_CONF = {}

# Defines which languages should be offered.
CMS_LANGUAGES = LANGUAGES

# If you have different sites with different languages you can configure them here
# and you will only be able to edit the languages that are actually on the site.
# example: {1:['en','de'],
#           2:['en','fr'],
#           3:['en'],}
CMS_SITE_LANGUAGES = LANGUAGES

CMS_SITE_CHOICES_CACHE_KEY = 'CMS:site_choices'
CMS_PAGE_CHOICES_CACHE_KEY = 'CMS:page_choices'

# Languages that are visible in the frontend (Language Chooser)
CMS_FRONTEND_LANGUAGES = [x[0] for x in CMS_LANGUAGES]


# Path for CMS media (uses <MEDIA_ROOT>/cms by default)
CMS_MEDIA_PATH = 'cms/'
CMS_MEDIA_ROOT = os.path.join(MEDIA_ROOT, CMS_MEDIA_PATH)
CMS_MEDIA_URL = os.path.join(MEDIA_URL, CMS_MEDIA_PATH)

# Path (relative to MEDIA_ROOT/MEDIA_URL) to directory for storing page-scope files.
CMS_PAGE_MEDIA_PATH = 'cms_page_media/'

CMS_MODERATOR = False 

# Defines what character will be used for the __unicode__ handling of cms pages
CMS_TITLE_CHARACTER = '+'

# Enable non-cms placeholder frontend editing
PLACEHOLDER_FRONTEND_EDITING = True

# Cache prefix so one can deploy several sites on one cache server
CMS_CACHE_PREFIX = 'cms-'

# they are missing in the permission-merge2 branch
CMS_PLUGIN_PROCESSORS = tuple()
CMS_PLUGIN_CONTEXT_PROCESSORS = tuple()
ZINNIA_ENTRY_BASE_MODEL = 'zinnia.plugins.placeholder.EntryPlaceholder'
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'debug_toolbar',
    'cms',
    'menus',
    'mptt',
    'appmedia',
    'south',
    'sekizai',
    'zinnia',
    'tagging',
    'zinnia.plugins',
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cms.plugins.snippet',
    'cms.plugins.teaser',
    'cms.plugins.text',
    'cms.plugins.video',
    'cms.plugins.twitter',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
#    'filters': {
#        'special': {
#            '()': 'project.logging.SpecialFilter',
#            'foo': 'bar',
#        }
#    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
#            'filters': ['special']
        }
    },
    'loggers': {
        'django': {
            'handlers':['null'],
            'propagate': True,
            'level':'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
#        'myproject.custom': {
#            'handlers': ['console', 'mail_admins'],
#            'level': 'INFO',
#            'filters': ['special']
#        }
    }
}
