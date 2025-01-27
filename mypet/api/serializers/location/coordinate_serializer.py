from mypet.api.models import Coordinate
from rest_framework.serializers import ModelSerializer


class CoordinateSerializer(ModelSerializer):
    class Meta:
        model = Coordinate
        exclude = ["created", "modified", "created_by", "modified_by", "is_active"]
