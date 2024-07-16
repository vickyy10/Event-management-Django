from django import forms
from .models import ratingEvent


# class UpcomingEventsForm(forms.Form):
#     Event_name=forms.CharField()
#     loaction=forms.CharField()
#     date=forms.DateField()
#     image=forms.ImageField()
#     ticket_availability=forms.IntegerField()
#     ticket_price=forms.IntegerField()
#     peoplestrength=forms.IntegerField()

class ratingEventForm(forms.ModelForm):

    class Meta:
        model=ratingEvent
        fields =  fields=('review',)
