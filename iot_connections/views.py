from django.shortcuts import render

# Create your views here.
def mainFrame(request):
    return render(request,'index.html')

def deviceControl(request,device_code):
    pass

def microCommunication(request,device_code):
    pass

def showCodePastMicro(request,device_code):
    pass