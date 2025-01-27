from rest_framework.viewsets import ModelViewSet
from mypet.api.models import Country, Department, City, District, TimeZone
from mypet.api.serializers import (
    CountrySerializer,
    DepartmentSerializer,
    CitySerializer,
    DistrictSerializer,
    TimeZoneSerializer,
)
from rest_framework.permissions import IsAuthenticated


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.filter(is_active=True)
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.filter(is_active=True)
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]


class CityViewSet(ModelViewSet):
    queryset = City.objects.filter(is_active=True)
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]


class DistrictViewSet(ModelViewSet):
    queryset = District.objects.filter(is_active=True)
    serializer_class = DistrictSerializer
    permission_classes = [IsAuthenticated]


class TimeZoneViewSet(ModelViewSet):
    queryset = TimeZone.objects.filter(is_active=True)
    serializer_class = TimeZoneSerializer
    permission_classes = [IsAuthenticated]
