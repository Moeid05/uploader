from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import File
import uuid
def generate_link(file_name):
    return f"{file_name}-{uuid.uuid4()}"
def uploader(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            loaded = form.cleaned_data['file']
            file_name = loaded.name
            link = generate_link(file_name)
            ins = File(fileField=loaded,link=link)
            ins.save()
            return redirect('download',link=link)
    else:
        form = UploadFileForm()
    return render(request, 'uploader/pages/upload.html', {'form': form})

def downloader(request,link) :
    direct_link = link
    forum_link = 'idk'
    return render(request, 'uploader/pages/download.html', {
        'direct_link': direct_link,
        'forum_link': forum_link,
    })