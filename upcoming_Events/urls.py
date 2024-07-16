from django.urls import path
from . import views


urlpatterns = [
    path('events',views.Events,name='events'),
    path('upcomingevent',views.upcoming_Events,name='upcomingevent'),
    path('upcomingeventdetails/<int:id>',views.upcoming_EventsDetails,name='upcomingeventdetails'),
    path('upcomingeventcheckout/<int:id>',views.upcoming_Eventscheckout,name='upcomingeventcheckout'),
    path('completedevent',views.completedevents,name='completedevent'),
    path('eventreviews/<int:id>',views.Eventreviews,name='eventreviews'),
    path('payment/success1/<int:id>/',views.PaymentSuccess1,name='PaymentSuccess1'),
    path('booked/events',views.bookedevents,name='bookedUPevents'), 
    path('deleteupevent/<int:id>',views.DeleteUPevent,name='deleteupevent'),
    
    
    # path('ticketwallet',views.TicketWallet,name='ticketwallet'),
    # path('addticket/<int:id>',views.AddTicket,name='addticket')
  

]