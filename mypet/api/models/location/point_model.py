from .coordinate_model import Coordinate
from ..base.base_model import Base
from mypet.users.models import User
from django.db.models import Model, OneToOneField, CASCADE, CharField, ForeignKey, DecimalField


class Point(Base):
    user = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=50, blank=True)
    description = CharField(max_length=255, blank=True)
    lat = DecimalField(max_digits=9, decimal_places=6)
    long = DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name
