from django.conf.urls import patterns, url

from .views import GuideDetailView, guide_list

urlpatterns = patterns('guide.views',
    url(r'^$', guide_list, name='guide-list'),
    url(r'^(?P<slug>[-_\w]+)/$', GuideDetailView.as_view(), name='guide-detail'),
)