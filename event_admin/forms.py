from django import forms
from .models import Gallery,Events,CareerAvailability
from django.contrib.auth import get_user_model

from upcoming_Events .models import UpcomingEvents

User = get_user_model()

class GalleryForm(forms.ModelForm):
    
    class Meta:
        model = Gallery
        fields = "__all__"

class EventsForm(forms.ModelForm):
     
     class Meta:
        model = Events
        fields = "__all__"


class AdminUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('is_active',)

class CareerAvailabilityForm(forms.ModelForm):
    class Meta:
        model=CareerAvailability
        fields ="__all__"

class UpcomingEventsForm(forms.ModelForm):
    class Meta:
        model = UpcomingEvents
        fields='__all__'
