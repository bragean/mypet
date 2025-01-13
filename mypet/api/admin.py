from django.contrib import admin
from .models import (
    Coordinate,
    Pet,
    PetFeatures,
    PetType,
    Breed,
    Point,
    Country,
    City,
    Department,
    District,
    TimeZone
)


admin.site.register(Coordinate)
admin.site.register(Point)

admin.site.register(Pet)
admin.site.register(PetFeatures)
admin.site.register(PetType)
admin.site.register(Breed)

admin.site.register(Country)
admin.site.register(Department)
admin.site.register(City)
admin.site.register(District)
admin.site.register(TimeZone)