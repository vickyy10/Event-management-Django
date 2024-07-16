from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .forms import ClientDetailsForm,ClientLoginform
from event_admin . models import Events,Gallery
from upcoming_Events.models import UpcomingEvents
import datetime


# Create your views here.



def home(request):

    event=Events.objects.all()
    now=datetime.date.today()

    upevent = UpcomingEvents.objects.filter(date__gte=now).order_by('-id')[:3]
    return render(request,'index.html',{'event':event,'upevent':upevent})


def registration(request):
    if request.method == 'POST':
        form = ClientDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = ClientDetailsForm()
    return render(request, 'Register.html', {'form': form})




def clientlogin(request):
    
    if request.method == 'POST':
        form = ClientLoginform(request.POST)    
    

        if form.is_valid():
            LoginUsername = form.cleaned_data.get('username')
            LoginPassword = form.cleaned_data.get('password')
            user = authenticate(request, username=LoginUsername, password=LoginPassword)

            if user is not None and not user.is_superuser:
                login(request, user)

                return redirect('home')
            elif user is not None and user.is_superuser:
                return redirect('admin')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = ClientLoginform()

    return render(request,'Login.html', {'form': form})



def Clientlogout(request):

    logout(request)

    return redirect('home')




def gallery(request):
    data=Gallery.objects.all()

    return render(request,'Gallery.html',{'images':data})


def contactview(request):

    return render(request,'contact.html')



    