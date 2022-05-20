from rest_framework import urlpatterns
from rest_framework.urls import path
from .views import AnimalView, AnimalRetriveView



urlpatterns = [
    path('animals/', AnimalView.as_view()),
    path('animals/<int:animal_id>/', AnimalRetriveView.as_view()),
]