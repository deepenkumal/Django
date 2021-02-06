from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import PeopleForm
from . models import People


def index(request):
    return render(request,'index.html')

def add_people(request):
    if request.method=="POST":
        form=PeopleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form=PeopleForm()
    return render(request,'addpeople.html',{'form':form})

def update_people(request,id):
    if request.method=="POST":
        p_id=People.objects.get(id=id)
        form=PeopleForm(request.POST,request.FILES,instance=p_id)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form=PeopleForm()
    return render(request,'update.html',{'form':form})


def show(request):
    peoples=People.objects.all()
    return render(request,'show.html',{'peoples':peoples})

def delete_people(request,id):
    if request.method=="GET":
        p_id=People.objects.get(id=id)
        p_id.delete()
        return redirect('show')