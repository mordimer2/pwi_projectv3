from django.shortcuts import render
from .models import Job, Experience, Education, Workflows, Skills 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

import json
# Create your views here.
def homepage(request, lang="en"):
    data = None
    fil2O = "./jobs/static/lang/en.json"
    if 'lang' in request.COOKIES:
        lang=request.COOKIES['lang']
        print(lang)

    if (lang=='pl'): fil2O ="./jobs/static/lang/pl.json"
    
    with open(fil2O ,"r", encoding="UTF-8") as fil:
        data=json.load(fil)
    exp=Experience.objects.filter(language=lang).order_by('-start_date')

    edu=Education.objects.filter(language=lang).order_by('-start_date')

    skillss=Skills.objects

    workflows=Workflows.objects.filter(language=lang)

    return render(request, "jobs/home.html", {'exp': exp, 
                                            'edu': edu,
                                            'skillss': skillss,
                                            'workflows': workflows,
                                            'cookieTitle':data['cookieTitle'],
                                            'cookieDesc':data['cookieDesc'],
                                            'cookieBtn':data['cookieBtn'],
                                            'title': data['title'],
                                            'shortDesc': data['shortDesc'],
                                            'sidebar': data['sidebar'],
                                            'skills': data['skills'],
                                            'int1': data['interests1'],
                                            'int2': data['interests2'],
                                            'lang': lang,
                                            'code': data['code']
                                            })

def index(request):
    request.session.set_test_cookie()
    return homepage(request)

def language(request):
    lng=request.POST.get('lng','')
    response=HttpResponseRedirect("/")
    response.set_cookie('lang', lng)
    return response