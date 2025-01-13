
from .coordinate_model import Coordinate
from ..base.base_model import Base

from django.db.models import Model, OneToOneField, CASCADE, CharField


class Point(Base):
    name = CharField(max_length=50)
    description = CharField(max_length=255, blank=True)
    coordinate = OneToOneField(Coordinate, on_delete=CASCADE)

    def __str__(self):
        return self.name