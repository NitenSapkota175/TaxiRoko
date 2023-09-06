from django.contrib import admin
from . models import CabBooking
from django.contrib.auth.models import User,Group
# Register your models here.
class CabBookingAdmin(admin.ModelAdmin):
    readonly_fields = ('full_name','phone_number','email','from_destination','to_destination','date')
    list_filter = ('date_and_time',)
    ordering = ('-id',) 
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        # Disable delete functionality for all instances
        return False
    
    
admin.site.register(CabBooking , CabBookingAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)