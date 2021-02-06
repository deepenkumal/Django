from django import forms
from .models import Product

# class ProductForm(forms.Form):
#     product_name=forms.CharField()
#     product_details=forms.CharField()
#     product_image=forms.FileField()

class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields =('product_name','product_detail','product_image')
        widgets={
            'product_name':forms.TextInput(attrs={'class':'form-control'}),
            'product_details':forms.TextInput(attrs={'class':'form-control'}),
            'product_image':forms.FileInput(attrs={'class':'form-control'}),
        }

class ConfirmForm(forms.Form):
    pass

