from django.forms import ModelForm
from .models import Contact
from django.utils.translation import gettext as _

class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'address', 'email', 'phone', 'birthday']
        labels = {'name': _('Name'), 'address': _('Address'), 'email': _('Email'), 'phone': _('Phone number'), 'birthday': _('Birthday')}
        help_texts = {'name': _('Enter contact name'), 'address': _('Enter contact address'),
        'email': _('Enter contact email'), 'phone': _('Enter contact phone number'), 'birthday': _('Enter contact birthday')}