from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'game_guides.views.index', name='index'),

    # # Django App URLs:
    url(r'^accounts/', include('accounts.urls')),
    url(r'^contributors/', include('contributors.urls')),
    url(r'^guides/', include('guides.urls')),
    url(r'^lessons/', include('lessons.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),

    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
