from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FileForm
from .models import File


TYPES_FILE = {'all': 'All',
              'doc': 'Documents',
              'tb': 'Tables',
              'zip': 'Archives',
              'img': 'Images',
              'mp3': 'Audio',
              'avi': 'Video',
              'dr': 'Other'}


@login_required(redirect_field_name='file_list')
def delete_file(request, pk):
    if request.method == 'POST':
        file = File.objects.get(pk=pk)
        file.delete()
    return redirect('file_list')


@login_required(redirect_field_name='file_list')
def upload_file(request):
    files = File.objects.filter(author=request.user)
    type_files = TYPES_FILE
    files_select = request.POST.get('file_categories', 'All')
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES, instance=File(author=request.user))
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileForm()
    if files_select == 'All':
        files = File.objects.filter(author=request.user)
        # files = File.objects.all()
        form = FileForm()
    else:
        # files = File.objects.filter(type=(list(type_files.keys())[list(type_files.values()).index(files_select)]))
        files = File.objects.filter(type=(list(type_files.keys())[list(type_files.values()).index(files_select)])).filter(author=request.user)
        form = FileForm()
    return render(request, 'file_list.html', {
        'form': form,
        'files': files,
        'type_files': type_files,
    })
