from django.db import models

from embed_video.fields import EmbedVideoField
import django_filters

from categories.models import Category


class Guide(models.Model):
    """
    All pertinent information for a guide to include the link for the appropriate Vimeo video,
    any comment text, the contributor of the video, etc
    """
    class Meta:
        app_label = "guides"

    name = models.CharField(max_length=128, default='', blank=True)
    description = models.CharField(max_length=2048)
    hit_count = models.IntegerField(default=0)
    video = EmbedVideoField(blank=True) # Need to make this not required

    contributor = models.ForeignKey('contributors.Contributor')
    category = models.ForeignKey('categories.Category')

    def suggested_videos(self):
        return Guide.objects.filter(category=self.category).order_by('hit_count')

    def __unicode__(self):
        return unicode(self.name)


class GuideFilter(django_filters.FilterSet):
    """
    Class to handle filtering for guides
    """
    class Meta:
        model = Guide
        fields = ['category']


    cs = Category.objects.get(name="Counter-Strike")
    category = django_filters.ModelChoiceFilter(queryset=cs.get_descendants().filter(level=2))

    def get_category(self):
        cs = Category.objects.get(name="Counter-Strike")
        return cs.get_descendants().filter(level=2)
