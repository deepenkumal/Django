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

class ConfirmForm(forms.Form):
    pass

