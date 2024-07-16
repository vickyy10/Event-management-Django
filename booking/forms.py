from django import forms
from django.forms.widgets import DateInput

from .models import bookingDetails




class bookingDetailsForm(forms.ModelForm):


    
    class Meta:
        model = bookingDetails
        exclude=('user',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phonenumber': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'booking_date': forms.DateInput(attrs={'placeholder': 'Booking Date', 'type': 'date'}),
            'Event_date': forms.DateInput(attrs={'placeholder': 'Event Date', 'type': 'date'}),
            'Adress': forms.TextInput(attrs={'placeholder': 'Address'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'pin': forms.NumberInput(attrs={'placeholder': 'PIN Code'}),
            'peoplestrength': forms.NumberInput(attrs={'placeholder': 'Number of People'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['event_type'].empty_label = 'Select'

        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control Container'  
            })