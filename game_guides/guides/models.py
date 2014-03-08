from django.db import models

from embed_video.fields import EmbedVideoField
import django_filters

class Guide(models.Model):
    """
    All pertinent information for a guide to include the link for the appropriate Vimeo video, any comment text, the contributor of the video, etc
    """
    class Meta:
        app_label = "guides"

    name = models.CharField(max_length=128, default='', null=True, blank=True)
    description = models.CharField(max_length=2048)
    video = EmbedVideoField(blank=True) # Need to make this not required

    contributor = models.ForeignKey('contributors.Contributor')
    category = models.ForeignKey('categories.Category')

    def __unicode__(self):
        return unicode(self.name)

# class GuideFilter(django_filters.FilterSet):
#     """
#     Class to handle filtering for guides
#     """
#     class Meta:
#         model = Guide

#     def __init__(self, *args, **kwargs):
#         super(GuideFilter, self).__init__(*args, **kwargs)
#         self.filters['category'].extra.update({'empty_label': 'All Categorys'})
