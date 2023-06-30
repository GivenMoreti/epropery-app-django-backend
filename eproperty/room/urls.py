from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),


    path('',views.get_rooms,name='rooms')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)