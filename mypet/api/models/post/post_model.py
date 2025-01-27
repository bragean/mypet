from django.db.models import CharField, ImageField, ForeignKey, CASCADE, SET_NULL
from ..base.base_model import Base
from ..pet.pet_model import Pet
from ..location.location_model import District
from ..location.point_model import Point


class Post(Base):
    title = CharField(max_length=100)
    description = CharField(max_length=255)
    pet = ForeignKey(Pet, on_delete=CASCADE)
    district = ForeignKey(District, on_delete=SET_NULL, null=True)
    point = ForeignKey(Point, on_delete=SET_NULL, null=True)


class PostImage(Base):
    name = CharField(max_length=32, blank=True)
    image = ImageField(upload_to="post/", null=True, blank=True)
