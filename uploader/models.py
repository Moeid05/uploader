from django.db import models

class File(models.Model) :
    fileField = models.FileField(upload_to='uploads/%Y/%m/%d')
    link = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        app_label = 'uploader'