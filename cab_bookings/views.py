from django.shortcuts import render
from . models import CabBooking
import random
from django.contrib import messages
import http.client

from django.conf import settings

# Create your views here.


def Home(request):
    
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        pickup = request.POST.get('pickup')
        
        dropoff = request.POST.get('dropoff')
        
        phoneNumber = request.POST.get('phonenumber')
        
        date = request.POST.get('date')
        
        if name == "" or email  == "" or pickup  == "" or dropoff  == "" or phoneNumber  == "" or date  == "":
            
             messages.error(request, 'Invalid form submission.')
             return render(request,'cab_bookings/Home.html');
    
        
        CabBooking.objects.create( 
              
              full_name = name,
              email = email,
              phone_number = phoneNumber,
              from_destination = pickup,
              to_destination = dropoff,
              date = date                   
         )
        messages.success(request, 'Your request has been forwarded , we will contact you shortly')
        return render(request,'cab_bookings/Home.html');
        
        
        
        
    return render(request,'cab_bookings/Home.html')


def About_Us(request):
    
    return render(request,'cab_bookings/About_Us.html');







