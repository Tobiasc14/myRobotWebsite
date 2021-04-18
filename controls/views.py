from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse
from controls.models import Button

#This is a view called index
# Third variable of each render request is a context, mapping a term in the template
# folder back to
def controls(request):
    return render(request, 'controls/controls.html')

def test(request):
    return HttpResponse("Test was sucessful")

def driving(request):
    button = get_list_or_404(Button.objects.all())
    return render(request, 'controls/ready.html', {'button': button})