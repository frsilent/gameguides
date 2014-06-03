from django.http import HttpResponse

from django.contrib.auth.models import Group
from rest_framework import viewsets, generics
from api.serializers import GuideSerializer


from guides.models import Guide

class GuideViewSet(viewsets.ModelViewSet):
    """
    API Endpoint to view a location
    """
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
