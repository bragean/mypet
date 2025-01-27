from rest_framework.viewsets import ModelViewSet
from mypet.api.models import Coordinate
from mypet.api.serializers import CoordinateSerializer
from rest_framework.permissions import IsAuthenticated


class CoordinateViewSet(ModelViewSet):
    queryset = Coordinate.objects.filter(is_active=True)
    serializer_class = CoordinateSerializer
    permission_classes = [IsAuthenticated]