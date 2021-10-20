from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from invites.views import *
from votes.views import message

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="Home"),
    path("message/", message, name="Message"),
    path("votes/", include("votes.urls")),
    url(r"^invite$", invite, name="INVITE RECORDER"),
]
