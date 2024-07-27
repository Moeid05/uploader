from django.contrib import admin
from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.uploader.as_view(), name='upload'),
    re_path(r'^(?P<link>[\w-]+)/', views.downloader, name='download'),
]
