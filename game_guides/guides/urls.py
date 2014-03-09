from django.conf.urls import patterns, url
from guides.views import GuideListView, GuideDetailView, guide_list, TestListView

urlpatterns = patterns('guide.views',
    url(r'^$', guide_list, name='guide-list'),
    # url(r'^$', GuideListView.as_view(), name='guide-list'),
    url(r'^(?P<slug>[-_\w]+)/$', GuideDetailView.as_view(), name='guide-detail'),
    # url(r'^test$', TestListView.as_view(), name='test-list'),
)