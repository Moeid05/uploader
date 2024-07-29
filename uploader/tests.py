# tests/test_commands.py
from django.test import TestCase
from django.core.management import call_command
from uploader.models import File
from datetime import datetime, timedelta

class DeleteExpiredFilesTest(TestCase):
    def setUp(self):
        # Create some test files
        self.file1 = File.objects.create(fileField='test1.txt', Expiration_date=datetime.now() + timedelta(days=1))
        self.file2 = File.objects.create(fileField='test2.txt', Expiration_date=datetime.now() - timedelta(days=1))
        self.file3 = File.objects.create(fileField='test3.txt', Expiration_date=datetime.now() + timedelta(days=30))

    def test_delete_expired_files(self):
        # Call the command
        call_command('delete_expired_files')

        # Check that the expired file was deleted
        self.assertFalse(File.objects.filter(id=self.file2.id).exists())

        # Check that the non-expired files were not deleted
        self.assertTrue(File.objects.filter(id=self.file1.id).exists())
        self.assertTrue(File.objects.filter(id=self.file3.id).exists())

    def test_delete_expired_files_multiple_expired(self):
        # Create another expired file
        self.file4 = File.objects.create(fileField='test4.txt', Expiration_date=datetime.now() - timedelta(days=1))

        # Call the command
        call_command('delete_expired_files')

        # Check that both expired files were deleted
        self.assertFalse(File.objects.filter(id=self.file2.id).exists())
        self.assertFalse(File.objects.filter(id=self.file4.id).exists())

        # Check that the non-expired files were not deleted
        self.assertTrue(File.objects.filter(id=self.file1.id).exists())
        self.assertTrue(File.objects.filter(id=self.file3.id).exists())