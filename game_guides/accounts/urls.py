from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('accounts.views',
    url(r'^$', 'accounts', name='accounts-dashboard'),


    # Django Defaults
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}),
)
