from django.conf.urls import patterns, url

from .views import GuideDetailView, guide_list

urlpatterns = patterns('guide.views',
   # TODO: guide-listing is a hack to avoid conflicting with django rest framework's register guide-list
    url(r'^$', guide_list, name='guide-listing'),
    url(r'^(?P<slug>[-_\w]+)/$', GuideDetailView.as_view(), name='guide-detail'),
)