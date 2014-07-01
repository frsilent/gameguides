from django.conf.urls import patterns, url, include

from accounts.views import Login, Logout


urlpatterns = patterns('accounts.views',
    url(r'^$', 'accounts', name='accounts-dashboard'),


    # Django Defaults

    url(r'^login/$', Login),
    url(r'^logout/$', Logout),
)
