from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from cms.sitemaps import CMSSitemap
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('lincdm.grappelli.urls')),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^', include('cms.urls')),
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}}) 
)
urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
        url(r'^media/(?P<path>.*)$', 'serve'),
        )

if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),
    ) + urlpatterns
