from ast import Delete
from urllib import request, response
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .models import Animal
from .serializers import AnimalSerializer
from .serializers import CharacteristcSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
# Create your views here.

class AnimalView(APIView):
    def get(self, request):
        animal = Animal.objects.all()
        seriealizer = AnimalSerializer(animal, many = True)
        return Response(seriealizer.data, status=status.HTTP_200_OK)


class AnimalRetriveView(APIView):
    def get(self, request, animal_id=''):
        if animal_id:
            try:
                animal = Animal.objects.get(id=animal_id)
                seriealizer = AnimalSerializer(animal)
                return Response(seriealizer.data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response({'message':'err not found animal'}, status=status.HTTP_404_NOT_FOUND)
    def delete(self,request, animal_id=''):
        if(animal_id):
            try:
                animal = Animal.objects.get(id=animal_id)
                animal.delete()
                return Response({'message':'animal deletado'})
            except ObjectDoesNotExist:
                return  Response({'message': 'not found animal'}, status=status.HTTP_404_NOT_FOUND)