from django.conf.urls import patterns, url

urlpatterns = patterns('contributors.views',
    url(r'^$', 'contributors', name='contributors-listing'),
)
