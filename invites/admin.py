from django.contrib import admin
from django.contrib.auth.admin import Group
from .models import *

# Register your models here.
class InviteAdmin(admin.ModelAdmin):
    list_display = ('sitename','invites')

admin.site.register(ListingSite, InviteAdmin)
admin.site.unregister(Group)