from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from game_guides.settings import base
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('cms.urls')),

    # url(r'^$', TemplateView.as_view(template_name='base.html')),

    url(r'^$', 'game_guides.views.home', name='home'),

    # Django App URLs:
    url(r'^accounts/', include('accounts.urls')),

    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if base.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': base.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
