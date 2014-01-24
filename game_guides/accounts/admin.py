from django.contrib import admin
from models import Account

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'accounts'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (AccountInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# admin.site.register(Account)
