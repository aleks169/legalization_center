"""
Definition of forms.
"""

from django import forms
from .models import PrintFileUs
from .models import ContactUs


class ContactForm(forms.ModelForm):
    contact_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Ваше имя', 'class': 'form-control'}))
    contact_message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'С какой страны запросить справку о несудимости', 'class': 'form-control'}), max_length=100, )
    contact_email = forms.EmailField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Ваш Email:', 'class': 'form-control'}))
    contact_phone = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Ваше телефон', 'class': 'form-control'}))

    class Meta:
        model = ContactUs
        fields = ('contact_name', 'contact_email',
                  'contact_message', 'contact_phone',)

###################################################


class PrintForm(forms.ModelForm):
    print_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Ваше имя', 'class': 'form-control'}))
    print_content = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'С какой страны запросить справку о несудимости', 'class': 'form-control'}), max_length=100, )
    print_email = forms.EmailField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Ваш Email:', 'class': 'form-control'}))
    print_phone = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Ваше телефон', 'class': 'form-control'}))

    print_file = forms.FileField(required=False, widget=forms.FileInput(
        attrs={'class': 'form-control'}))


    class Meta:
        model = PrintFileUs
        fields = ('print_name', 'print_email', 'print_content',
                  'print_phone', 'print_file',)
