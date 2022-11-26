from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from controls.models import Button

# Create your views here.

def projectNavigator(request):
    return render(request, 'ProjectNavigator/homepage.html')


