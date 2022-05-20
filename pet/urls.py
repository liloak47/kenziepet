from rest_framework import urlpatterns
from rest_framework.urls import path
from .views import AnimalView 


urlpatterns = [
    path('animals/', AnimalView.as_view())
]