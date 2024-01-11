from django.contrib import admin
from django.urls import path
from app import views
from .views import *
urlpatterns = [
    path('',add_song, name='add_song'),
    path('song_list/', song_list, name='song_list'),
    path('update_song/<int:song_id>/', update_song, name='update_song'),
    # Add other URL patterns as needed
]
