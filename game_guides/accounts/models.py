from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Account(models.Model):
    """
    Extends Django's User model with additional fields unique to the site
    """
    class Meta:
        app_label = "accounts"

    user = models.OneToOneField(User, unique=True)
    is_premium = models.BooleanField(default=False)
    steam_id = models.CharField(max_length=16, default='', null=True, blank=True)
    summoner = models.CharField(max_length=64, default='', null=True, blank=True)
    picture = models.ImageField(upload_to='account_images/', default='account_images/None/no-image.jpg', blank=True, null=True)

    #TODO: FK to Forum account

    def __unicode__(self):
        return u'Profile of user: %s' % unicode(self.user.username)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Account.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                p = Account.objects.get(user=self.user)
                self.pk = p.pk
            except Account.DoesNotExist:
                pass
        super(Account, self).save(*args, **kwargs)
