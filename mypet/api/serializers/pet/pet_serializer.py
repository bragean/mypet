from mypet.api.models import PetType, Breed, Pet, PetFeatures
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (
    Serializer,
    ModelSerializer,
    CharField,
    UUIDField,
    EmailField,
    PrimaryKeyRelatedField,
    TimeField,
    DateField,
)


class PetTypeSerializer(ModelSerializer):
    class Meta:
        model = PetType
        exclude = ["created", "modified", "created_by", "modified_by", "is_active"]


class BreedSerializer(ModelSerializer):
    class Meta:
        model = Breed
        exclude = ["created", "modified", "created_by", "modified_by", "is_active"]


class PetSerializer(ModelSerializer):
    class Meta:
        model = Pet
        exclude = ["created", "modified", "created_by", "modified_by", "is_active"]


class PetFeaturesSerializer(ModelSerializer):
    class Meta:
        model = PetFeatures
        exclude = ["created", "modified", "created_by", "modified_by", "is_active"]


class PetCompleteSerializer(Serializer):
    id = UUIDField(read_only=True)
    name = CharField(max_length=20)
    description = CharField(max_length=255)
    color = CharField(max_length=20)
    breed = BreedSerializer(read_only=True)
    pet_type = PetTypeSerializer(read_only=True)
    pet_features = PetFeaturesSerializer(read_only=True, many=True)
