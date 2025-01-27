from mypet.api.models import Country, Department, City, District, TimeZone
from rest_framework.serializers import ModelSerializer


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        exclude = ["created", "modified", "created_by", "modified_by", "is_active"]


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        exclude = ["created", "modified", "created_by", "modified_by", "is_active"]


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        exclude = ["created", "modified", "created_by", "modified_by", "is_active"]


class DistrictSerializer(ModelSerializer):
    class Meta:
        model = District
        exclude = ["created", "modified", "created_by", "modified_by", "is_active"]


class TimeZoneSerializer(ModelSerializer):
    class Meta:
        model = TimeZone
        exclude = ["created", "modified", "created_by", "modified_by", "is_active"]
