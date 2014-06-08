from django.db import models

from embed_video.fields import EmbedVideoField


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
    video = EmbedVideoField(blank=True)

    contributor = models.ForeignKey('contributors.Contributor')
    categories = models.ManyToManyField('categories.Category', related_name='categories')

    def suggested_videos(self):
        return Guide.objects.filter(category=self.category).order_by('hit_count')

    def __unicode__(self):
        return unicode(self.name)
