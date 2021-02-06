from django import forms
from .models import People


class PeopleForm(forms.ModelForm):
    class Meta:
        model=People
        fields=['name','country','age','image']
        widgets={
            'name':forms.TextInput(attrs={'class':'from form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }