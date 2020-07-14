from django import forms 
from OMTBApp.models import Movie,Customer,Shows,Bookings

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class ShowForm(forms.ModelForm):
    class Meta:
        model = Shows
        fields = "__all__"

class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ['bookedShow','bookedSeats','totalPrice']
