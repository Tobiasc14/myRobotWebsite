from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.
from RobinCam.forms import ImageForm
from RobinCam.models import Picture


def robinCam(request):
    #picture = get_object_or_404(Picture)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            loc = img_obj.picture.url
            title = img_obj.title

            return render(request, 'RobinCam/whatthedogdoin.html', {'form': form, 'img_obj': loc, 'title': title})
    else:
        form = ImageForm()
        img_obj = get_list_or_404(Picture)[-1]
        loc = img_obj.picture.url
        title = img_obj.title
    return render(request, 'RobinCam/whatthedogdoin.html', {'form': form,'img_obj': loc, 'title': title})


    #return render(request, 'RobinCam/whatthedogdoin.html', {'image': picture})
