from ..base.base_model import Base
from django.db.models import CharField, ForeignKey, CASCADE


class Country(Base):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Department(Base):
    name = CharField(max_length=255)
    country = ForeignKey(Country, on_delete=CASCADE)

    def __str__(self):
        return self.name


class City(Base):
    name = CharField(max_length=255)
    department = ForeignKey(Department, on_delete=CASCADE)

    def __str__(self):
        return self.name


class District(Base):
    name = CharField(max_length=255)
    city = ForeignKey(City, on_delete=CASCADE)

    def __str__(self):
        return self.name


class TimeZone(Base):
    name = CharField(max_length=255)
    code = CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name