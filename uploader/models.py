from django.db import models

class File(models.Model) :
    fileField = models.FileField()
    class Meta:
        app_label = 'uploader'