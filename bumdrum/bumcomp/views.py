from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import django.template
import msd_api.api

def index(request):
#    tmplt_2bums = django.template.loader.get_template('bumcomp/twobums.html')
#    return HttpResponse(tmplt_2bums.render({}, request))
    staticpg = open("bumcomp/templates/bumcomp/twobums.html").read()

    return HttpResponse(staticpg)

# Create your views here.


def boxscore(request, away='blank', home='blank',  date=0):
    t = django.template.loader.get_template('bumcomp/boxscore.html')
    context = { 'home' : home,
                'away' : away,
                'date' : msd_api.api.talkback()
    }
    return HttpResponse(t.render(context, request))

def pbp_json(request, away='blank', home='blank',  date=0):
     payload = msd_api.api.playbyplay(away, home, date)
     return JsonResponse(payload)

        
