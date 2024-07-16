from django.shortcuts import render,redirect
# from .forms import UpcomingEventsForm
from django.contrib.auth.decorators import login_required
from .models import UpcomingEvents,UpcomingEventsBooking,UpcomingEventsBooked
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse
from . forms import ratingEventForm
from .models import ratingEvent
import datetime
from django.db.models import F
from .smtp import send_email
from .notyify import send_whatsapp_message
from home.models import ClientDetails

# Create your views here.


def Events(request):

    return render(request,'events.html')




def upcoming_Events(request,id=0):

    today = datetime.date.today()

    data = UpcomingEvents.objects.filter(date__gte=today)
    

    return render(request,'upcomingevent.html',{'data':data})


@login_required(login_url='login')
def upcoming_EventsDetails(request,id):

    data=UpcomingEvents.objects.get(id=id)

    if request.method == 'POST':
        tcket_qty=request.POST['numberoftickets']
        if int(tcket_qty) <= int(data.ticket_availability):
            UpcomingEventsBooking.objects.create(Event=data,no_ticket=tcket_qty,user=request.user)

            return redirect('upcomingeventcheckout',id)


    return render(request,'upcomingeventdetails.html',{'data':data,})







def upcoming_Eventscheckout(request,id):

    data=UpcomingEvents.objects.get(id=id)

    price=data.ticket_price
    tickets=UpcomingEventsBooking.objects.last()
    tcket_qty=int(tickets.no_ticket) 
    price = int(tickets.no_ticket) * int(data.ticket_price)

    
    host=request.get_host()

    paypal_checkout={
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': price,
        'item_name': data.Event_name,
        'invoice': uuid.uuid4(),
        'currency_code':'USD',
        'notify_url':f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('PaymentSuccess1',kwargs={'id':id})}",
        'cancel_url': f"http://{host}{reverse('PaymentFailed',kwargs={'id':id})}"
    }


    paypal_payment=PayPalPaymentsForm(initial=paypal_checkout)


    return render(request,'upcomeventcheckout.html',{'data':data,'price':price,'paypal':paypal_payment,'tcket_qty':tcket_qty})




def completedevents(request):
    today = datetime.date.today()
   

    data = UpcomingEvents.objects.filter(date__lt=today)

    return render(request,'completedevent.html',{"data":data})


def Eventreviews(request,id):

    data=UpcomingEvents.objects.get(id=id)
    if request.method == 'POST':
        form=ratingEventForm(request.POST)
        if form.is_valid():   
            ratingEvent.objects.create(user=request.user,review=form.cleaned_data['review'],event=data)
            return redirect('eventreviews',id=id)

    reviews=ratingEvent.objects.filter(event=data)
    context = {'data':data,'reviews':reviews}

    form=ratingEventForm()
    try:
        bookedevent = UpcomingEventsBooked.objects.get(user=request.user,event=data)
       
        context = {'data':data,'form':form,'reviews':reviews}
    except UpcomingEventsBooked.MultipleObjectsReturned:
 
        context = {'data':data,'form':form,'reviews':reviews}
    except UpcomingEventsBooked.DoesNotExist:
        pass

    except:
        context = {'data':data,'reviews':reviews}


    return render(request,'eventreview.html',context)




def PaymentSuccess1(request,id=0):
    
    token = request.GET['PayerID']

    if token :
        last_booking = UpcomingEventsBooking.objects.last()
        event = UpcomingEvents.objects.get(id=id)
        event.ticket_availability = F('ticket_availability') - last_booking.no_ticket
        event.save()
        temp=UpcomingEventsBooking.objects.all()
        event=UpcomingEvents.objects.get(id=id)
        UpcomingEventsBooked.objects.create(user=request.user,event=event,payment=token,no_ticket=last_booking.no_ticket)
        temp.delete()
        subject = f" thank you{request.user} for booking an {event.Event_name} event form Royal events"
        message = f"""event Date: {event.date} Enjoy your   {event.Event_name} !.."""

        sender = settings.EMAIL_HOST_USER
        recipient_list = (request.user.email,)
        send_email(subject, message, sender, recipient_list)
        client=ClientDetails.objects.get(username=request.user)
        print(client,'helo')
        whatsapp_number='+91'+client.phone_number
        print(whatsapp_number,'number')
        send_whatsapp_message(whatsapp_number, message)
       
    return redirect('home')

def bookedevents(request):

    data=UpcomingEventsBooked.objects.filter(user=request.user)

    return render(request,'upcomEventbooked.html',{'data':data})

def DeleteUPevent(request,id):

    data=UpcomingEventsBooked.objects.get(id=id)
    data.delete()

    return redirect('bookedUPevents')




# mutliple ticket at a time

# def TicketWallet(request):

#     print('hu')
#     data = UpcomingEventsWallet.objects.filter(user=request.user)
#     print(data)
#     return render(request,'ticketwallet.html',{'data':data})







# def AddTicket(request,id):

#     data=UpcomingEvents.objects.get(id=id)
#     UpcomingEventsWallet.objects.create(user=request.user,event=data)


#     return render(request,'upcomingeventdetails.html',{'data':data})