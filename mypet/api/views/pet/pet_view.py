from rest_framework.viewsets import ModelViewSet
from mypet.api.models import PetType, Pet, Breed, PetFeatures
from mypet.api.serializers import (
    PetTypeSerializer,
    PetSerializer,
    BreedSerializer,
    PetFeaturesSerializer,
)
from rest_framework.permissions import IsAuthenticated


class PetTypeViewSet(ModelViewSet):
    queryset = PetType.objects.filter(is_active=True)
    serializer_class = PetTypeSerializer
    permission_classes = [IsAuthenticated]


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.filter(is_active=True)
    serializer_class = BreedSerializer
    permission_classes = [IsAuthenticated]


class PetViewSet(ModelViewSet):
    queryset = Pet.objects.filter(is_active=True)
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]


class PetFeaturesViewSet(ModelViewSet):
    queryset = PetFeatures.objects.filter(is_active=True)
    serializer_class = PetFeaturesSerializer
    permission_classes = [IsAuthenticated]
