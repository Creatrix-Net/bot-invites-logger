from django.urls import path

from .views import *

urlpatterns = [
    path("topgg/", topgg, name="Top.GG"),
    path("discordbotlist/", discordbotlist, name="Discord Bot List"),
    path("botsfordiscord/", botsfordiscord, name="Bots For Discord"),
    path("discordlistspace/", discordlistspace, name="Discordlist Space"),
    path("fateslist/", fateslist, name="Fates List"),
    # path("bladebotlist/", bladebotlist, name="Blade Bot List"),
    path("voidbots/", voidbots, name="Void Bots"),
    path("infinity/", infinity, name="Infinity"),
    path("discordlabs/", discordlabs, name="Discord Labs"),
    path("radarbotdirectory/", radarbotdirectory, name="Radar Bot Directory"),
    path("blist/", blist, name="Blist"),
    path("botlistme/", botlistme, name="Botlist Me"),
    path("motiondevelopment/", motiondevelopment, name="Motiondevelopment"),
    path("rovelstars/", rovel, name="Rovel Stars"),
    path("discordservices/", discordservices, name="Discord Services"),
    path("discordz/", discordz, name="Discordz"),
]
