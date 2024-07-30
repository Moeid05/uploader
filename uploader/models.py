from django.db import models
from datetime import datetime, timedelta
class File(models.Model):
    fileName = models.CharField(max_length=12, blank=True, null=True)
    fileField = models.FileField(upload_to='uploads/%Y/%m/%d')
    link = models.CharField(max_length=255, blank=True, null=True, unique=True)
    create_data = models.DateTimeField(auto_now_add=True)
    Expiration_date = models.DateTimeField(default=datetime.now() + timedelta(days=1))

    def save(self, *args, **kwargs):
        if not self.fileName:
            self.fileName = self.fileField.name
        super().save(*args, **kwargs)
    
    class Meta:
        app_label = 'uploader'