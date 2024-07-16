from django.shortcuts import render,redirect
from home.models import ClientDetails
from career.models import careermodel
from .models import CareerAvailability
from .forms import GalleryForm,EventsForm,AdminUserForm,CareerAvailabilityForm, UpcomingEventsForm


# Create your views here.





def usersview(request):

    users=ClientDetails.objects.exclude(is_superuser=True)



    return render(request,'admin/Users.html',{'userdata':users})



def Adminusercntrl(request,id=0):

    user=ClientDetails.objects.get(id=id)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    return redirect('admin')


def removeuser(request,id=0):

    user= ClientDetails.objects.get(id=id)
    user.delete()

    return redirect('admin')



def JobReq(request):
    jobreq = careermodel.objects.all()
    vacancy=CareerAvailability.objects.all()
    if request.method== 'POST':
        form=CareerAvailabilityForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CareerAvailabilityForm()
        
    return render(request,'admin/JobReq.html',{'jobreq':jobreq,'form':form,'vacancy':vacancy})


def Gallery(request):
    if request.method == 'POST':
        form=GalleryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=GalleryForm() 

    return render(request,'admin/Gallery.html',{'form':form})


def addevents(request):

    form=EventsForm() 
    form1=UpcomingEventsForm()
    if request.method == 'POST':
        form=EventsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

        
    


    
    return render(request,'admin/addevents.html',{'form':form,'form1':form1})

def deleteposition(request,id=0):

    data=CareerAvailability.objects.get(id=id)
    data.delete()

    return redirect('jobreq')


def deljobreq(request,id=0):

    data=careermodel.objects.get(id=id)

    data.delete()

    return redirect('jobreq')



def AddUpcomingEvents(request):
 
    if request.method == 'POST':
        form=UpcomingEventsForm(request.POST,request.FILES)
        if form.is_valid():
            event=form.save()

    return redirect('addevent')





    