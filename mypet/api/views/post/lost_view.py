from rest_framework.viewsets import ModelViewSet
from mypet.api.models import Lost
from mypet.api.serializers import LostSerializer
from rest_framework.permissions import IsAuthenticated


class LostViewSet(ModelViewSet):
    queryset = Lost.objects.filter(is_active=True)
    serializer_class = LostSerializer
    permission_classes = [IsAuthenticated]
