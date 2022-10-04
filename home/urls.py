from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
   path("", views.home , name='home'),
   path("void/", views.void , name='void'),
   path("about/", views.about , name='about'),
   path("cart/", views.cart , name='cart'),
   path("cloth/", views.cloth , name='cloth'),
   path("next/", include('home.more')),
   path("myaccount/", views.myaccount, name='myaccount'),
]
