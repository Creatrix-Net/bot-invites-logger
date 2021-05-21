from django.shortcuts import render
from django.views.decorators.http import require_GET
from .models import *
from django.http import HttpResponseNotAllowed, HttpResponse, HttpResponsePermanentRedirect
from django.conf import settings
from django.db.models import F

# Create your views here.
@require_GET
def invite(request):
    try:
        sitename = request.GET['sitename']
        password = request.GET['password']
        
        if password != settings.PASSWORD:
            return HttpResponseNotAllowed()
        
        ListingSite.objects.update_or_create(
            sitename=sitename.capitalize(),
            invites = F('invites')+1
        )
        a=ListingSite.objects.filter(sitename=sitename).get()['url']
        if a != '' or a != None:
            return HttpResponsePermanentRedirect(a)
        else:
            return HttpResponsePermanentRedirect('https://github.com/The-4th-Hokage')
    except:
        return HttpResponseNotAllowed()
    