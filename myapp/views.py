from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name':'David Boateng',
        'index_no':10888204,
        'course':'Computer Science',
    }   
    return render(request,'index.html',context)

def count(request):
    text = len(request.GET['text'].split())

    return render(request,'index.html',{'text':text})