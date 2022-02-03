from django import forms
from .models import File


class FileForm(forms.ModelForm):

    class Meta:
        comment = forms.CharField(required=True)
        model = File
        fields = ('name', 'type', 'comment', 'url')
