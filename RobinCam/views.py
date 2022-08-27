from django.shortcuts import render

# Create your views here.

def robinCam(request):
    return render(request, 'RobinCam/whatthedogdoin.html')
