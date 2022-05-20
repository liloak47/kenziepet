from urllib import response
from rest_framework.views import APIView
from rest_framework.views import Response
from .models import Animal
from .serializers import AnimalSerializer
from .serializers import CharacteristcSerializer
# Create your views here.

class AnimalView(APIView):
    def get(self, request):
        animal = Animal.objects.all()
        seriealizer = AnimalSerializer(animal, many = True)
        
        return Response(seriealizer.data)
