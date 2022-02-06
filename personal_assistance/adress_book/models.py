import email
from django.db import models
from django.urls import reverse


class Contact(models.Model):
    '''Address Book model which contains all contacts and information about them.
    Save to database name of the contact, it's phone number, address, email and birthday date.'''

    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=12)
    birthday = models.DateField(null=True)

    def __str__(self):
        return f'{self.name} has number {self.phone}'

    def get_absolute_url(self):
        '''Return absolute url to each contacts information'''
        return reverse('contact-detail', args=[str(self.id)])

    class Meta:
        ordering = ['name']