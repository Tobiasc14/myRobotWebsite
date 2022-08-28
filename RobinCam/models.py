from django.db import models

# Create your models here.

class Picture(models.Model):
    title = models.CharField(max_length = 30, default="Robin")
    picture = models.ImageField(upload_to='RobinCam/images')


