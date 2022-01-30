from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage


class FileManager(TemplateView):
    template_name = 'file_manager.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        file_system = FileSystemStorage()
        name = file_system.save(uploaded_file.name, uploaded_file)
        context['url'] = file_system.url(name)
    return render(request, 'upload.html', context)
