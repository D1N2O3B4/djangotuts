from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

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
    return render(request,'index.html',{'context':context,'feature':feature})

def count(request):
    text = len(request.POST['text'].split())

    return render(request,'index.html',{'text':text})