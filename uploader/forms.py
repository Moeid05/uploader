from django import forms
from django.core.validators import FileExtensionValidator


class UploadFileForm(forms.Form):
    file_name = forms.CharField(
        label='enter a name for file',
        max_length=12,
        required=False,
        widget=forms.TextInput(attrs={'id': 'file-name'})
    )
    file = forms.FileField(
        label='Select a file',
        widget=forms.FileInput(attrs={'id': 'file-input'}),
        validators=[FileExtensionValidator(allowed_extensions=[
            'pdf', 'docx', 'txt',
            'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'ico',
            'webp', 'svg', 'psd', 'ai', 'cdr', 'eps'
        ])]
    )
    expiration_date = forms.ChoiceField(
        label='Expiration Date',
        choices=[
            (1, '1 day'),
            (3, '3 days'),
            (7, '1 week'),
            (14, '2 weeks'),
            (30, '1 month')
        ],
        widget=forms.Select(attrs={'id': 'expiration-date'})
    )