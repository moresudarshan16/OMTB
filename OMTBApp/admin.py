from django.contrib import admin
from OMTBApp.models import Movie
from OMTBApp.models import Customer
from OMTBApp.models import Admin,Shows,Bookings
# Register your models here.
admin.site.register(Movie)
admin.site.register(Admin)
admin.site.register(Customer)
admin.site.register(Shows)
admin.site.register(Bookings)
