from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class ClientDetailsForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control container'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control container'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control container'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control container'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control container'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control container'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control container'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control container'}))


    class Meta:
        model = User
        fields = ('first_name','last_name','phone_number','address','email','username', 'password1', 'password2')

        help_texts={
            'username' : None,
        }
    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use")
        return email 
    


class ClientLoginform(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control container'}))
    password=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control container'}))




    

