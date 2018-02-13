"""mlserver URL Configuration

Created on Thu Feb  12 00:20:19 2018
@author: Dhruv.Shah

"""
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('mlapp/', include('mlapp.urls')),
    path('admin/', admin.site.urls),
]