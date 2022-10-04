"""Store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/

from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "Tehami"
admin.site.site_title = "Tehami's Portal"
admin.site.index_title = "Welcome to our Research Portal"

urlpatterns = [
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),

    path('', include('home.urls'))
]
