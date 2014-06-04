from django.contrib.auth.models import Group

from rest_framework import serializers

from guides.models import Guide


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ('id', 'name', 'category')
        read_only_fields = ('id', 'name', 'category')
