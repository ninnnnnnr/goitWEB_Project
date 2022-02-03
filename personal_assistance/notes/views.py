from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from django.shortcuts import redirect, render


from .models import Note



class CustomLoginView(LoginView):
    template_name = 'notes/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('notes')


class RegisterPage(FormView):
    template_name = 'notes/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes')
        return super(RegisterPage, self).get(*args, **kwargs)


class Notes(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/notes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = context['notes'].order_by('-created')
        context['notes_by_author'] = context['notes'].filter(author=self.request.user).order_by('-created')

        search_input = self.request.GET.get('search') or ''
        scope = self.request.GET.get('scope')
        input_filter = self.request.GET.get('filter')
        if search_input and scope == 'all':
            if input_filter == "text":
                context['notes'] = context['notes'].filter(text__icontains=search_input).order_by('-created')
            else:
                context['notes'] = context['notes'].filter(tags__icontains=search_input).order_by('-created')
        elif search_input and scope == 'current':
            if input_filter == "text":
                context['notes'] = context['notes_by_author'].filter(text__icontains=search_input).order_by('-created')
            else:
                context['notes'] = context['notes_by_author'].filter(tags__icontains=search_input).order_by('-created')
        else:
            if scope == "current":
                context['notes'] = context['notes_by_author']
        context['notes'] = context['notes'][:10]




        context['search_input'] = search_input
        context['scope'] = scope
        context['input_filter'] = input_filter

        return context



class Detail(LoginRequiredMixin, DetailView):
    model = Note
    template_name = "notes/detail.html"

    def book_detail_view(request, primary_key):
        note = get_object_or_404(Note, pk=primary_key)
        return render(request, 'notes/detail.html', context={'note': note})


class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'text', 'tags']
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NoteCreate, self).form_valid(form)


class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'text', 'tags']
    success_url = reverse_lazy('notes')


class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    context_object_name = 'note'
    success_url = reverse_lazy('notes')
    template_name = 'notes/delete.html'

