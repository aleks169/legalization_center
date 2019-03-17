"""
Definition of models.
"""

from django.db import models

# Create your models here.
from django.utils import timezone


class ContactUs(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=50)
    contact_phone = models.CharField(max_length=100)
    contact_message = models.TextField(max_length=240)
    date = models.DateTimeField(default=timezone.now)
    # class Meta:
    # model = ContactUs
    #fields =('contact_name', 'contact_email',' contact_phone','contact_message')

    def __str__(self):
        # %s подставляет значения
        return "Пользователь %s %s %s" % (self.contact_name, self.contact_email, self.date)


class PrintFileUs(models.Model):
    print_name = models.CharField(max_length=50)
    print_email = models.EmailField(max_length=50)
    print_phone = models.CharField(max_length=100)
    print_content = models.TextField(max_length=240)
    print_file = models.FileField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # %s подставляет значения
        return "Пользователь %s %s %s" % (self.print_name, self.print_email, self.date)
   # class Meta:
      #  model = PrintFileUs
      #  fields =('print_name', 'print_email',' print_phone','print_content','print_file')
