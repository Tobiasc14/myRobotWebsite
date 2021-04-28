from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from controls.models import Button

#This is a view called index
# Third variable of each render request is a context, mapping a term in the template
# folder back to


def controls(request):
    return render(request, 'controls/controls.html')

def test(request):
    return HttpResponse("Test was sucessful")

def ready(request):
    button = get_list_or_404(Button.objects.all())
    return render(request, 'controls/ready.html', {'buttonList': button})

def driving(request):
    #print(request.POST)
    buttonPushed = get_object_or_404(Button, name=request.POST)
    buttonPushed.push()
    return HttpResponseRedirect(reverse('controls:ready'))