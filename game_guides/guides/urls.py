from django.conf.urls import patterns, url
from guides.views import GuideListView, GuideDetailView

urlpatterns = patterns('guide.views',
    url(r'^$', GuideListView.as_view(), name='guide-list'),
    url(r'^(?P<slug>[-_\w]+)/$', GuideDetailView.as_view(), name='guide-detail'),
)