"""OnlineMovieTicketBooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from OMTBApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index),
    path('addmovie',views.addmovie),
 
    path('movielist',views.movieList),
    path('deletemovie/<int:movieId>',views.deleteMovie),
    path('updatemovie/<int:movieId>',views.updateMovie),
    path('custfield',views.custfield),
    path('custlist',views.custList),
    path('login',views.login),
    path("deletecust/<int:custId>",views.deleteCust),
    path('updatecust/<int:custId>',views.updateCust),
    path('logout',views.logout),
    path('addshow',views.addshow),
    path('movieshows',views.movieshows),
    path('deleteshow/<int:showId>',views.deleteshow),
    path('updateshow/<int:showId>',views.updateshow),
    path('bookShowSeats/<int:showId>',views.bookShowSeats),
    path('bookTheShow',views.bookTheShow),
    path('booklist',views.booklist),
    path('emailIdVer',views.emailIdVer),
    path('editprofile/<str:custEmailId>',views.editprofile),
    path('forgetpassword',views.forgetpassword)

   


]

urlpatterns = urlpatterns   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
