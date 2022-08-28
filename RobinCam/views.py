from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.
from RobinCam.models import Picture


def robinCam(request):
    picture = get_object_or_404(Picture)
    url = picture.image.url
    return render(request, 'RobinCam/whatthedogdoin.html', {'location': url})
