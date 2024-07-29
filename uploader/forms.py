from django import forms
from django.core.validators import FileExtensionValidator


class UploadFileForm(forms.Form):
    file = forms.FileField(
        label='Select a file',
        widget=forms.FileInput(attrs={'id': 'file-input'})
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