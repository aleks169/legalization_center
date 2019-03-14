"""
Definition of models.
"""

from django.db import models

# Create your models here.
from django.utils import timezone


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=100)
    message = models.TextField(max_length=240)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # %s подставляет значения
        return "Пользователь %s %s %s" % (self.name, self.email, self.date)



from django.core.files.storage import FileSystemStorage

     fs = FileSystemStorage(location='/media/photos')

class Spravka(models.Model):
    photo = models.ImageField(storage=fs)