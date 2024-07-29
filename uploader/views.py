from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import File
import uuid
from django.http import FileResponse
def generate_link(file_name):
    return f"{file_name}-{uuid.uuid4()}"
def uploader_page(request):
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

def downloader_page(request,link) :
    direct_link = link
    forum_link = 'idk'
    return render(request, 'uploader/pages/download.html', {
        'direct_link': direct_link,
        'forum_link': forum_link,
    })

def download(request, link):
    file_obj = File.objects.get(link=link)
    file_path = file_obj.fileField.path
    file_name = file_obj.fileField.name
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)