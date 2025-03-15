from mypet.api.models import Sighting
from rest_framework.serializers import ModelSerializer


class SightingSerializer(ModelSerializer):
    class Meta:
        model = Sighting
        exclude = ["created", "modified", "created_by", "modified_by", "is_active"]
