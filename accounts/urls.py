from django.shortcuts import render
from django.urls import path,include
from accounts.views import *

urlpatterns = [
    path('', SignUp),
    path('user/', include('django.contrib.auth.urls')),
    path('edit/',ChangeUsr),
    path('user_delete/',usrDelete),
    path('user_deleted/',userDeleted),
    
]
