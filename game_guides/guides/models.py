from django.db import models

class Guide(models.Model):
    """
    All pertinent information for a guide to include the link for the appropriate Vimeo video, any comment text, the contributor of the video, etc
    """
    class Meta:
        app_label = "guides"

    name = models.TextField(default='', null=True, blank=True)
    contributor = models.ForeignKey('contributors.Contributor')
    # game = models.ForeignKey('Game')

    def __unicode__(self):
        return self.name
