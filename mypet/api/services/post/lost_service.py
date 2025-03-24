from mypet.api.models import Lost, PostImage
from mypet.api.serializers import (
    LostSerializer,
    LostImageSerializer,
    PetSerializer,
    PostImageSerializer,
    PointSerializer,
)
from ..location.point_service import PointService
from ..pet.pet_service import PetService


class LostService:
    def get(id):
        lost_instance = Lost.objects.get(id=id)
        lost_serializer = LostSerializer(lost_instance)
        return lost_serializer.data

    def get_complete(id):
        lost_instance = Lost.objects.get(id=id)
        images = []
        if LostService.has_images(lost_instance.id):
            post_images_list = LostService.get_images(lost_instance.id)
            images = PostImageSerializer(post_images_list, many=True).data
        lost_data = {
            "id": lost_instance.id,
            "owner": lost_instance.owner.id,
            "owner_name": lost_instance.owner.name,
            "title": lost_instance.title,
            "description": lost_instance.description,
            "district": (
                None if lost_instance.district is None else lost_instance.district.id
            ),
            "district_name": (
                "" if lost_instance.district is None else lost_instance.district.name
            ),
            "point": (
                None
                if lost_instance.point is None
                else PointService.get(id=lost_instance.point.id)
            ),
            "contact_number": lost_instance.contact_number,
            "date": lost_instance.date,
            "time": lost_instance.time,
            "pet": (
                None
                if lost_instance.pet is None
                else PetService.get(id=lost_instance.pet.id)
            ),
            "images": images,
        }
        return lost_data

    def retrieve(id):
        lost_instance = Lost.objects.get(id=id)
        lost_serializer = LostSerializer(lost_instance)
        return lost_serializer.data

    def exists(id):
        return Lost.objects.filter(id=id).exists()

    def create(data):
        lost_serializer = LostSerializer(data=data)
        lost_serializer.is_valid(raise_exception=True)
        lost_serializer.save()
        return lost_serializer.data

    def update(data, id):
        lost_instance = Lost.objects.get(id=id)
        lost_serializer = LostSerializer(lost_instance, data=data, partial=True)
        lost_serializer.is_valid(raise_exception=True)
        lost_serializer.save()
        return lost_serializer.data

    def update_complete(data, id):
        # update_point
        PointService.update(data["point"], data["point"]["id"])
        del(data["point"])
        LostService.update(data, id)
        return LostService.get_complete(id)

    def create_complete(data, user):
        data["user"] = user
        data["owner"] = user
        point_data = PointService.create(data=data)
        data["point"] = point_data["id"]
        return LostService.create(data)

    def list(user):
        lost_instance_list = Lost.objects.filter(owner=user, is_active=True)
        lost_serializer_list = LostSerializer(lost_instance_list, many=True)
        return lost_serializer_list.data

    def has_images(id):
        return PostImage.objects.filter(post=id).exists()

    def get_images(id):
        return PostImage.objects.filter(post=id)

    def list_complete(user):
        lost_instance_list = Lost.objects.filter(owner=user, is_active=True)
        lost_list_data = []
        for lost_instance in lost_instance_list:
            print(lost_instance)
            lost_data = LostService.get_complete(lost_instance.id)
            lost_list_data.append(lost_data)

        return lost_list_data
