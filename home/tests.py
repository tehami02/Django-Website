from django.urls import path,include
from home import views

# Create your tests here.
urlpatterns=[
    path("cloth/",views.cloth,name='cloth')
]