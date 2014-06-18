from rest_framework import serializers

from embed_video.backends import detect_backend

from guides.models import Guide
from categories.models import Category


class GuideSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField('guide_categories')
    thumb = serializers.SerializerMethodField('guide_video_thumbnail')

    def guide_categories(self, guide):
        return guide.categories.values_list('id', flat=True)

    def guide_video_thumbnail(self, guide):
        video = detect_backend(guide.video)  # TODO: Need to cache this. Costly query to vimeo's api
        # '100x75.jpg' '200x150.jpg' possible thumbnail sizing

        thumb_string = video.get_thumbnail_url()[:-7] + '100x75.jpg'
        return thumb_string

    class Meta:
        model = Guide
        fields = ('id', 'name', 'categories', 'thumb')
        read_only_fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        read_only_fields = ('id', 'name')
