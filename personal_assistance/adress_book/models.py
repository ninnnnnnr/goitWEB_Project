import email
from django.db import models
from django.urls import reverse



class Contact(models.Model):

    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=12)
    birthday = models.DateField(null=True)
    #'name', 'address', 'email', 'phone', 'birthday'


    def __str__(self):
        return f'{self.name} has number {self.phone}'

    
    def get_absolute_url(self):
        return reverse('contact-detail', args= [str(self.id)])

    
    class Meta:
        ordering = ['name']