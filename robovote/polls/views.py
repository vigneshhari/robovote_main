from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Team, Backer
from django.contrib.sessions.backends.db import SessionStore
import datetime

def index(request):
    teams = Team.objects.all()
    counter = 0 
    data = []
    for i in teams:
        val = 0
        if counter == 3:
            print("Hello")
            counter = 0
            val = 1
        data.append({  "url":"/vote?id="+str(i.id), "Name" : i.Name , "Image" : i.Image , "Bot" : i.Bot , "Members" : i.Members , "Val" : val}  ) 
        counter += 1
    context = {'teams':data , 'error' : request.GET.get("error",0)} 
    return render(request,'index.html',context)

def vote(request):
    if("id" not in request.GET.keys()):return HttpResponseRedirect("/")
    team = Team.objects.all().filter(id=request.GET.get("id",0))
    backers = Team.objects.get(id=request.GET.get("id",0)).Backers.all()
    request.session["id"] = request.GET.get("id",0)
    backersc = 0
    for i in team:
        backersc = i.Backers.all().count()
    return render(request,'hero.html',{'teams':team ,"count" : backersc ,  "url" : "/confirm?id=" + str(request.GET.get("id",0)) ,"backer" : backers })

def saveuser(**kwargs):
    backend = kwargs["backend"].__class__.__name__
    s = SessionStore()
    if(backend == "FacebookOAuth2"):
        pass
    else:        
        s['email'] = kwargs['uid'] 
        s["username"] = kwargs['details']['username']
    s.create()
    return HttpResponseRedirect("/confirm?s=" + s.session_key) 
    

def confirm(request):
    if('s' not in request.GET.keys()):return HttpResponseRedirect("/")
    try:
        s = SessionStore(request.GET.get('s'))
        print s["username"] , s["email"]
        n = 0 
        if(Backer.objects.all().filter(Name = s["username"] , OId = s["email"] ).count() == 0 ):
            temp = Backer(Name = s["username"] , OId = s["email"] , LTime = datetime.datetime.now() )
            print "Hello"
            n = 1
            temp.save()
            team = Team.objects.get(id = request.session["id"])
            team.Backers.add(temp)
        else:
            s.delete()
            return HttpResponseRedirect("/view?error=2")
        s.delete()
        return HttpResponseRedirect("/view?error=1")
    except Exception as e :
        print e
        return HttpResponseRedirect("/app")