from django.contrib import admin, messages
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import Group
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext

from .models import *


@admin.register(ListingSite)
class InviteAdmin(admin.ModelAdmin):
    list_display = search_fields = ("sitename", "invites")
    list_per_page = 100

    def reset_invite(self, request, queryset):
        queryset.update(invites=0)

        self.message_user(
            request,
            ngettext(
                "%d invite was successfully reset.",
                "%d invites were successfully reset.",
                len(queryset),
            ) % int(len(queryset)),
            messages.SUCCESS,
        )

    reset_invite.short_description = ("Reset Invites")

    actions = [reset_invite]


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    def delete_admin_logs(self, request, queryset):
        queryset.delete()

        self.message_user(
            request,
            ngettext(
                "%d log was successfully deleted.",
                "%d logs were successfully deleted.",
                len(queryset),
            ) % int(len(queryset)),
            messages.SUCCESS,
        )

    delete_admin_logs.short_description = (
        "Delete the selected ADMIN Logs without sticking")

    actions = [delete_admin_logs]


admin.site.unregister(Group)

admin.site.site_header = (
    admin.site.site_title
) = admin.site.index_title = "Minato Namikaze | Invite Stats"
