"""
Definition of models.
"""
from .validators import validate_file_extension
from django.db import models

# Create your models here.
from django.utils import timezone


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=100)
    message = models.TextField(max_length=240)
    #file = models.FileField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension])

    def __str__(self):
        # %s подставляет значения
        return "Пользователь %s %s %s" % (self.name, self.email, self.date)



        


