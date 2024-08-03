from django.core.management.base import BaseCommand
from datetime import datetime
from uploader.models import File

class Command(BaseCommand):
    help = 'Delete expired files'

    def handle(self, *args, **options):
        now = datetime.now()
        expired_files = File.objects.filter(Expiration_date__lte=now)
        expired_files.delete()
        self.stdout.write(self.style.SUCCESS('Expired files deleted'))