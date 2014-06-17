from rest_framework import viewsets
from api.serializers import GuideSerializer, CategorySerializer


from guides.models import Guide
from categories.models import Category

class GuideViewSet(viewsets.ModelViewSet):
    """
    API Endpoint to view all guides
    """
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API Endpoint to view all categories
    """
    queryset = Category.objects.get(id=1).get_descendants().filter(level=2)
    serializer_class = CategorySerializer
