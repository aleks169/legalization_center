"""
Definition of forms.
"""

from django import forms

from .models import ContactUs


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Ваше имя','class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Сообщение', 'class':'form-control'}), max_length=100, )
    email = forms.EmailField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Ваш Email:','class':'form-control'}))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Ваше телефон','class':'form-control'}))




    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'message' ,'phone')
