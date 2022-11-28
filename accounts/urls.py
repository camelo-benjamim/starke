from django.shortcuts import render
from django.urls import path,include
from accounts.views import *

urlpatterns = [
    path('user/', include('django.contrib.auth.urls')),
]
