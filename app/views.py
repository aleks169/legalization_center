

from django.core.mail import EmailMessage
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from .forms import PrintForm


def home(request):
    if request.method == 'GET':
        contact_form = ContactForm()
        print_form = PrintForm()
    else:
        contact_form = ContactForm(request.POST or None)
        print_form = PrintForm(request.POST or None)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['contact_name']
            mail = contact_form.cleaned_data['contact_email']
            message = contact_form.cleaned_data['contact_message']
            phone = contact_form.cleaned_data['contact_phone']

            subject = "Новое сообщение"
            body = " %s, Сообщение: %s телефон : %s, %s" % (
                name, message, phone, mail)

            try:
                send_mail(subject, body,  mail,
                          ['av591955@gmail.com'], fail_silently=False,)

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # return redirect('thanks')

        if print_form.is_valid():
            print_name = print_form.cleaned_data['print_name']
            print_email = print_form.cleaned_data['print_email']
            print_content = print_form.cleaned_data['print_content']
            print_phone = print_form.cleaned_data['print_phone']
            subject = "Новое сообщение"
            body = " %s, Сообщение: %s телефон : %s" % (
                print_name, print_content, print_phone)

            try:
                email = EmailMessage(
                    subject,
                    body,
                    print_email,
                    ['av591955@gmail.com'],
                    headers={'Reply-To': print_email}
                )
                if request.FILES:
                   # uploaded_file = request.POST.get('print_file')
                    uploaded_file = request.FILES['print_file']
                    email.attach(
                        uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)

                email.send()
            except:
               # return "Attachment error"
                return HttpResponse('Attachment error')
            #messages.success(request, "Thank you for your message.")

    return render(request, "app/legalization.html", {'contact_form': contact_form, 'print_form': print_form})
