from django.urls import path
from . import views

urlpatterns = [
    path('songs/search/', views.search_song, name='search_song'),
]
