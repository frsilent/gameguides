from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.TextField(default='', null=True, blank=True)
    official_site = models.URLField(default='', null=True, blank=True)

    def __unicode__(self):
        return self.name
