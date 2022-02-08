from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path

from invites.views import *
from votes.views import message

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="Home"),
    path("message/", message, name="Message"),
    path("votes/", include("votes.urls")),
    re_path(r"^invite$", invite, name="INVITE RECORDER"),
]
