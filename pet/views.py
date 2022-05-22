from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .models import Animal, Group
from .serializers import AnimalSerializer, GroupSerializer
from django.core.exceptions import ObjectDoesNotExist
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
                return Response({'message':'animal deletado'}, status=status.HTTP_204_NO_CONTENT)
            except ObjectDoesNotExist:
                return  Response({'message': 'not found animal'}, status=status.HTTP_404_NOT_FOUND)

class AnimalCreateView(APIView):
    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class CreateGroup(APIView):
    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

class GetAllGroups(APIView):
    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)