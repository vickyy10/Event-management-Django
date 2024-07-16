from django import forms
from .models import careermodel

    



class careermodelform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control container'}))
    Mobile = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control container'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control container'}))
    

    

    class Meta:
        model= careermodel
        fields='__all__'
