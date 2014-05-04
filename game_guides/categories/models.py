from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """
    Generic object for categorizing Guides. The Root nodes are the individual Game identifiers
    """
    class Meta:
        app_label = "categories"

    class MPTTMeta:
        order_insertion_by = ['name']

    name = models.CharField(max_length=50, unique=True)
    thumb = models.ImageField(upload_to='category_images/',
                              default='category_images/None/no-image.jpg', blank=True, null=True)
    game = models.ForeignKey('games.Game', null=True, blank=True,
                             help_text='This is field is necessary for Root Nodes but no others.')

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def __unicode__(self):
        name = self.name
        if self.level > 0:
            for parent in self.get_ancestors()[::-1]:
                name = parent.name + ' >> ' + name
        return name
