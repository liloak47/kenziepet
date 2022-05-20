from rest_framework import serializers

from pet.models import Characteristc


class GroupSerializer(serializers.Serializer):
    name = serializers.CharField()
    scientific_name = serializers.CharField()

class CharacteristcSerializer(serializers.Serializer):
    name = serializers.CharField()

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.FloatField()
    sex = serializers.CharField()
    group = GroupSerializer()
    characteristc_set = CharacteristcSerializer(many=True)