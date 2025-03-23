from mypet.api.models import Lost, PostImage
from mypet.api.serializers import (
    LostSerializer,
    LostImageSerializer,
    PetSerializer,
    PostImageSerializer,
    PointSerializer,
)
from ..location.point_service import PointService


class LostService:

    def create(data):
        lost_serializer = LostSerializer(data=data)
        lost_serializer.is_valid(raise_exception=True)
        lost_serializer.save()
        return lost_serializer.data

    def create_complete(data, user):
        data["user"] = user
        data["owner"] = user
        point_data = PointService.create(data=data)
        data["point"] = point_data["id"]
        print(data)
        return LostService.create(data)

    def list(user):
        lost_instance_list = Lost.objects.filter(owner=user, is_active=True)
        lost_serializer_list = LostSerializer(lost_instance_list, many=True)
        return lost_serializer_list.data

    def get(id):
        lost_instance = Lost.objects.get(id=id)
        lost_serializer = LostSerializer(lost_instance)
        return lost_serializer.data

    def exists(id):
        return Lost.objects.filter(id=id).exists()

    def has_images(id):
        return PostImage.objects.filter(post=id).exists()

    def get_images(id):
        return PostImage.objects.filter(post=id)

    def list_with_images(user):
        lost_instance_list = Lost.objects.filter(owner=user, is_active=True)
        lost_list_serializer = []
        for lost_instance in lost_instance_list:
            pet_data = None
            point_data = None
            images = []
            if lost_instance.pet is None:
                pet_data = PetSerializer(lost_instance.pet).data
            if LostService.has_images(lost_instance.id):
                post_images_list = LostService.get_images(lost_instance.id)
                images = PostImageSerializer(post_images_list, many=True).data
            if lost_instance.point is not None:
                point_data = PointSerializer(lost_instance.point).data

            lost_list_serializer.append(
                {
                    "id": lost_instance.id,
                    "owner": lost_instance.owner.id,
                    "owner_name": lost_instance.owner.name,
                    "title": lost_instance.title,
                    "description": lost_instance.description,
                    "district": (
                        lost_instance.district.id
                        if lost_instance.district is not None
                        else None
                    ),
                    "district_name": (
                        lost_instance.district.name
                        if lost_instance.district is not None
                        else ""
                    ),
                    "point": point_data,
                    "contact_number": lost_instance.contact_number,
                    "date": lost_instance.date,
                    "time": lost_instance.time,
                    "pet": pet_data,
                    "images": images,
                }
            )

        return lost_list_serializer
