from django.db import models
from accounts.models import UserProfile
from games.models import Game

class Contributor(models.Model):
    """
    Relates back to a user account but is used to define authorship of guides.
    Will be used to find guides by author, hold a global ranking maybe, etc
    """
    class Meta:
        app_label = "contributors"

    account = models.OneToOneField(UserProfile)
    games_played = models.ManyToManyField('games.Game')
    bio     = models.TextField(default='', blank=True)

    def __unicode__(self):
        return self.account
