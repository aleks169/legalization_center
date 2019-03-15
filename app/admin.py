
from .models import ContactUs
from django.contrib import admin
from .models import PrintFileUs
#class ContactUsAdmin(admin.ModelAdmin):
    #list_display = ('name', 'email', 'date')
    #list_display = (field.name for field in ContactUs._meta.fields) 
    #search_fields = ('name', 'email')

    #class Meta:
       # model = ContactUs

admin.site.register(ContactUs)

admin.site.register(PrintFileUs)
