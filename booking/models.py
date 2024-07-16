from django.db import models

from event_admin.models import Events
from home.models import ClientDetails
from phonenumber_field.modelfields import PhoneNumberField




# Create your models here.

class bookingDetails(models.Model):
    user=models.ForeignKey(ClientDetails,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    phonenumber=PhoneNumberField()
    email=models.EmailField(unique=True)
    booking_date=models.DateField(auto_now_add=True)
    Event_date=models.DateField()
    Adress=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pin=models.IntegerField()
    event_type = models.ForeignKey(Events,on_delete=models.CASCADE)
    peoplestrength=models.BigIntegerField()

    
