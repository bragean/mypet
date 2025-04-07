from mypet.api.models import Lost
from .post_serializer import PostImageSerializer
from ..pet.pet_serializer import PetSerializer, PetStateSerializer
from ..location.point_model import PointSerializer
from rest_framework.serializers import (
    Serializer,
    ModelSerializer,
    CharField,
    UUIDField,
    EmailField,
    PrimaryKeyRelatedField,
    TimeField,
    DateField,
    BooleanField,
    IntegerField,
)


class LostSerializer(ModelSerializer):
    class Meta:
        model = Lost
        exclude = ["created", "modified", "created_by", "modified_by", "is_active"]


class LostCreateSerializer(Serializer):
    title = CharField(max_length=100)
    description = CharField(max_length=255)
    contact_number = CharField(max_length=20, allow_blank=True)
    date = DateField(allow_null=True)
    time = TimeField(allow_null=True)
    district = UUIDField()
    pet = UUIDField()
    lat = CharField(max_length=32, allow_blank=True)
    lon = CharField(max_length=32, allow_blank=True)


class LostImageSerializer(Serializer):
    id = UUIDField(read_only=True)
    owner = UUIDField(read_only=True)
    title = CharField(max_length=100)
    description = CharField(max_length=255)
    district = UUIDField(read_only=True)
    district_name = CharField(max_length=50)
    contact_number = CharField(max_length=20, allow_blank=True)
    date = DateField(allow_null=True)
    time = TimeField(allow_null=True)
    pet = PetSerializer(read_only=True, allow_null=True)
    point = PointSerializer(read_only=True, allow_null=True)
    images = PostImageSerializer(read_only=True, many=True, allow_null=True)


class LostListSerializer(Serializer):
    id = UUIDField(read_only=True)
    description = CharField(max_length=255)
    district = UUIDField(read_only=True)
    district_name = CharField(max_length=50)
    date = DateField(allow_null=True)
    has_reward = BooleanField()
    reward = IntegerField()
    pet_type_name = CharField()
    pet_name = CharField(max_length=20)
    pet_image = CharField()
    pet_state = PetStateSerializer(read_only=True)
