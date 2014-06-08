from django.contrib.auth.models import Group

from rest_framework import serializers

from guides.models import Guide


class GuideSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField('guide_categories')

    def guide_categories(self, guide):
        return guide.categories.values_list('id')

    class Meta:
        model = Guide
        fields = ('id', 'name', 'categories')
        read_only_fields = ('id', 'name')
