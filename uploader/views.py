from django.shortcuts import render, redirect
from django.views import View
from .forms import UploadFileForm
from .models import File
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
def uploader(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            got = File(fileField=form.cleaned_data['file'])
            got.save
            return redirect('download',link='link')
    else:
        form = UploadFileForm()
    return render(request, 'uploader/pages/upload.html', {'form': form})

def downloader(request,link) :
    direct_link = 'https://example.com/direct-link'
    forum_link = 'https://example.com/forum-link'
    return render(request, 'uploader/pages/download.html', {
        'direct_link': direct_link,
        'forum_link': forum_link,
    })