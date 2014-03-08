from django.db import models
from games.models import Game
from django.conf import settings

from guides.models import Guide

class Contributor(models.Model):
    """
    Relates back to a user account but is used to define authorship of guides.
    Will be used to find guides by author, hold a global ranking maybe, etc
    """
    class Meta:
        app_label = "contributors"

    account = models.ForeignKey('accounts.Account')
    bio     = models.CharField(max_length=2048, default='', blank=True)

    def get_guides(self):
        guides = Guide.objects.filter(contributor = self.id)
        return guides

    def __unicode__(self):
        return unicode(self.account)
