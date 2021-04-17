from django.shortcuts import render
from django.http import HttpResponse

#This is a view called index
def controls(request):
    return HttpResponse("This is the controls page.")

def test(request):
    return HttpResponse("Test was sucessful")

def areYouReady(request):
    return HttpResponse('Are you Ready to Drive?')

def driving(request):
    return HttpResponse('Driving')