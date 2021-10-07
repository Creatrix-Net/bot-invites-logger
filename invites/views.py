from django.conf import settings
from django.db.models import F
from django.http import (HttpResponse, HttpResponseNotAllowed,
                         HttpResponsePermanentRedirect)
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET
from asgiref.sync import sync_to_async

from .models import *


@sync_to_async
@require_GET
def invite(request):
    try:
        password, sitename = request.GET['state'].split('/')
        if password != settings.PASSWORD:
            return HttpResponseNotAllowed(['GET','POST'])
    except:
        return HttpResponseNotAllowed(['GET','POST'])
    if request.GET.get('code') or sitename.lower() == 'Direct From Bot'.lower():
        try:   
            ListingSite.objects.filter(sitename=sitename).update(
                    invites = F('invites')+1
        )
            a=ListingSite.objects.filter(sitename=sitename).get().url
            if a != '' or a != None:
                return HttpResponsePermanentRedirect(a)
            else:
                return HttpResponsePermanentRedirect(settings.WEBSITE)
        except:
            site_listing = ListingSite(sitename=sitename, invites=1)
            site_listing.save()
            return HttpResponsePermanentRedirect(settings.WEBSITE)
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@sync_to_async
@require_GET
def home(request):
    a=ListingSite.objects.iterator()
    l1=[['Listing Sites', 'No of Invites'],]
    l = [[i.sitename,i.invites] for i in a]
    l1.extend(l)
    return render(
        request,
        'index.html',
        {
            'invite':l1,
        }
    )

