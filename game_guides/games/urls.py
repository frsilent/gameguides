from django.conf.urls import patterns, url
# from guides.views import GuideListView

urlpatterns = patterns('guides.views',
    url(r'^$', 'guides', name='guides-listing'),
    # url(r'^$', GuideListView.as_view(), name='guide-list'),
)
