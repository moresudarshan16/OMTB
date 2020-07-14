from django.db import models

# Create your models here.
class Movie(models.Model):
    movieId = models.AutoField(primary_key=True)
    movieName = models.CharField(max_length=50)
    movieType= models.CharField(max_length=50)
    movieLanguage=models.CharField(max_length=50)
    movieCast=models.CharField(max_length=50)
    movieDirector=models.CharField(max_length=50)
    movieDuration=models.CharField(max_length=50)
    movieReleaseDate=models.CharField(max_length=50)
    movieImg=models.ImageField(upload_to="movieImage/",default="No-img.jpg")

    class Meta:
        db_table = 'movie_22344'

class Customer(models.Model):
    custId= models.AutoField(primary_key=True)
    custName=models.CharField(max_length=50)
    custEmailId=models.CharField(max_length=50)
    custPassword=models.CharField(max_length=50)
    custContactNo=models.CharField(max_length=20)
    custAddress=models.CharField(max_length=50)

    class Meta:
        db_table = 'cust_22344'

class Admin(models.Model):
    adminEmailId = models.CharField(primary_key=True , max_length=50)
    adminPassword=models.CharField(max_length=30)

    class Meta:
        db_table= "admin_22344"

class Shows(models.Model):
    showId= models.AutoField(primary_key=True)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    # when movie get delete show  also deleted automatically
    theaterNameLocation =models.CharField(max_length=100)
    screen = models.CharField(max_length=20)
    showDate = models.CharField(max_length=50)
    showTime = models.CharField(max_length=50)
    showPrice = models.FloatField(max_length=20)
    class Meta:
        db_table= "shows_22344" 

class Bookings(models.Model):
    bookingId = models.AutoField(primary_key=True)
    bookedShow = models.ForeignKey(Shows,on_delete=models.CASCADE)
    bookedSeats = models.CharField(max_length=100)
    totalPrice = models.FloatField(max_length=50)
    bookingDate = models.CharField(max_length=50)
    bookingStatus = models.CharField(max_length=50,default="Processing")
    custEmailId = models.CharField(max_length=50,default="Anonymous")
    class Meta:
        db_table= "booking_22344"