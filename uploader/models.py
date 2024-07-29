from django.db import models
from datetime import datetime, timedelta
class File(models.Model) :
    fileField = models.FileField(upload_to='uploads/%Y/%m/%d')
    link = models.CharField(max_length=255, blank=True, null=True,unique=True)
    create_data = models.DateTimeField(auto_now_add=True)
    Expiration_date = models.DateTimeField(default=datetime.now() + timedelta(days=1))
    class Meta:
        app_label = 'uploader'