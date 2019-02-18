"""
Definition of models.
"""

from django.db import models

# Create your models here.
from django.utils import timezone


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=240)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # %s подставляет значения
        return "Пользователь %s %s %s" % (self.name, self.email, self.date)