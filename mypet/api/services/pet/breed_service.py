from mypet.api.serializers import BreedSerializer
from mypet.api.models import Breed


class BreedService():

    def exists(id):
        return Breed.objects.filter(id=id, is_active=True)

    def get(id):
        breed_instance = Breed.objects.get(id=id)
        breed_serializer = BreedSerializer(breed_instance)
        return breed_serializer.data

    def create(data):
        breed_serializer = BreedSerializer(data=data)
        breed_serializer.is_valid(raise_exception=True)
        breed_serializer.save()
        return breed_serializer.data

    def update(data, id):
        breed_instance = Breed.objects.get(id=id)
        breed_serializer = BreedSerializer(breed_instance, data=data, partial=True)
        breed_serializer.is_valid(raise_exception=True)
        breed_serializer.save()
        return breed_serializer.data

    def list(user):
        breed_list_instance = Breed.objects.filter(user=user, is_active=True)
        breed_serializer = BreedSerializer(breed_list_instance, many=True)
        return breed_serializer.data

