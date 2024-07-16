from django.shortcuts import render,redirect
from upcoming_Events. models import UpcomingEvents,UpcomingEventsBooking,UpcomingEventsBooked

from .forms import bookingDetailsForm
from .models import bookingDetails
from django.contrib.auth.decorators import login_required
from event_admin.models import Events
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse



# Create your views here.


@login_required(login_url='login')
def EventBooking(request):
  
    if request.method == 'POST':
       
        form=bookingDetailsForm(request.POST)

        if form.is_valid():
            print('hi')
            data=bookingDetails.objects.create(
                user=request.user,
                name = form.cleaned_data['name'],
                phonenumber=form.cleaned_data['phonenumber'],
                email=form.cleaned_data['email'],
                Event_date=form.cleaned_data['Event_date'],
                Adress=form.cleaned_data['Adress'],
                state=form.cleaned_data['state'],
                pin=form.cleaned_data['pin'],
                event_type=form.cleaned_data['event_type'],
                peoplestrength=form.cleaned_data['peoplestrength']
            )
            return redirect('bookedDetails',data.id)  
        
                 
    else:
        form=bookingDetailsForm()   
    return render(request,'eventBooking.html',{'form':form})



@login_required(login_url='login')
def bookedDetails(request,id=0):

    
    data = bookingDetails.objects.get(id=id)
    form=bookingDetailsForm(instance = data) 
   
    
    if request.method == 'POST':
        
        
        form=bookingDetailsForm(request.POST,instance = data)
       

        if form.is_valid():
            event_type = form.cleaned_data['event_type']
            data = form.save()
            
        
            
       
    event=Events.objects.get(eventname=data.event_type)



    host=request.get_host()

    paypal_checkout={
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': event.advanceprice,
        'item_name': data.name,
        'invoice': uuid.uuid4(),
        'currency_code':'USD',
        'notify_url':f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('PaymentSuccess',kwargs={'id':id})}",
        'cancel_url': f"http://{host}{reverse('PaymentFailed',kwargs={'id':id})}"
    }

    paypal_payment=PayPalPaymentsForm(initial=paypal_checkout)

    

    return render(request,'bookedDetails.html',{'form':form,'data':data,'price':event.advanceprice,'paypal':paypal_payment})




def bookedcart(request):

    data=bookingDetails.objects.filter(user=request.user)

    print(data)

    return render(request,'bookedcart.html',{'data':data})






def PaymentSuccess(request,id=0):
    

    

    
    return render(request,'PaymentSuccess.html')





def PaymentFailed(request,id=0):



    return render(request,'PaymentFailed.html')