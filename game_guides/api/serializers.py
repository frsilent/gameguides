from rest_framework import serializers

from guides.models import Guide
from categories.models import Category


class GuideSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField('guide_categories')

    def guide_categories(self, guide):
        return guide.categories.values_list('id', flat=True)

    class Meta:
        model = Guide
        fields = ('id', 'name', 'categories')
        read_only_fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        read_only_fields = ('id', 'name')
