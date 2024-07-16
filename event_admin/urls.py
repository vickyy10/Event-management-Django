
from django.urls import path
from . import views

urlpatterns = [
    path('adminn',views.usersview,name='admin'),
    path('adminn/jobreq',views.JobReq,name='jobreq'),
    path('adminn/Gallery',views.Gallery,name='addgalleryimg'),
    path('adminn/events',views.addevents,name='addevent'),
    path('adminn/upcomingevents',views.AddUpcomingEvents,name='addupcomingevent'),
    path('blocking/<int:id>/',views.Adminusercntrl,name='blocking'),
    path('remove/<int:id>/',views.removeuser,name='remove'),
    path('deleteposition/<int:id>/',views.deleteposition,name='deleteposition'),
    path('deljobreq/<int:id>/',views.deljobreq,name='deljobreq'),
     


    
]