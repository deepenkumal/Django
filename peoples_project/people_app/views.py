from django.shortcuts import render
from django.http import HttpResponse
from . forms import PeopleForm


def index(request):
    return render(request,'index.html')

def addpeople(request):
    form=PeopleForm()
    return render(request,'addpeople.html',{'form':form})

