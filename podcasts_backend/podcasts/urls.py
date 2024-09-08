from django.urls import path
from . import views


urlpatterns = [
    path('echo/', views.EchoView.as_view(), name='echo'),
]
