from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.urls import reverse_lazy
from .models import Note


class CustomLoginView(LoginView):
    """
    Display a login page.

    **Template:**

    :template:'notes/login.html'
    """
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        """
        Redirect after authentication
        """
        return reverse_lazy('notes')


class RegisterPage(FormView):
    """
        Display a registration page.

        **Template:**

        :template:'notes/register.html'
        """
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        """
        Validation of the given data for registration
        """
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        """
        Checking if user is authenticated
        """
        if self.request.user.is_authenticated:
            return redirect('notes')
        return super(RegisterPage, self).get(*args, **kwargs)


class Notes(LoginRequiredMixin, ListView):
    """
    Display notes from the database.
    Suggest actions for the notes and variants for notes representation set

    **Template:**

        :template:'notes/notes.html'

    **Model:**

        :model:'models.Note'

    **Context:**

        ''notes''
            A set of all notes in the database
    """
    model = Note
    context_object_name = 'all_records'
    template_name = 'notes.html'

    def get_context_data(self, **kwargs):
        """
        Proceed context data in respect to the chosen actions
        :param kwargs: 'all content data from the database'
        :return: 'proceeded content'
        """
        context = super().get_context_data(**kwargs)
        context['all_records'] = context['all_records'].order_by('-created')
        context['notes_by_author'] = context['all_records'].filter(author=self.request.user).order_by('-created')
        context['notes'] = context['notes_by_author']

        search_input = self.request.GET.get('search') or ''  # getting chosen options
        scope = self.request.GET.get('scope')  # getting chosen options
        input_filter = self.request.GET.get('filter')  # getting chosen options
        if search_input and scope == 'all':  # search for all authors
            if input_filter == "text":  # search for all authors in texts
                context['notes'] = context['all_records'].filter(text__icontains=search_input).order_by('-created')
            else:  # search for all authors in tags
                context['notes'] = context['all_records'].filter(tags__icontains=search_input).order_by('-created')
        elif search_input and scope == 'current':  # search for current author
            if input_filter == "text":  # search for current author in texts
                context['notes'] = context['notes_by_author'].filter(text__icontains=search_input).order_by('-created')
            else:  # search for current author in tags
                context['notes'] = context['notes_by_author'].filter(tags__icontains=search_input).order_by('-created')
        else:
            if scope == "all":  # default notes list set for all user
                context['notes'] = context['all_records']
        context['notes'] = context['notes'][:10]  # limiting number of notes to 10 on the page
        context['search_input'] = search_input
        context['scope'] = scope
        context['input_filter'] = input_filter

        return context


class Detail(LoginRequiredMixin, DetailView):
    """
    Display the note in detail
    """
    model = Note
    template_name = "detail.html"

    def book_detail_view(request, primary_key):
        note = get_object_or_404(Note, pk=primary_key)  # getting the note record from the database
        return render(request, 'detail.html', context={'note': note})


class NoteCreate(LoginRequiredMixin, CreateView):
    """
    Create valid note instance from filled form and add it to the database
    """
    model = Note
    fields = ['title', 'text', 'tags']
    success_url = reverse_lazy('notes')
    template_name = "note_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user  # getting authenticated user's name as 'author' for the note
        return super(NoteCreate, self).form_valid(form)


class NoteUpdate(LoginRequiredMixin, UpdateView):
    """
    Update the existing note record
    """
    model = Note
    fields = ['title', 'text', 'tags']
    success_url = reverse_lazy('notes')
    template_name = "note_form.html"


class NoteDelete(LoginRequiredMixin, DeleteView):
    """
    Delete the note from the database
    """
    model = Note
    context_object_name = 'note'
    success_url = reverse_lazy('notes')
    template_name = 'delete.html'

