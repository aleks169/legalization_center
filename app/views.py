"""
Definition of views.
"""
#from django.shortcuts import render
#from django.http import HttpRequest
#from django.template import RequestContext
#from datetime import datetime
#from .forms import ContactForm

from django.core.mail import EmailMessage





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
    if request.method == 'POST':
        form = ContactForm()
        form = PrintForm()
    else:
        form = ContactForm(request.POST or None)

        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            phone = form.cleaned_data['phone']
            body = " %s, Сообщение: %s телефон : %s"% (name, message, phone, ) 
    
            try:
                send_mail( body,  from_email, 'from@example.com',  
    ['av591955@gmail.com'], fail_silently=False)
     
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            #return redirect('thanks')
    return render(request, "app/legalization.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your email, phone, message.')



#################################################################################


def upload(request):
    if request.method == 'POST':
        form = PrintForm(request.POST)
        #form = PrintForm(data=request.POST, request = request)
    else:
   
        if form.is_valid():
            form_name = request.POST.get('form_name', '')
            form_email = request.POST.get('form_email', '')
            form_content = request.POST.get('form_content', '')
            form_phone = request.POST.get('form_phone', '')
            subject = "New message"
            body = " %s, Сообщение: %s телефон : %s"% (form_name, form_content, phone, ) 
            try:
                email = EmailMessage(
                    subject,
                    body,
                    form_email,
                    ['av591955@gmail.com'],
                    headers={'Reply-To': form_email}
                )
                if request.FILES:
                    #uploaded_file = request.POST.get('file')
                    uploaded_file = request.FILES['file']  # file is the name value which you have provided in form for file field
                    email.attach('uploaded_file.name, uploaded_file.read(), uploaded_file.content_type')
                    #message.attach('design.png', img_data, 'image/png')
                email.send()
            except:
               # return "Attachment error"
                return HttpResponse('Attachment error')
            #messages.success(request, "Thank you for your message.")
    #else:
        #form = PrintForm(request=request)
    #context_dict = {}
    #context_dict['printers'] = Printer.objects.all()
    #context_dict['form'] = form
    return render(request, 'app/legalization.html',{'form': form})