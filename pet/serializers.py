from rest_framework import serializers
from pet.models import Animal, Characteristc, Group


class GroupSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    scientific_name = serializers.CharField()

    def create(self,validated_data):
        group_instance = Group.objects.create(**validated_data)
        return group_instance

class CharacteristcSerializer(serializers.Serializer):
    name = serializers.CharField()
    
    def create(self, validated_data):
        character_instance = Characteristc.objects.create(name=validated_data)
        character_instance.animals.add(self)
        return character_instance

class AnimalSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField()
    group = GroupSerializer()
    characteristc_set = CharacteristcSerializer(many=True)

    def create(self, validated_data):
        group_data = validated_data.pop('group')
        characters_data = validated_data.pop('characteristc_set')
        group_create = GroupSerializer.create(self,group_data)

        animal_instance = Animal.objects.create(**validated_data,  group=group_create)

        for character in characters_data:
            CharacteristcSerializer.create(animal_instance,character['name'])
        return animal_instance

    