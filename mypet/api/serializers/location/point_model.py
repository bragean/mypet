from mypet.api.models import Point
from rest_framework.serializers import ModelSerializer


class PointSerializer(ModelSerializer):
    class Meta:
        model = Point
        exclude = ["created", "modified", "created_by", "modified_by", "is_active"]
