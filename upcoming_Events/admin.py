from django.contrib import admin
from .models import UpcomingEvents,ratingEvent,UpcomingEventsBooking

# Register your models here.


admin.site.register(UpcomingEvents)

admin.site.register(ratingEvent)
admin.site.register(UpcomingEventsBooking)


