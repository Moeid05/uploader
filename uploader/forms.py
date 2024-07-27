from django import forms
from django.core.validators import FileExtensionValidator


class UploadFileForm(forms.Form):
    file = forms.FileField(
        label='Select a file',
        widget=forms.FileInput(attrs={'id': 'file-input'})
    )