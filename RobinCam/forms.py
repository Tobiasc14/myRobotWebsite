from django import forms
from .models import Picture


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        app_label = 'RobinCam'
        model = Picture
        fields = ('title', 'picture')