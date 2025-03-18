from mypet.api.models import Lost
from mypet.api.serializers import LostSerializer


class LostService:

    def list(user):
        lost_instance_list = Lost.objects.filter(owner=user, is_active=True)
        lost_serializer_list = LostSerializer(lost_instance_list, many=True)
        return lost_serializer_list.data

    def get(id):
        lost_instance = Lost.objects.get(id=id)
        lost_serializer = LostSerializer(lost_instance)
        return lost_serializer.data

    def exists(id):
        return Lost.objects.filter(id=id).exists()
