from django.shortcuts import render
from django.http import HttpResponse

#This is a view called index
def controls(request):
    return render(request, 'controls/controls.html')

def test(request):
    return HttpResponse("Test was sucessful")

def areYouReady(request):
    return HttpResponse('Are you Ready to Drive?')

def driving(request):
    return HttpResponse('Driving')