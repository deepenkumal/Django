from django.shortcuts import render,redirect
from django.http import HttpResponse
#from . forms import ProductForm
from .forms import AddProduct
from .models import Product
from django.contrib import messages
from . forms import ConfirmForm



def index(request):
    allproduct=Product.objects.all()
    print(allproduct)
    print("printing all data by fetching from database")
    return render(request,'index.html',{'products':allproduct})


def addproduct(request):
    if request.method=='POST':
        form=AddProduct(request.POST,request.FILES)
        print(request.POST)
        print("it is executing")
        if form.is_valid():
            print("iam valid")
            form.save()
            form=AddProduct()
            messages.success(request,'product added successfully')
            return redirect('show')

        else:
            print("error")
            #return redirect('index')
    else:
        form=AddProduct()
    return render(request,'form.html',{'form':form})

    
def show(request):
    products=Product.objects.all()
    return render(request,'show.html',{'products':products})

     

def confirm_delete(request):
    form=ConfirmForm(request.GET)
    return render(request,'delete.html',{'form':form})


        

def delete_data(request,id):
    if request.method=='GET':
        de=Product.objects.get(pk=id)
        de.delete()
        messages.success(request,'Producted deleted successfully')
        return redirect('show')

def update(request,id):
    if request.method=='POST':
        product = Product.objects.get(id=id)
        form=AddProduct(request.POST, request.FILES, instance=product)
        if form.is_valid():
            # name=form.changed_data['product_name']
            # detail=form.changed_data['product_detail']
            # image=form.changed_data['product_image']

            # fr=Product(product_name=name,product_detail=detail,product_image=image)
            # fr.save()
            form.save()
            messages.success(request, 'Product updated')
            return redirect('show')
        else:
            messages.error(request, 'unable to update')
            return redirect('show')
            
    else:
        form=AddProduct()

    return render(request,'update.html',{'form':form})



