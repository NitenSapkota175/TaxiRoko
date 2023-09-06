from django.db import models


class CabBooking(models.Model):
        full_name = models.CharField(max_length=255)
        phone_number = models.CharField(max_length=255,null=True)
        email = models.EmailField()
        from_destination  = models.CharField(max_length=100)
        to_destination = models.CharField(max_length=100)
        date = models.DateField()
        
        #this is for only for to  recognising when the entry was inserted
        date_and_time = models.DateTimeField(auto_now_add=True,null=True)
                
        def  __str__(self):
                return self.full_name;
                    