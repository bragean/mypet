from mypet.api.models import PetType, Breed, Pet, PetFeatures
from rest_framework.serializers import ModelSerializer


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
