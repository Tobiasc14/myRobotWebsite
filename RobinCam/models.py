from django.db import models

# Create your models here.

class Picture(models.Model):
    name = models.CharField(max_length = 30, default="Robin")
    image = models.ImageField(upload_to='RobinCam/images')


