
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('sign up',views.registration,name='register'),
    path('log in',views.clientlogin,name='login'),
    path('logout',views.Clientlogout,name='logout'),
    path('gallery',views.gallery,name='gallery'),
     path('contact',views.contactview,name='contact'),
    
]
