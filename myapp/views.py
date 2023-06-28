from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
from .models import Facts

# Create your views here.
def index(request):
    context = {
        'name':'David Boateng',
        'index_no':10888204,
        'course':'Computer Science',
    }

    feature = Feature()
    feature.title = "About Me"
    feature.content = "I am a student studying @ University Of Ghana.  Help is on its way please. Do you need assistance" 

    f1 = Facts()
    f1.ratings = 500
    f1.title = "Clients who are Happy"
    f1.description = " I always deliver my guy!"

    f2 = Facts()
    f2.ratings = 135
    f2.title = "Projects"
    f2.description = "My Projects are always fire!"

    f3 = Facts()
    f3.ratings = 720
    f3.title = "We Offer Support"
    f3.description = "Support is there when you need me don't hesitate"

    f4 = Facts()
    f4.ratings = 110
    f4.title = "Workers Of The League"
    f4.description = "My workers are professionals!!!"

    facts = [f1,f2,f3,f4]
     

    return render(request,'index.html',{'context':context,'feature':feature,'facts':facts})

def count(request):
    text = len(request.POST['text'].split())

    return render(request,'index.html',{'text':text})