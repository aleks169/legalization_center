"""
Definition of forms.
"""

from django import forms
from .models import PrintFileUs
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
    #file = forms.FileField(widget=FoundationFileInput)
    #my_image = forms.FileField(widget=FoundationImageInput)
    #files = forms.ImageField(max_length=100,widget=forms.FileInput(
        #attrs={'class':'form-control', 'name':'document'}))
    #file =forms.FileField()


    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'message', 'phone',)

###################################################

class PrintForm(forms.ModelForm):
    form_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Ваше имя','class':'form-control'}))
    form_content = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'С какой страны запросить справку о несудимости', 'class':'form-control'}), max_length=100, )
    form_email = forms.EmailField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Ваш Email:','class':'form-control'}))
    form_phone = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Ваше телефон','class':'form-control'}))

    file = forms.FileField(required=False,widget=forms.FileInput(
        attrs={'class':'form-control'})) 
    file.help_text = "Upload your file as .STL format. If you have more than one file, " \
                     "make a .zip and upload them all at once"
    #form_content = forms.CharField(
        #required=True,
        #widget=forms.Textarea
    #)
    class Meta:
        model = PrintFileUs
        fields = ('form_name', 'form_email', 'form_content', 'form_phone', 'file',)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(PrintForm, self).__init__(*args, **kwargs)
        self.fields['form_name'].label = "Your name:"
        self.fields['file'].label = "Choose your design file:"

       