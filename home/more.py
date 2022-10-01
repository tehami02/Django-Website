from django.urls import path,include
from home import views

urlpatterns=[
    path('',views.void,name="void"),
    path('cloth/',views.cloth,name='path')
]