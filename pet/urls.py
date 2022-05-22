from rest_framework import urlpatterns
from rest_framework.urls import path
from .views import AnimalView, AnimalRetriveView, AnimalCreateView, CreateGroup, GetAllGroups



urlpatterns = [
    path('animals/', AnimalView.as_view()),
    path('animals/<int:animal_id>/', AnimalRetriveView.as_view()),
    path('animal/create/', AnimalCreateView.as_view()),
    path('group/create/', CreateGroup.as_view()),
    path('groups/', GetAllGroups.as_view())

]