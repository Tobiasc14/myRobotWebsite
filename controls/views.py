from django.shortcuts import render
from django.http import HttpResponse

#This is a view called index
def index(request):
    return HttpResponse("Hello, world. You're at the controls index.")

def test(request):
    return HttpResponse("Test was sucessful")