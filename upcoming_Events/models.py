from django.db import models
from home.models import ClientDetails


# Create your models here.



class UpcomingEvents(models.Model):

    Event_name=models.CharField(max_length=50)
    loaction=models.CharField(max_length=50)
    date=models.DateField()
    image=models.ImageField()
    ticket_availability=models.BigIntegerField()
    ticket_price=models.BigIntegerField()
    peoplestrength=models.BigIntegerField()

    def __str__(self):
        return self.Event_name      


class ratingEvent(models.Model):
    user=models.ForeignKey(ClientDetails,on_delete=models.CASCADE)
    event=models.ForeignKey(UpcomingEvents,on_delete=models.CASCADE)
    review=models.TextField()


class UpcomingEventsBooking(models.Model):
    user=models.ForeignKey(ClientDetails,on_delete=models.CASCADE)
    Event=models.ForeignKey(UpcomingEvents,on_delete=models.CASCADE)
    no_ticket=models.BigIntegerField()

    


class UpcomingEventsBooked(models.Model):
    user=models.ForeignKey(ClientDetails,on_delete=models.CASCADE)
    event=models.ForeignKey(UpcomingEvents,on_delete=models.CASCADE)
    payment=models.CharField(max_length=50,null=True,blank=True)
    no_ticket=models.BigIntegerField()






# class UpcomingEventsWallet(models.Model):
#     user=models.ForeignKey(ClientDetails,on_delete=models.CASCADE)
#     event = models.ForeignKey(UpcomingEvents,on_delete=models.CASCADE)

