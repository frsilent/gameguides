from django.db import models

class Game(models.Model):
    """
    Class for the game context of the site. Will initially only have "Counter-Strike" instance but
    will be expanded to League of Legends & other games when content makers are found.
    """
    class Meta:
        app_label = "games"
    
    name = models.CharField(max_length=128, default='', null=True, blank=True)
    official_site = models.URLField(default='', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.name)
