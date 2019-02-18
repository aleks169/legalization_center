"""
Definition of views.
"""
from django.shortcuts import render
#from django.http import HttpRequest
#from django.template import RequestContext
#from datetime import datetime
from .forms import ContactForm




def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            new_form = form.save()
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, 'app/legalization.html', {'form': form})