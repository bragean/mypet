from django.db.models import (
    CharField,
    ImageField,
    ForeignKey,
    CASCADE,
    SET_NULL,
    DateField,
    TimeField,
)
from ..base.base_model import Base
from ..pet.pet_model import Pet
from ..location.location_model import District
from ..location.point_model import Point
from mypet.users.models import User


class Post(Base):
    owner = ForeignKey(User, on_delete=CASCADE)
    title = CharField(max_length=100)
    description = CharField(max_length=255)
    pet = ForeignKey(Pet, on_delete=CASCADE)
    district = ForeignKey(District, on_delete=SET_NULL, null=True)
    point = ForeignKey(Point, on_delete=SET_NULL, null=True)
    contact_number = CharField(max_length=20, blank=True)
    date = DateField(null=True)
    time = TimeField(null=True)


class PostImage(Base):
    post = ForeignKey(Post, on_delete=CASCADE)
    name = CharField(max_length=32, blank=True)
    image = ImageField(upload_to="post/", null=True, blank=True)
