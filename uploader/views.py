from django.shortcuts import render, redirect
from django.http import FileResponse
from .forms import UploadFileForm
from .models import File
import uuid
from django.contrib.auth import get_user_model
from django.http import Http404


User = get_user_model()  # Get the active user model

def generate_link(file_name):
    return f"{file_name}-{uuid.uuid4()}"

def uploader_page(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            loaded = form.cleaned_data['file']
            file_name = form.cleaned_data['file_name']
            link = generate_link(file_name)
            instance = File(fileName=file_name, fileField=loaded, link=link)
            instance.save()
            if request.user.is_authenticated:
                request.user.myFiles.add(instance)  # Use the correct related_name
            return redirect('download', link=link)
    else:
        form = UploadFileForm()
    return render(request, 'uploader/pages/upload.html', {'form': form})

def downloader_page(request, link):
    files = File.objects.all()
    links = [file.link for file in files]
    if link in links :
        return render(request, 'uploader/pages/download.html', {
            'link' : link,
        })
    else : 
        raise Http404('Page not found')

def download(request, link):
    file_obj = File.objects.get(link=link)
    file_path = file_obj.fileField.path
    file_name = file_obj.fileField.name
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)