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
    #search code
    people_name = request.GET.get('people_name')
    if people_name != '' and people_name is not None:
        peoples = People.objects.filter(name__icontains=people_name)
    return render(request,'show.html',{'peoples':peoples})

def delete_people(request,id):
    people=People.objects.get(id=id)
    if request.method=="POST":
        people.delete()
        return redirect('show')
    return render(request,'delete_people.html',{'people':people})