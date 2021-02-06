from django.shortcuts import render
from django.http import HttpResponse
from . forms import PeopleForm


def index(request):
    return render(request,'index.html')

def addpeople(request):
    if request.method=="POST":
        form=PeopleForm(request.POST,request.FILES)
        if form.is_valid():
            print("Valid")

    form=PeopleForm()
    return render(request,'addpeople.html',{'form':form})

