from mypet.api.serializers import PetSerializer, PetTypeSerializer, BreedSerializer
from mypet.api.models import Pet


class PetService:

    def get(id):
        pet_instance = Pet.objects.get(id=id)
        pet_serializer = PetSerializer(pet_instance)
        return pet_serializer.data

    def create(data):
        pet_serializer = PetSerializer(data=data)
        pet_serializer.is_valid(raise_exception=True)
        pet_serializer.save()
        return pet_serializer.data

    def update(data, id):
        pet_instance = Pet.objects.get(id=id)
        pet_serializer = PetSerializer(pet_instance, data=data, partial=True)
        pet_serializer.is_valid(raise_exception=True)
        pet_serializer.save()
        return pet_serializer.data

    def list(user):
        pet_list_instance = Pet.objects.filter(user=user, is_active=True)
        pet_serializer = PetSerializer(pet_list_instance, many=True)
        return pet_serializer.data

    def list_complete(user):
        pass
