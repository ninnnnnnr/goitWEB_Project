from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Contact

import re
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

    def form_valid(self, form):
        pattern = r'\d{12}'
        if not re.fullmatch(pattern, form.cleaned_data['phone']):
            form.add_error('phone', 'Phone number should contain only digits')
            return self.form_invalid(form)
        return super(AddContact, self).form_valid(form)


class UpdateContact(UpdateView):
    model = Contact
    fields = '__all__'

    def form_valid(self, form):
        pattern = r'\d{12}'
        if not re.fullmatch(pattern, form.cleaned_data['phone']):
            form.add_error('phone', 'Phone number should contain only digits')
            return self.form_invalid(form)
        return super(UpdateContact, self).form_valid(form)


class DeleteContact(DeleteView):
    model = Contact
    success_url = reverse_lazy('contacts')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = reverse_lazy('contacts')
            return HttpResponseRedirect(url)
        else:
            return super(DeleteContact, self).post(request, *args, **kwargs)


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