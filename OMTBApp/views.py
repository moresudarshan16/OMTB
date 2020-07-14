from django.shortcuts import render
from django.http import HttpResponse
from OMTBApp.models import Movie,Customer,Admin,Shows,Bookings
from OMTBApp.forms import MovieForm
from OMTBApp.forms import CustomerForm,ShowForm,BookingForm
from datetime import datetime

# Create your views here.

def index(request):
    return render(request,"OMTBApp/index.html")

def addmovie(request):
    if request.method=="POST":
        movieformobj=MovieForm(request.POST,request.FILES)
        if movieformobj.is_valid():
            movieformobj.save() 

            return render(request,'OMTBApp/addmovie.html',{"status":"Movie Added"})
        else:
            return render(request,"OMTBApp/addmovie.html",{"status":"Movie not Added"})
    else:
            return render(request,"OMTBApp/addmovie.html")

def movieList(request):
    movielist = Movie.objects.all()
    return render(request,'OMTBApp/movielist.html',{'movielist':movielist})

def deleteMovie(request,movieId):
        movie= Movie.objects.get(movieId=movieId)
        movie.delete()
        movielist = Movie.objects.all()

        return render(request,"OMTBApp/movielist.html",{"status":"Movie deleted succesfully","movielist":movielist})
    


def custfield(request):
    if request.method=="POST":
        custformobj=CustomerForm(request.POST)
        if custformobj.is_valid():
            custformobj.save() 
            return render(request,'OMTBApp/custfield.html',{"status":"Customer Added"})
        else:
            return render(request,"OMTBApp/custfield.html",{"status":"Customer not Added"})
    else:
        return render(request,"OMTBApp/custfield.html")

def custList(request):
    custlist = Customer.objects.all()
    return render(request,'OMTBApp/custlist.html',{'custlist':custlist})
def login(request):
    if request.method=="GET":
        return render(request,"OMTBApp/login.html")

    elif request.method=="POST":
        usertype=request.POST["usertype"]
        EmailId=request.POST["EmailId"]
        Password=request.POST["Password"]
        
        if usertype == "admin":
            try:
                admin = Admin.objects.get(adminEmailId=EmailId)
                if admin.adminEmailId == EmailId and admin.adminPassword==Password:
                    request.session["admin"]=admin.adminEmailId
                    request.session["customerDetails"]={"custName":admin.adminEmailId}
                    return render(request,"OMTBApp/index.html",{"status":"admin Login Successfully"})
                else:
                    return render(request,"OMTBApp/login.html",{"status":"admin Login Unsuccessfully"})
            except Exception as e:
                return render(request,"OMTBApp/login.html",{"status":"Admin login Unsuccessfully"},{"e":"error"})
        elif usertype == "Customer":
            try:
                customer = Customer.objects.get(custEmailId=EmailId)
                if customer.custEmailId==EmailId and customer.custPassword==Password:
                    request.session["customer"]=customer.custEmailId
                    request.session["customerDetails"]={"custName":customer.custName}
                    return render(request,"OMTBApp/index.html",{"status":"Customer Login Successfully"})
                else:
                    return render(request,"OMTBApp/login.html",{"status":"Customer Login Unsuccessfully"})

            except Exception as e:
                return render(request,"OMTBApp/login.html",{"status":"Customer login Unsuccessfully"},{"e":"error"})
       


def deleteCust(request,custId):
        customer= Customer.objects.get(custId=custId)
        customer.delete()
        custlist = Customer.objects.all()

        return render(request,"OMTBApp/custlist.html",{"status":"Customer deleted succesfully","custlist":custlist})

def updateCust(request,custId):
    
    if request.method=='GET':
        customer= Customer.objects.get(custId=custId)

        return render(request,'OMTBApp/updatecust.html',{'updatecust':customer})
    elif request.method=="POST":
        customer= Customer.objects.get(custId=custId)
        customerformobj=CustomerForm(request.POST,instance=customer)
        if customerformobj.is_valid():
            customerformobj.save() 
           
            return render(request,'OMTBApp/index.html',{"status":"customer updated"})
        return render(request,"OMTBApp/updatecust.html")

def updateMovie(request,movieId):
    if request.method=='GET':
        movie= Movie.objects.get(movieId=movieId)

        return render(request,'OMTBApp/updatemovie.html',{'updatemovie':movie})
    elif request.method=="POST":
        movie= Movie.objects.get(movieId=movieId)
        movieformobj=MovieForm(request.POST,request.FILES,instance=movie)
        if movieformobj.is_valid():
            movieformobj.save() 
            movielist = Movie.objects.all()
            return render(request,'OMTBApp/movielist.html',{"status":"movie updated",'movielist':movielist})
        return render(request,"OMTBApp/updatemovie.html",{"status":"movie not updated"})


def logout(request):
    session_keys = list (request.session.keys())
    for key in session_keys:
        del request.session[key]
    return render(request,"OMTBApp/index.html",{"status":"Logout Successfully"})

def addshow(request):
    movielist = Movie.objects.all()
    if request.method == "GET":
        

        return render (request,"OMTBApp/addshow.html",{"movielist":movielist})
    elif request.method == "POST":
        showformobj = ShowForm(request.POST,request.FILES)
        
        if showformobj.is_valid():
            showformobj.save()
            return render (request,"OMTBApp/addshow.html",{"movielist":movielist,"status":"Show Created Successfully"})
        else:
            return render (request,"OMTBApp/addshow.html",{"movielist":movielist,"status":"Show Not Created Successfully"})

def movieshows(request):
    movieshows = Shows.objects.all()
    return render(request,"OMTBApp/movieshows.html",{"movieshows":movieshows})

def deleteshow(request,showId):
        show = Shows.objects.get(showId=showId)
        show.delete()
        movieshows = Shows.objects.all()

        return render(request,"OMTBApp/movieshows.html",{"status":"show deleted succesfully","movieshows":movieshows})

def updateshow(request,showId):
    movielist = Movie.objects.all()
    if request.method=='GET':
        show = Shows.objects.get(showId=showId)
        return render(request,"OMTBApp/updateshow.html",{"movielist":movielist,"show":show})
    
    elif request.method == 'POST':
        show = Shows.objects.get(showId=showId)
        showformobj=ShowForm(request.POST,request.FILES,instance=show)
        if showformobj.is_valid():
            showformobj.save()
            movieshows = Shows.objects.all()
            return render(request,'OMTBApp/movieshows.html',{"status":"show updated",'movieshows':movieshows})
        return render(request,"OMTBApp/updateshow.html",{"status":"movie not updated"})


def bookShowSeats(request,showId):
    if request.method == "GET":
        show = Shows.objects.get(showId=showId)
        reserveSeats = Bookings.objects.filter(bookedShow=show)
        rslist = []
        for rs in reserveSeats:
            rslist.extend(rs.bookedSeats.split(','))
            
        return render(request,"OMTBApp/selectseats.html",{"show":show,'reserveSeats':rslist})

def bookTheShow(request):
    if request.method == 'POST':
        sId = request.POST['showId']
        bshow = Shows.objects.get(showId=sId)
        seats = request.POST['bookedseats']
        tprice = request.POST['totalPrice']
        cEmailId = request.session["customer"]
        bDate = datetime.now()
        bookedshow = Bookings.objects.create(bookedShow=bshow,bookedSeats=seats,totalPrice=tprice,custEmailId=cEmailId,bookingDate=bDate,bookingStatus='booked') 
        bookedshow.save()
        bookedshow = Bookings.objects.get(custEmailId=cEmailId,bookingDate=bDate)
        return render(request,"OMTBApp/bookingDetails.html",{"status":"Show is booke","bookedShow":bookedshow}) 
        

def booklist(request):
    booklist= Bookings.objects.all()
    return render(request,"OMTBApp/booklist.html",{"booklist":booklist})



def emailIdVer(request):
    emailId =request.GET["emailId"]
    try:
        cust= Customer.objects.get(custEmailId=emailId)
        if cust != None :
            return HttpResponse("<h5 style='color:red;'>Your Email Id is already Exist try another email Id</h5>")
    except Exception as e:
    
        return HttpResponse("<h5 style='color:green;'>Your Email Id is valid</h5>")


def editprofile(request,custEmailId):
    cust=Customer.objects.get(custEmailId=custEmailId)

    return render(request,"OMTBApp/updatecust.html",{"updatecust":cust})
    
def forgetpassword(request):
    if request.method == "POST":
        custEmailId = request.POST['custEmailId']
        custPassword = request.POST['custPassword']
        custContactNo = request.POST['custContactNo']
        try:    
            forgetpassobj = Customer.objects.filter(custEmailId=custEmailId,custContactNo=custContactNo).update(custPassword=custPassword)
            if forgetpassobj != None:
                return render(request,"OMTBApp/login.html",{"status":"Password Change"})
        except Exception as e:
            return render(request,"OMTBApp/forgetpassword.html")

    else:
        return render(request,"OMTBApp/forgetpassword.html")
