from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from models import Guide


class GuideAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Guide, GuideAdmin)
