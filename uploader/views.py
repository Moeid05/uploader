from django.shortcuts import render, redirect
from django.views import View
from .forms import UploadFileForm
from .models import File
from django.contrib import messages
from django.http import JsonResponse , HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class uploader(View) :
    def get(self, request) :
        return render(request, "uploader/pages/upload.html", context={'form': UploadFileForm()})
    
    def post(self, request) :
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = File(fileField=request.FILES["file"])
            instance.save()
            return redirect(instance)
        messages.error(request, 'Error uploading file.')
        return render(request, 'uploader/pages/upload.html', {'form': form})

def downloader(request, link) :
    return render(request, 'uploader/pages/download.html', {'uploaded_file_url': link})