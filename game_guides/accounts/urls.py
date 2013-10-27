from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('accounts.views',
    url(r'^$', 'accounts',             name='accounts-dash'),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
)
