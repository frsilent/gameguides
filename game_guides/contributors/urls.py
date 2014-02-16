from django.conf.urls import patterns, url
from contributors.views import ContributorListView, ContributorDetailView

urlpatterns = patterns('contributors.views',
    url(r'^$', ContributorListView.as_view(), name='contributor-list'),
    url(r'^(?P<slug>[-_\w]+)/$', ContributorDetailView.as_view(), name='contributor-detail'),
)


# url(r'^item/(?P<item_id>\d+)/$',                        'edit_item',            name='core-edit_item'),
#     url(r'^(?P<section_id>\d+)/(?P<item_id>\d+)/$',         'edit_item',            name='core-edit_item'),
