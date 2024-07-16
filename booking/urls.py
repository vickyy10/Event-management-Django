
from django.urls import path
from . import views

urlpatterns = [
    path('booking',views.EventBooking,name='eventbooking'),
    path('bookedDetails/<int:id>/',views.bookedDetails,name='bookedDetails'),
     path('bookedcart/',views.bookedcart,name='bookedcart'),  
    path('payment/success/<int:id>/',views.PaymentSuccess,name='PaymentSuccess'), 
    path('payment/failed/<int:id>/',views.PaymentFailed,name='PaymentFailed'), 
]