from ..base.base_model import Base
from django.db.models import Model, DecimalField


class Coordinate(Base):
    lat = DecimalField(max_digits=9, decimal_places=6)
    long = DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"{self.lat}, {self.long}"
