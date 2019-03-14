"""
Definition of forms.
"""

from django import forms

from .models import ContactUs
#from foundation_filefield_widget.widgets import FoundationFileInput, FoundationImageInput

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Ваше имя','class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'С какой страны запросить справку о несудимости', 'class':'form-control'}), max_length=100, )
    email = forms.EmailField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Ваш Email:','class':'form-control'}))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Ваше телефон','class':'form-control'}))
    #my_file = forms.FileField(widget=FoundationFileInput)
    #my_image = forms.FileField(widget=FoundationImageInput)
    file = forms.ImageField(max_length=100,widget=forms.FileInput(
        attrs={'class':'form-control'}))
    #file =forms.FileField()

    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'message', 'phone','file')

  