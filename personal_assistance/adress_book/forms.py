from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ('author',)
        fields = ('name', 'address', 'email', 'phone', 'birthday')
