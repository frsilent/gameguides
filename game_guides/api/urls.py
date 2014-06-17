from django.conf.urls import patterns, include, url

from rest_framework import viewsets, routers

# from guides.models import Guide
from api.views import GuideViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'guides', GuideViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
