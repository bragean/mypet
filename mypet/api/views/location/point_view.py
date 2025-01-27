from rest_framework.viewsets import ModelViewSet
from mypet.api.models import Point
from mypet.api.serializers import PointSerializer
from rest_framework.permissions import IsAuthenticated


class PointViewSet(ModelViewSet):
    queryset = Point.objects.filter(is_active=True)
    serializer_class = PointSerializer
    permission_classes = [IsAuthenticated]
