from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    """
    Extends Django's User model with additional fields unique to the site
    """
    class Meta:
        app_label = "accounts"

    user = models.OneToOneField(User)
    is_premium = models.BooleanField(default=False)
    steam_id   = models.CharField(max_length=16, default='', null=True, blank=True)
    summoner   = models.CharField(max_length=64, default='', null=True, blank=True)
    #TODO: FK to Forum account

    def __unicode__(self):
        return u'Profile of user: %s' % unicode(self.user.username)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Account.objects.create(user=instance)

        post_save.connect(create_user_profile, sender=Account)


# Outline: Inherit from the Django user model (django.contrib.auth.models.User)
# Game specific details? (Steamid, summoner name, etc)
# Bio 
# Some form of IP tracking (Text field, IPs added as a list if new.)
# Address, Address2, State/Province, City, Country, Zip
# Website??
# Postcount, for forums
# Followers (Many to one.)
# Referrer (FK to self)