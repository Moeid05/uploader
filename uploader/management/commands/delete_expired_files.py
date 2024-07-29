from django.core.management.base import BaseCommand
from django.db.models import Q
from datetime import datetime
from uploader.models import File
import os

class Command(BaseCommand):
    help = 'Delete expired files'

    def handle(self, *args, **options):
        now = datetime.now()
        expired_files = File.objects.filter(Expiration_date__lte=now)
        # for file in expired_files:
        #     # Delete the actual file
        #     os.remove(file.fileField.path)
        expired_files.delete()
        self.stdout.write(self.style.SUCCESS('Expired files deleted'))