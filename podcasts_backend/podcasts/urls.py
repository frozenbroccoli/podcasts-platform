from django.urls import path
from . import views


urlpatterns = [
    path('echo/', views.EchoView.as_view(), name='echo'),
    path('search/', views.PodcastSearchView.as_view(), name='search'),
    path('episodes/', views.PodcastEpisodesView.as_view(), name='episodes'),
]
