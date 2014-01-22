from django.db import models

class Category(models.Model):
    """
    Object to relate a game to various filters.
    IE for Counter-strike "Map" would be a category with possible values of "dust2, inferno, cache"
    League could have a category labeled "Role" with possible values of "jungle, adc, support"
    """
    class Meta:
        app_label = "categories"

    game = models.ForeignKey('games.Game')
    name = models.TextField(default='', null=True, blank=True)

    def __unicode__(self):
        return '%s %s' % (self.game,self.name)
