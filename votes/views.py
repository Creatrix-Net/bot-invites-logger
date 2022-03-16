import ast
import json

from asgiref.sync import sync_to_async
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_POST

from .utils import message_me


@sync_to_async
def message(request):
    if settings.LOCAL:
        message_me(settings.DISCORD_ID, "LOCAL")
        return HttpResponse("Thanks")
    else:
        return HttpResponseNotAllowed(["GET", "POST"])


@sync_to_async
@require_POST
def topgg(request):
    if (
        request.META["HTTP_AUTHORIZATION"] or 
        request.headers.get("Authorization") == settings.PASSWORD
    ):
        userid = json.loads(request.body.decode("utf-8")).get("user")
        message_me(int(userid), "Top.GG")
        return HttpResponse("Thanks")
    else:
        return HttpResponseNotAllowed(["GET", "POST"])


@sync_to_async
def discordbotlist(request):
    if (
        request.META.get("HTTP_AUTHORIZATION") or 
        request.headers.get("Authorization") == settings.PASSWORD
    ):
        userid = json.loads(request.body.decode("utf-8")).get("id")
        message_me(int(userid), "Discord Bot List")
        return HttpResponse("Thanks")
    else:
        return HttpResponseNotAllowed(["GET", "POST"])


@sync_to_async
@require_POST
def botsfordiscord(request):
    if (
        request.META["HTTP_AUTHORIZATION"] or 
        request.headers.get("Authorization") == settings.PASSWORD
    ):
        userid = request.POST.get("user") or ast.literal_eval(
            request.body.decode("utf-8")).get("user")
        message_me(int(userid), "Bots For Discord")
        return HttpResponse("Thanks")
    else:
        return HttpResponseNotAllowed(["GET", "POST"])


@sync_to_async
@require_POST
def discordlistspace(request):
    if (
        request.META["HTTP_AUTHORIZATION"] or 
        request.headers.get("Authorization") == settings.TOKEN
    ):
        userid = json.loads(request.body.decode("utf-8")).get("user").get("id")
        message_me(int(userid), "Discordlist Space")
        return HttpResponse("Thanks")
    else:
        return HttpResponseNotAllowed(["GET", "POST"])


@sync_to_async
@require_POST
def fateslist(request):
    if (
        request.META["HTTP_AUTHORIZATION"] or 
        request.headers.get("Authorization") == settings.PASSWORD
    ):
        userid = json.loads(request.body.decode("utf-8")).get("id")
        message_me(int(userid), "Fates List")
        return HttpResponse("Thanks")
    else:
        return HttpResponseNotAllowed(["GET", "POST"])


# @sync_to_async
# @require_POST
# def bladebotlist(request):
#     if (request.META.get("HTTP_AUTHORIZATION")
#             or request.headers.get("Authorization")
#             or request.headers.get("Password")
#             or request.headers.get("password") == settings.PASSWORD):
#         try:
#             userid = (
#                 request.POST.get("userid") or 
#                 ast.literal_eval(request.body.decode("utf-8")).get("userid")
#             )
#         except:
#             userid = json.loads(request.body.decode("utf-8")).get("userid")
#         message_me(int(userid), "Blade Bot List")
#         return HttpResponse("Thanks")
#     else:
#         return HttpResponseNotAllowed(["GET", "POST"])


@sync_to_async
@require_POST
def voidbots(request):
    if (
        request.META["HTTP_AUTHORIZATION"] or 
        request.headers.get("Authorization") == settings.PASSWORD
    ):
        userid = (
            request.POST.get("user") or 
            ast.literal_eval(request.body.decode("utf-8")).get("user")
        )
        message_me(int(userid), "Void Bots")
        return HttpResponse("Thanks")
    else:
        return HttpResponseNotAllowed(["GET", "POST"])


@sync_to_async
@require_POST
def infinity(request):
    if (
        request.META["HTTP_AUTHORIZATION"] or 
        request.headers.get("Authorization") == settings.PASSWORD
    ):
        userid = (request.POST.get("userID") or ast.literal_eval(
            request.body.decode("utf-8")).get("userID")
            or json.loads(request.body.decode("utf-8")).get("userID"))
        message_me(int(userid), "Infinity")
        return HttpResponse("Thanks")
    else:
        return HttpResponseNotAllowed(["GET", "POST"])


@sync_to_async
@require_POST
def discordlabs(request):
    if (
        request.META["HTTP_AUTHORIZATION"] or 
        request.headers.get("Authorization") == settings.PASSWORD
    ):
        userid = (
            request.POST.get("uid") or 
            ast.literal_eval(request.body.decode("utf-8")).get("uid") or 
            json.loads(request.body.decode("utf-8")).get("uid")
        )
        message_me(int(userid), "Discord Labs")
        return HttpResponse("Thanks")
    else:
        return HttpResponseNotAllowed(["GET", "POST"])


@sync_to_async
@require_POST
def radarbotdirectory(request):
    userid = (
        request.POST.get("user") or 
        ast.literal_eval(request.body.decode("utf-8")).get("user") or 
        json.loads(request.body.decode("utf-8")).get("user")
    )
    message_me(int(userid), "Radar Bot Directory")
    return HttpResponse("Thanks")


@sync_to_async
@require_POST
def blist(request):
    print(request.POST)
    userid = (
        request.POST.get("user") or 
        ast.literal_eval(request.body.decode("utf-8")).get("user") or 
        json.loads(request.body.decode("utf-8")).get("user")
    )
    message_me(int(userid), "Blist")
    return HttpResponse("Thanks")

@sync_to_async
@require_POST
def botlistme(request):
    print(request.POST)
    userid = (
        request.POST.get("user") or 
        ast.literal_eval(request.body.decode("utf-8")).get("user") or 
        json.loads(request.body.decode("utf-8")).get("user")
    )
    message_me(int(userid), "Blist")
    return HttpResponse("Thanks")
