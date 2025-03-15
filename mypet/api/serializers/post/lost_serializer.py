from mypet.api.models import Lost
from rest_framework.serializers import ModelSerializer


class LostSerializer(ModelSerializer):
    class Meta:
        model = Lost
        exclude = ["created", "modified", "created_by", "modified_by", "is_active"]
