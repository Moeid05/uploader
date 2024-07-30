from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.uploader_page, name='upload'),
    path('<str:link>/', views.downloader_page, name='download'),
    path('download/<str:link>/',views.download),
    path('accounts/',include('users.urls')),
]