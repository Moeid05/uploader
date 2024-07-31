from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from uploader.models import File
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    myFiles = models.ManyToManyField(File, blank=True,related_name='my_files')
    objects = CustomUserManager()