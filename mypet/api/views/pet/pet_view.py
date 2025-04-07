from rest_framework.viewsets import ModelViewSet, ViewSet
from mypet.api.models import PetType, Pet, Breed, PetFeatures
from mypet.api.serializers import (
    PetTypeSerializer,
    PetSerializer,
    BreedSerializer,
    PetFeaturesSerializer,
)
from rest_framework.permissions import IsAuthenticated
from mypet.api.services import PetService
from rest_framework.response import Response
from rest_framework import status

class PetTypeViewSet(ModelViewSet):
    queryset = PetType.objects.filter(is_active=True)
    serializer_class = PetTypeSerializer
    permission_classes = [IsAuthenticated]


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.filter(is_active=True)
    serializer_class = BreedSerializer
    permission_classes = [IsAuthenticated]


class PetFeaturesViewSet(ModelViewSet):
    queryset = PetFeatures.objects.filter(is_active=True)
    serializer_class = PetFeaturesSerializer
    permission_classes = [IsAuthenticated]


class PetViewSet(ViewSet):
    
    def list(self, request):
        user = request.user.id
        pet_list_data = PetService.list(user=user)
        return Response(pet_list_data, status=status.HTTP_200_OK)   
