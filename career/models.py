from django.db import models
from event_admin.models import CareerAvailability
from phonenumber_field.modelfields import PhoneNumberField 

# Create your models here.


class careermodel(models.Model):
    position=models.ForeignKey(CareerAvailability,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    Mobile=PhoneNumberField()
    email=models.EmailField(unique=True)
    resume=models.ImageField(upload_to='resume')
    comment=models.TextField()  

