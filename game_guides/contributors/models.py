from django.db import models
from accounts.models import UserProfile
from games.models import Game


# Create your models here.
class Contributor(models.Model):
    account = models.OneToOneField(UserProfile)
    game_played = models.ManyToManyField(Game)
    bio     = models.TextField(default='', blank=True)

    def __unicode__(self):
        return self.account
