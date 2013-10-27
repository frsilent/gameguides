from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Extends Django's User model with additional fields
    """
    user = models.OneToOneField(User)
    
    is_premium = models.BooleanField(default=False)

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

        post_save.connect(create_user_profile, sender=User)
