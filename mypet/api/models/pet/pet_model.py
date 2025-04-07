from django.db.models import (
    CharField,
    ImageField,
    ForeignKey,
    CASCADE,
    BooleanField,
    PositiveIntegerField,
)
from ..base.base_model import Base
from mypet.users.models import User


class PetType(Base):
    name = CharField(max_length=20)
    description = CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Breed(Base):
    name = CharField(max_length=20)
    image = ImageField(upload_to="media/breed/", null=True, blank=True)
    pet_type = ForeignKey(PetType, on_delete=CASCADE)

    def __str__(self):
        return self.name


class PetState(Base):
    name = CharField(max_length=20, unique=True)
    color = CharField(max_length=20)
    code = CharField(max_length=20, unique=20)


class Pet(Base):
    user = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=20)
    description = CharField(max_length=255)
    color = CharField(max_length=255)
    breed = ForeignKey(Breed, on_delete=CASCADE)
    pet_state = ForeignKey(PetState, on_delete=CASCADE)
    reward = PositiveIntegerField(default=0)
    has_reward = BooleanField(default=False)

    def __str__(self):
        return self.name


class PetFeatures(Base):
    name = CharField(max_length=20)
    description = CharField(max_length=100)
    pet = ForeignKey(Pet, on_delete=CASCADE)

    def __str__(self):
        return self.name
