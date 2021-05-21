from django.shortcuts import render
from django.views.decorators.http import require_GET
from .models import *
from django.http import HttpResponseNotAllowed
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
    except:
        return HttpResponseNotAllowed()
    