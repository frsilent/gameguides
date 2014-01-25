from django.db import models
from games.models import Game
from django.conf import settings

class Contributor(models.Model):
    """
    Relates back to a user account but is used to define authorship of guides.
    Will be used to find guides by author, hold a global ranking maybe, etc
    """
    class Meta:
        app_label = "contributors"

    account = models.ForeignKey('accounts.Account') # Think this should exist but Joe says no. If removed a lot of these things will need to be ported over to User account
    # games_played = models.ManyToManyField('games.Game')
    bio     = models.CharField(max_length=2048, default='', blank=True)

    def __unicode__(self):
        return unicode(self.account)
