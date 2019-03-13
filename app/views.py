"""
Definition of views.
"""
#from django.shortcuts import render
#from django.http import HttpRequest
#from django.template import RequestContext
#from datetime import datetime
#from .forms import ContactForm





#def home(request):
	
    #if request.method == "POST":

       # form = ContactForm(request.POST or None)
        #if form.is_valid():
        	
           # new_form = form.save()
           # form = ContactForm()
    #else:
        #form = ContactForm()

    #return render(request, 'app/legalization.html', {'form': form})





from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def home(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            phone = form.cleaned_data['phone']
            body = " %s, Сообщение: %s телефон :%s"% (name, message, phone) 
            try:
                send_mail( body,  email, 'from@example.com',  ['av591955@gmail.com'])
     
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            #return redirect('thanks')
    return render(request, "app/legalization.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your email, phone, message.')


       
 