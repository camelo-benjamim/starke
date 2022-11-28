from django.shortcuts import render

# Create your views here.
def mainFrame(request):
    return render(request,'index.html')
