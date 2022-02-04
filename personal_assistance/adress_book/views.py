from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Contact

from datetime import datetime, timedelta


class ContactListView(generic.ListView):
    model = Contact
    paginate_by = 40


class ContactDetailView(generic.DetailView):
    model = Contact

class AddContact(CreateView):
    model = Contact
    fields = '__all__'
    success_url = reverse_lazy('contacts')


class UpdateContact(UpdateView):
    model = Contact
    fields = '__all__'


class DeleteContact(DeleteView):
    model = Contact
    success_url = reverse_lazy('contacts')


class SearchResultsView(generic.ListView):
    model = Contact
    #template_name = 'adress_book/search_results.html'
 
    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Contact.objects.filter(
            Q(name__icontains=query) | Q(phone__icontains=query) | Q(email__icontains=query)
        )
        return object_list


class DaysToBirthdayResultsView(generic.ListView):
    model = Contact
    #template_name = 'adress_book/days_to_birthday_results.html'
 
    def get_queryset(self): # новый
        query = self.request.GET.get('q1')
        today = datetime.now().date()
        needed = today + timedelta(days=int(query))
        needed_str = needed.strftime("%m-%d")

        object_list = Contact.objects.all()
        res_list = object_list.filter(birthday__contains= needed_str)
        
        return res_list