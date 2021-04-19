from django.db import models

# Create your models here.

class Button(models.Model):
    isPushed = models.BooleanField(default=False)
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def push(self):
        if self.isPushed:
            self.isPushed = False
        else:
            self.isPushed = True





